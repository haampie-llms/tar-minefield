"""A hardlink to a member that is not in the archive.

The member `h` is a hardlink to `missing`. Depending on the implementation, extraction fails, the
link is skipped, or it links to a file of that name that already exists where it extracts.

Decision point: what a hardlink to nothing does.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "S03"
FEATURES = ['hardlink.missing-target']


def build(a):
    a.hardlink(b"h", b"missing")
    a.end()
