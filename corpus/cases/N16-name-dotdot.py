"""`..` in a name, which climbs out of the directory the archive is extracted to.

The name `tar-minefield/../../tar-minefield-escaped` resolves to a path outside the destination.
An extractor may refuse the member, rewrite its name, or write it where it points. The file is
harmless: its name and contents say what happened.

Decision point: whether a name with `..` is rejected, rewritten, or followed.
Seen in: no tarball of the scans.
"""

VERDICT = "reject"
CODE = "N16"
FEATURES = ["name.dotdot"]


def build(a):
    a.file(
        b"tar-minefield/../../tar-minefield-escaped",
        b"If this file is outside the directory you extracted to, the extractor followed `..`.\n",
    )
    a.end()
