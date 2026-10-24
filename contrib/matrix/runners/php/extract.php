<?php
// Extract a tar archive with PHP, for contrib/matrix/matrix.py.
//
//     php extract.php ARCHIVE DEST phar
//     php -d include_path=DIR extract.php ARCHIVE DEST archive_tar
//
// `phar` is ext/phar's PharData, as Composer's TarDownloader calls it. `archive_tar` is PEAR's
// Archive_Tar, whose files sources.txt lists, from the include path. An error is printed on
// stderr, with status 1.
[, $archive, $dest, $mode] = $argv;
if ($mode === 'phar') {
    try {
        (new PharData($archive))->extractTo($dest, null, true);
    } catch (Exception $e) {
        fwrite(STDERR, get_class($e) . ': ' . $e->getMessage() . "\n");
        exit(1);
    }
} else {
    require 'Archive/Tar.php';
    $tar = new Archive_Tar($archive);
    if (!$tar->extract($dest)) {
        fwrite(STDERR, ($tar->error_object ? $tar->error_object->getMessage() : 'extract failed') . "\n");
        exit(1);
    }
}
