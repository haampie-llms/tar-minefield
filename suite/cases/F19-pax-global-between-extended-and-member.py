"""A global pax header between an extended header and its member.

An `x` header, then a `g` header, then the member. Depending on the implementation, the extended
header applies to the global header, which is the next header, or the global header is skipped and
the extended header applies to the member.

Decision point: which header an extended header applies to.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F19"
FEATURES = ['pax-global.between-extended-and-member']


def build(a):
    a.pax([(b"path", b"from-pax")])
    a.pax([(b"comment", b"between")], typeflag=b"g", name=b"pax_global_header")
    a.file(b"header-name", b"which name?\n")
    a.end()
