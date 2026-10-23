# Scan of all 19086 nixpkgs tarballs, 2026-10-23

Every tarball that the Hydra jobs of nixpkgs fetch with `fetchurl`, not a sample. In a checkout
of nixpkgs, with the jobs of `all-tarballs.nix` evaluated in chunks of 1000, each in its own
process (all at once takes over 10 GB of memory):

```console
$ nix-instantiate --eval --json --strict -E \
      'builtins.attrNames (import ./maintainers/scripts/all-tarballs.nix)' > attrs.json
$ # for each chunk.json of 1000 names of attrs.json:
$ nix-instantiate --readonly-mode --eval --json --strict maintainers/scripts/find-tarballs.nix \
      --arg expr 'let all = import ./maintainers/scripts/all-tarballs.nix;
                  in map (n: all.${n}) (builtins.fromJSON (builtins.readFile ./chunk.json))' \
      > chunk-files.json
$ nix-instantiate --eval --json --strict -E \
      'removeAttrs (import ./pkgs/build-support/fetchurl/mirrors.nix) [ "hashedMirrors" ]' \
      > mirrors.json
$ python -I scanner/nix_list.py mirrors.json chunk-*-files.json > sample.jsonl
$ TMPDIR=~/.cache/tar-minefield-tmp python -I scanner/run.py scan sample.jsonl results.jsonl \
      --untar ~/untar --jobs 8 --cache ~/.cache/tar-minefield \
      --reuse ../../spack/2026-10-23/results.jsonl --reuse ../../spack/2026-10-23-b/results.jsonl \
      --reuse ../../live-bootstrap/2026-10-23/results.jsonl
$ python -I scanner/report.py --title "Scan of all 19086 nixpkgs tarballs" results.jsonl > REPORT.md
```

The scan started on the chunks that were evaluated, and was run again as more were: `run.py
scan` skips the tarballs it has.

- Scanner: `tarscan.py` version `25bfa32e6e71`.
- Packages: nixpkgs `75ba83324cc35b3e156ac46ee379f38e8f0b1808` (2026-10-23), 25,703 jobs for
  x86_64-linux. Evaluated with the static Nix 2.28.9 of Hydra build 349255020 (sha256
  `7f1eded4292ff1159ef938b134d7016d09b6d678325d638ac82eb4a93466d150`), without a daemon and
  with `--readonly-mode`: 26 chunks, 13 minutes in total, at most 10.6 GB of memory for a chunk.
- untar: `2305390138cf436059b89b7b15146dc5213a3ba5`, `untar.py` version `51a9c3aa565c`.
- Platform: Ubuntu 26.04 (Linux 7.0) on x86_64, Python 3.14.4. untar extracted to ext4, which is
  case-sensitive, so no failures are caused by the filesystem.

What the list holds: the files that nixpkgs fetches with a flat hash, so not those of
`fetchFromGitHub` or `fetchzip`, which hash the unpacked tree, and of those, the tar files with a
sha256 that are not changed after the download. One revision of nixpkgs has about one version
of each package, so nearly all are `latest`: 1,035 are not, mostly where nixpkgs has several
versions of a package (`latest` is the highest). It has whole package ecosystems, abandoned
packages included: 7,190 tarballs (38%) are from Hackage, 3,851 from PyPI and 1,899 from CPAN.
Read results by origin, so that one producer, such as `cabal sdist`, does not dominate.

Downloads: 9,190 from tarballs.nixos.org, the others from their upstream URLs, which nixpkgs
lists after it: the mirror does not have about half of them, Hackage's above all. 74 could not
be downloaded from any URL. 217 were reused from the Spack and live-bootstrap scans. 78 GB in
35 minutes.

22 tarballs are `.tar.lz` (11) and `.tar.zst` (11), which `tarscan.py` does not decompress. It
scans them as uncompressed, stops at the first header (`invalid checksum at offset 0`), and untar
rejects them with `Archive contains an invalid number`. These are not rejections of the
archives: of the 100 that untar rejects, 78 are.
