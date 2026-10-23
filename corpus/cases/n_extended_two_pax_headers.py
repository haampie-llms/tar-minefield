"""Two pax extended headers for one member, with different paths.

Two `x` headers come before one member, with the paths `first` and `second`. A reader may apply
the first, the last, or merge them.

Decision point: which of two extended headers of one kind applies.
Seen in: libmygpo-qt 1.2.0, with the same xattr keys in two headers.
"""

VERDICT = "n"
CODE = "N09"
FEATURES = ['extended.two-pax-headers']


def build(a):
    a.pax([(b"path", b"first")])
    a.pax([(b"path", b"second")])
    a.file(b"header-name", b"which name?\n")
    a.end()
