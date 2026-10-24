"""A pax `size` with a leading zero, `0777`: 777 in decimal, as POSIX says, or 511 in octal.

A pax size is decimal, and POSIX does not forbid leading zeros. But a reader that converts with C's
`strtoul(s, NULL, 0)`, or that knows the header's octal numbers, reads `0777` as octal, 511. The
decimal reading takes the next two blocks as the data of `a`, the octal one the next block only,
and the header of `smuggled-2` after it; an implementation that rejects the size and falls back to
the header's, 0, extracts both `smuggled-1` and `smuggled-2`.

Decision point: whether a pax number with a leading zero is decimal or octal.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F26"
FEATURES = ["pax.size-leading-zero"]


def build(a):
    a.pax([(b"size", b"0777")], note="size=0777, for a")
    a.header(b"a", b"0", 0, note="size 0")
    a.file(b"smuggled-1", b"", note="the data of a, to any reading of its pax size")
    a.file(b"smuggled-2", b"", note="the data of a, to a decimal reading of its pax size")
    a.end()
