"""An empty pax `size`, which in POSIX removes the size rather than giving one.

A record with an empty value deletes the key: `size=` leaves `a` with no size at all, not even that
of its header, which says 512. Implementations take it as 0, and read the next block as the header
of `smuggled`; or fall back to the header's size, and read that block as the data of `a`; or reject
it. Nothing defines what a member without a size is, so a strict parser rejects it.

Decision point: what an empty pax size means: no size, 0, or the header's size.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F21"
FEATURES = ["pax.empty-value.size", "pax.invalid-size"]


def build(a):
    a.pax([(b"size", b"")], note="size=, which removes the size")
    a.header(b"a", b"0", 512, note="size 512")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that takes the header's size")
    a.end()
