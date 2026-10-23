"""A symlink, then a file of the same name: replace the link, or write through it?

`a` is a symlink to `target`, then a file `a`. An implementation that replaces the link writes the
file `a`; one that opens `a` for writing follows the link and writes `target` instead.

Decision point: whether writing a member follows a symlink in its place.
Seen in: no source tarball.
"""

VERDICT = "reject"
CODE = "S10"
FEATURES = ['tree.duplicate.symlink-file']


def build(a):
    a.symlink(b"a", b"target")
    a.file(b"a", b"written to a, or to target?\n")
    a.end()
