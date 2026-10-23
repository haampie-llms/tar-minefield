"""A global pax header between an extended header and its member.

An `x` header, then a `g` header, then the member. A reader may apply the extended header to the
global header, which is the next header, or skip the global header and apply it to the member.

Decision point: which header an extended header applies to.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "G03"
FEATURES = ['pax-global.between-extended-and-member']


def build(a):
    a.pax([(b"path", b"from-pax")])
    a.pax([(b"comment", b"between")], typeflag=b"g", name=b"pax_global_header")
    a.file(b"header-name", b"which name?\n")
    a.end()
