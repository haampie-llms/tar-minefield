"""A backslash in a name: a character on Unix, a separator on Windows.

`a\\b` is one file named with a backslash on Unix, and the file `b` in the directory `a` on
Windows. With `..\\` the same rule lets a name climb out of the destination there.

Decision point: whether a backslash separates components.
Seen in: texi2html 5.0 and gstreamer-docs 1.28.1.
"""

VERDICT = "reject"
CODE = "N13"
FEATURES = ['name.backslash']


def build(a):
    a.file(b"a\\b", b"one file, or b in a?\n")
    a.end()
