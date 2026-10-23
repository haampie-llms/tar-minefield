"""An end-of-archive marker of one zero block, not two.

Seen in: eng-rus, srecord 1.64 and cdi2iso 0.1.
"""

F = lambda path, contents: {"path": path, "kind": "file", "contents": contents, "executable": False}

VERDICT = "tolerate"
ID = "F03"
FEATURES = ['end.lone-zero-block']
TREE = [F('a', b'a\n')]


def build(a):
    a.file(b"a", b"a\n")
    a.zeros(1, note="one zero block, and the file ends")
