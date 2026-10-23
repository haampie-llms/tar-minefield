"""A member with an empty name.

The name field is all NULs. A reader may skip the member, take it for the end of the archive,
extract it as the destination directory itself, or fail.

Decision point: what an empty name refers to.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
FEATURES = ['name.empty']


def build(a):
    a.file(b"", b"no name\n")
    a.end()
