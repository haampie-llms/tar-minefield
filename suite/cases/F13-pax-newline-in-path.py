"""A newline in a pax `path`, where implementations that split records on lines see another record.

pax records are delimited by their length, so a value may hold a newline. An implementation that
splits the extended header on newlines instead sees the record end at it, and the rest as a record
of its own: here `path=evil`. The path is `good\n1 path=evil` to one implementation, `good` or
`evil` to others.

Decision point: whether a pax record is delimited by its length or by a newline.
Seen in: no source tarball. Newlines in pax values are only in xattrs, such as Minion
10.31, which the default policy accepts as xattrs are not extracted.
"""

VERDICT = "reject"
ID = "F13"
FEATURES = ['pax.newline-in-value.path']


def build(a):
    a.pax([(b"path", b"good\n1 path=evil")], note="a path with a newline")
    a.file(b"plain", b"which name?\n")
    a.end()
