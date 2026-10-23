"""A pax `size` on a directory, which hides a header from the parsers that honor it.

A directory has no data, but its pax extended header says `size=512`. A parser that applies the
pax size to every member skips the next block as the directory's data; a parser that knows
directories have no data reads that block as the header of a file, `smuggled`. One parser then
extracts a directory, the other a directory and a file. This is the bug class of CVE-2025-62518
(tokio-tar), GHSA-3pv8-6f4r-ffg2 (tar-rs) and CVE-2026-53655 (node-tar), where the hidden block is
a header that only one parser sees.

Decision point: whether a pax `size` applies to a member that has no data.
Seen in: llama_index_workflows 2.26.0, with a pax size on a directory.
"""

VERDICT = "n"
CODE = "F15"
FEATURES = ["pax.size-on-dir"]


def build(a):
    a.pax([(b"size", b"512")], note="for dir/, with size=512")
    a.directory(b"dir/", note="no data, but the pax size says 512 bytes")
    a.file(b"dir/smuggled", b"", note="the block that the pax size covers")
    a.end()
