"""A symlink to an absolute path, created as it is.

The default policy creates the link, and rejects writing through any symlink. The target does
not exist.

Seen in: tachyon 0.99.5, notmuch 0.40 and others: see contrib/data/STRICT.md.
"""

L = lambda path, target: {"path": path, "kind": "symlink", "target": target}

VERDICT = "tolerate"
CODE = "N07"
FEATURES = ['symlink.absolute']
TREE = [L('link', '/tar-minefield-nonexistent')]


def build(a):
    a.symlink(b"link", b"/tar-minefield-nonexistent")
    a.end()
