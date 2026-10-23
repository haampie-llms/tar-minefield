# All scans

Rates are per dataset. Counts below are of the distinct tarballs of all datasets.

| dataset | tarballs | scanned | latest | untar rejects | latest | filesystem only |
|---|---|---|---|---|---|---|
| live-bootstrap/2026-10-23 | 171 | 171 | 74 | 0 (0.00%) | 0 (0.00%) | 0 |
| nix/2026-10-23 | 19086 | 19012 | 17977 | 100 (0.53%) | 94 (0.52%) | 0 |
| guix/2026-10-23 | 10200 | 10199 | 9705 | 69 (0.68%) | 64 (0.66%) | 0 |
| spack/2026-10-23-c | 34050 | 33844 | 6250 | 38 (0.11%) | 7 (0.11%) | 0 |

- tarballs: 59240, scanned: 58963 (30229 latest versions, 28734 older)
- not downloaded: 277, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 48679
- copied from other scans with `--reuse`: 5, read from `--cache`: 32; sources by host: mirror.spack.io 32044, tarballs.nixos.org 9418, bordeaux.guix.gnu.org 7090, hackage.haskell.org 6143, files.pythonhosted.org 1509, download.kde.org 488
- size: 562.4 GB compressed
- origins: other 19916, pypi 12975, github-archive 11030, cran/bioconductor 6775, github-release 3726, cpan 2629, gnu 1238, gitlab 674
- producers: GNU format 17001, ustar 14700, git archive 13367, Python tarfile (pax) 9603, v7 3261, GNU tar (pax) 849, libarchive (pax) 79, posix-version-0000 53, none 49, star 1
- compression: gzip 51868, xz 4010, bzip2 2345, none 738
- scanner stopped early: 56
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
  - tarlz@0.21: invalid checksum at offset 0
  - deutex@5.2.2: invalid checksum at offset 0
  - guile-xapian@0.6.0: invalid checksum at offset 0
  - ccwl@0.5.0: invalid checksum at offset 0
  - fcitx5-chinese-addons@5.1.13_dict: invalid checksum at offset 0
  - run64@0.1.0: invalid checksum at offset 0
  - fcitx5-lua@5.0.17: invalid checksum at offset 0
  - mupdf@1.27.2-source: invalid checksum at offset 0
  - jakarta-oro@2.0.8: invalid checksum at offset 2377216
  - fcitx5-configtool@5.1.14: invalid checksum at offset 0
  - ed@1.21: invalid checksum at offset 0
  - xcb-imdkit@1.0.9: invalid checksum at offset 0
  - fcitx5-rime@5.1.14: invalid checksum at offset 0
  - tissue@0.1.0: invalid checksum at offset 0
  - fcitx5@5.1.21_dict: invalid checksum at offset 0
  - zutils@1.12: invalid checksum at offset 0
  - serveez@0.3.0: invalid checksum at offset 0
  - sirit-source@1.0.3: invalid checksum at offset 0
  - libime@1.1.15_dict: invalid checksum at offset 0
  - alive@2.0.5: invalid checksum at offset 0
  - guile-email@0.4.1: invalid checksum at offset 0
  - PullParser@2.1.10: invalid checksum at offset 5556736
  - commons-cli@1.2-src: invalid checksum at offset 398848
  - kolam@0.1.0: invalid checksum at offset 0
  - fcitx5-anthy@5.1.10: invalid checksum at offset 0
  - libbs2b@3.1.0: invalid checksum at offset 0
  - fcitx5-gtk@5.1.7: invalid checksum at offset 0
  - commons-jxpath@1.3-src: invalid checksum at offset 1840640
  - gnuastro@0.24: invalid checksum at offset 0
  - fcitx5-qt@5.1.14: invalid checksum at offset 0
  - py-multiprocess@0.70.12.2: invalid checksum at offset 0
  - aida@3.2.1: invalid checksum at offset 2802176
  - commons-lang@2.4: invalid checksum at offset 6874624
  - commons-logging@1.1.1: invalid checksum at offset 3452928

## untar

Rejects 189 of 58963 (0.3%); 149 of 30229 latest versions (0.5%).

| reason | tarballs | latest | origins | producers | examples |
|---|---|---|---|---|---|
| FileExistsError: [Errno N] File exists: '…' | 78 | 62 | other 69, github-release 5, pypi 4 | ustar 58, GNU format 8, git archive 6 | snap-loader-static@1.0.0.1; htn@0.1.0.0; shelly-extra@0.3.0.2 |
| Archive contains an invalid number b'…' | 49 | 48 | other 23, gnu 16, github-release 9 | none 49 | ocrad@0.29; git-warp-time@1.0.0; wget@1.25.0 |
| Archive contains data after the end-of-archive marker | 27 | 21 | other 24, cpan 1, github-release 1 | posix-version-0000 17, v7 7, ustar 2 | bsf-bin@2.4.0; psutils-p17@; Logfile-Rotate@1.04 |
| Archive is truncated | 24 | 12 | other 24 | ustar 18, GNU format 4, v7 2 | SDL2_ttf@2.24.0; SDL2_image@2.8.12; eng-rus@ |
| Archive contains a lone zero block | 7 | 4 | other 7 | posix-version-0000 7 | jakarta-oro@2.0.8; PullParser@2.1.10; commons-cli@1.2-src |
| Archive contains unsafe path … | 2 | 1 | other 1, github-release 1 | git archive 1, GNU format 1 | dtv-scan-tables@2024-03-24-7098bdd27548; masurca@3.3.1 |
| Archive contains forktty-N.N/pipe of unsupported type b'…' | 1 | 1 | other 1 | GNU format 1 | forktty@1.3 |
| Archive contains a name prefix in a header that is not ustar | 1 | 0 | other 1 | v7 1 | gtkmm@2.4.11 |

## Features

Number of tarballs with each feature, of which latest versions; their origins, producers and median mtime years, and what untar did with them.

| feature | tarballs | latest | origins | producers | years | untar rejects | examples |
|---|---|---|---|---|---|---|---|
| `name.fills-field` | 6734 | 1524 | github-archive 2451, other 1701, pypi 1459 | git archive 3254, GNU format 1434, Python tarfile (pax) 1246 | 1970–2026 | 18 | texinfo@7.2 `texinfo-7.2/tp/t/results/init_files_tests/documentation_exam`; linux@4.14.336 `linux-4.14.336/Documentation/devicetree/bindings/interrupt-c` |
| `ustar.prefix` | 5672 | 1215 | github-archive 3327, other 963, github-release 603 | git archive 4298, ustar 1285, GNU tar (pax) 60 | 1980–2026 | 18 | texinfo@7.2 `split_test_before_first_node.info`; linux@4.14.336 `samsung,exynos4210-combiner.txt` |
| `type.nul` | 3336 | 1599 | other 2187, github-release 529, gnu 489 | v7 3238, GNU format 98 | 1970–2026 | 8 | make@3.82 `make-3.82/vmsfunctions.c`; gzip@1.2.4 `gzip-1.2.4/README` |
| `v7.bytes-after-linkname` | 2685 | 1180 | other 1814, github-release 430, gnu 412 | v7 2685 | 1970–2026 | 3 | make@3.82 `make-3.82/`; m4@1.4.7 `m4-1.4.7/` |
| `name.dir-without-trailing-slash` | 1100 | 937 | cpan 581, github-release 303, other 194 | ustar 992, GNU format 93, GNU tar (pax) 15 | 1970–2026 | 1 | oyacc@6.6 `oyacc-6.6`; perl@5.15.7 `perl-5.15.7` |
| `tree.dir-after-contents` | 851 | 775 | other 783, cpan 30, pypi 22 | ustar 795, GNU format 27, git archive 13 | 1970–2026 | 9 | streaming-utils@0.2.6.0 `streaming-utils-0.2.6.0/Streaming/`; distributed-closure@0.5.0.0 `distributed-closure-0.5.0.0/src/Data/Profunctor/` |
| `number.size.leading-space` | 799 | 714 | cpan 665, other 107, gnu 13 | ustar 660, posix-version-0000 53, GNU format 50 | 1990–2026 | 34 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `name.non-ascii` | 684 | 135 | github-archive 241, other 228, pypi 149 | git archive 294, GNU format 159, Python tarfile (pax) 120 | 2004–2026 | 0 | kbd@1.15 `kbd-1.15/doc/utf/♪♬`; gcc@15.2.0 `gcc-15.2.0/gcc/testsuite/go.test/test/fixedbugs/issue27836.d` |
| `platform.case-collision` | 637 | 114 | other 419, github-release 102, github-archive 61 | git archive 372, GNU format 93, v7 86 | 1980–2026 | 1 | perl@5.003 `perl5-perl-5.003/configure`; perl@5.004_05 `perl5.004_05/Configure` |
| `platform.windows-reserved-name` | 401 | 38 | other 278, github-release 79, github-archive 41 | git archive 241, GNU tar (pax) 73, GNU format 53 | 1994–2026 | 0 | perl@5.000 `perl5-perl-5.000/hints/aux.sh`; perl@5.003 `perl5-perl-5.003/hints/aux.sh` |
| `number.gid.no-digits` | 252 | 107 | pypi 192, other 43, github-release 16 | GNU format 182, ustar 50, posix-version-0000 18 | 1970–2026 | 0 | hadoop@3.4.2-src `hadoop-3.4.2-src/README.txt`; ipv8_rust_tunnels@0.1.53 `ipv8_rust_tunnels-0.1.53/PKG-INFO` |
| `number.uid.no-digits` | 252 | 107 | pypi 192, other 43, github-release 16 | GNU format 182, ustar 50, posix-version-0000 18 | 1970–2026 | 0 | hadoop@3.4.2-src `hadoop-3.4.2-src/README.txt`; ipv8_rust_tunnels@0.1.53 `ipv8_rust_tunnels-0.1.53/PKG-INFO` |
| `name.leading-dot-slash` | 184 | 71 | other 141, github-release 25, gnu 9 | GNU format 147, ustar 33, GNU tar (pax) 2 | 1970–2026 | 1 | curie@v1.0 `./LICENSE`; hdf5@1.10.11 `./hdf5-1.10.11/` |
| `platform.windows-invalid-character` | 177 | 62 | other 93, github-archive 67, github-release 7 | git archive 104, GNU format 38, ustar 20 | 2003–2026 | 1 | xitomatl_0.0.0-akku.208.62a8243_repack@ `fmt/let-optionals*.larceny.sls`; courier-unicode@2.6.0 `courier-unicode-2.6.0/man/unicode::ucs_4.3` |
| `tree.duplicate.dir-dir` | 148 | 26 | github-release 83, other 62, gnu 3 | git archive 98, ustar 45, GNU format 3 | 2017–2026 | 3 | besu@24.1.2 `besu-24.1.2/./`; lightweight-testing@0.1 `lightweight-testing-0.1/./` |
| `number.gid.leading-space` | 141 | 90 | other 106, gnu 12, cpan 11 | posix-version-0000 52, GNU format 49, v7 36 | 1990–2026 | 34 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.uid.base256` | 141 | 69 | pypi 65, other 35, github-release 27 | GNU format 130, libarchive (pax) 11 | 2008–2026 | 0 | leo@2_v1.7.0 `leo2/`; Bytes-Random-Secure-Tiny@1.011 `Bytes-Random-Secure-Tiny-1.011/` |
| `number.uid.leading-space` | 141 | 90 | other 106, gnu 12, cpan 11 | posix-version-0000 52, GNU format 49, v7 36 | 1990–2026 | 34 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `number.gid.base256` | 137 | 64 | pypi 62, github-release 33, other 30 | GNU format 122, libarchive (pax) 15 | 2008–2026 | 0 | Bytes-Random-Secure-Tiny@1.011 `Bytes-Random-Secure-Tiny-1.011/`; pyannotate@1.2.0 `pyannotate-1.2.0/` |
| `number.mode.leading-space` | 131 | 82 | other 96, gnu 12, cpan 11 | posix-version-0000 51, GNU format 44, v7 33 | 1990–2026 | 30 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `pax-global.after-members` | 79 | 16 | github-release 60, other 19 | git archive 79 | 2018–2026 | 1 | inform@6.44-r3 `pax_global_header`; rpm@4.20.1 `pax_global_header` |
| `symlink.absolute` | 78 | 34 | github-archive 35, other 30, github-release 12 | git archive 39, GNU format 27, GNU tar (pax) 6 | 2006–2026 | 1 | live.2026.01.12@ `live/testProgs/whiteroom.mp3`; imapsync@2.314 `imapsync-2.314/X/fullchain.pem` |
| `tree.duplicate.file-file` | 78 | 62 | other 69, github-release 5, pypi 4 | ustar 58, GNU format 8, git archive 6 | 1970–2026 | 78 | snap-loader-static@1.0.0.1 `snap-loader-static-1.0.0.1/LICENSE`; htn@0.1.0.0 `htn-0.1.0.0/src/Algorithms/Htn.hs` |
| `number.mtime.leading-space` | 64 | 50 | other 42, gnu 11, cpan 10 | GNU format 41, v7 16, posix-version-0000 4 | 1990–2013 | 12 | gzip@1.2.4 `gzip-1.2.4/README`; tar@1.12 `tar-1.12/` |
| `magic.posix-with-odd-version` | 53 | 27 | other 43, github-release 10 | posix-version-0000 53 | 2003–2026 | 24 | hadoop@3.4.2-src `hadoop-3.4.2-src/README.txt`; bsf-bin@2.4.0 `bsf-2.4.0/` |
| `name.dot` | 38 | 22 | other 18, github-release 12, gnu 7 | GNU format 37, v7 1 | 1970–2026 | 1 | partclone-utils@0.4.3 `./`; cmucl@21d-x86-linux `./` |
| `pax.nul-in-value.SCHILY.xattr.*` | 31 | 24 | other 12, cpan 10, github-release 8 | libarchive (pax) 30, git archive 1 | 2018–2026 | 0 | Crypt-X509@0.55 `Crypt-X509-0.55/PaxHeader/README`; djview@4.12.3 `PaxHeader/djview-4.12.3` |
| `platform.windows-trailing-dot-or-space` | 31 | 15 | other 22, pypi 4, github-archive 3 | v7 12, git archive 8, Python tarfile (pax) 5 | 1994–2026 | 0 | perl@5.000 `perl5-perl-5.000/vms/makefile.`; Python@2.3.7 `Python-2.3.7/Mac/IDE scripts/Search Python Documentation...` |
| `name.not-nfc` | 28 | 3 | github-archive 20, pypi 6, other 2 | git archive 20, GNU format 7, Python tarfile (pax) 1 | 2016–2026 | 0 | discount@2.2.7d `discount-2.2.7d/tests/muñoz.t`; discount@3.0.2.0 `discount-3.0.2.0/tests/muñoz.t` |
| `end.data-after` | 23 | 19 | other 20, cpan 1, github-release 1 | posix-version-0000 15, v7 5, ustar 2 | 1995–2026 | 23 | bsf-bin@2.4.0 `bsf-2.4.0/samples/xsl/table-data.xml`; psutils-p17@ `psutils/showchar.sh` |
| `linkname.no-nul` | 22 | 7 | other 17, github-release 3, github-archive 2 | GNU format 14, git archive 5, Python tarfile (pax) 3 | 2014–2026 | 0 | ghc@9.12.4-src `ghc-9.12.4/libraries/Cabal/cabal-testsuite/PackageTests/Requ`; nextcloud@34.0.5 `nextcloud/apps/app_api/js/app_api-vendors-node_modules_nextc` |
| `platform.normalization-collision` | 20 | 1 | github-archive 20 | git archive 20 | 2016–2020 | 0 | plexus-archiver@4.2.2 `plexus-archiver-plexus-archiver-4.2.2/src/test/resources/utf`; lmod@7.8.15 `Lmod-7.8.15/contrib/Presentations/Keynote_Lmod_SC14-Calcul_Q` |
| `end.missing` | 19 | 7 | other 19 | ustar 18, v7 1 | 1992–2026 | 19 | SDL2_ttf@2.24.0 `SDL2_ttf-2.24.0/external/harfbuzz/README`; SDL2_image@2.8.12 `SDL2_image-2.8.12/Xcode/macOS/SDL2.framework/Resources` |
| `pax.LIBARCHIVE.creationtime` | 18 | 8 | github-release 10, other 6, cpan 1 | libarchive (pax) 17, GNU tar (pax) 1 | 2014–2025 | 0 | leo@2_v1.7.0 `leo2/`; Proc-Wait3@0.05 `Proc-Wait3-0.05/Changes` |
| `hardlink.to-itself` | 15 | 3 | other 15 | GNU format 14, GNU tar (pax) 1 | 2012–2022 | 0 | atari++_1.85@ `atari++/winmain.cpp`; xscreensaver@6.12 `xscreensaver-6.12/driver/wayland-dpy.c` |
| `tree.duplicate.file-hardlink` | 15 | 3 | other 15 | GNU format 14, GNU tar (pax) 1 | 2012–2022 | 0 | atari++_1.85@ `atari++/winmain.cpp`; xscreensaver@6.12 `xscreensaver-6.12/driver/wayland-dpy.c` |
| `number.uid.no-terminator` | 12 | 12 | cpan 12 | ustar 12 | 2014–2022 | 0 | App-rainbarf@1.4 `App-rainbarf-1.4`; JSON-WebToken@0.10 `Build.PL` |
| `pax.newline-in-value.SCHILY.xattr.*` | 12 | 10 | cpan 5, other 4, github-release 3 | libarchive (pax) 12 | 2018–2025 | 0 | Minion@10.31 `Minion-10.31/lib/Mojolicious/Plugin/Minion/resources/public/`; Term-ReadLine-Gnu@1.47 `Term-ReadLine-Gnu-1.47/t/comptest/PaxHeader/README` |
| `number.gid.no-terminator` | 11 | 11 | cpan 11 | ustar 11 | 2014–2022 | 0 | App-rainbarf@1.4 `App-rainbarf-1.4`; JSON-WebToken@0.10 `Build.PL` |
| `name.dot-component` | 10 | 6 | other 10 | GNU format 5, ustar 4, GNU tar (pax) 1 | 2012–2026 | 0 | besu@24.1.2 `besu-24.1.2/./`; lightweight-testing@0.1 `lightweight-testing-0.1/./` |
| `name.control-character` | 8 | 3 | github-archive 7, other 1 | git archive 7, ustar 1 | 2009–2025 | 0 | cdrtools@3.02a09 `cdrtools-3.02/libfind/ifpdi`; wgrib2@3.6.0 `wgrib2-3.6.0/docs/web_docs/jj` |
| `end.zero-block-before-member` | 7 | 4 | other 7 | posix-version-0000 7 | 2003–2009 | 7 | jakarta-oro@2.0.8 `jakarta-oro-2.0.8/jakarta-oro-2.0.8.jar`; PullParser@2.1.10 `PullParser2.1.10/src/java/x2/README.txt` |
| `end.lone-zero-block` | 5 | 5 | other 5 | GNU format 4, v7 1 | 1998–2014 | 5 | eng-rus@ `eng-rus.index`; srecord@1.64 `srecord-1.64/debian/srecord.install` |
| `name.trailing-slash-on-file` | 5 | 4 | other 4, gnu 1 | v7 5 | 1994–2023 | 3 | sendmail.8.18.2@ `sendmail-8.18.2/`; tcp_wrappers_7.6@ `tcp_wrappers_7.6/` |
| `end.archive-after` | 4 | 2 | other 4 | posix-version-0000 2, v7 2 | 2005–2016 | 4 | commons-jexl@2.1.1-src `commons-jexl-2.1.1-src/jexl2-compat/src/main/java/org/apache`; jmol@14.8.0 `jmol-14.7.5_2016.12.17/jmol.sh` |
| `name.backslash` | 4 | 3 | gnu 2, other 1, github-archive 1 | ustar 2, Python tarfile (pax) 1, git archive 1 | 2010–2026 | 0 | texi2html@5.0 `texi2html-5.0/test/info_coverage/f--ile""\.png`; gstreamer-docs@1.28.1 `gstreamer-docs-1.28.1/html/assets/js/search/hotdoc_fragments` |
| `tree.under-file` | 4 | 3 | other 3, gnu 1 | v7 4 | 1994–2023 | 2 | sendmail.8.18.2@ `sendmail-8.18.2/Makefile`; tcp_wrappers_7.6@ `tcp_wrappers_7.6/README` |
| `name.absolute` | 2 | 1 | other 1, github-release 1 | git archive 1, GNU format 1 | 2018–2024 | 2 | dtv-scan-tables@2024-03-24-7098bdd27548 `/usr/share/dvb/`; masurca@3.3.1 `/MaSuRCA-3.3.1/` |
| `name.not-utf8` | 2 | 2 | gnu 2 | GNU format 2 | 2004–2004 | 0 | aspell-is@0.51.1-0 `aspell-is-0.51.1-0/\xedslenska.alias`; aspell-nb@0.50.1-0 `aspell-nb-0.50.1-0/bokm\xe5l.alias` |
| `number.mtime.no-digits` | 2 | 2 | github-release 2 | ustar 2 | 2025–2026 | 0 | camunda-modeler@5.52.0-linux-x64 `camunda-modeler-5.52.0-linux-x64/`; stretchly@1.19.0 `Stretchly-1.19.0/` |
| `format.star` | 1 | 1 | other 1 | star 1 | 2020–2020 | 0 | berkeley-db@18.1.40 `db-18.1.40/` |
| `linkname.on-dir` | 1 | 1 | other 1 | ustar 1 | 2020–2020 | 0 | bgen@1.1.7 `BGEN-6ac2d582f9/doc/wiki` |
| `linkname.on-file` | 1 | 1 | other 1 | ustar 1 | 2020–2020 | 0 | bgen@1.1.7 `BGEN-6ac2d582f9/doc/html/spec/v1.1.html` |
| `name.double-slash` | 1 | 0 | other 1 | GNU format 1 | 2021–2021 | 0 | ghc@9.0.2-x86_64-deb10-linux `ghc-9.0.2/libraries/ghc-bignum/dist-install/build/include//H` |
| `pax.LIBARCHIVE.symlinktype` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | crow-translate@4.0.2 `crow-translate/src/3rdparty/espeak-ng/src/include/espeak/spe` |
| `pax.key-in-two-headers.LIBARCHIVE.xattr.*` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | libmygpo-qt.1.2.0@ `libmygpo-qt/` |
| `pax.key-in-two-headers.SCHILY.xattr.*` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | libmygpo-qt.1.2.0@ `libmygpo-qt/` |
| `pax.repeated-key` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | libmygpo-qt.1.2.0@ `PaxHeader/libmygpo-qt` |
| `pax.size-on-dir` | 1 | 1 | pypi 1 | GNU tar (pax) 1 | 1970–1970 | 0 | llama_index_workflows@2.26.0 `llama_index_workflows-2.26.0/` |

## Fingerprints

- magic (tarballs using each): posix 38600, gnu 17092, v7 3261, posix-version-0000 53, star 1
- size (tarballs using each): dn 55907, ds 2188, sdn 664, sds 135, dsn 28
- mode (tarballs using each): dn 56562, dsn 2159, ds 177, sdsn 123, sdn 8
- checksum (tarballs using each): dns 43124, dn 14798, sdns 770, d 360, dsn 36, x 36, sdsn 20, ds 14, sdn 6, xdx 6, xd 3, sds 3
- pax_header_name (tarballs using each): ././@PaxHeader 9601, */PaxHeaders/* 421, */PaxHeaders.N/* 396, ./PaxHeaders/* 340, H.paxheader 327, ./PaxHeaders.N/* 318, */PaxHeader/* 76, */PaxHeaders.N 51, * 44, PaxHeader/* 44, */PaxHeaders.N/ 44, */PaxHeaders 37
- extended_sequence (tarballs using each): - 49452, x 10867, L 1942, KL 10, K 9
- gnu_long_name (tarballs using each): ././@LongLink 1942
- end (tarballs using each): padded-to-10240 47916, unpadded 10967
- zero_blocks_after_end (tarballs using each): 0 13878, 9 2447, 17 2417, 11 2417, 6 2404, 7 2399, 3 2392, 18 2389, 16 2380, 12 2369, 8 2351, 4 2351
- pax_keys (tarballs using each): mtime 10139, path 2746, atime 680, ctime 666, uid 102, gid 71, LIBARCHIVE.xattr.* 38, SCHILY.xattr.* 37, LIBARCHIVE.creationtime 17, SCHILY.dev 15, SCHILY.ino 15, SCHILY.nlink 15
- pax_global_keys (tarballs using each): comment 13367
- compression layer: several streams 4, trailing zeros 2
