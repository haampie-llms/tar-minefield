# Second scan of 1989 Spack tarballs

- tarballs: 1989, scanned: 1981 (992 latest versions, 989 older)
- not downloaded: 8, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 1973
- origins: pypi 621, github-archive 519, cran/bioconductor 305, other 299, github-release 100, cpan 83, gitlab 28, gnu 26
- producers: GNU format 697, git archive 575, Python tarfile (pax) 369, ustar 178, v7 123, GNU tar (pax) 25, libarchive (pax) 8, posix-version-0000 5, star 1
- compression: gzip 1885, xz 53, bzip2 40, none 3
- scanner stopped early: 1
  - commons-logging@1.1.1: invalid checksum at offset 3452928

Failed only because of the case-insensitive filesystem of the scanning machine, not counted as rejections: 10, 3 latest (libbigwig@0.4.7; launchmon@1.2.1; environment-modules@5.7.0; linux-headers@4.9.10; py-healpy@1.13.0; scafacos@1.0.1).

## untar

Rejects 8 of 1981 (0.4%); 6 of 992 latest versions (0.6%).

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
| `name.fills-field` | 183 | 73 | github-archive 88, pypi 37, other 27 | git archive 98, GNU format 36, Python tarfile (pax) 31 | 1970–2026 | 4 | typescript@5.8.3 `TypeScript-5.8.3/tests/baselines/reference/ClassDeclarationW`; serenity@1.6.1 `serenity-1.6.1/data/testresources/TestSystem_H2_6_31Gs_BP86/` |
| `ustar.prefix` | 174 | 73 | github-archive 122, other 17, cpan 15 | git archive 140, ustar 30, libarchive (pax) 4 | 2009–2026 | 5 | typescript@5.8.3 `AmbientModuleAndAmbientFunctionWithTheSameNameAndCommonRoot.`; serenity@1.6.1 `TestSystem_Diaziridine_HF_AUG_CC_PVDZ.FockMatrix.res.h5` |
| `type.nul` | 125 | 68 | other 74, github-release 28, gnu 18 | v7 121, GNU format 4 | 1970–2026 | 2 | fonttosfnt@1.2.3 `fonttosfnt-1.2.3/read.c`; libxfont2@2.0.7 `libXfont2-2.0.7/xfont2.pc.in` |
| `v7.bytes-after-linkname` | 97 | 47 | other 60, github-release 23, gnu 13 | v7 97 | 1970–2026 | 1 | fonttosfnt@1.2.3 `fonttosfnt-1.2.3/`; dri2proto@2.8 `dri2proto-2.8/` |
| `number.size.leading-space` | 27 | 20 | cpan 19, other 8 | ustar 19, posix-version-0000 5, v7 3 | 1997–2023 | 4 | giraph@1.2.0 `giraph-1.2.0/`; perl-uri-find@20160806 `URI-Find-20160806` |
| `name.non-ascii` | 24 | 10 | github-archive 14, other 6, pypi 2 | git archive 16, GNU format 4, Python tarfile (pax) 2 | 2016–2026 | 1 | flac@1.5.0 `flac-1.5.0/test/flac-to-flac-metadata-test-files/🤔.flac`; py-meson-python@0.19.0 `meson_python-0.19.0/tests/packages/encoding/テスト.py` |
| `name.dir-without-trailing-slash` | 19 | 15 | cpan 18, other 1 | ustar 18, GNU tar (pax) 1 | 2003–2026 | 0 | perl-uri-find@20160806 `URI-Find-20160806`; perl-catalyst-action-rest@1.21 `Catalyst-Action-REST-1.21` |
| `number.gid.no-digits` | 10 | 7 | pypi 8, other 2 | GNU format 7, ustar 2, posix-version-0000 1 | 1985–2025 | 0 | giraph@1.2.0 `giraph-1.2.0/bin/`; py-tokenizers@0.23.1 `tokenizers-0.23.1/PKG-INFO` |
| `number.uid.base256` | 10 | 7 | pypi 6, other 3, github-release 1 | GNU format 8, libarchive (pax) 2 | 2015–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; mxnet@1.9.1 `apache-mxnet-src-1.9.1-incubating/` |
| `number.uid.no-digits` | 10 | 7 | pypi 8, other 2 | GNU format 7, ustar 2, posix-version-0000 1 | 1985–2025 | 0 | giraph@1.2.0 `giraph-1.2.0/bin/`; py-tokenizers@0.23.1 `tokenizers-0.23.1/PKG-INFO` |
| `platform.case-collision` | 10 | 3 | github-release 4, github-archive 3, other 2 | git archive 5, GNU format 2, Python tarfile (pax) 2 | 2017–2026 | 10 | libbigwig@0.4.7 `libBigWig-0.4.7/docs/html/bigWigIO_8h.html`; launchmon@1.2.1 `launchmon-1.2.1/install/` |
| `number.gid.base256` | 9 | 6 | pypi 6, other 2, github-release 1 | GNU format 7, libarchive (pax) 2 | 2015–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; py-lightly-utils@0.0.2 `lightly_utils-0.0.2/` |
| `number.gid.leading-space` | 8 | 5 | other 8 | posix-version-0000 5, v7 3 | 1997–2020 | 4 | giraph@1.2.0 `giraph-1.2.0/`; cdd@0.61a `cdd-061/` |
| `number.mode.leading-space` | 8 | 5 | other 8 | posix-version-0000 5, v7 3 | 1997–2020 | 4 | giraph@1.2.0 `giraph-1.2.0/`; cdd@0.61a `cdd-061/` |
| `number.uid.leading-space` | 8 | 5 | other 8 | posix-version-0000 5, v7 3 | 1997–2020 | 4 | giraph@1.2.0 `giraph-1.2.0/`; cdd@0.61a `cdd-061/` |
| `platform.windows-invalid-character` | 7 | 3 | other 4, github-archive 2, github-release 1 | GNU format 4, git archive 3 | 2007–2021 | 1 | fermisciencetools@11r5p3 `ScienceTools-v11r5p3-fssc-20180124-x86_64-unknown-linux-gnu-`; notmuch@0.23.7 `notmuch-0.23.7/test/corpora/default/01:2,` |
| `name.leading-dot-slash` | 6 | 4 | other 4, gitlab 2 | GNU format 5, ustar 1 | 2017–2024 | 0 | dhpmm-f@alpha `./._DHPMM_F_alpha`; starlight@313 `./` |
| `magic.posix-with-odd-version` | 5 | 3 | other 5 | posix-version-0000 5 | 2007–2016 | 3 | giraph@1.2.0 `giraph-1.2.0/`; hama@0.7.1 `hama-0.7.1/hama-commons-0.7.1.jar` |
| `platform.windows-reserved-name` | 5 | 1 | other 3, github-archive 1, gitlab 1 | git archive 3, GNU format 2 | 2017–2025 | 1 | lvm2@2.03.14 `LVM2.2.03.14/test/lib/aux.sh`; linux-headers@4.9.10 `linux-4.9.10/drivers/gpu/drm/nouveau/nvkm/subdev/i2c/aux.c` |
| `tree.dir-after-contents` | 5 | 2 | other 3, cpan 2 | ustar 3, posix-version-0000 1, GNU tar (pax) 1 | 2014–2023 | 1 | mitofates@1.2 `MitoFates/bin/Setting/`; sqoop@1.99.7 `sqoop-1.99.7/common/` |
| `tree.duplicate.dir-dir` | 4 | 1 | other 2, github-release 2 | git archive 3, ustar 1 | 2020–2023 | 0 | swipl@8.2.0 `swipl-8.2.0/bench/`; helics@3.5.2 `ThirdParty/asio/` |
| `pax-global.after-members` | 3 | 1 | other 2, github-release 1 | git archive 3 | 2020–2023 | 0 | swipl@8.2.0 `pax_global_header`; prometheus-cpp@1.2.4 `pax_global_header` |
| `pax.nul-in-value.SCHILY.xattr.*` | 3 | 3 | github-release 1, cpan 1, other 1 | libarchive (pax) 3 | 2022–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/docs/user/examples/magma-2d/figs/PaxHeader/step`; perl-module-find@0.16 `PaxHeader/Module-Find-0.16` |
| `symlink.absolute` | 3 | 2 | github-archive 2, other 1 | git archive 2, GNU format 1 | 2022–2025 | 0 | crtm-fix@3.1.2.0 `fix_REL-3.1.2.0/fix/CloudCoeff/netCDF/CloudCoeff_Inspect`; mothur@1.48.0 `mothur-1.48.0/Products/Debug/mothur 2` |
| `tree.duplicate.file-file` | 3 | 3 | other 3 | git archive 1, GNU format 1, posix-version-0000 1 | 2011–2017 | 3 | notmuch@0.23.7 `notmuch-0.23.7/version`; swftools@0.9.2 `swftools-0.9.2/lib/kdtree.c` |
| `end.data-after` | 2 | 2 | other 2 | v7 1, posix-version-0000 1 | 1997–2016 | 2 | cdd@0.61a `cdd-061/ine/verifyinput2.ine`; hama@0.7.1 `hama-0.7.1/docs/diagram/yarn-hama-diagram.pptx` |
| `pax.LIBARCHIVE.creationtime` | 2 | 1 | github-release 1, other 1 | libarchive (pax) 2 | 2017–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; gatk@3.8.0 `GenomeAnalysisTK-3.8-0-ge9d806836/` |
| `platform.windows-trailing-dot-or-space` | 2 | 1 | github-archive 1, other 1 | git archive 1, GNU format 1 | 2016–2023 | 0 | hyphy@2.5.51hf `hyphy-2.5.51hf/res/SubstitutionClasses/CodonEFV/Observed Nuc`; nauty@2.6r7 `nauty26r7/This_is_nauty26r7.` |
| `end.archive-after` | 1 | 0 | other 1 | v7 1 | 2008–2008 | 1 | glibmm@2.16.0 `glibmm-2.16.0/` |
| `end.missing` | 1 | 1 | other 1 | ustar 1 | 2024–2024 | 1 | ruby@3.3.5 `ruby-3.3.5/yjit.rbinc` |
| `end.zero-block-before-member` | 1 | 0 | other 1 | posix-version-0000 1 | 2007–2007 | 1 | commons-logging@1.1.1 `commons-logging-1.1.1/site/xref-test/stylesheet.css` |
| `format.star` | 1 | 0 | gnu 1 | star 1 | 2010–2010 | 0 | ncurses@5.9 `ncurses-5.9/` |
| `hardlink.to-itself` | 1 | 1 | other 1 | GNU format 1 | 2018–2018 | 0 | atlas@3.11.41 `ATLAS/tune/blas/gemm/uammgen.c` |
| `linkname.no-nul` | 1 | 1 | github-release 1 | GNU format 1 | 2025–2025 | 0 | code-server@4.96.4 `code-server-4.96.4-linux-amd64/lib/vscode/node_modules/@vsco` |
| `name.control-character` | 1 | 0 | github-archive 1 | git archive 1 | 2022–2022 | 0 | apktool@2.6.1 `Apktool-2.6.1/brut.apktool/apktool-lib/src/test/resources/aa` |
| `name.dot` | 1 | 1 | other 1 | GNU format 1 | 2019–2019 | 0 | starlight@313 `./` |
| `name.not-nfc` | 1 | 0 | other 1 | libarchive (pax) 1 | 2022–2022 | 0 | go-bootstrap@1.17.13 `go/test/fixedbugs/issue27836.dir/Äfoo.go` |
| `name.trailing-slash-on-file` | 1 | 1 | other 1 | v7 1 | 1997–1997 | 1 | cdd@0.61a `cdd-061/` |
| `number.mtime.leading-space` | 1 | 1 | other 1 | v7 1 | 1997–1997 | 1 | cdd@0.61a `cdd-061/` |
| `pax.newline-in-value.SCHILY.xattr.*` | 1 | 1 | cpan 1 | libarchive (pax) 1 | 2022–2022 | 0 | perl-module-find@0.16 `PaxHeader/Module-Find-0.16` |
| `tree.duplicate.file-hardlink` | 1 | 1 | other 1 | GNU format 1 | 2018–2018 | 0 | atlas@3.11.41 `ATLAS/tune/blas/gemm/uammgen.c` |
| `tree.under-file` | 1 | 1 | other 1 | v7 1 | 1997–1997 | 1 | cdd@0.61a `cdd-061/COPYING` |

## Fingerprints

- magic (tarballs using each): posix 1155, gnu 700, v7 123, posix-version-0000 5, star 1
- size (tarballs using each): dn 1890, ds 63, sdn 19, sds 8, dsn 1
- mode (tarballs using each): dn 1909, dsn 64, sdsn 8, ds 6
- checksum (tarballs using each): dns 1341, dn 613, sdns 26, dsn 1, ds 1, sdsn 1, x 1
- pax_header_name (tarballs using each): ././@PaxHeader 369, H.paxheader 14, */PaxHeaders.N/* 14, ./PaxHeaders.N/* 14, */PaxHeaders/* 10, ./PaxHeaders/* 10, */PaxHeader/* 7, PaxHeader/* 4, */PaxHeaders.N/en@quot.header 1, */PaxHeaders.N/en@boldquot.header 1, */PaxH 1, */ 1
- extended_sequence (tarballs using each): - 1625, x 416, L 60, KL 1
- gnu_long_name (tarballs using each): ././@LongLink 60
- end (tarballs using each): padded-to-10240 1885, unpadded 94
- zero_blocks_after_end (tarballs using each): 0 206, 15 112, 5 108, 13 107, 10 103, 11 100, 6 97, 19 95, 17 95, 7 94, 12 94, 18 92
- pax_keys (tarballs using each): mtime 391, path 79, atime 27, ctime 26, gid 8, uid 7, LIBARCHIVE.xattr.* 4, SCHILY.xattr.* 4, LIBARCHIVE.creationtime 2, linkpath 1, SCHILY.dev 1, SCHILY.ino 1
- pax_global_keys (tarballs using each): comment 575
- compression layer: several streams 1
