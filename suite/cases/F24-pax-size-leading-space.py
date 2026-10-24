"""A pax `size` with a leading space, ` 512`, which conversions of strings to numbers skip.

A pax record is `<length> <key>=<value>\\n`, and its value starts right after the `=`: here, with a
space. Python's `int` and C's `strtoull` skip leading whitespace, read 512, and the next block as the
data of `a`; implementations that check for digits reject it, or fall back to the header's size, 0,
and read that block as the header of `smuggled`.

Decision point: whether a pax size may have whitespace.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F24"
FEATURES = ["pax.invalid-size"]


def build(a):
    a.pax([(b"size", b" 512")], note="size= 512, for a")
    a.header(b"a", b"0", 0, note="size 0")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that skips the space")
    a.end()
