# Scan of all 171 live-bootstrap tarballs

- tarballs: 171, scanned: 171 (74 latest versions, 97 older)
- not downloaded: 0, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 171
- copied from other scans with `--reuse`: 0, read from `--cache`: 0; sources by host: live-bootstrap.stikonas.eu 171
- size: 1.1 GB compressed
- origins: gnu 98, other 24, cpan 20, github-archive 17, github-release 11, gitlab 1
- producers: v7 61, git archive 49, GNU format 42, ustar 17, GNU tar (pax) 2
- compression: gzip 82, xz 54, bzip2 33, lzma 2
- scanner stopped early: 0

## untar

Rejects 0 of 171 (0.0%); 0 of 74 latest versions (0.0%).

| reason | tarballs | latest | origins | producers | examples |
|---|---|---|---|---|---|

## Features

Number of tarballs with each feature, of which latest versions; their origins, producers and median mtime years, and what untar did with them.

| feature | tarballs | latest | origins | producers | years | untar rejects | examples |
|---|---:|---:|---|---|---|---:|---|
| `type.nul` | 61 | 29 | gnu 50, other 6, github-release 5 | v7 61 | 1993–2026 | 0 | make@3.82 `make-3.82/vmsfunctions.c`; gzip@1.2.4 `gzip-1.2.4/README` |
| `v7.bytes-after-linkname` | 37 | 20 | gnu 30, other 5, github-release 2 | v7 37 | 2003–2026 | 0 | make@3.82 `make-3.82/`; m4@1.4.7 `m4-1.4.7/` |
| `number.gid.leading-space` | 8 | 0 | gnu 6, cpan 2 | GNU format 5, v7 3 | 1993–2001 | 0 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.mode.leading-space` | 8 | 0 | gnu 6, cpan 2 | GNU format 5, v7 3 | 1993–2001 | 0 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.mtime.leading-space` | 8 | 0 | gnu 6, cpan 2 | GNU format 5, v7 3 | 1993–2001 | 0 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.size.leading-space` | 8 | 0 | gnu 6, cpan 2 | GNU format 5, v7 3 | 1993–2001 | 0 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.uid.leading-space` | 8 | 0 | gnu 6, cpan 2 | GNU format 5, v7 3 | 1993–2001 | 0 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `name.fills-field` | 6 | 4 | gnu 4, other 2 | GNU format 2, GNU tar (pax) 2, ustar 1 | 2009–2025 | 0 | texinfo@7.2 `texinfo-7.2/tp/t/results/init_files_tests/documentation_exam`; linux@4.14.336 `linux-4.14.336/Documentation/devicetree/bindings/interrupt-c` |
| `platform.case-collision` | 5 | 1 | github-archive 3, cpan 1, other 1 | git archive 4, GNU format 1 | 1996–2024 | 0 | perl@5.003 `perl5-perl-5.003/configure`; perl@5.004_05 `perl5.004_05/Configure` |
| `platform.windows-reserved-name` | 3 | 1 | github-archive 2, other 1 | git archive 3 | 1994–2024 | 0 | perl@5.000 `perl5-perl-5.000/hints/aux.sh`; perl@5.003 `perl5-perl-5.003/hints/aux.sh` |
| `ustar.prefix` | 3 | 3 | gnu 1, other 1, github-archive 1 | git archive 2, ustar 1 | 2021–2024 | 0 | texinfo@7.2 `split_test_before_first_node.info`; linux@4.14.336 `samsung,exynos4210-combiner.txt` |
| `name.dir-without-trailing-slash` | 2 | 1 | github-release 1, cpan 1 | ustar 1, GNU format 1 | 2011–2019 | 0 | oyacc@6.6 `oyacc-6.6`; perl@5.15.7 `perl-5.15.7` |
| `name.non-ascii` | 2 | 2 | other 1, gnu 1 | v7 1, GNU tar (pax) 1 | 2008–2025 | 0 | kbd@1.15 `kbd-1.15/doc/utf/♪♬`; gcc@15.2.0 `gcc-15.2.0/gcc/testsuite/go.test/test/fixedbugs/issue27836.d` |
| `platform.windows-trailing-dot-or-space` | 2 | 0 | github-archive 1, other 1 | git archive 1, GNU format 1 | 1994–2002 | 0 | perl@5.000 `perl5-perl-5.000/vms/makefile.`; Python@2.3.7 `Python-2.3.7/Mac/IDE scripts/Search Python Documentation...` |

## Fingerprints

- magic (tarballs using each): posix 68, v7 61, gnu 42
- size (tarballs using each): dn 154, ds 9, sds 8
- mode (tarballs using each): dn 154, dsn 14, sdsn 8
- checksum (tarballs using each): dns 110, dn 53, sdns 8
- pax_header_name (tarballs using each): */PaxHeaders/* 2, * 2, */PaxHeaders 2, */PaxHead 2, */PaxHeader 2, */PaxHeaders/ 2, */PaxHe 2, */PaxH 1, */PaxHea 1
- extended_sequence (tarballs using each): - 169, L 3, x 2
- gnu_long_name (tarballs using each): ././@LongLink 3
- end (tarballs using each): padded-to-10240 167, unpadded 4
- zero_blocks_after_end (tarballs using each): 7 18, 18 15, 2 14, 8 13, 17 12, 0 11, 11 10, 14 8, 4 8, 5 8, 9 7, 10 7
- pax_keys (tarballs using each): mtime 2, atime 2, ctime 2, path 2
- pax_global_keys (tarballs using each): comment 49
- compression layer: 
