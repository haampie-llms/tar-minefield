"""A regular file with a link target.

The header has typeflag `0` and the linkname `target`. An implementation that decides the kind by
the typeflag extracts a file; one that takes a linkname to mean a link makes a link to `target`.

Decision point: whether a linkname makes a member a link.
Seen in: bgen 1.1.7.
"""

VERDICT = "n"
CODE = "K02"
FEATURES = ['linkname.on-file']


def build(a):
    a.file(b"a", b"a file, or a link?\n", linkname=b"target")
    a.end()
