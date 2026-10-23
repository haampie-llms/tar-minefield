# Extract a tar archive with Julia's Tar.jl, for corpus/matrix.py.
#
#     julia --startup-file=no extract.jl ARCHIVE DEST
#
# An error is printed on stderr, as one message without the stack trace, with status 1.
using Tar
try
    Tar.extract(ARGS[1], ARGS[2])
catch e
    println(stderr, sprint(showerror, e))
    exit(1)
end
