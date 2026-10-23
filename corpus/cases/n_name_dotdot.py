"""`..` in a name, which climbs out of the directory the archive is extracted to.

The name `tar-minefield/../../tar-minefield-escaped` resolves to a path outside the destination.
An extractor may refuse the member, rewrite its name, or write it where it points. The file is
harmless: its name and contents say what happened.

Decision point: whether a name with `..` is rejected, rewritten, or followed.
Seen in: no tarball of the scans.
Observed: GNU tar 1.35 and BusyBox 1.37.0 list it as `tar-minefield-escaped`, without the leading
`tar-minefield/../../`; 7-Zip 26.00 and the tarfile of CPython 3.14.4 list it as it is.
"""

VERDICT = "n"
FEATURES = ["name.dotdot"]


def build(a):
    a.file(
        b"tar-minefield/../../tar-minefield-escaped",
        b"If this file is outside the directory you extracted to, the extractor followed `..`.\n",
    )
    a.end()
