# All scans

Rates are per dataset. Counts below are of the distinct tarballs of all datasets.

| dataset | tarballs | scanned | latest | untar rejects | latest | filesystem only |
|---|---|---|---|---|---|---|
| spack/2026-10-23-b | 1989 | 1981 | 992 | 8 (0.40%) | 6 (0.60%) | 10 |
| spack/2026-10-23 | 2000 | 1990 | 994 | 0 (0.00%) | 0 (0.00%) | 12 |

- tarballs: 3768, scanned: 3751 (1848 latest versions, 1903 older)
- not downloaded: 17, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 3737
- origins: pypi 1187, github-archive 987, other 585, cran/bioconductor 562, github-release 168, cpan 166, gitlab 51, gnu 45
- producers: GNU format 1277, git archive 1086, Python tarfile (pax) 752, ustar 332, v7 237, GNU tar (pax) 47, libarchive (pax) 11, posix-version-0000 8, star 1
- compression: gzip 3569, xz 95, bzip2 81, none 6
- scanner stopped early: 1
  - commons-logging@1.1.1: invalid checksum at offset 3452928

Failed only because of the case-insensitive filesystem of the scanning machine, not counted as rejections: 21, 6 latest (libbigwig@0.4.7; launchmon@1.2.1; environment-modules@5.7.0; linux-headers@4.9.10; py-healpy@1.13.0; scafacos@1.0.1).

## untar

Rejects 8 of 3751 (0.2%); 6 of 1848 latest versions (0.3%).

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
| `name.fills-field` | 353 | 148 | github-archive 175, pypi 73, other 50 | git archive 196, GNU format 63, Python tarfile (pax) 61 | 1970–2026 | 7 | typescript@5.8.3 `TypeScript-5.8.3/tests/baselines/reference/ClassDeclarationW`; serenity@1.6.1 `serenity-1.6.1/data/testresources/TestSystem_H2_6_31Gs_BP86/` |
| `ustar.prefix` | 321 | 142 | github-archive 234, cpan 26, other 25 | git archive 264, ustar 53, libarchive (pax) 4 | 2006–2026 | 7 | typescript@5.8.3 `AmbientModuleAndAmbientFunctionWithTheSameNameAndCommonRoot.`; serenity@1.6.1 `TestSystem_Diaziridine_HF_AUG_CC_PVDZ.FockMatrix.res.h5` |
| `type.nul` | 247 | 124 | other 157, github-release 50, gnu 27 | v7 235, GNU format 12 | 1970–2026 | 4 | fonttosfnt@1.2.3 `fonttosfnt-1.2.3/read.c`; libxfont2@2.0.7 `libXfont2-2.0.7/xfont2.pc.in` |
| `v7.bytes-after-linkname` | 194 | 91 | other 135, github-release 39, gnu 19 | v7 194 | 1970–2026 | 3 | fonttosfnt@1.2.3 `fonttosfnt-1.2.3/`; dri2proto@2.8 `dri2proto-2.8/` |
| `number.size.leading-space` | 44 | 33 | cpan 32, other 11, gnu 1 | ustar 32, posix-version-0000 8, v7 3 | 1995–2023 | 4 | giraph@1.2.0 `giraph-1.2.0/`; perl-uri-find@20160806 `URI-Find-20160806` |
| `name.non-ascii` | 38 | 16 | github-archive 25, other 7, pypi 4 | git archive 27, GNU format 5, Python tarfile (pax) 4 | 2016–2026 | 1 | flac@1.5.0 `flac-1.5.0/test/flac-to-flac-metadata-test-files/🤔.flac`; py-meson-python@0.19.0 `meson_python-0.19.0/tests/packages/encoding/テスト.py` |
| `name.dir-without-trailing-slash` | 31 | 25 | cpan 29, other 2 | ustar 29, GNU tar (pax) 1, GNU format 1 | 2003–2026 | 0 | perl-uri-find@20160806 `URI-Find-20160806`; perl-catalyst-action-rest@1.21 `Catalyst-Action-REST-1.21` |
| `number.gid.no-digits` | 24 | 13 | pypi 20, other 4 | GNU format 17, ustar 5, posix-version-0000 2 | 1985–2025 | 0 | giraph@1.2.0 `giraph-1.2.0/bin/`; py-tokenizers@0.23.1 `tokenizers-0.23.1/PKG-INFO` |
| `number.uid.no-digits` | 24 | 13 | pypi 20, other 4 | GNU format 17, ustar 5, posix-version-0000 2 | 1985–2025 | 0 | giraph@1.2.0 `giraph-1.2.0/bin/`; py-tokenizers@0.23.1 `tokenizers-0.23.1/PKG-INFO` |
| `platform.case-collision` | 22 | 7 | other 9, github-archive 7, github-release 5 | git archive 12, GNU format 4, Python tarfile (pax) 3 | 2011–2026 | 21 | libbigwig@0.4.7 `libBigWig-0.4.7/docs/html/bigWigIO_8h.html`; launchmon@1.2.1 `launchmon-1.2.1/install/` |
| `number.uid.base256` | 14 | 11 | pypi 8, other 4, github-release 1 | GNU format 11, libarchive (pax) 3 | 2015–2025 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; mxnet@1.9.1 `apache-mxnet-src-1.9.1-incubating/` |
| `name.leading-dot-slash` | 13 | 8 | other 10, gitlab 3 | GNU format 12, ustar 1 | 2003–2026 | 0 | dhpmm-f@alpha `./._DHPMM_F_alpha`; starlight@313 `./` |
| `number.gid.base256` | 13 | 10 | pypi 8, other 4, github-release 1 | GNU format 11, libarchive (pax) 2 | 2015–2025 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; py-lightly-utils@0.0.2 `lightly_utils-0.0.2/` |
| `number.gid.leading-space` | 12 | 7 | other 11, gnu 1 | posix-version-0000 8, v7 3, GNU format 1 | 1995–2020 | 4 | giraph@1.2.0 `giraph-1.2.0/`; cdd@0.61a `cdd-061/` |
| `number.mode.leading-space` | 12 | 7 | other 11, gnu 1 | posix-version-0000 8, v7 3, GNU format 1 | 1995–2020 | 4 | giraph@1.2.0 `giraph-1.2.0/`; cdd@0.61a `cdd-061/` |
| `number.uid.leading-space` | 12 | 7 | other 11, gnu 1 | posix-version-0000 8, v7 3, GNU format 1 | 1995–2020 | 4 | giraph@1.2.0 `giraph-1.2.0/`; cdd@0.61a `cdd-061/` |
| `platform.windows-invalid-character` | 12 | 7 | other 5, github-archive 4, github-release 2 | git archive 7, GNU format 4, Python tarfile (pax) 1 | 2007–2025 | 2 | fermisciencetools@11r5p3 `ScienceTools-v11r5p3-fssc-20180124-x86_64-unknown-linux-gnu-`; notmuch@0.23.7 `notmuch-0.23.7/test/corpora/default/01:2,` |
| `platform.windows-reserved-name` | 12 | 3 | other 9, gitlab 2, github-archive 1 | GNU format 6, git archive 5, v7 1 | 2012–2025 | 3 | lvm2@2.03.14 `LVM2.2.03.14/test/lib/aux.sh`; linux-headers@4.9.10 `linux-4.9.10/drivers/gpu/drm/nouveau/nvkm/subdev/i2c/aux.c` |
| `magic.posix-with-odd-version` | 8 | 5 | other 8 | posix-version-0000 8 | 2007–2020 | 3 | giraph@1.2.0 `giraph-1.2.0/`; hama@0.7.1 `hama-0.7.1/hama-commons-0.7.1.jar` |
| `tree.dir-after-contents` | 8 | 5 | other 5, cpan 3 | ustar 4, posix-version-0000 2, GNU tar (pax) 2 | 2014–2023 | 1 | mitofates@1.2 `MitoFates/bin/Setting/`; sqoop@1.99.7 `sqoop-1.99.7/common/` |
| `symlink.absolute` | 7 | 4 | github-archive 4, other 2, github-release 1 | git archive 6, GNU format 1 | 2017–2025 | 0 | crtm-fix@3.1.2.0 `fix_REL-3.1.2.0/fix/CloudCoeff/netCDF/CloudCoeff_Inspect`; mothur@1.48.0 `mothur-1.48.0/Products/Debug/mothur 2` |
| `tree.duplicate.dir-dir` | 5 | 1 | github-release 3, other 2 | git archive 4, ustar 1 | 2020–2023 | 0 | swipl@8.2.0 `swipl-8.2.0/bench/`; helics@3.5.2 `ThirdParty/asio/` |
| `pax-global.after-members` | 4 | 1 | other 2, github-release 2 | git archive 4 | 2020–2023 | 0 | swipl@8.2.0 `pax_global_header`; prometheus-cpp@1.2.4 `pax_global_header` |
| `pax.LIBARCHIVE.creationtime` | 3 | 2 | github-release 1, other 1, cpan 1 | libarchive (pax) 3 | 2017–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/`; gatk@3.8.0 `GenomeAnalysisTK-3.8-0-ge9d806836/` |
| `pax.nul-in-value.SCHILY.xattr.*` | 3 | 3 | github-release 1, cpan 1, other 1 | libarchive (pax) 3 | 2022–2023 | 0 | py-pylith@4.0.0 `pylith-4.0.0/docs/user/examples/magma-2d/figs/PaxHeader/step`; perl-module-find@0.16 `PaxHeader/Module-Find-0.16` |
| `tree.duplicate.file-file` | 3 | 3 | other 3 | git archive 1, GNU format 1, posix-version-0000 1 | 2011–2017 | 3 | notmuch@0.23.7 `notmuch-0.23.7/version`; swftools@0.9.2 `swftools-0.9.2/lib/kdtree.c` |
| `end.data-after` | 2 | 2 | other 2 | v7 1, posix-version-0000 1 | 1997–2016 | 2 | cdd@0.61a `cdd-061/ine/verifyinput2.ine`; hama@0.7.1 `hama-0.7.1/docs/diagram/yarn-hama-diagram.pptx` |
| `linkname.no-nul` | 2 | 1 | github-release 2 | GNU format 1, git archive 1 | 2025–2025 | 0 | code-server@4.96.4 `code-server-4.96.4-linux-amd64/lib/vscode/node_modules/@vsco`; gocryptfs@2.5.1 `gocryptfs_v2.5.1_src/tests/example_filesystems/v0.4/TBIgdfhD` |
| `name.control-character` | 2 | 0 | github-archive 1, github-release 1 | git archive 2 | 2022–2025 | 0 | apktool@2.6.1 `Apktool-2.6.1/brut.apktool/apktool-lib/src/test/resources/aa`; gocryptfs@2.5.1 `gocryptfs_v2.5.1_src/tests/fsck/malleable_base64/27AG8t-XZH7` |
| `number.mtime.leading-space` | 2 | 1 | other 1, gnu 1 | v7 1, GNU format 1 | 1995–1997 | 1 | cdd@0.61a `cdd-061/`; termcap@1.3 `termcap-1.3/` |
| `platform.windows-trailing-dot-or-space` | 2 | 1 | github-archive 1, other 1 | git archive 1, GNU format 1 | 2016–2023 | 0 | hyphy@2.5.51hf `hyphy-2.5.51hf/res/SubstitutionClasses/CodonEFV/Observed Nuc`; nauty@2.6r7 `nauty26r7/This_is_nauty26r7.` |
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

- magic (tarballs using each): posix 2228, gnu 1282, v7 237, posix-version-0000 8, star 1
- size (tarballs using each): dn 3581, ds 124, sdn 32, sds 12, dsn 2
- mode (tarballs using each): dn 3613, dsn 126, sdsn 12, ds 10
- checksum (tarballs using each): dns 2543, dn 1164, sdns 43, dsn 2, ds 2, sdsn 1, x 1
- pax_header_name (tarballs using each): ././@PaxHeader 752, */PaxHeaders.N/* 30, ./PaxHeaders.N/* 29, H.paxheader 25, */PaxHeaders/* 15, ./PaxHeaders/* 15, */PaxHeader/* 10, PaxHeader/* 5, */PaxHea 2, * 2, ./PaxHeaders.X/* 2, */PaxHeaders.N 2
- extended_sequence (tarballs using each): - 3039, x 835, L 97, KL 1
- gnu_long_name (tarballs using each): ././@LongLink 97
- end (tarballs using each): padded-to-10240 3570, unpadded 179
- zero_blocks_after_end (tarballs using each): 0 390, 15 216, 13 195, 10 187, 14 186, 19 185, 17 184, 5 182, 6 178, 11 177, 7 175, 18 175
- pax_keys (tarballs using each): mtime 781, path 154, atime 49, ctime 48, uid 12, gid 11, LIBARCHIVE.xattr.* 4, SCHILY.xattr.* 4, LIBARCHIVE.creationtime 3, linkpath 2, SCHILY.dev 2, SCHILY.ino 2
- pax_global_keys (tarballs using each): comment 1086
- compression layer: several streams 1, trailing zeros 1
