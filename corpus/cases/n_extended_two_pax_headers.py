"""Two pax extended headers for one member, with different paths.

Two `x` headers come before one member, with the paths `first` and `second`. A reader may apply
the first, the last, or merge them.

Decision point: which of two extended headers of one kind applies.
Seen in: no tarball of the scans. libmygpo-qt 1.2.0 repeats xattr keys within one header, which is
N20, pax-repeated-key.
"""

VERDICT = "n"
CODE = "N09"
FEATURES = ['extended.two-pax-headers']


def build(a):
    a.pax([(b"path", b"first")])
    a.pax([(b"path", b"second")])
    a.file(b"header-name", b"which name?\n")
    a.end()
