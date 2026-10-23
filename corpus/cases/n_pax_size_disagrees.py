"""A pax `size` that disagrees with the header's size, which hides a header from one parser.

The header of `a` says size 512, and its pax extended header says `size=0`. A parser that takes
the pax size reads the next block as the header of another file, `smuggled`; a parser that takes
the header's size, or does not know pax, reads that block as the data of `a`.

Decision point: which of two sizes frames the member.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "F14"
FEATURES = ["pax.size-disagrees"]


def build(a):
    a.pax([(b"size", b"0")], note="size=0, for a")
    a.header(b"a", b"0", 512, note="size 512")
    a.file(b"smuggled", b"", note="the data of a, to a parser that takes the header's size")
    a.end()
