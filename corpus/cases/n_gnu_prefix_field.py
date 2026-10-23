"""The prefix field of a header with GNU magic, which GNU tar uses for times.

GNU's format has no prefix field: GNU tar writes the access and change times where ustar has its
prefix. An implementation that reads the field as a prefix, as CPython's tarfile did (gh-155629),
puts the member under a directory named after the time.

Decision point: whether a header with GNU magic has a prefix.
Seen in: no tarball of the scans with times there.
"""

VERDICT = "n"
CODE = "N11"
FEATURES = ['gnu.atime-ctime']


def build(a):
    a.file(b"a", b"a\n", magic=b"ustar ", version=b" \0", prefix=b"15000000000\0" + b"15000000000\0",
           note="GNU magic, with an access and change time where ustar has its prefix")
    a.end()
