"""The POSIX magic with a version that is neither `00` nor NULs.

`ustar\0` is followed by the version `01`. An implementation may take the header as ustar, or as
some other format, and read its prefix field and other fields accordingly. The default policy
accepts only the version `00`, and NULs as some Java archivers write.

Decision point: which format the header is in.
Seen in: only the version of NULs, as in commons-lang 2.6 and apache-solr 3.6.2.
"""

VERDICT = "reject"
CODE = "F11"
FEATURES = ['magic.posix-with-odd-version']


def build(a):
    a.file(b"a", b"a\n", version=b"01")
    a.end()
