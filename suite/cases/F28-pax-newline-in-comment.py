r"""A newline in a pax `comment`, after which an implementation that splits on lines sees a `size`.

pax records are delimited by their length, so a value may hold a newline. Here the only record is a
`comment`, `x\n12 size=512`, which an implementation that reads records by their length ignores, as
it does every comment: it reads `a` with the size of its header, 0, and the next block as the
header of `smuggled`. An implementation that splits the extended header on newlines sees the record
end at the newline, and the rest as a record of its own, `size=512`: the next block is the data of
`a` to it. Unlike F13, the value that hides the record is one that no implementation applies.

Decision point: whether a pax record is delimited by its length or by a newline.
Seen in: no source tarball. Newlines in pax values are only in xattrs, such as Minion 10.31, which
the default policy accepts as xattrs are not extracted.
"""

VERDICT = "reject"
ID = "F28"
FEATURES = ["pax.newline-in-value.comment"]


def build(a):
    a.pax([(b"comment", b"x\n12 size=512")], note="a comment with a newline")
    a.header(b"a", b"0", 0, note="size 0")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that splits records on lines")
    a.end()
