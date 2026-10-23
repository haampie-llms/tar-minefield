"""A name over 100 bytes, in a GNU long name.

GNU tar's own format: a header of typeflag `L` whose data is the name of the next member.

Seen in: most tarballs that GNU tar wrote in its default format.
"""

F = lambda path, contents: {"path": path, "kind": "file", "contents": contents, "executable": False}
D = lambda path: {"path": path, "kind": "directory"}

VERDICT = "accept"
CODE = "N01"
FEATURES = []
TREE = [D('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'), F('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd/ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', b'long\n')]


def build(a):
    a.gnu_long(b"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd/ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
    a.file(b"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd/fffffffffffffffffffffffffffffffffffffff", b"long\n", magic=b"ustar ", version=b" \0")
    a.end()
