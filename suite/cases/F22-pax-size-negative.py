"""A negative pax `size`, which hides a header from the implementations that read it as a number.

The pax header of `a` says `size=-512`, and its header says size 0. No size can be negative, but the
grammar of a pax number does not forbid a sign. Implementations reject it; fall back to the header's
size, and read the next block as the header of `smuggled`; or read it as an unsigned number, and so
as a size of almost 2^64, which runs past the end of the archive.

Decision point: whether a pax size may be negative, and what a negative one means.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F22"
FEATURES = ["pax.invalid-size"]


def build(a):
    a.pax([(b"size", b"-512")], note="size=-512, for a")
    a.header(b"a", b"0", 0, note="size 0")
    a.file(b"smuggled", b"", note="a member, unless a reading of the pax size covers it")
    a.end()
