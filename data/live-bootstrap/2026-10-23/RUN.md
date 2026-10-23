# Scan of 171 live-bootstrap tarballs, 2026-10-23

```console
$ git clone https://github.com/fosslinux/live-bootstrap
$ python -I scanner/live_bootstrap_list.py live-bootstrap > live-bootstrap.jsonl
$ grep -v '\.tar\.lzma"' live-bootstrap.jsonl > sample.jsonl
$ python -I scanner/run.py scan sample.jsonl results.jsonl --untar ~/untar --jobs 8
$ python -I scanner/report.py --title "Scan of 171 live-bootstrap tarballs" results.jsonl > REPORT.md
```

- Scanner: `tarscan.py` version `25bfa32e6e71`, the same as for the Spack scan of 2026-10-23.
- Packages: live-bootstrap `b1ceced7ea8a819a26f23796f6dd7ae8496a33a4` (2026-09-17). Its
  `steps/*/sources` list 426 files, of which 171 distinct tarballs of 74 packages: the rest are
  text files, zip files and duplicates. Every tarball is scanned, not a sample. 23 are made by
  live-bootstrap's `mirror.sh` with `git archive` (mostly gnulib), and have no upstream URL.
- untar: `464647b69df6c3bf53ab740bff40281af407e342` (0.2.0), `untar.py` version `b2cd8ae76874`.
  This is a later untar than the Spack scans used, so `--reuse` of their results does not apply;
  only 3 tarballs are in both anyway (bzip2 1.0.8 and patch 2.8 in 2026-10-23, musl 1.1.24 in
  2026-10-23-b), and their features are the same.
- Platform: Ubuntu 26.04 (Linux 7.0) on x86_64, Python 3.14.4. untar extracted to tmpfs, which is
  case-sensitive, so no failures are caused by the filesystem.

Downloads: every tarball came from the first of its URLs, the live-bootstrap mirror
`live-bootstrap.stikonas.eu`, in about 40 seconds in total. Its bytes match the sha256 that
live-bootstrap pins, also for the tarballs that `git archive` makes. The upstream URLs (72 of
them on mirrors.kernel.org/gnu) were not needed, and were not checked.

`latest` marks, for each package, the last tarball that a step in `steps/manifest` uses: the
version that the bootstrapped system ends up with. Two tarballs are only used by steps that are
not in the manifest (guile 3.0.9, perl 5.10.1).

Two tarballs are `.tar.lzma` (coreutils 6.10, libtool 2.2.4), in the LZMA-alone format, which
has no magic and which `tarscan.py` does not detect. They are left out of `sample.jsonl`. Their
rows in `results.jsonl` were made outside `run.py`: the files were downloaded from the same
mirror, checked against their sha256, decompressed with Python's `lzma` (`FORMAT_ALONE`), and
passed to `tarscan.scan` and untar as `run.py` does. These rows have
`"decompressed_by": "python lzma FORMAT_ALONE, outside run.py"`.

## Notes

- untar extracts all 171.
- The tarballs are older than Spack's: v7 headers in 61 of 171 (Spack: 125 of 1991), and number
  fields with leading spaces in 8, all from 1993 to 2001: gzip 1.2.4, diffutils 2.7, gawk 3.0.4,
  tar 1.12, perl 5.004_05 and 5.005_03, grep 2.4 and bash 2.05b.
- Names that some filesystems cannot hold, in 7 tarballs: `Configure` and `configure` in perl 5.003
  and 5.004_05, `filexp.U` and `Filexp.U` in metaconfig, the netfilter headers of
  linux 4.14.336 (`xt_mark.h` and `xt_MARK.h`), `aux.sh` in perl 5.000 and 5.003, and names
  ending in a dot or space in perl 5.000 and Python 2.3.7. Extracting these fails on macOS or
  Windows.
- Nothing from the catalogue's framing or name ambiguities occurs: no GNU sparse, multivolume or
  volume headers, no pax `size`, no duplicate paths, no data after the end-of-archive marker.
