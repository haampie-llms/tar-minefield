"""A regular file whose name ends in a slash: a file, or a directory?

The header says typeflag `0`, a regular file, of size 0, but the name is `a/`. v7 tar had no
typeflag for directories, and wrote them like this, so readers that keep that convention extract
a directory `a`; readers that follow the typeflag extract an empty file `a`, or fail to create a
file with a trailing slash.

Decision point: whether the typeflag or the trailing slash decides the kind.
Seen in: v7 archives only, such as sendmail 8.18.2, tcp_wrappers 7.6 and unclutter 8.
"""

VERDICT = "n"
FEATURES = ["name.trailing-slash-on-file"]


def build(a):
    a.header(b"a/", b"0", 0, note="typeflag of a file, name of a directory")
    a.end()
