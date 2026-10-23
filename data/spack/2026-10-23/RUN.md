# Scan of 2000 Spack tarballs, 2026-10-23

```console
$ spack python scanner/spack_list.py > spack.jsonl
$ python -I scanner/run.py sample spack.jsonl 2000 0 > sample.jsonl
$ python -I scanner/run.py scan sample.jsonl results.jsonl --untar ~/untar --jobs 8
$ python -I scanner/report.py results.jsonl "Scan of 2000 Spack tarballs" > REPORT.md
```

- Scanner: `tarscan.py` version `25bfa32e6e71`, as committed with this data.
- Packages: spack-packages `73b099d5c1118951de3ac69b91e6f73afc41690e` (2026-10-19), listed with
  Spack `37c7f2646a`: 38,284 tarballs of 7,835 packages, without packages that need a manual
  download.
- untar: `2305390138cf436059b89b7b15146dc5213a3ba5`, `untar.py` version `51a9c3aa565c`.
- Platform: macOS 15 (Darwin 24.6) on arm64, Python 3.9.6, on APFS that is case-insensitive.
  untar's failures on names that only collide there are counted apart in REPORT.md.

The first version of this dataset left out the 50 tarballs whose URL is on ftp://, by mistake.
The sample of the corrected list differs in 7 tarballs: they were scanned, the 1,993 others
copied from the first version, and the 9 that could not be downloaded tried again.

The scan ran with a `run.py` from just before its first commit, and its rows were converted to
the current format afterwards:

- the list fields `mirror` (a path on mirror.spack.io) became `urls`, and `source` (`mirror` or
  `upstream`) the URL it names,
- `scanner` and `untar` were added: `tarscan.py` and `untar.py` did not change during the run,
- 11 tarballs where untar failed with `FileExistsError` were recorded as `untar_skipped`,
  because the child process did not yet catch `OSError`. They are `untar_error` now, as the
  current `run.py` records them: all 11 have names that collide on a case-insensitive filesystem.

A first run on a different sample of 1976 tarballs, with an earlier scanner, found 5 that untar
rejects with its own errors: ruby 3.3.5 (no end-of-archive marker, like every Ruby release from
2.6 on), cdd 0.61a (a v7 archive with directories named like files, `cdd-061/`, and data after the
end-of-archive marker), hama 0.7.1 (data after the end-of-archive marker), glibmm 2.16.0 (the
whole archive twice, the second copy after the first's end-of-archive marker) and
commons-logging 1.1.1 (corrupt: a zero block in place of a header). Its results are not included.
