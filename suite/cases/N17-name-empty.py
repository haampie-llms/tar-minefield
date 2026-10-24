"""A member with an empty name.

The name field is all NULs. Depending on the implementation, the member is skipped, taken for the
end of the archive, extracted as the destination directory itself, or extraction fails.

Decision point: what an empty name refers to.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "N17"
FEATURES = ['name.empty']


def build(a):
    a.file(b"", b"no name\n")
    a.end()
