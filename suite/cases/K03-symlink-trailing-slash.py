"""A symlink whose name ends in a slash.

`link/` is a symlink to `target`. With the slash, the name refers to what the link points to, so
depending on the implementation, the link `link` is created, the link is written through, or
extraction fails.

Decision point: what a trailing slash on a link means.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "K03"
FEATURES = ['name.trailing-slash-on-symlink']


def build(a):
    a.directory(b"target/")
    a.symlink(b"link/", b"target")
    a.end()
