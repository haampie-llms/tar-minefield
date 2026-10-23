"""A global pax header with a `path`.

A global header applies to every member after it. With a `path`, every member would have the same
name; implementations apply it, ignore it, or apply it to the next member only.

Decision point: whether a global `path` applies.
Seen in: no tarball of the scans.
"""

VERDICT = "reject"
CODE = "G04"
FEATURES = ['pax-global.path']


def build(a):
    a.pax([(b"path", b"global-name")], typeflag=b"g", name=b"pax_global_header")
    a.file(b"a", b"a\n")
    a.file(b"b", b"b\n")
    a.end()
