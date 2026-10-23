"""A NUL inside a pax `path`.

The pax path is `a\0b`. C implementations end the name at the NUL and extract `a`; others keep the
NUL, which no filesystem allows, and fail or replace it.

Decision point: where a pax path ends.
Seen in: no source tarball.
"""

VERDICT = "reject"
CODE = "N19"
FEATURES = ['pax.nul-in-value.path']


def build(a):
    a.pax([(b"path", b"a\0b")])
    a.file(b"header-name", b"a, or a\\0b?\n")
    a.end()
