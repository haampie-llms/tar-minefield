"""A pax `size` of 2^64 + 512, which a 64-bit reader that wraps around reads as 512.

pax numbers have no limit, but implementations keep sizes in 64 bits. One that converts digit by
digit without checking for overflow wraps 2^64 + 512 around to 512, and reads the next block as the
data of `a`; one that checks for it rejects the size, or falls back to the header's size, 0, and
reads that block as the header of `smuggled`; one that clamps it runs past the end of the archive.

Decision point: what a pax number too large for the reader means.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F27"
FEATURES = ["pax.size-too-large"]


def build(a):
    a.pax([(b"size", b"%d" % (2**64 + 512))], note="size=2^64+512, for a")
    a.header(b"a", b"0", 0, note="size 0")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that wraps the size to 512")
    a.end()
