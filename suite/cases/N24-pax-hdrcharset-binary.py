r"""`hdrcharset=BINARY`, which declares a pax path that is not UTF-8 as bytes.

POSIX lets a pax header declare with `hdrcharset=BINARY` that its names are bytes in no particular
encoding, rather than UTF-8. Here the path is `caf\xe9`, in Latin-1. Implementations write the bytes
as they are, decode them as Latin-1 or with replacement characters, or fail, as they do with N18:
the name of the extracted file differs. A strict parser has no use for names that are not UTF-8.

Decision point: how a name that is not UTF-8 becomes a path.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "N24"
FEATURES = ["pax.hdrcharset", "pax.path-not-utf8"]


def build(a):
    a.pax([(b"hdrcharset", b"BINARY"), (b"path", b"caf\xe9")], note="a path in Latin-1")
    a.file(b"cafe", b"which name?\n")
    a.end()
