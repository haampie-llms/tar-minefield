# All scans

Rates are per dataset. Counts below are of the distinct tarballs of all datasets.

| dataset | tarballs | scanned | latest | untar rejects | latest | filesystem only |
|---|---|---|---|---|---|---|
| live-bootstrap/2026-10-23 | 171 | 171 | 74 | 0 (0.00%) | 0 (0.00%) | 0 |
| spack/2026-10-23-b | 1989 | 1981 | 992 | 8 (0.40%) | 6 (0.60%) | 10 |
| spack/2026-10-23 | 2000 | 1990 | 994 | 0 (0.00%) | 0 (0.00%) | 12 |

- tarballs: 3936, scanned: 3919 (1920 latest versions, 1999 older)
- not downloaded: 17, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 3905
- origins: pypi 1187, github-archive 1004, other 607, cran/bioconductor 562, cpan 186, github-release 179, gnu 142, gitlab 52
- producers: GNU format 1318, git archive 1134, Python tarfile (pax) 752, ustar 349, v7 297, GNU tar (pax) 49, libarchive (pax) 11, posix-version-0000 8, star 1
- compression: gzip 3649, xz 148, bzip2 114, none 6
- scanner stopped early: 1
  - commons-logging@1.1.1: invalid checksum at offset 3452928

Failed only because of the case-insensitive filesystem of the scanning machine, not counted as rejections: 21, 6 latest (libbigwig@0.4.7; launchmon@1.2.1; environment-modules@5.7.0; linux-headers@4.9.10; py-healpy@1.13.0; scafacos@1.0.1).

## untar

Rejects 8 of 3919 (0.2%); 6 of 1920 latest versions (0.3%).

| reason | tarballs | latest | origins | producers | examples |
|---|---|---|---|---|---|
| FileExistsError: [Errno N] File exists: '…' | 3 | 3 | other 3 | git archive 1, GNU format 1, posix-version-0000 1 | notmuch@0.23.7; swftools@0.9.2; sqoop@1.99.7 |
| Archive contains data after the end-of-archive marker | 3 | 2 | other 3 | v7 2, posix-version-0000 1 | cdd@0.61a; hama@0.7.1; glibmm@2.16.0 |
| Archive is truncated | 1 | 1 | other 1 | ustar 1 | ruby@3.3.5 |
| Archive contains a lone zero block | 1 | 0 | other 1 | posix-version-0000 1 | commons-logging@1.1.1 |

## Features

Number of tarballs with each feature, of which latest versions; their origins, producers and median mtime years, and what untar did with them.

| feature | tarballs | latest | origins | producers | years | untar rejects | examples |
|---|---|---|---|---|---|---|---|
| `name.fills-field` | 359 | 152 | github-archive 175, pypi 73, other 52 | git archive 197, GNU format 65, Python tarfile (pax) 61 | 1970–2026 | 7 | texinfo@7.2 `texinfo-7.2/tp/t/results/init_files_tests/documentation_exam`; linux@4.14.336 `linux-4.14.336/Documentation/devicetree/bindings/interrupt-c` |
| `ustar.prefix` | 324 | 145 | github-archive 235, other 26, cpan 26 | git archive 266, ustar 54, libarchive (pax) 4 | 2006–2026 | 7 | texinfo@7.2 `split_test_before_first_node.info`; linux@4.14.336 `samsung,exynos4210-combiner.txt` |
| `type.nul` | 307 | 152 | other 163, gnu 76, github-release 55 | v7 295, GNU format 12 | 1970–2026 | 4 | make@3.82 `make-3.82/vmsfunctions.c`; gzip@1.2.4 `gzip-1.2.4/README` |
| `v7.bytes-after-linkname` | 231 | 111 | other 140, gnu 49, github-release 41 | v7 231 | 1970–2026 | 3 | make@3.82 `make-3.82/`; m4@1.4.7 `m4-1.4.7/` |
| `number.size.leading-space` | 52 | 33 | cpan 34, other 11, gnu 7 | ustar 32, posix-version-0000 8, v7 6 | 1993–2023 | 4 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `name.non-ascii` | 40 | 18 | github-archive 25, other 8, pypi 4 | git archive 27, GNU format 5, Python tarfile (pax) 4 | 2008–2026 | 1 | kbd@1.15 `kbd-1.15/doc/utf/♪♬`; gcc@15.2.0 `gcc-15.2.0/gcc/testsuite/go.test/test/fixedbugs/issue27836.d` |
| `name.dir-without-trailing-slash` | 33 | 26 | cpan 30, other 2, github-release 1 | ustar 30, GNU format 2, GNU tar (pax) 1 | 2003–2026 | 0 | oyacc@6.6 `oyacc-6.6`; perl@5.15.7 `perl-5.15.7` |
| `platform.case-collision` | 27 | 8 | github-archive 10, other 10, github-release 5 | git archive 16, GNU format 5, Python tarfile (pax) 3 | 1996–2026 | 21 | perl@5.003 `perl5-perl-5.003/configure`; perl@5.004_05 `perl5.004_05/Configure` |
| `number.gid.no-digits` | 24 | 13 | pypi 20, other 4 | GNU format 17, ustar 5, posix-version-0000 2 | 1985–2025 | 0 | giraph@1.2.0 `giraph-1.2.0/bin/`; py-tokenizers@0.23.1 `tokenizers-0.23.1/PKG-INFO` |
| `number.uid.no-digits` | 24 | 13 | pypi 20, other 4 | GNU format 17, ustar 5, posix-version-0000 2 | 1985–2025 | 0 | giraph@1.2.0 `giraph-1.2.0/bin/`; py-tokenizers@0.23.1 `tokenizers-0.23.1/PKG-INFO` |
| `number.gid.leading-space` | 20 | 7 | other 11, gnu 7, cpan 2 | posix-version-0000 8, v7 6, GNU format 6 | 1993–2020 | 4 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.mode.leading-space` | 20 | 7 | other 11, gnu 7, cpan 2 | posix-version-0000 8, v7 6, GNU format 6 | 1993–2020 | 4 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.uid.leading-space` | 20 | 7 | other 11, gnu 7, cpan 2 | posix-version-0000 8, v7 6, GNU format 6 | 1993–2020 | 4 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `platform.windows-reserved-name` | 15 | 4 | other 10, github-archive 3, gitlab 2 | git archive 8, GNU format 6, v7 1 | 1994–2025 | 3 | perl@5.000 `perl5-perl-5.000/hints/aux.sh`; perl@5.003 `perl5-perl-5.003/hints/aux.sh` |
| `number.uid.base256` | 14 | 11 | pypi 8, other 4, github-release 1 | GNU format 11, libarchive (pax) 3 | 2015–2025 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; mxnet@1.9.1 `apache-mxnet-src-1.9.1-incubating/` |
| `name.leading-dot-slash` | 13 | 8 | other 10, gitlab 3 | GNU format 12, ustar 1 | 2003–2026 | 0 | dhpmm-f@alpha `./._DHPMM_F_alpha`; starlight@313 `./` |
| `number.gid.base256` | 13 | 10 | pypi 8, other 4, github-release 1 | GNU format 11, libarchive (pax) 2 | 2015–2025 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; py-lightly-utils@0.0.2 `lightly_utils-0.0.2/` |
| `platform.windows-invalid-character` | 12 | 7 | other 5, github-archive 4, github-release 2 | git archive 7, GNU format 4, Python tarfile (pax) 1 | 2007–2025 | 2 | fermisciencetools@11r5p3 `ScienceTools-v11r5p3-fssc-20180124-x86_64-unknown-linux-gnu-`; notmuch@0.23.7 `notmuch-0.23.7/test/corpora/default/01:2,` |
| `number.mtime.leading-space` | 10 | 1 | gnu 7, cpan 2, other 1 | GNU format 6, v7 4 | 1993–2001 | 1 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `magic.posix-with-odd-version` | 8 | 5 | other 8 | posix-version-0000 8 | 2007–2020 | 3 | giraph@1.2.0 `giraph-1.2.0/`; hama@0.7.1 `hama-0.7.1/hama-commons-0.7.1.jar` |
| `tree.dir-after-contents` | 8 | 5 | other 5, cpan 3 | ustar 4, posix-version-0000 2, GNU tar (pax) 2 | 2014–2023 | 1 | mitofates@1.2 `MitoFates/bin/Setting/`; sqoop@1.99.7 `sqoop-1.99.7/common/` |
| `symlink.absolute` | 7 | 4 | github-archive 4, other 2, github-release 1 | git archive 6, GNU format 1 | 2017–2025 | 0 | crtm-fix@3.1.2.0 `fix_REL-3.1.2.0/fix/CloudCoeff/netCDF/CloudCoeff_Inspect`; mothur@1.48.0 `mothur-1.48.0/Products/Debug/mothur 2` |
| `tree.duplicate.dir-dir` | 5 | 1 | github-release 3, other 2 | git archive 4, ustar 1 | 2020–2023 | 0 | swipl@8.2.0 `swipl-8.2.0/bench/`; helics@3.5.2 `ThirdParty/asio/` |
| `pax-global.after-members` | 4 | 1 | other 2, github-release 2 | git archive 4 | 2020–2023 | 0 | swipl@8.2.0 `pax_global_header`; prometheus-cpp@1.2.4 `pax_global_header` |
| `platform.windows-trailing-dot-or-space` | 4 | 1 | github-archive 2, other 2 | git archive 2, GNU format 2 | 1994–2023 | 0 | perl@5.000 `perl5-perl-5.000/vms/makefile.`; Python@2.3.7 `Python-2.3.7/Mac/IDE scripts/Search Python Documentation...` |
| `pax.LIBARCHIVE.creationtime` | 3 | 2 | github-release 1, other 1, cpan 1 | libarchive (pax) 3 | 2017–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; gatk@3.8.0 `GenomeAnalysisTK-3.8-0-ge9d806836/` |
| `pax.nul-in-value.SCHILY.xattr.*` | 3 | 3 | github-release 1, cpan 1, other 1 | libarchive (pax) 3 | 2022–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/docs/user/examples/magma-2d/figs/PaxHeader/step`; perl-module-find@0.16 `PaxHeader/Module-Find-0.16` |
| `tree.duplicate.file-file` | 3 | 3 | other 3 | git archive 1, GNU format 1, posix-version-0000 1 | 2011–2017 | 3 | notmuch@0.23.7 `notmuch-0.23.7/version`; swftools@0.9.2 `swftools-0.9.2/lib/kdtree.c` |
| `end.data-after` | 2 | 2 | other 2 | v7 1, posix-version-0000 1 | 1997–2016 | 2 | cdd@0.61a `cdd-061/ine/verifyinput2.ine`; hama@0.7.1 `hama-0.7.1/docs/diagram/yarn-hama-diagram.pptx` |
| `linkname.no-nul` | 2 | 1 | github-release 2 | GNU format 1, git archive 1 | 2025–2025 | 0 | code-server@4.96.4 `code-server-4.96.4-linux-amd64/lib/vscode/node_modules/@vsco`; gocryptfs@2.5.1 `gocryptfs_v2.5.1_src/tests/example_filesystems/v0.4/TBIgdfhD` |
| `name.control-character` | 2 | 0 | github-archive 1, github-release 1 | git archive 2 | 2022–2025 | 0 | apktool@2.6.1 `Apktool-2.6.1/brut.apktool/apktool-lib/src/test/resources/aa`; gocryptfs@2.5.1 `gocryptfs_v2.5.1_src/tests/fsck/malleable_base64/27AG8t-XZH7` |
| `end.archive-after` | 1 | 0 | other 1 | v7 1 | 2008–2008 | 1 | glibmm@2.16.0 `glibmm-2.16.0/` |
| `end.missing` | 1 | 1 | other 1 | ustar 1 | 2024–2024 | 1 | ruby@3.3.5 `ruby-3.3.5/yjit.rbinc` |
| `end.zero-block-before-member` | 1 | 0 | other 1 | posix-version-0000 1 | 2007–2007 | 1 | commons-logging@1.1.1 `commons-logging-1.1.1/site/xref-test/stylesheet.css` |
| `format.star` | 1 | 0 | gnu 1 | star 1 | 2010–2010 | 0 | ncurses@5.9 `ncurses-5.9/` |
| `hardlink.to-itself` | 1 | 1 | other 1 | GNU format 1 | 2018–2018 | 0 | atlas@3.11.41 `ATLAS/tune/blas/gemm/uammgen.c` |
| `hardlink.to-symlink` | 1 | 1 | other 1 | GNU format 1 | 2020–2020 | 0 | octa@8.4 `OCTA84/Python37/bin/python` |
| `name.backslash` | 1 | 1 | github-archive 1 | git archive 1 | 2024–2024 | 0 | systemd@256.7 `systemd-256.7/test/fuzz/fuzz-unit-file/dm-back\x2dslash.swap` |
| `name.dot` | 1 | 1 | other 1 | GNU format 1 | 2019–2019 | 0 | starlight@313 `./` |
| `name.double-slash` | 1 | 0 | github-release 1 | GNU format 1 | 2019–2019 | 0 | shapemapper@2.1.5 `shapemapper-2.1.5-source-only//shapemapper` |
| `name.not-nfc` | 1 | 0 | other 1 | libarchive (pax) 1 | 2022–2022 | 0 | go-bootstrap@1.17.13 `go/test/fixedbugs/issue27836.dir/Äfoo.go` |
| `name.trailing-slash-on-file` | 1 | 1 | other 1 | v7 1 | 1997–1997 | 1 | cdd@0.61a `cdd-061/` |
| `pax.LIBARCHIVE.symlinktype` | 1 | 1 | other 1 | libarchive (pax) 1 | 2023–2023 | 0 | win-file@5.45 `file/src/file-FILE5_45/src/.libs/libmagic.la` |
| `pax.newline-in-value.SCHILY.xattr.*` | 1 | 1 | cpan 1 | libarchive (pax) 1 | 2022–2022 | 0 | perl-module-find@0.16 `PaxHeader/Module-Find-0.16` |
| `tree.duplicate.file-hardlink` | 1 | 1 | other 1 | GNU format 1 | 2018–2018 | 0 | atlas@3.11.41 `ATLAS/tune/blas/gemm/uammgen.c` |
| `tree.under-file` | 1 | 1 | other 1 | v7 1 | 1997–1997 | 1 | cdd@0.61a `cdd-061/COPYING` |

## Fingerprints

- magic (tarballs using each): posix 2295, gnu 1323, v7 297, posix-version-0000 8, star 1
- size (tarballs using each): dn 3732, ds 133, sdn 32, sds 20, dsn 2
- mode (tarballs using each): dn 3764, dsn 140, sdsn 20, ds 10
- checksum (tarballs using each): dns 2651, dn 1216, sdns 51, dsn 2, ds 2, sdsn 1, x 1
- pax_header_name (tarballs using each): ././@PaxHeader 752, */PaxHeaders.N/* 30, ./PaxHeaders.N/* 29, H.paxheader 25, */PaxHeaders/* 17, ./PaxHeaders/* 15, */PaxHeader/* 10, PaxHeader/* 5, * 4, */PaxHeader 3, */PaxHe 3, */PaxHea 3
- extended_sequence (tarballs using each): - 3205, x 837, L 100, KL 1
- gnu_long_name (tarballs using each): ././@LongLink 100
- end (tarballs using each): padded-to-10240 3734, unpadded 183
- zero_blocks_after_end (tarballs using each): 0 401, 15 221, 13 200, 17 196, 14 194, 10 194, 7 192, 5 190, 18 189, 19 189, 11 187, 6 183
- pax_keys (tarballs using each): mtime 783, path 156, atime 51, ctime 50, uid 12, gid 11, LIBARCHIVE.xattr.* 4, SCHILY.xattr.* 4, LIBARCHIVE.creationtime 3, linkpath 2, SCHILY.dev 2, SCHILY.ino 2
- pax_global_keys (tarballs using each): comment 1134
- compression layer: several streams 1, trailing zeros 1
