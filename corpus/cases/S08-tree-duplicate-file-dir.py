"""A file, then a directory of the same name.

`a` is a file, then `a/` a directory. An implementation may replace the file with the directory,
keep the file and fail on the directory, or keep the first.

Decision point: whether a later member replaces an earlier one of another kind.
Seen in: no tarball of the scans.
"""

VERDICT = "reject"
CODE = "S08"
FEATURES = ['tree.duplicate.file-dir']


def build(a):
    a.file(b"a", b"a file first\n")
    a.directory(b"a/")
    a.end()
