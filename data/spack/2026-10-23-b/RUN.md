# Second scan of 1989 Spack tarballs, 2026-10-23

The tarballs of the first, unpublished scan of 2026-10-23, scanned again with the current
scanner. That scan sampled with `random.shuffle`, which the current `run.py sample` no longer
does, so `sample.jsonl` is the sample itself: 2000 tarballs, without the 11 of packages that
need a manual download. It overlaps with [2026-10-23](../2026-10-23) in 221 tarballs. The
results of 220 tarballs were copied from there (`reused`), all others downloaded again.

```console
$ python -I scanner/run.py scan sample.jsonl results.jsonl --untar ~/untar --jobs 8 \
      --reuse ../2026-10-23/results.jsonl
$ python -I scanner/report.py --title "Second scan of 1989 Spack tarballs" results.jsonl > REPORT.md
```

- Scanner: `tarscan.py` version `25bfa32e6e71`.
- Packages: spack-packages `73b099d5c1118951de3ac69b91e6f73afc41690e` (2026-10-19), listed with
  Spack `37c7f2646a`.
- untar: `2305390138cf436059b89b7b15146dc5213a3ba5`, `untar.py` version `51a9c3aa565c`.
- Platform: macOS 15 (Darwin 24.6) on arm64, Python 3.9.6, on APFS that is case-insensitive.

As a sample, it is half latest versions and half older versions of distinct packages, like
2026-10-23, but drawn in a different order, so the two are independent samples of the same
population.
