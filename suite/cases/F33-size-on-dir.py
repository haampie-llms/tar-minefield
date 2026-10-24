"""A size in the header of a directory, which hides a header from the implementations that honor it.

F15 with the size in the ustar header rather than a pax header. A directory has no data, but its
header says 512 bytes. An implementation that skips the size of every member skips the next block
as the directory's data; an implementation that knows directories have no data reads that block as
the header of a file, `smuggled`. One implementation then extracts a directory, the other a
directory and a file. The same goes for links and devices, which have no data either.

Decision point: whether a size in the header applies to a member that has no data.
Seen in: no source tarball has a size on a member without data.
"""

VERDICT = "reject"
ID = "F33"
FEATURES = ["size.on-dir"]


def build(a):
    a.header(b"dir/", b"5", 512, note="no data, but the size says 512 bytes")
    a.file(b"dir/smuggled", b"", note="the block that the size covers")
    a.end()
