"""A hardlink to a member that comes later.

`h` is a hardlink to `f`, which comes after it. A parser that extracts in order has nothing to
link to; one that reads the whole archive first links `h` to `f`.

Decision point: whether a hardlink may name a later member.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "S05"
FEATURES = ['hardlink.to-later-member']


def build(a):
    a.hardlink(b"h", b"f")
    a.file(b"f", b"f\n")
    a.end()
