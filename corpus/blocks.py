"""Build tar archives from raw 512-byte blocks, and describe every block as it is written.

The cases of the corpus use this instead of tarfile or any other implementation under test: it
writes exactly the bytes it is given, and normalizes nothing. Every field of a header is either
a value, which it encodes the usual way, or raw bytes, which it writes as they are. The dump of an
archive comes from what was written, so it does not parse the archive.
"""

BLOCK = 512

# (field, offset, width) of a ustar header
FIELDS = [
    ("name", 0, 100),
    ("mode", 100, 8),
    ("uid", 108, 8),
    ("gid", 116, 8),
    ("size", 124, 12),
    ("mtime", 136, 12),
    ("chksum", 148, 8),
    ("typeflag", 156, 1),
    ("linkname", 157, 100),
    ("magic", 257, 6),
    ("version", 263, 2),
    ("uname", 265, 32),
    ("gname", 297, 32),
    ("devmajor", 329, 8),
    ("devminor", 337, 8),
    ("prefix", 345, 155),
    ("pad", 500, 12),
]
NUMBERS = ("mode", "uid", "gid", "size", "mtime", "devmajor", "devminor")
TYPES = {
    b"0": "regular file",
    b"\0": "regular file (pre-POSIX)",
    b"1": "hardlink",
    b"2": "symlink",
    b"5": "directory",
    b"x": "pax extended header, for the next member",
    b"g": "pax global header",
    b"L": "GNU long name, for the next member",
    b"K": "GNU long link name, for the next member",
}


def octal(value, width):
    """value in octal, padded with zeros, and ended by a NUL: the usual encoding."""
    return b"%0*o\0" % (width - 1, value)


def pax_record(key, value):
    """A pax record, `<length> <key>=<value>\\n`, whose length counts itself."""
    body = b" " + key + b"=" + value + b"\n"
    length = len(body) + 1
    while len(b"%d" % length) + len(body) != length:
        length += 1
    return b"%d" % length + body


def show(raw):
    """Bytes as a string literal, with a run of NULs at the end counted rather than written."""
    stripped = raw.rstrip(b"\0")
    nuls = len(raw) - len(stripped)
    text = ""
    for b in stripped:
        c = chr(b)
        if c == "\\":
            text += "\\\\"
        elif c == '"':
            text += '\\"'
        elif c == "\0":
            text += "\\0"
        elif c == "\n":
            text += "\\n"
        elif 32 <= b < 127:
            text += c
        else:
            text += f"\\x{b:02x}"
    parts = [f'"{text}"'] if stripped else []
    if nuls:
        parts.append(f"{nuls} NUL" if nuls > 1 or not stripped else "NUL")
    return " + ".join(parts) if parts else '""'


class Archive:
    def __init__(self):
        self.blocks = []  # (bytes, title, [(field, offset, width, raw, meaning)] or text lines)
        self.size = 0

    def _add(self, data, title, details):
        assert len(data) % BLOCK == 0
        self.blocks.append((self.size, data, title, details))
        self.size += len(data)

    def header(self, name, typeflag=b"0", size=0, note="", **raw):
        """A ustar header. Fields not given are the usual ones: mode 644 for files and 755 for
        directories, uid and gid 0, mtime 0, empty names, and the POSIX magic `ustar\\0` with
        version `00`. A keyword with bytes for a field writes those bytes as they are, padded
        with NULs; the checksum is computed, unless it is given too."""
        values = {
            "name": name,
            "mode": 0o755 if typeflag == b"5" else 0o644,
            "uid": 0,
            "gid": 0,
            "size": size,
            "mtime": 0,
            "typeflag": typeflag,
            "linkname": b"",
            "magic": b"ustar\0",
            "version": b"00",
            "uname": b"",
            "gname": b"",
            "devmajor": 0,
            "devminor": 0,
            "prefix": b"",
            "pad": b"",
        }
        for key, value in raw.items():
            assert key in values, key
            values[key] = value
        block = bytearray(BLOCK)
        fields = []
        for field, offset, width in FIELDS:
            if field == "chksum":
                continue
            value = values[field]
            if isinstance(value, int):
                encoded = octal(value, width)
                meaning = f"{value:o} (octal)" if field == "mode" else str(value)
            else:
                encoded, meaning = value, ""
            assert len(encoded) <= width, (field, encoded)
            block[offset : offset + len(encoded)] = encoded
            if field == "typeflag":
                meaning = TYPES.get(value, "unknown typeflag")
            fields.append((field, offset, width, meaning))
        if "chksum" in raw:
            chksum, meaning = raw["chksum"], "given"
        else:
            block[148:156] = b" " * 8
            total = sum(block)
            chksum = b"%06o\0 " % total
            meaning = f"{total}: the unsigned sum of the header, this field as spaces"
        block[148 : 148 + len(chksum)] = chksum
        fields.append(("chksum", 148, 8, meaning))
        fields.sort(key=lambda f: f[1])
        details = [(f, o, w, bytes(block[o : o + w]), m) for f, o, w, m in fields]
        title = f"header: {TYPES.get(typeflag, 'unknown type')}" + (f", {note}" if note else "")
        self._add(bytes(block), title, details)
        return self

    def data(self, content, note=""):
        """The data of a member, padded with NULs to a whole block."""
        if not content:
            return self
        padded = content + bytes(-len(content) % BLOCK)
        lines = [f"{len(content)} bytes, then {len(padded) - len(content)} NUL to the end of the block"]
        if content:
            lines.append(show(content) if len(content) <= 400 else show(content[:400]) + " ...")
        self._add(padded, "data" + (f": {note}" if note else ""), lines)
        return self

    def file(self, name, content, note="", **raw):
        return self.header(name, b"0", len(content), note, **raw).data(content)

    def directory(self, name, note="", **raw):
        return self.header(name, b"5", 0, note, **raw)

    def symlink(self, name, target, note="", **raw):
        return self.header(name, b"2", 0, note, linkname=target, **raw)

    def hardlink(self, name, target, note="", **raw):
        return self.header(name, b"1", 0, note, linkname=target, **raw)

    def pax(self, records, typeflag=b"x", name=b"PaxHeader", note=""):
        """A pax extended (x) or global (g) header with the records given as (key, value)."""
        data = b"".join(pax_record(k, v) for k, v in records)
        self.header(name, typeflag, len(data), note)
        lines = [f"{len(data)} bytes of pax records, then {-len(data) % BLOCK} NUL"]
        lines += [show(pax_record(k, v)) for k, v in records]
        self._add(data + bytes(-len(data) % BLOCK), "data: pax records", lines)
        return self

    def zeros(self, count=1, note=""):
        title = f"{count} zero block{'s' if count > 1 else ''}" + (f": {note}" if note else "")
        self._add(bytes(BLOCK * count), title, [])
        return self

    def end(self):
        return self.zeros(2, "the end-of-archive marker")

    def bytes(self):
        return b"".join(data for _, data, _, _ in self.blocks)

    def dump(self):
        """Every block: its offset, what it is, and for a header every field, as written."""
        out = []
        for offset, data, title, details in self.blocks:
            out.append(f"{offset:#08x}  {title}")
            for d in details:
                if isinstance(d, str):
                    out.append(f"          {d}")
                else:
                    field, start, width, raw, meaning = d
                    line = f"          {field:<9}[{start:3},{start + width:3})  {show(raw)}"
                    out.append(line + (f"  {meaning}" if meaning else ""))
        out.append(f"{self.size:#08x}  end of file")
        return "\n".join(out) + "\n"
