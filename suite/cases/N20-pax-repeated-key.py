"""One pax key twice in one extended header.

The extended header has the records `path=first` and `path=second`. Implementations that keep the
first value and those that keep the last extract different names.

Decision point: which of two values of one key applies.
Seen in: libmygpo-qt 1.2.0, with xattr keys.
"""

VERDICT = "reject"
CODE = "N20"
FEATURES = ['pax.repeated-key']


def build(a):
    a.pax([(b"path", b"first"), (b"path", b"second")])
    a.file(b"header-name", b"which name?\n")
    a.end()
