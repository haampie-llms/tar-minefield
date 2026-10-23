# Extract a tar archive with Archive::Tar, which CPAN clients use, for contrib/matrix/matrix.py.
#
#     perl extract.pl ARCHIVE DEST
#
# An error is printed on stderr, with status 1.
use strict;
use warnings;
use Archive::Tar;

my ($archive, $dest) = @ARGV;
my $tar = Archive::Tar->new;
$tar->read($archive) or do { print STDERR Archive::Tar->error, "\n"; exit 1 };
chdir $dest or die "chdir: $!\n";
$tar->extract or do { print STDERR $tar->error, "\n"; exit 1 };
