"""A checksum that only matches as the signed sum of the header.

POSIX sums the bytes of a header as unsigned numbers; some old tars summed them as signed, and
parsers still accept either. With a byte over 127 in the header, here in `uname`, the two sums
differ, so a parser that accepts only the unsigned one rejects the header.

Decision point: whether a signed checksum makes a header valid.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "F06"
FEATURES = ['checksum.signed']


def build(a):
    a.file(b"a", b"a\n", uname=b"\xe9", chksum="signed", note="a byte over 127 in uname")
    a.end()
