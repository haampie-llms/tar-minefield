# Extract a tar archive with R's own extractor, utils::untar with tar = "internal", for
# contrib/matrix/matrix.py. By default untar runs the tar program of $TAR, if there is one.
#
#     Rscript --vanilla extract.R ARCHIVE DEST
#
# An error is printed on stderr, with status 1.
args <- commandArgs(trailingOnly = TRUE)
tryCatch(
    utils::untar(args[1], exdir = args[2], tar = "internal"),
    error = function(e) {
        message(conditionMessage(e))
        quit(status = 1)
    }
)
