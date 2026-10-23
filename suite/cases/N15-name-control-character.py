"""A control character in a name, here a newline.

`a\nb` is a valid name on Unix, but listings, manifests and scripts that read names line by line
see two names. Implementations that escape or reject control characters disagree with those that
write them as they are.

Decision point: whether a name may contain control characters.
Seen in: cdrtools 3.02a09, wgrib2 3.6.0 and apktool 2.6.0.
"""

VERDICT = "reject"
ID = "N15"
FEATURES = ['name.control-character']


def build(a):
    a.file(b"a\nb", b"a newline in my name\n")
    a.end()
