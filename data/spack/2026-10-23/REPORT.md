# Scan of 2000 Spack tarballs

- tarballs: 2000, scanned: 1990 (994 latest versions, 996 older)
- not downloaded: 10, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 1984
- origins: pypi 647, github-archive 518, other 322, cran/bioconductor 293, cpan 93, github-release 73, gitlab 25, gnu 19
- producers: GNU format 651, git archive 564, Python tarfile (pax) 435, ustar 183, v7 126, GNU tar (pax) 23, libarchive (pax) 5, posix-version-0000 3
- compression: gzip 1900, bzip2 45, xz 42, none 3
- scanner stopped early: 0

Failed only because of the case-insensitive filesystem of the scanning machine, not counted as rejections: 12, 3 latest (sysstat@12.7.6; pagit@1.01; cmaq@5.3.1; pango@1.49.4; linux-external-modules@6.0.7; mpich@4.2.0).

## untar

Rejects 0 of 1990 (0.0%); 0 of 994 latest versions (0.0%).

| reason | tarballs | latest | origins | producers | examples |
|---|---|---|---|---|---|

## Features

Number of tarballs with each feature, of which latest versions; their origins, producers and median mtime years, and what untar did with them.

| feature | tarballs | latest | origins | producers | years | untar rejects | examples |
|---|---|---|---|---|---|---|---|
| `name.fills-field` | 188 | 87 | github-archive 94, pypi 44, other 24 | git archive 105, Python tarfile (pax) 36, GNU format 31 | 1980–2026 | 3 | pmix@6.1.0 `pmix-6.1.0/docs/_build/html/_sources/installing-pmix/configu`; typescript@5.8.3 `TypeScript-5.8.3/tests/baselines/reference/ClassDeclarationW` |
| `ustar.prefix` | 161 | 81 | github-archive 123, cpan 12, other 10 | git archive 135, ustar 25, libarchive (pax) 1 | 2006–2026 | 2 | typescript@5.8.3 `AmbientModuleAndAmbientFunctionWithTheSameNameAndCommonRoot.`; perl-net-http@6.23 `LICENSE` |
| `type.nul` | 135 | 68 | other 92, github-release 24, gnu 9 | v7 126, GNU format 9 | 2003–2026 | 2 | libdmx@1.1.5 `libdmx-1.1.5/config.guess`; dri3proto@1.0 `dri3proto-1.0/configure` |
| `v7.bytes-after-linkname` | 108 | 54 | other 83, github-release 18, gnu 6 | v7 108 | 2005–2025 | 2 | libdmx@1.1.5 `libdmx-1.1.5/`; dri3proto@1.0 `dri3proto-1.0/` |
| `number.size.leading-space` | 19 | 15 | cpan 15, other 3, gnu 1 | ustar 15, posix-version-0000 3, GNU format 1 | 1995–2023 | 0 | perl-net-http@6.23 `Net-HTTP-6.23`; perl-tie-ixhash@1.23 `Tie-IxHash-1.23` |
| `name.non-ascii` | 17 | 8 | github-archive 13, pypi 3, other 1 | git archive 13, Python tarfile (pax) 3, GNU format 1 | 2017–2026 | 1 | doxygen@1.17.0 `doxygen-Release_1_17_0/testing/061_Únicod€_file.cpp`; py-sphinx@9.1.0 `sphinx-9.1.0/tests/roots/test-images/testimäge.png` |
| `number.gid.no-digits` | 15 | 7 | pypi 13, other 2 | GNU format 11, ustar 3, posix-version-0000 1 | 1985–2025 | 0 | sourmash@4.8.2 `sourmash-4.8.2/src/core/Cargo.toml`; py-orjson@3.11.5 `orjson-3.11.5/README.md` |
| `number.uid.no-digits` | 15 | 7 | pypi 13, other 2 | GNU format 11, ustar 3, posix-version-0000 1 | 1985–2025 | 0 | sourmash@4.8.2 `sourmash-4.8.2/src/core/Cargo.toml`; py-orjson@3.11.5 `orjson-3.11.5/README.md` |
| `name.dir-without-trailing-slash` | 14 | 12 | cpan 13, other 1 | ustar 13, GNU format 1 | 2010–2026 | 0 | perl-net-http@6.23 `Net-HTTP-6.23`; perl-tie-ixhash@1.23 `Tie-IxHash-1.23` |
| `platform.case-collision` | 13 | 4 | other 7, github-archive 5, github-release 1 | git archive 8, GNU format 2, v7 2 | 2011–2024 | 12 | sysstat@12.7.6 `sysstat-12.7.6/tests/expected.sadf-d-t-tz`; open-isns@0.100 `open-isns-0.100/tests/data/test01/` |
| `name.leading-dot-slash` | 7 | 4 | other 6, gitlab 1 | GNU format 7 | 2003–2026 | 0 | cvector@1.0.3.1 `./CVector-1.0.3.1/`; pdt@3.25.2 `./pdtoolkit-3.25.2/` |
| `number.gid.base256` | 7 | 5 | pypi 4, other 3 | GNU format 6, libarchive (pax) 1 | 2017–2025 | 0 | superchic@4.01 `superchic4.01/`; py-lightly-utils@0.0.2 `lightly_utils-0.0.2/` |
| `number.uid.base256` | 7 | 5 | pypi 4, other 2, cpan 1 | GNU format 5, libarchive (pax) 2 | 2017–2025 | 0 | perl-test-xml-simple@1.05 `Test-XML-Simple-1.05/`; py-lightly-utils@0.0.2 `lightly_utils-0.0.2/` |
| `platform.windows-reserved-name` | 7 | 2 | other 6, gitlab 1 | GNU format 4, git archive 2, v7 1 | 2012–2024 | 2 | molden@7.3 `molden7.3/haux/plush/PRN`; chaplin@1.2 `chaplin-1.2/src/aux.f` |
| `platform.windows-invalid-character` | 6 | 4 | github-archive 2, other 2, gitlab 1 | git archive 4, Python tarfile (pax) 1, GNU format 1 | 2007–2025 | 1 | systemd@256.7 `systemd-256.7/test/test-journals/corrupted/id:000000,sig:06,`; sysstat@12.7.6 `sysstat-12.7.6/tests/root1/dev/disk/by-id/usb-Generic-_Compa` |
| `number.gid.leading-space` | 4 | 2 | other 3, gnu 1 | posix-version-0000 3, GNU format 1 | 1995–2020 | 0 | jmol@14.31.0 `jmol-14.31.0/`; mahout@0.13.0 `apache-mahout-distribution-0.13.0/flink/src/` |
| `number.mode.leading-space` | 4 | 2 | other 3, gnu 1 | posix-version-0000 3, GNU format 1 | 1995–2020 | 0 | jmol@14.31.0 `jmol-14.31.0/`; mahout@0.13.0 `apache-mahout-distribution-0.13.0/flink/src/` |
| `number.uid.leading-space` | 4 | 2 | other 3, gnu 1 | posix-version-0000 3, GNU format 1 | 1995–2020 | 0 | jmol@14.31.0 `jmol-14.31.0/`; mahout@0.13.0 `apache-mahout-distribution-0.13.0/flink/src/` |
| `symlink.absolute` | 4 | 2 | github-archive 2, other 1, github-release 1 | git archive 4 | 2017–2025 | 0 | openmc@0.11.0 `openmc-dev-openmc-7a4c5b4/examples/jupyter/chain_simple.xml`; fastme@2.1.5.1 `FastME-v2.1.5.1-18f12a0544dec28a2cda5c0c866f984b12cd773d/COP` |
| `magic.posix-with-odd-version` | 3 | 2 | other 3 | posix-version-0000 3 | 2014–2020 | 0 | jmol@14.31.0 `jmol-14.31.0/`; mahout@0.13.0 `apache-mahout-distribution-0.13.0/flink/src/` |
| `tree.dir-after-contents` | 3 | 3 | other 2, cpan 1 | GNU tar (pax) 1, ustar 1, posix-version-0000 1 | 2017–2023 | 0 | storm@2.6.2 `apache-storm-2.6.2/public/js/`; perl-file-sharedir-install@0.14 `File-ShareDir-Install-0.14/t` |
| `pax-global.after-members` | 2 | 1 | other 1, github-release 1 | git archive 2 | 2020–2020 | 0 | swipl@8.2.0 `pax_global_header`; pfunit@4.1.10 `pax_global_header` |
| `pax.LIBARCHIVE.creationtime` | 2 | 1 | cpan 1, other 1 | libarchive (pax) 2 | 2017–2017 | 0 | perl-test-xml-simple@1.05 `Test-XML-Simple-1.05/MANIFEST`; gatk@3.8.0 `GenomeAnalysisTK-3.8-0-ge9d806836/` |
| `tree.duplicate.dir-dir` | 2 | 1 | other 1, github-release 1 | git archive 2 | 2020–2020 | 0 | swipl@8.2.0 `swipl-8.2.0/bench/`; pfunit@4.1.10 `pFUnit-4.1.10/extern/fArgParse/` |
| `hardlink.to-symlink` | 1 | 1 | other 1 | GNU format 1 | 2020–2020 | 0 | octa@8.4 `OCTA84/Python37/bin/python` |
| `linkname.no-nul` | 1 | 0 | github-release 1 | git archive 1 | 2025–2025 | 0 | gocryptfs@2.5.1 `gocryptfs_v2.5.1_src/tests/example_filesystems/v0.4/TBIgdfhD` |
| `name.backslash` | 1 | 1 | github-archive 1 | git archive 1 | 2024–2024 | 0 | systemd@256.7 `systemd-256.7/test/fuzz/fuzz-unit-file/dm-back\x2dslash.swap` |
| `name.control-character` | 1 | 0 | github-release 1 | git archive 1 | 2025–2025 | 0 | gocryptfs@2.5.1 `gocryptfs_v2.5.1_src/tests/fsck/malleable_base64/27AG8t-XZH7` |
| `name.double-slash` | 1 | 0 | github-release 1 | GNU format 1 | 2019–2019 | 0 | shapemapper@2.1.5 `shapemapper-2.1.5-source-only//shapemapper` |
| `number.mtime.leading-space` | 1 | 0 | gnu 1 | GNU format 1 | 1995–1995 | 0 | termcap@1.3 `termcap-1.3/` |
| `pax.LIBARCHIVE.symlinktype` | 1 | 1 | other 1 | libarchive (pax) 1 | 2023–2023 | 0 | win-file@5.45 `file/src/file-FILE5_45/src/.libs/libmagic.la` |
| `platform.windows-trailing-dot-or-space` | 1 | 1 | github-archive 1 | git archive 1 | 2023–2023 | 0 | hyphy@2.5.51hf `hyphy-2.5.51hf/res/SubstitutionClasses/CodonEFV/Observed Nuc` |

## Fingerprints

- magic (tarballs using each): posix 1210, gnu 654, v7 126, posix-version-0000 3
- size (tarballs using each): dn 1900, ds 70, sdn 15, sds 4, dsn 1
- mode (tarballs using each): dn 1915, dsn 70, ds 5, sdsn 4
- checksum (tarballs using each): dns 1358, dn 613, sdns 19, dsn 1, ds 1
- pax_header_name (tarballs using each): ././@PaxHeader 435, */PaxHeaders.N/* 17, ./PaxHeaders.N/* 16, H.paxheader 12, */PaxHeaders/* 5, ./PaxHeaders/* 5, */PaxHeader/* 4, PaxHeader/* 3, * 1, */Pax 1, */PaxHe 1, ./PaxHeaders.X/* 1
- extended_sequence (tarballs using each): - 1584, x 475, L 44
- gnu_long_name (tarballs using each): ././@LongLink 44
- end (tarballs using each): padded-to-10240 1887, unpadded 103
- zero_blocks_after_end (tarballs using each): 0 222, 15 115, 14 104, 13 103, 9 100, 17 99, 19 97, 16 95, 10 94, 3 93, 6 93, 18 91
- pax_keys (tarballs using each): mtime 443, path 85, atime 25, ctime 25, uid 7, gid 5, SCHILY.dev 2, SCHILY.ino 2, SCHILY.nlink 2, LIBARCHIVE.creationtime 2, LIBARCHIVE.symlinktype 1, linkpath 1
- pax_global_keys (tarballs using each): comment 564
- compression layer: trailing zeros 1
