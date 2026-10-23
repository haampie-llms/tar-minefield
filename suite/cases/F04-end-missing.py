"""No end-of-archive marker: the archive ends after a complete member.

The default policy accepts it: the archive is pinned by its sha256, so one that ends early is
caught before it is parsed.

Seen in: SDL2_image 2.8.8, ruby 4.0.5 and fastcap 2.0-18Sep92.
"""

F = lambda path, contents: {"path": path, "kind": "file", "contents": contents, "executable": False}

VERDICT = "tolerate"
CODE = "F04"
FEATURES = ['end.missing']
TREE = [F('a', b'a\n')]


def build(a):
    a.file(b"a", b"a\n")
