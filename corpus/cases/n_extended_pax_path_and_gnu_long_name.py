"""A pax `path` and a GNU long name for one member, and a third name in its header.

The member has the name `from-header`, a GNU long name `from-gnu`, and a pax path `from-pax`.
Readers that prefer pax, those that prefer the GNU long name, and those that apply the one that
comes last extract different names.

Decision point: which of several sources gives a member its name.
Seen in: no tarball of the scans.
"""

VERDICT = "n"
FEATURES = ['extended.pax-path-and-gnu-long-name']


def build(a):
    a.gnu_long(b"from-gnu")
    a.pax([(b"path", b"from-pax")])
    a.file(b"from-header", b"which name?\n")
    a.end()
