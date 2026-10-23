# Extract a tar archive with RubyGems' Gem::Package#extract_tar_gz, which installs the files of
# a gem, for corpus/matrix.py. It takes a gzipped archive, so the archive is gzipped first.
#
#     ruby extract.rb ARCHIVE DEST
#
# An error is printed on stderr, with status 1.
require "fileutils"
require "rubygems/package"
require "stringio"
require "zlib"

archive, dest = ARGV
gz = StringIO.new
writer = Zlib::GzipWriter.new(gz)
writer.write(File.binread(archive))
writer.finish
package = Gem::Package.new(File.join(dest, "unused.gem"))
package.spec = Gem::Specification.new { |s| s.name = "corpus"; s.version = "0" }
begin
  package.extract_tar_gz(StringIO.new(gz.string), dest)
rescue StandardError => e
  warn "#{e.class}: #{e.message}"
  exit 1
end
