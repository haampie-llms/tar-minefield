# All scans

Rates are per dataset. Counts below are of the distinct tarballs of all datasets.

| dataset | tarballs | scanned | latest | untar rejects | latest | filesystem only |
|---|---|---|---|---|---|---|
| live-bootstrap/2026-10-23 | 171 | 171 | 74 | 0 (0.00%) | 0 (0.00%) | 0 |
| nix/2026-10-23 | 19086 | 19012 | 17977 | 100 (0.53%) | 94 (0.52%) | 0 |
| spack/2026-10-23-b | 1989 | 1981 | 992 | 8 (0.40%) | 6 (0.60%) | 10 |
| spack/2026-10-23 | 2000 | 1990 | 994 | 0 (0.00%) | 0 (0.00%) | 12 |

- tarballs: 22805, scanned: 22714 (19691 latest versions, 3023 older)
- not downloaded: 91, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 12887
- origins: other 12550, pypi 4975, cpan 2000, github-archive 1054, github-release 987, cran/bioconductor 630, gnu 438, gitlab 80
- producers: ustar 10487, GNU format 5515, Python tarfile (pax) 3801, git archive 1527, v7 1037, GNU tar (pax) 268, libarchive (pax) 39, none 22, posix-version-0000 17, star 1
- compression: gzip 19759, xz 1683, bzip2 937, none 333
- scanner stopped early: 23
  - ocrad@0.29: invalid checksum at offset 0
  - git-warp-time@1.0.0: invalid checksum at offset 0
  - wget@1.25.0: invalid checksum at offset 0
  - ddrescue@1.30: invalid checksum at offset 0
  - Libertinus@7.051: invalid checksum at offset 0
  - fcitx5-rime@5.1.16: invalid checksum at offset 0
  - decasify@0.11.4: invalid checksum at offset 0
  - ed@1.22.6: invalid checksum at offset 0
  - rcs@5.10.1: invalid checksum at offset 0
  - moe@1.16: invalid checksum at offset 0
  - maptool@1.18.7-x86_64.pkg: invalid checksum at offset 0
  - bc@1.08.2: invalid checksum at offset 0
  - plzip@1.13: invalid checksum at offset 0
  - goredo@2.10.0: invalid checksum at offset 0
  - libpsl@0.21.5: invalid checksum at offset 0
  - fcitx5-anthy@5.1.11: invalid checksum at offset 0
  - parsers-linux-x86_64@: invalid checksum at offset 0
  - lzlib@1.16: invalid checksum at offset 0
  - vors@6.3.0: invalid checksum at offset 0
  - sile@0.15.13: invalid checksum at offset 0
  - warp-terminal@v0.2026.10.14.08.27.stable_01-1-x86_64.pkg: invalid checksum at offset 0
  - tarlz@0.30: invalid checksum at offset 0
  - commons-logging@1.1.1: invalid checksum at offset 3452928

Failed only because of the case-insensitive filesystem of the scanning machine, not counted as rejections: 21, 6 latest (libbigwig@0.4.7; launchmon@1.2.1; environment-modules@5.7.0; linux-headers@4.9.10; py-healpy@1.13.0; scafacos@1.0.1).

## untar

Rejects 108 of 22714 (0.5%); 100 of 19691 latest versions (0.5%).

| reason | tarballs | latest | origins | producers | examples |
|---|---|---|---|---|---|
| FileExistsError: [Errno N] File exists: '…' | 62 | 57 | other 60, pypi 1, github-release 1 | ustar 50, git archive 5, Python tarfile (pax) 4 | snap-loader-static@1.0.0.1; htn@0.1.0.0; shelly-extra@0.3.0.2 |
| Archive contains an invalid number b'…' | 22 | 22 | gnu 10, github-release 7, other 5 | none 22 | ocrad@0.29; git-warp-time@1.0.0; wget@1.25.0 |
| Archive contains data after the end-of-archive marker | 11 | 10 | other 9, cpan 1, github-release 1 | v7 6, posix-version-0000 3, ustar 2 | bsf-bin@2.4.0; psutils-p17@; Logfile-Rotate@1.04 |
| Archive is truncated | 10 | 9 | other 10 | ustar 5, GNU format 4, v7 1 | SDL2_ttf@2.24.0; SDL2_image@2.8.12; eng-rus@ |
| Archive contains unsafe path … | 1 | 1 | other 1 | git archive 1 | dtv-scan-tables@2024-03-24-7098bdd27548 |
| Archive contains forktty-N.N/pipe of unsupported type b'…' | 1 | 1 | other 1 | GNU format 1 | forktty@1.3 |
| Archive contains a lone zero block | 1 | 0 | other 1 | posix-version-0000 1 | commons-logging@1.1.1 |

## Features

Number of tarballs with each feature, of which latest versions; their origins, producers and median mtime years, and what untar did with them.

| feature | tarballs | latest | origins | producers | years | untar rejects | examples |
|---|---|---|---|---|---|---|---|
| `name.fills-field` | 1160 | 870 | pypi 421, other 418, github-archive 183 | GNU format 374, Python tarfile (pax) 356, git archive 242 | 1970–2026 | 14 | texinfo@7.2 `texinfo-7.2/tp/t/results/init_files_tests/documentation_exam`; linux@4.14.336 `linux-4.14.336/Documentation/devicetree/bindings/interrupt-c` |
| `type.nul` | 1050 | 872 | other 743, gnu 181, github-release 94 | v7 1025, GNU format 25 | 1970–2026 | 8 | make@3.82 `make-3.82/vmsfunctions.c`; gzip@1.2.4 `gzip-1.2.4/README` |
| `ustar.prefix` | 928 | 702 | cpan 343, github-archive 245, other 241 | ustar 586, git archive 331, libarchive (pax) 8 | 1981–2026 | 14 | texinfo@7.2 `split_test_before_first_node.info`; linux@4.14.336 `samsung,exynos4210-combiner.txt` |
| `name.dir-without-trailing-slash` | 833 | 774 | cpan 444, github-release 294, other 80 | ustar 797, GNU format 28, GNU tar (pax) 8 | 1970–2026 | 0 | oyacc@6.6 `oyacc-6.6`; perl@5.15.7 `perl-5.15.7` |
| `v7.bytes-after-linkname` | 756 | 616 | other 562, gnu 127, github-release 61 | v7 756 | 1970–2026 | 3 | make@3.82 `make-3.82/`; m4@1.4.7 `m4-1.4.7/` |
| `tree.dir-after-contents` | 754 | 713 | other 717, cpan 22, pypi 15 | ustar 727, GNU format 17, posix-version-0000 6 | 1970–2026 | 8 | File-ShareDir-Install@0.14 `File-ShareDir-Install-0.14/t`; streaming-utils@0.2.6.0 `streaming-utils-0.2.6.0/Streaming/` |
| `number.size.leading-space` | 577 | 555 | cpan 504, other 61, gnu 9 | ustar 498, GNU format 39, v7 23 | 1992–2026 | 15 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `name.non-ascii` | 113 | 73 | other 63, github-archive 29, pypi 10 | GNU format 53, git archive 32, Python tarfile (pax) 14 | 2004–2026 | 1 | kbd@1.15 `kbd-1.15/doc/utf/♪♬`; gcc@15.2.0 `gcc-15.2.0/gcc/testsuite/go.test/test/fixedbugs/issue27836.d` |
| `platform.case-collision` | 93 | 60 | other 63, github-archive 13, github-release 6 | git archive 36, GNU format 22, ustar 12 | 1980–2026 | 22 | perl@5.003 `perl5-perl-5.003/configure`; perl@5.004_05 `perl5.004_05/Configure` |
| `number.gid.no-digits` | 88 | 70 | pypi 55, other 29, github-release 4 | GNU format 55, ustar 26, posix-version-0000 7 | 1970–2026 | 0 | rpds_py@2026.6.3 `rpds_py-2026.6.3/PKG-INFO`; hadoop@3.4.2-src `hadoop-3.4.2-src/README.txt` |
| `number.uid.no-digits` | 88 | 70 | pypi 55, other 29, github-release 4 | GNU format 55, ustar 26, posix-version-0000 7 | 1970–2026 | 0 | rpds_py@2026.6.3 `rpds_py-2026.6.3/PKG-INFO`; hadoop@3.4.2-src `hadoop-3.4.2-src/README.txt` |
| `number.gid.leading-space` | 82 | 66 | other 61, cpan 11, gnu 9 | GNU format 39, v7 23, posix-version-0000 16 | 1992–2026 | 15 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.uid.leading-space` | 82 | 66 | other 61, cpan 11, gnu 9 | GNU format 39, v7 23, posix-version-0000 16 | 1992–2026 | 15 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.mode.leading-space` | 75 | 59 | other 54, cpan 11, gnu 9 | GNU format 34, v7 22, posix-version-0000 16 | 1992–2026 | 12 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `tree.duplicate.file-file` | 62 | 57 | other 60, pypi 1, github-release 1 | ustar 50, git archive 5, Python tarfile (pax) 4 | 1970–2026 | 62 | snap-loader-static@1.0.0.1 `snap-loader-static-1.0.0.1/LICENSE`; htn@0.1.0.0 `htn-0.1.0.0/src/Algorithms/Htn.hs` |
| `number.mtime.leading-space` | 49 | 40 | other 31, cpan 10, gnu 8 | GNU format 34, v7 12, ustar 3 | 1992–2004 | 9 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `name.leading-dot-slash` | 48 | 41 | other 30, github-release 13, gitlab 3 | GNU format 41, ustar 4, GNU tar (pax) 1 | 1998–2026 | 1 | curie@v1.0 `./LICENSE`; hdf5@1.10.11 `./hdf5-1.10.11/` |
| `number.uid.base256` | 45 | 41 | pypi 21, cpan 13, other 9 | GNU format 38, libarchive (pax) 7 | 2008–2026 | 0 | apache-mxnet-src@1.9.1-incubating `apache-mxnet-src-1.9.1-incubating/`; rfc3986_validator@0.1.1 `rfc3986_validator-0.1.1/` |
| `number.gid.base256` | 40 | 36 | pypi 20, cpan 11, other 7 | GNU format 35, libarchive (pax) 5 | 2008–2026 | 0 | rfc3986_validator@0.1.1 `rfc3986_validator-0.1.1/`; papi@7.2.0 `papi-7.2.0/` |
| `platform.windows-invalid-character` | 39 | 33 | other 26, github-archive 4, github-release 3 | GNU format 16, git archive 13, Python tarfile (pax) 5 | 2003–2026 | 3 | pulseaudio@17.0 `pulseaudio-17.0/src/modules/alsa/mixer/samples/USB Device 0x`; xitomatl_0.0.0-akku.208.62a8243_repack@ `fmt/let-optionals*.larceny.sls` |
| `platform.windows-reserved-name` | 31 | 14 | other 23, github-archive 4, gitlab 2 | git archive 16, GNU format 11, v7 3 | 1994–2026 | 3 | perl@5.000 `perl5-perl-5.000/hints/aux.sh`; perl@5.003 `perl5-perl-5.003/hints/aux.sh` |
| `symlink.absolute` | 22 | 19 | other 16, github-archive 4, github-release 2 | GNU format 10, git archive 8, ustar 2 | 2008–2026 | 1 | live.2026.01.12@ `live/testProgs/whiteroom.mp3`; imapsync@2.314 `imapsync-2.314/X/fullchain.pem` |
| `name.dot` | 19 | 17 | github-release 12, other 6, cpan 1 | GNU format 18, v7 1 | 1998–2026 | 1 | partclone-utils@0.4.3 `./`; cmucl@21d-x86-linux `./` |
| `pax.nul-in-value.SCHILY.xattr.*` | 18 | 18 | cpan 10, other 6, github-release 2 | libarchive (pax) 18 | 2019–2026 | 0 | Module-Find@0.16 `PaxHeader/Module-Find-0.16`; Crypt-X509@0.55 `Crypt-X509-0.55/PaxHeader/README` |
| `linkname.no-nul` | 17 | 6 | other 14, github-release 3 | GNU format 14, Python tarfile (pax) 2, git archive 1 | 2023–2026 | 0 | ghc@9.12.4-src `ghc-9.12.4/libraries/Cabal/cabal-testsuite/PackageTests/Requ`; nextcloud@34.0.5 `nextcloud/apps/app_api/js/app_api-vendors-node_modules_nextc` |
| `magic.posix-with-odd-version` | 17 | 12 | other 15, github-release 2 | posix-version-0000 17 | 2006–2026 | 5 | hadoop@3.4.2-src `hadoop-3.4.2-src/README.txt`; bsf-bin@2.4.0 `bsf-2.4.0/` |
| `tree.duplicate.dir-dir` | 16 | 12 | other 10, github-release 6 | git archive 12, ustar 4 | 2020–2026 | 2 | besu@24.1.2 `besu-24.1.2/./`; lightweight-testing@0.1 `lightweight-testing-0.1/./` |
| `platform.windows-trailing-dot-or-space` | 13 | 9 | other 10, github-archive 2, gnu 1 | git archive 4, GNU format 3, Python tarfile (pax) 2 | 1994–2026 | 0 | perl@5.000 `perl5-perl-5.000/vms/makefile.`; Python@2.3.7 `Python-2.3.7/Mac/IDE scripts/Search Python Documentation...` |
| `pax-global.after-members` | 11 | 8 | other 7, github-release 4 | git archive 11 | 2020–2026 | 1 | inform@6.44-r3 `pax_global_header`; rpm@4.20.1 `pax_global_header` |
| `end.data-after` | 10 | 10 | other 8, cpan 1, github-release 1 | v7 5, posix-version-0000 3, ustar 2 | 1995–2016 | 10 | bsf-bin@2.4.0 `bsf-2.4.0/samples/xsl/table-data.xml`; psutils-p17@ `psutils/showchar.sh` |
| `number.gid.no-terminator` | 9 | 9 | cpan 9 | ustar 9 | 2014–2022 | 0 | App-rainbarf@1.4 `App-rainbarf-1.4`; JSON-WebToken@0.10 `Build.PL` |
| `number.uid.no-terminator` | 9 | 9 | cpan 9 | ustar 9 | 2014–2022 | 0 | App-rainbarf@1.4 `App-rainbarf-1.4`; JSON-WebToken@0.10 `Build.PL` |
| `pax.newline-in-value.SCHILY.xattr.*` | 7 | 7 | cpan 5, other 2 | libarchive (pax) 7 | 2020–2025 | 0 | Module-Find@0.16 `PaxHeader/Module-Find-0.16`; Minion@10.31 `Minion-10.31/lib/Mojolicious/Plugin/Minion/resources/public/` |
| `end.lone-zero-block` | 5 | 5 | other 5 | GNU format 4, v7 1 | 1998–2014 | 5 | eng-rus@ `eng-rus.index`; srecord@1.64 `srecord-1.64/debian/srecord.install` |
| `end.missing` | 5 | 4 | other 5 | ustar 5 | 2023–2026 | 5 | SDL2_ttf@2.24.0 `SDL2_ttf-2.24.0/external/harfbuzz/README`; SDL2_image@2.8.12 `SDL2_image-2.8.12/Xcode/macOS/SDL2.framework/Resources` |
| `name.dot-component` | 5 | 4 | other 5 | ustar 3, GNU format 1, GNU tar (pax) 1 | 2018–2026 | 0 | besu@24.1.2 `besu-24.1.2/./`; lightweight-testing@0.1 `lightweight-testing-0.1/./` |
| `name.trailing-slash-on-file` | 5 | 5 | other 5 | v7 5 | 1994–2023 | 3 | sendmail.8.18.2@ `sendmail-8.18.2/`; tcp_wrappers_7.6@ `tcp_wrappers_7.6/` |
| `pax.LIBARCHIVE.creationtime` | 5 | 4 | other 2, cpan 2, github-release 1 | libarchive (pax) 5 | 2015–2023 | 0 | leo@2_v1.7.0 `leo2/`; Proc-Wait3@0.05 `Proc-Wait3-0.05/Changes` |
| `tree.under-file` | 4 | 4 | other 4 | v7 4 | 1994–2023 | 2 | sendmail.8.18.2@ `sendmail-8.18.2/Makefile`; tcp_wrappers_7.6@ `tcp_wrappers_7.6/README` |
| `name.control-character` | 3 | 1 | other 1, github-archive 1, github-release 1 | git archive 2, ustar 1 | 2009–2025 | 0 | cdrtools@3.02a09 `cdrtools-3.02/libfind/ifpdi`; apktool@2.6.1 `Apktool-2.6.1/brut.apktool/apktool-lib/src/test/resources/aa` |
| `hardlink.to-itself` | 2 | 2 | other 2 | GNU format 2 | 2018–2020 | 0 | atari++_1.85@ `atari++/winmain.cpp`; atlas@3.11.41 `ATLAS/tune/blas/gemm/uammgen.c` |
| `name.backslash` | 2 | 2 | gnu 1, github-archive 1 | ustar 1, git archive 1 | 2010–2024 | 0 | texi2html@5.0 `texi2html-5.0/test/info_coverage/f--ile""\.png`; systemd@256.7 `systemd-256.7/test/fuzz/fuzz-unit-file/dm-back\x2dslash.swap` |
| `name.double-slash` | 2 | 0 | other 1, github-release 1 | GNU format 2 | 2019–2021 | 0 | ghc@9.0.2-x86_64-deb10-linux `ghc-9.0.2/libraries/ghc-bignum/dist-install/build/include//H`; shapemapper@2.1.5 `shapemapper-2.1.5-source-only//shapemapper` |
| `name.not-utf8` | 2 | 2 | gnu 2 | GNU format 2 | 2004–2004 | 0 | aspell-is@0.51.1-0 `aspell-is-0.51.1-0/\xedslenska.alias`; aspell-nb@0.50.1-0 `aspell-nb-0.50.1-0/bokm\xe5l.alias` |
| `number.mtime.no-digits` | 2 | 2 | github-release 2 | ustar 2 | 2025–2026 | 0 | camunda-modeler@5.52.0-linux-x64 `camunda-modeler-5.52.0-linux-x64/`; stretchly@1.19.0 `Stretchly-1.19.0/` |
| `tree.duplicate.file-hardlink` | 2 | 2 | other 2 | GNU format 2 | 2018–2020 | 0 | atari++_1.85@ `atari++/winmain.cpp`; atlas@3.11.41 `ATLAS/tune/blas/gemm/uammgen.c` |
| `end.archive-after` | 1 | 0 | other 1 | v7 1 | 2008–2008 | 1 | glibmm@2.16.0 `glibmm-2.16.0/` |
| `end.zero-block-before-member` | 1 | 0 | other 1 | posix-version-0000 1 | 2007–2007 | 1 | commons-logging@1.1.1 `commons-logging-1.1.1/site/xref-test/stylesheet.css` |
| `format.star` | 1 | 0 | gnu 1 | star 1 | 2010–2010 | 0 | ncurses@5.9 `ncurses-5.9/` |
| `hardlink.to-symlink` | 1 | 1 | other 1 | GNU format 1 | 2020–2020 | 0 | octa@8.4 `OCTA84/Python37/bin/python` |
| `name.absolute` | 1 | 1 | other 1 | git archive 1 | 2024–2024 | 1 | dtv-scan-tables@2024-03-24-7098bdd27548 `/usr/share/dvb/` |
| `name.not-nfc` | 1 | 0 | other 1 | libarchive (pax) 1 | 2022–2022 | 0 | go-bootstrap@1.17.13 `go/test/fixedbugs/issue27836.dir/Äfoo.go` |
| `pax.LIBARCHIVE.symlinktype` | 1 | 1 | other 1 | libarchive (pax) 1 | 2023–2023 | 0 | win-file@5.45 `file/src/file-FILE5_45/src/.libs/libmagic.la` |
| `pax.size-on-dir` | 1 | 1 | pypi 1 | GNU tar (pax) 1 | 1970–1970 | 0 | llama_index_workflows@2.26.0 `llama_index_workflows-2.26.0/` |

## Fingerprints

- magic (tarballs using each): posix 16122, gnu 5537, v7 1037, posix-version-0000 17, star 1
- size (tarballs using each): dn 21175, ds 928, sdn 501, sds 76, dsn 13
- mode (tarballs using each): dn 21668, dsn 924, ds 76, sdsn 68, sdn 7
- checksum (tarballs using each): dns 19498, dn 2272, sdns 559, d 339, dsn 17, x 16, ds 10, sdsn 10, sdn 5, sds 3, xd 2, xdx 2
- pax_header_name (tarballs using each): ././@PaxHeader 3802, */PaxHeaders/* 187, ./PaxHeaders/* 157, */PaxHeaders.N/* 63, ./PaxHeaders.N/* 60, */PaxHeader/* 37, H.paxheader 32, ./PaxHeaders.X/* 18, PaxHeader/* 17, * 11, */PaxHeaders 11, */PaxHeader 8
- extended_sequence (tarballs using each): - 18892, x 4144, L 574, KL 10, K 8
- gnu_long_name (tarballs using each): ././@LongLink 574
- end (tarballs using each): padded-to-10240 14078, unpadded 8603
- zero_blocks_after_end (tarballs using each): 0 9761, 11 737, 9 708, 6 700, 10 694, 17 693, 13 691, 16 682, 1 680, 15 679, 19 678, 14 676
- pax_keys (tarballs using each): mtime 4015, path 756, atime 181, ctime 174, uid 42, gid 39, LIBARCHIVE.xattr.* 22, SCHILY.xattr.* 21, SCHILY.dev 7, SCHILY.ino 7, SCHILY.nlink 7, LIBARCHIVE.creationtime 5
- pax_global_keys (tarballs using each): comment 1527
- compression layer: trailing zeros 2, several streams 2
