"""The global pax header with only a `comment`, as `git archive` writes it.

`git archive` starts every tarball with a global header whose only record is the commit, as a
`comment`, which no reader applies to the tree. GitHub's release tarballs are made this way, so a
strict parser that rejects global headers rejects most of them.

Seen in: every tarball that `git archive` made, such as GitHub's release tarballs.
"""

VERDICT = "y"
CODE = "G01"
TREE = [
    {"path": "project", "kind": "directory"},
    {"path": "project/README", "kind": "file", "contents": b"hello\n", "executable": False},
]


def build(a):
    a.pax(
        [(b"comment", b"0123456789abcdef0123456789abcdef01234567")],
        typeflag=b"g",
        name=b"pax_global_header",
        note="the commit, as git archive writes it",
    )
    a.directory(b"project/", mode=0o775)
    a.file(b"project/README", b"hello\n", mode=0o664)
    a.end()
