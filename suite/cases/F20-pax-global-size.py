"""A global pax header with a `size`, which frames every member after it, or none.

POSIX applies the records of a global header to every member after it that does not override them,
and so a `size=512` in one to `a`, whose header says size 0. An implementation that applies it reads
the next block as the data of `a`; one that ignores global headers, or the size in them, reads that
block as the header of another file, `smuggled`. No archiver writes a size in a global header.

Decision point: whether a `size` in a global header applies.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F20"
FEATURES = ["pax-global.size"]


def build(a):
    a.pax([(b"size", b"512")], typeflag=b"g", name=b"pax_global_header", note="size=512")
    a.header(b"a", b"0", 0, note="size 0, but the global size says 512")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that applies the global size")
    a.end()
