"""The same file twice, with the same contents.

Whichever copy an implementation keeps, the tree is the same. But an implementation would have to
compare the copies to know that, so the default policy rejects every duplicate file.

Decision point: which of two members of one path is the file.
Seen in: tarballs of `cabal sdist`, such as string-conversions 0.4.0.1 and multipart 0.2.1.
"""

VERDICT = "n"
CODE = "S09"
FEATURES = ['tree.duplicate.file-file']


def build(a):
    a.file(b"a", b"same\n")
    a.file(b"a", b"same\n")
    a.end()
