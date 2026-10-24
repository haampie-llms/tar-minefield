"""A hardlink to a member that comes later.

The member `h` is a hardlink to `f`, which comes after it. An implementation that extracts in order
has nothing to link to; one that reads the whole archive first links `h` to `f`.

Decision point: whether a hardlink may name a later member.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "S05"
FEATURES = ['hardlink.to-later-member']


def build(a):
    a.hardlink(b"h", b"f")
    a.file(b"f", b"f\n")
    a.end()
