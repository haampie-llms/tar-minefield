"""The POSIX magic with NULs for its version, `ustar\0\0\0`, as some Java archivers write.

Seen in: commons-lang 2.6, apache-solr 3.6.2 and commons-logging 1.2.
"""

F = lambda path, contents: {"path": path, "kind": "file", "contents": contents, "executable": False}

VERDICT = "i"
FEATURES = ['magic.posix-with-odd-version']
TREE = [F('a', b'a\n')]


def build(a):
    a.file(b"a", b"a\n", version=b"\0\0")
    a.end()
