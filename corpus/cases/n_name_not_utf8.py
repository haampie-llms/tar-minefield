"""A name that is not UTF-8.

`caf\xe9` is Latin-1. A reader may write the bytes as they are, decode them as Latin-1 and write
`café` in UTF-8, replace the byte, or fail: different names on disk.

Decision point: how a name that is not UTF-8 is decoded.
Seen in: aspell-is 0.51.1-0 and aspell-nb 0.50.1-0.
"""

VERDICT = "n"
CODE = "N18"
FEATURES = ['name.not-utf8']


def build(a):
    a.file(b"caf\xe9", b"Latin-1\n")
    a.end()
