"""A base-256 size of 2^64 + 512 in the header, which a 64-bit reader that wraps around reads as 512.

A base-256 number has 11 bytes, 88 bits, after its first byte, 0x80, but implementations keep sizes
in 64 bits. One that shifts the bytes in without checking for overflow keeps the low 64 bits, 512,
and reads the next block as the data of `a`; one that checks for it rejects the archive; one that
reads the whole number runs past the end of the archive.

Decision point: what a size too large for the reader means.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F30"
FEATURES = ["number.size.base256-too-large"]


def build(a):
    a.header(b"a", b"0", size=b"\x80" + (2**64 + 512).to_bytes(11, "big"),
             note="size 2^64+512, in base 256")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that keeps the low 64 bits")
    a.end()
