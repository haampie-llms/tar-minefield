"""Bytes after the NUL that ends a name.

The name field holds `a`, a NUL, and `b`. C readers stop at the NUL and read `a`; a reader that
strips NULs from the end of the field reads `a\0b`, or `ab` once it drops the NUL.

Decision point: where a name ends.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "N14"
FEATURES = ['name.bytes-after-nul']


def build(a):
    a.file(b"a\0b", b"a, or ab?\n")
    a.end()
