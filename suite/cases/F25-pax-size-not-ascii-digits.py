"""A pax `size` in Arabic-Indic digits, `٥١٢`, which some conversions of strings read as 512.

A pax size is ASCII decimal digits. Python's `int` takes any decimal digit of Unicode, and so reads
`٥١٢` (U+0665 U+0661 U+0662, in UTF-8) as 512, and the next block as the data of `a`. Implementations that check for ASCII digits reject it, or fall back to the header's
size, 0, and read that block as the header of `smuggled`.

Decision point: which digits a pax number may have.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F25"
FEATURES = ["pax.invalid-size"]


def build(a):
    a.pax([(b"size", "٥١٢".encode())], note="size=512 in Arabic-Indic digits, for a")
    a.header(b"a", b"0", 0, note="size 0")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that reads 512")
    a.end()
