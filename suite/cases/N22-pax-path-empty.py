"""An empty pax `path`, which in POSIX removes the path rather than giving one.

A record with an empty value deletes the key: `path=` leaves the member with no name, not even that
of its header, `from-header`. Implementations fall back to the header's name, or take the empty name
and fail to write it, or write a file of no name into the destination itself.

Decision point: what an empty pax path means: no name, an empty name, or the header's name.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "N22"
FEATURES = ["pax.empty-value.path"]


def build(a):
    a.pax([(b"path", b"")], note="path=, which removes the path")
    a.file(b"from-header", b"which name?\n")
    a.end()
