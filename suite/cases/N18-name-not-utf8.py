r"""A name that is not UTF-8.

The name `caf\xe9` is Latin-1. Depending on the implementation, the bytes are written as they are,
or decoded as Latin-1 and written as `café` in UTF-8, or the byte is replaced, or extraction fails:
different names on disk.

Decision point: how a name that is not UTF-8 is decoded.
Seen in: aspell-is 0.51.1-0 and aspell-nb 0.50.1-0.
"""

VERDICT = "reject"
ID = "N18"
FEATURES = ['name.not-utf8']


def build(a):
    a.file(b"caf\xe9", b"Latin-1\n")
    a.end()
