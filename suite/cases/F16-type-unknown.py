"""An unknown typeflag with a size: data, or no data?

POSIX says an implementation treats an unknown typeflag as a regular file, so its size is data. Some
implementations skip only the header of a member they do not know, and then read its data as the
next header, here that of `smuggled`.

Decision point: whether an unknown typeflag has data.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F16"
FEATURES = ['type.unknown-Z']


def build(a):
    a.header(b"unknown", b"Z", 512, note="typeflag Z, size 512")
    a.file(b"smuggled", b"", note="the data of the unknown member, read as a header by some")
    a.end()
