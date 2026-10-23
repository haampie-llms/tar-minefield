"""A hardlink to a member that is not in the archive.

`h` is a hardlink to `missing`. An implementation may fail, skip the link, or link to a file of that
name that already exists where it extracts.

Decision point: what a hardlink to nothing does.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "S03"
FEATURES = ['hardlink.missing-target']


def build(a):
    a.hardlink(b"h", b"missing")
    a.end()
