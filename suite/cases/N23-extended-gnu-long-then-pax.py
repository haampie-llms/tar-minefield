"""A GNU long name, then a pax header, then the member: which of them does the long name name?

GNU long names and pax headers are two ways of extending the next header, and neither knows the
other. Here a GNU long name `from-gnu` is followed by a pax header with only an `mtime`, and then by
the member `from-header`. An implementation that applies the long name to the header that follows
it gives it to the pax header, where it is lost, and extracts `from-header`; one that applies it to
the next member extracts `from-gnu`.

Decision point: whether a GNU long name applies to the next header or to the next member.
Seen in: no source tarball. No scanned tarball mixes GNU long names and pax headers for one member.
"""

VERDICT = "reject"
ID = "N23"
FEATURES = ["extended.gnu-long-and-pax"]


def build(a):
    a.gnu_long(b"from-gnu", note="the name of the next header, or of the next member")
    a.pax([(b"mtime", b"1")], note="only an mtime")
    a.file(b"from-header", b"which name?\n")
    a.end()
