"""A hardlink to itself.

The first member is a file `a`, the second a hardlink `a` to `a`. An implementation that removes `a`
before linking has nothing left to link to; one that sees the link is to the same path keeps the
file.

Decision point: what a link to itself does to the file.
Seen in: xscreensaver 6.12 and atari++ 1.85.
"""

VERDICT = "reject"
ID = "S04"
FEATURES = ['hardlink.to-itself']


def build(a):
    a.file(b"a", b"a\n")
    a.hardlink(b"a", b"a")
    a.end()
