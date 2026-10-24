# Scan of all 10200 Guix tarballs

- tarballs: 10200, scanned: 10199 (9705 latest versions, 494 older)
- not downloaded: 1, scanner crashed: 0
- downloaded from the first of their URLs (a mirror): 7090
- copied from other scans with `--reuse`: 2491, read from `--cache`: 32; sources by host: bordeaux.guix.gnu.org 7090, tarballs.nixos.org 1559, hackage.haskell.org 622, ci.guix.gnu.org 334, cran.r-project.org 124, download.gnome.org 90
- size: 76.7 GB compressed
- origins: other 3845, cran/bioconductor 2833, pypi 1697, cpan 967, gnu 416, github-release 385, github-archive 43, gitlab 13
- producers: GNU format 4127, ustar 3024, Python tarfile (pax) 1702, v7 873, git archive 295, GNU tar (pax) 112, none 31, posix-version-0000 18, libarchive (pax) 17
- compression: gzip 8009, xz 1406, bzip2 429, none 355
- scanner stopped early: 35
  - ocrad@0.29: invalid checksum at offset 0
  - wget@1.25.0: invalid checksum at offset 0
  - ddrescue@1.30: invalid checksum at offset 0
  - rcs@5.10.1: invalid checksum at offset 0
  - moe@1.16: invalid checksum at offset 0
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

## untar

Rejects 69 of 10199 (0.7%); 64 of 9705 latest versions (0.7%).

| reason | tarballs | latest | origins | producers | examples |
|---|---:|---:|---|---|---|
| Archive contains an invalid number b'…' | 31 | 31 | other 18, gnu 11, github-release 2 | none 31 | ocrad@0.29; wget@1.25.0; ddrescue@1.30 |
| FileExistsError: [Errno N] File exists: '…' | 17 | 16 | other 15, pypi 1, github-release 1 | ustar 10, Python tarfile (pax) 4, git archive 3 | string-conversions@0.4.0.1; notmuch@0.40; multipart@0.2.1 |
| Archive contains data after the end-of-archive marker | 11 | 10 | other 11 | posix-version-0000 9, v7 1, git archive 1 | tcp_wrappers_7.6@; commons-lang@2.6-src; xml-commons-resolver@1.2 |
| Archive is truncated | 6 | 4 | other 6 | ustar 5, v7 1 | SDL2_image@2.8.8; ruby@4.0.5; fastcap@2.0-18Sep92 |
| Archive contains a lone zero block | 4 | 3 | other 4 | posix-version-0000 4 | jakarta-oro@2.0.8; PullParser@2.1.10; commons-cli@1.2-src |

## Features

Number of tarballs with each feature, of which latest versions; their origins, producers and median mtime years, and what untar did with them.

| feature | tarballs | latest | origins | producers | years | untar rejects | examples |
|---|---:|---:|---|---|---|---:|---|
| `type.nul` | 878 | 833 | other 608, gnu 146, github-release 110 | v7 867, GNU format 11 | 1970–2026 | 1 | libofa@0.9.3 `libofa-0.9.3/README`; libdvbpsi@1.3.3 `libdvbpsi-1.3.3/.auto/missing` |
| `v7.bytes-after-linkname` | 693 | 656 | other 481, gnu 120, github-release 89 | v7 693 | 1970–2026 | 0 | libofa@0.9.3 `libofa-0.9.3/`; libdvbpsi@1.3.3 `libdvbpsi-1.3.3/` |
| `name.fills-field` | 543 | 399 | other 343, pypi 82, github-release 52 | GNU format 199, Python tarfile (pax) 166, git archive 73 | 1970–2026 | 5 | dbus@1.16.2 `dbus-1.16.2/test/data/systemd-activation/com.example.SendDen`; qtserialbus-everywhere-src@6.12.0 `qtserialbus-everywhere-src-6.12.0/tests/auto/qcanuniqueiddes` |
| `ustar.prefix` | 339 | 295 | cpan 150, other 110, github-release 34 | ustar 236, git archive 95, libarchive (pax) 8 | 1981–2026 | 6 | Data-Stream-Bulk@0.11 `README`; CatalystX-Component-Traits@0.19 `README` |
| `name.dir-without-trailing-slash` | 318 | 273 | cpan 209, other 97, github-release 11 | ustar 258, GNU format 52, GNU tar (pax) 8 | 1970–2026 | 0 | Catalyst-DispatchType-Regex@5.90035 `Catalyst-DispatchType-Regex-5.90035`; Test-Future-IO-Impl@0.14 `Test-Future-IO-Impl-0.14` |
| `number.size.leading-space` | 272 | 268 | cpan 236, other 33, gnu 2 | ustar 236, posix-version-0000 18, GNU format 11 | 1995–2026 | 14 | Catalyst-DispatchType-Regex@5.90035 `Catalyst-DispatchType-Regex-5.90035`; Test-Future-IO-Impl@0.14 `Test-Future-IO-Impl-0.14` |
| `tree.dir-after-contents` | 154 | 145 | other 140, cpan 11, github-release 2 | ustar 148, GNU format 4, posix-version-0000 1 | 1970–2026 | 2 | network-control@0.1.7 `network-control-0.1.7/test/`; shelly@1.12.1.1 `shelly-1.12.1.1/test/` |
| `name.non-ascii` | 59 | 37 | other 36, pypi 12, gnu 7 | GNU format 34, Python tarfile (pax) 13, GNU tar (pax) 7 | 2015–2026 | 0 | libreoffice@26.8.0.3 `libreoffice-26.8.0.3/sc/qa/unit/data/gnumeric/täßt.gnumeric`; gcc@15.2.0 `gcc-15.2.0/gcc/testsuite/go.test/test/fixedbugs/issue27836.d` |
| `platform.case-collision` | 54 | 38 | other 37, gnu 11, pypi 3 | GNU format 25, git archive 11, v7 10 | 1981–2026 | 0 | bsd-games@2.17 `bsd-games-2.17/tests/morse.sos`; sword@1.9.0 `sword-1.9.0/bindings/objc/SWORD/` |
| `number.gid.leading-space` | 37 | 33 | other 32, cpan 3, gnu 2 | posix-version-0000 18, GNU format 11, v7 7 | 1995–2025 | 14 | Getopt-ArgvFile@1.11 `Getopt-ArgvFile-1.11/`; Crypt-RC4@2.02 `Crypt-RC4-2.02/` |
| `number.mode.leading-space` | 37 | 33 | other 32, cpan 3, gnu 2 | posix-version-0000 18, GNU format 11, v7 7 | 1995–2025 | 14 | Getopt-ArgvFile@1.11 `Getopt-ArgvFile-1.11/`; Crypt-RC4@2.02 `Crypt-RC4-2.02/` |
| `number.uid.leading-space` | 37 | 33 | other 32, cpan 3, gnu 2 | posix-version-0000 18, GNU format 11, v7 7 | 1995–2025 | 14 | Getopt-ArgvFile@1.11 `Getopt-ArgvFile-1.11/`; Crypt-RC4@2.02 `Crypt-RC4-2.02/` |
| `name.leading-dot-slash` | 31 | 21 | other 18, gnu 9, github-release 3 | GNU format 26, ustar 5 | 1970–2026 | 0 | sqliteodbc@0.99991 `./sqliteodbc-0.99991/`; numdiff@5.9.0 `./numdiff-5.9.0/` |
| `number.gid.no-digits` | 23 | 23 | pypi 16, github-release 4, other 2 | GNU format 15, ustar 7, posix-version-0000 1 | 1970–2026 | 0 | voila-dashboards-widgets-manager8@0.5.8 `package/lib/index.js`; HDO.db_1.0.0@ `HDO.db/DESCRIPTION` |
| `number.uid.no-digits` | 23 | 23 | pypi 16, github-release 4, other 2 | GNU format 15, ustar 7, posix-version-0000 1 | 1970–2026 | 0 | voila-dashboards-widgets-manager8@0.5.8 `package/lib/index.js`; HDO.db_1.0.0@ `HDO.db/DESCRIPTION` |
| `platform.windows-invalid-character` | 22 | 21 | other 16, gnu 3, pypi 2 | GNU format 8, git archive 4, Python tarfile (pax) 4 | 2008–2026 | 1 | gv@3.7.4 `gv-3.7.4/src/nls/noint:de.dat`; notmuch@0.40 `notmuch-0.40/test/corpora/default/01:2,` |
| `magic.posix-version-nuls` | 18 | 15 | other 18 | posix-version-0000 18 | 2003–2022 | 13 | commons-lang@2.6-src `commons-lang-2.6-src/build.xml`; apache-solr@3.6.2-src `apache-solr-3.6.2/dev-tools/` |
| `number.uid.base256` | 18 | 18 | pypi 9, other 4, cpan 2 | GNU format 16, libarchive (pax) 2 | 2011–2026 | 0 | clint@0.5.1 `clint-0.5.1/`; Number-Compare@0.03 `Number-Compare-0.03/` |
| `platform.windows-reserved-name` | 18 | 13 | other 16, gnu 2 | GNU format 7, git archive 5, ustar 2 | 2002–2026 | 0 | pies@1.8 `pies-1.8/tests/aux/`; rakarrack@0.6.1 `rakarrack-0.6.1/doc/help/imagenes/con.jpg` |
| `tree.duplicate.file-file` | 17 | 16 | other 15, pypi 1, github-release 1 | ustar 10, Python tarfile (pax) 4, git archive 3 | 2001–2026 | 17 | string-conversions@0.4.0.1 `string-conversions-0.4.0.1/src/Data/String/Conversions.hs`; notmuch@0.40 `notmuch-0.40/version.txt` |
| `number.gid.base256` | 16 | 16 | pypi 9, other 4, cpan 2 | GNU format 14, libarchive (pax) 2 | 2011–2026 | 0 | clint@0.5.1 `clint-0.5.1/`; Number-Compare@0.03 `Number-Compare-0.03/` |
| `number.mtime.leading-space` | 15 | 14 | other 12, cpan 2, gnu 1 | GNU format 7, v7 4, posix-version-0000 3 | 1995–2011 | 3 | Crypt-RC4@2.02 `Crypt-RC4-2.02/`; tcp_wrappers_7.6@ `tcp_wrappers_7.6/` |
| `name.dot` | 13 | 4 | gnu 7, other 6 | GNU format 13 | 1970–2026 | 0 | guile@2.0.9 `./`; hadrian-bootstrap-sources@9.8.1 `./` |
| `symlink.absolute` | 13 | 13 | other 12, pypi 1 | GNU format 8, Python tarfile (pax) 2, GNU tar (pax) 2 | 2006–2026 | 1 | tachyon@0.99.5 `tachyon/scenes/tpoly`; notmuch@0.40 `notmuch-0.40/devel/notmuch-web/static/css/jquery-ui.css` |
| `end.data-after` | 10 | 9 | other 10 | posix-version-0000 8, v7 1, git archive 1 | 1995–2026 | 10 | tcp_wrappers_7.6@ `tcp_wrappers_7.6/README.NIS`; commons-lang@2.6-src `commons-lang-2.6-src/src/test/java/org/apache/commons/lang/W` |
| `pax.nul-in-value.SCHILY.xattr.*` | 7 | 6 | other 6, github-release 1 | libarchive (pax) 7 | 2022–2025 | 0 | Healpix_3.82_2024Nov13@ `Healpix_3.82/src/common_libraries/libsharp/m4/PaxHeader/ltop`; libmygpo-qt.1.2.0@ `PaxHeader/libmygpo-qt` |
| `tree.duplicate.dir-dir` | 7 | 7 | other 4, gnu 3 | git archive 4, GNU format 3 | 2021–2026 | 1 | rpm@4.20.1 `rpm-4.20.1/po/`; subed@1.5.4 `subed-1.5.4/` |
| `end.missing` | 6 | 4 | other 6 | ustar 5, v7 1 | 1992–2026 | 6 | SDL2_image@2.8.8 `SDL2_image-2.8.8/Xcode/macOS/SDL2.framework/SDL2`; ruby@4.0.5 `ruby-4.0.5/zjit.rbinc` |
| `pax-global.after-members` | 6 | 5 | other 3, github-release 3 | git archive 6 | 2021–2025 | 0 | rpm@4.20.1 `pax_global_header`; x42-plugins@20230701 `pax_global_header` |
| `platform.windows-trailing-dot-or-space` | 5 | 5 | other 3, gnu 1, pypi 1 | Python tarfile (pax) 2, ustar 1, GNU format 1 | 2010–2026 | 0 | texi2html@5.0 `texi2html-5.0/test/manuals/res_info/ccvs_mediawiki_nosplit/c`; giac_2.0.0@21 `giac-2.0.0/check/oim.tst.` |
| `end.zero-block-before-member` | 4 | 3 | other 4 | posix-version-0000 4 | 2003–2009 | 4 | jakarta-oro@2.0.8 `jakarta-oro-2.0.8/jakarta-oro-2.0.8.jar`; PullParser@2.1.10 `PullParser2.1.10/src/java/x2/README.txt` |
| `name.dot-component` | 4 | 2 | other 4 | GNU format 3, ustar 1 | 2012–2023 | 0 | tuffy@20120614 `tuffy-20120614/./._Tuffy.otf`; privoxy@3.0.34-stable-src `privoxy-3.0.34-stable/./acconfig.h` |
| `name.not-nfc` | 4 | 3 | other 2, pypi 1, github-archive 1 | GNU format 2, Python tarfile (pax) 1, git archive 1 | 2020–2026 | 0 | discount@2.2.7d `discount-2.2.7d/tests/muñoz.t`; discount@3.0.2.0 `discount-3.0.2.0/tests/muñoz.t` |
| `pax.LIBARCHIVE.creationtime` | 3 | 2 | other 3 | libarchive (pax) 3 | 2019–2025 | 0 | asio@1.36.0 `asio-1.36.0/`; asio@1.28.2 `asio-1.28.2/` |
| `hardlink.to-itself` | 2 | 1 | other 2 | GNU tar (pax) 1, GNU format 1 | 2014–2022 | 0 | xscreensaver@6.12 `xscreensaver-6.12/driver/wayland-dpy.c`; ghc@7.8.4-x86_64-unknown-linux-deb7 `ghc-7.8.4/utils/haddock/dist/build/tmp/haddock` |
| `linkname.no-nul` | 2 | 1 | other 2 | GNU format 1, Python tarfile (pax) 1 | 2025–2026 | 0 | ghc@9.10.2-src `ghc-9.10.2/libraries/Cabal/cabal-testsuite/PackageTests/Back`; gnome-software@49.3 `gnome-software-49.3/plugins/flatpak/tests/app-update/org.tes` |
| `name.backslash` | 2 | 2 | gnu 1, other 1 | ustar 1, Python tarfile (pax) 1 | 2010–2026 | 0 | texi2html@5.0 `texi2html-5.0/test/info_coverage/f--ile""\.png`; gstreamer-docs@1.28.1 `gstreamer-docs-1.28.1/html/assets/js/search/hotdoc_fragments` |
| `pax.newline-in-value.SCHILY.xattr.*` | 2 | 2 | other 1, github-release 1 | libarchive (pax) 2 | 2023–2024 | 0 | qd@2.3.24 `qd-2.3.24/PaxHeader/NEWS`; libjwt@1.17.2 `libjwt-1.17.2/PaxHeader/CMakeLists.txt` |
| `tree.duplicate.file-hardlink` | 2 | 1 | other 2 | GNU tar (pax) 1, GNU format 1 | 2014–2022 | 0 | xscreensaver@6.12 `xscreensaver-6.12/driver/wayland-dpy.c`; ghc@7.8.4-x86_64-unknown-linux-deb7 `ghc-7.8.4/utils/haddock/dist/build/tmp/haddock` |
| `end.archive-after` | 1 | 1 | other 1 | posix-version-0000 1 | 2011–2011 | 1 | commons-jexl@2.1.1-src `commons-jexl-2.1.1-src/jexl2-compat/src/main/java/org/apache` |
| `name.trailing-slash-on-file` | 1 | 1 | other 1 | v7 1 | 1995–1995 | 1 | tcp_wrappers_7.6@ `tcp_wrappers_7.6/` |
| `number.uid.no-terminator` | 1 | 1 | cpan 1 | ustar 1 | 2016–2016 | 0 | Math-MatrixReal@2.13 `Math-MatrixReal-2.13` |
| `pax.LIBARCHIVE.symlinktype` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | crow-translate@4.0.2 `crow-translate/src/3rdparty/espeak-ng/src/include/espeak/spe` |
| `pax.key-in-two-headers.LIBARCHIVE.xattr.*` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | libmygpo-qt.1.2.0@ `libmygpo-qt/` |
| `pax.key-in-two-headers.SCHILY.xattr.*` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | libmygpo-qt.1.2.0@ `libmygpo-qt/` |
| `pax.repeated-key` | 1 | 1 | other 1 | libarchive (pax) 1 | 2025–2025 | 0 | libmygpo-qt.1.2.0@ `PaxHeader/libmygpo-qt` |
| `platform.normalization-collision` | 1 | 1 | github-archive 1 | git archive 1 | 2020–2020 | 0 | plexus-archiver@4.2.2 `plexus-archiver-plexus-archiver-4.2.2/src/test/resources/utf` |
| `tree.under-file` | 1 | 1 | other 1 | v7 1 | 1995–1995 | 1 | tcp_wrappers_7.6@ `tcp_wrappers_7.6/README` |

## Fingerprints

- magic (tarballs using each): posix 5150, gnu 4162, v7 873, posix-version-0000 18
- size (tarballs using each): dn 9350, ds 541, sdn 238, sds 34, dsn 5
- mode (tarballs using each): dn 9585, dsn 541, ds 39, sdsn 34, sdn 3
- checksum (tarballs using each): dns 9226, dn 641, sdns 266, d 31, x 23, dsn 5, ds 4, xdx 4, sdsn 3, sdn 2, dx 2, dnxs 1
- pax_header_name (tarballs using each): ././@PaxHeader 1702, */PaxHeaders/* 73, ./PaxHeaders/* 53, */PaxHeaders.N/* 40, ./PaxHeaders.N/* 37, * 16, */PaxHeader/* 16, */PaxHeaders 12, */PaxHead 11, */PaxHeader 11, */PaxHeaders/ 10, */PaxHea 9
- extended_sequence (tarballs using each): - 8490, x 1836, L 290, KL 1, K 1
- gnu_long_name (tarballs using each): ././@LongLink 290
- end (tarballs using each): padded-to-10240 7751, unpadded 2407
- zero_blocks_after_end (tarballs using each): 0 2900, 11 409, 5 403, 6 399, 17 396, 9 396, 7 393, 8 392, 3 390, 4 387, 18 384, 14 379
- pax_keys (tarballs using each): mtime 1793, path 330, atime 110, ctime 102, uid 12, gid 8, LIBARCHIVE.xattr.* 7, SCHILY.xattr.* 7, LIBARCHIVE.creationtime 2, LIBARCHIVE.symlinktype 1, SCHILY.fflags 1, linkpath 1
- pax_global_keys (tarballs using each): comment 295
- compression layer: several streams 3
