"""A symlink whose name ends in a slash.

`link/` is a symlink to `target`. With the slash, the name refers to what the link points to, so
a reader may create the link `link`, write through it, or fail.

Decision point: what a trailing slash on a link means.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
FEATURES = ['name.trailing-slash-on-symlink']


def build(a):
    a.directory(b"target/")
    a.symlink(b"link/", b"target")
    a.end()
