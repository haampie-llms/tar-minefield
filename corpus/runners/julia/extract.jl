# Extract a tar archive with Julia's Tar.jl, for corpus/matrix.py.
#
#     julia --startup-file=no extract.jl ARCHIVE DEST
#
# An error is printed on stderr, with status 1.
using Tar
Tar.extract(ARGS[1], ARGS[2])
