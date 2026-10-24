"""A pax `size` with a plus sign, `+512`, which conversions of strings to numbers accept.

A pax size is a decimal number, which has no sign. But the conversions of strings to numbers that
implementations use, such as Python's `int`, Go's `strconv.ParseInt` and Rust's `u64::from_str`,
read `+512` as 512, and the next block as the data of `a`. Implementations that check for digits
reject it, or fall back to the header's size, 0, and read that block as the header of `smuggled`.

Decision point: whether a pax size may have a sign.
Seen in: no source tarball.
"""

VERDICT = "reject"
ID = "F23"
FEATURES = ["pax.invalid-size"]


def build(a):
    a.pax([(b"size", b"+512")], note="size=+512, for a")
    a.header(b"a", b"0", 0, note="size 0")
    a.file(b"smuggled", b"", note="the data of a, to an implementation that reads +512 as 512")
    a.end()
