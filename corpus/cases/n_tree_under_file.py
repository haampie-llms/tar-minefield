"""A member under a file.

`a` is a file, then `a/b` is a file in it. A reader may fail, replace the file `a` with a
directory, or skip `a/b`.

Decision point: whether a member under a file replaces it.
Seen in: sendmail 8.18.2 and unclutter 8, where the file is a v7 directory named `a/`.
"""

VERDICT = "n"
CODE = "S12"
FEATURES = ['tree.under-file']


def build(a):
    a.file(b"a", b"a file\n")
    a.file(b"a/b", b"under a file\n")
    a.end()
