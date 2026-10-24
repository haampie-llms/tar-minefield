"""A hardlink to a symlink: a link to the symlink, or to its target?

The member `s` is a symlink to `f`, and `h` a hardlink to `s`. Depending on the implementation, `h`
links to the symlink, making another symlink, or to the file it points to.

Decision point: whether a hardlink follows a symlink.
Seen in: octa 8.4.
"""

VERDICT = "reject"
ID = "S06"
FEATURES = ['hardlink.to-symlink']


def build(a):
    a.file(b"f", b"f\n")
    a.symlink(b"s", b"f")
    a.hardlink(b"h", b"s")
    a.end()
