"""A file, then a directory of the same name.

`a` is a file, then `a/` a directory. Depending on the implementation, the directory replaces the
file, the file is kept and extraction fails on the directory, or the file is kept silently.

Decision point: whether a later member replaces an earlier one of another kind.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "S08"
FEATURES = ['tree.duplicate.file-dir']


def build(a):
    a.file(b"a", b"a file first\n")
    a.directory(b"a/")
    a.end()
