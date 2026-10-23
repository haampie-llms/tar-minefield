"""Bytes after the NUL that ends a name.

The name field holds `a`, a NUL, and `b`. C implementations stop at the NUL and read `a`; an
implementation that strips NULs from the end of the field reads `a\0b`, or `ab` once it drops the
NUL.

Decision point: where a name ends.
Seen in: no tarball of the scans.
"""

VERDICT = "reject"
CODE = "N14"
FEATURES = ['name.bytes-after-nul']


def build(a):
    a.file(b"a\0b", b"a, or ab?\n")
    a.end()
