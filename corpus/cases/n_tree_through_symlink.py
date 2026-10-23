"""A member written through a symlink, which points out of the destination.

`d` is a symlink to `..`, then `d/tar-minefield-through-symlink` is a file. A reader that follows
the link writes the file in the parent of the destination. The file is harmless.

Decision point: whether a member may be written through a symlink.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
FEATURES = ['tree.through-symlink']


def build(a):
    a.symlink(b"d", b"..")
    a.file(b"d/tar-minefield-through-symlink", b"If this file is outside the directory you extracted to, the extractor followed the name.\n")
    a.end()
