"""A size with a space among its digits: implementations read two sizes.

The size field is `000000 1000`. An implementation that stops at the first space reads 0; one that
skips spaces reads 1000 octal, 512. The 512 bytes that follow are the header of `smuggled` to the
first implementation, and the data of `a` to the second.

Decision point: how a number field with a space among its digits is read.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "F12"
FEATURES = ['number.size.gap-in-digits']


def build(a):
    a.header(b"a", b"0", b"000000 1000\0", note="size 0 or 512")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that skips spaces")
    a.end()
