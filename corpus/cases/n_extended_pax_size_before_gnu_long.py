"""A pax `size` followed by a GNU long name: which of them does the size apply to?

The pax header says `size=512` and is followed by a GNU long name header, then by the member.
Parsers that apply the pax size to the next header, whatever it is, misread the long name; those
that apply it to the member read one more block as its data, which here is the header of
`smuggled`.

Decision point: which header a pax size applies to, when another extended header follows.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
CODE = "F10"
FEATURES = ['extended.pax-size-before-gnu-long']


def build(a):
    a.pax([(b"size", b"512")], note="size=512")
    a.gnu_long(b"long-name", note="the name of the next member")
    a.header(b"short-name", b"0", 0, note="size 0, but the pax size says 512")
    a.file(b"smuggled", b"", note="covered by the pax size, to some parsers")
    a.end()
