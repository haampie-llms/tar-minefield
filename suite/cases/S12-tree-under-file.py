"""A member under a file.

The first member is a file `a`, the second a file `a/b` in it. Depending on the implementation,
extraction fails, the file `a` is replaced with a directory, or `a/b` is skipped.

Decision point: whether a member under a file replaces it.
Seen in: sendmail 8.18.2 and unclutter 8, where the file is a v7 directory named `a/`.
"""

VERDICT = "reject"
ID = "S12"
FEATURES = ['tree.under-file']


def build(a):
    a.file(b"a", b"a file\n")
    a.file(b"a/b", b"under a file\n")
    a.end()
