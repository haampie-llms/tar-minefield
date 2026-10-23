# Tar file extraction test suite

This repo provides an extensive **test suite for tar file extraction**, with the goal to ensure implementations extract tar archives the same way.

There are dozens of implementations of tar file extraction out there, from command line tools to libraries for programming languages. Because the tar file format leaves room for interpretation, different implementations can extract certain crafted tar files in different ways.

This is a security concern: for example, a security scanner could see different files than what is ultimately extracted.

By assigning [identifiers](https://haampie-llms.github.io/tar-minefield/) to these ambiguities, and providing test cases and usage data, the hope is that tar implementations can converge on a strict parser and identical behavior.

## Examples

| case | the archive | what implementations make of it |
|---|---|---|
| [F12](https://haampie-llms.github.io/tar-minefield/F12.html) | a size field of `000000 1000`, with a space | GNU tar, BusyBox and node-tar read 0, and find a file `smuggled` in the data; bsdtar, Python, Go and Rust reject it |
| [F14](https://haampie-llms.github.io/tar-minefield/F14.html) | a pax header says the file is empty, its own header says 512 bytes | GNU tar, bsdtar, Python, Go, Rust and node-tar extract an empty `a` and a file `smuggled`; BusyBox, Perl and RubyGems extract `a` with 512 bytes |
| [F15](https://haampie-llms.github.io/tar-minefield/F15.html) | a pax size on a directory | GNU tar, 7-Zip and Rust extract `dir/`; bsdtar, Python, Go and node-tar extract `dir/smuggled` as well |
| [N20](https://haampie-llms.github.io/tar-minefield/N20.html) | one pax header with both `path=first` and `path=second` | most extract `second`; Rust's tar crate and Haskell's tar extract `first`; Perl and RubyGems ignore both |
| [K01](https://haampie-llms.github.io/tar-minefield/K01.html) | a regular file named `a/` | GNU tar, bsdtar and node-tar create a directory `a`; Python, Go, Rust and BusyBox an empty file `a` |
| [S10](https://haampie-llms.github.io/tar-minefield/S10.html) | a symlink `a` to `target`, then a file `a` | GNU tar, bsdtar, Go and Rust replace the link with the file; Python's tarfile writes through it, to `target` |

A sha256 pins the bytes of a tarball, not the tree it extracts to. Tar leaves implementations room
to disagree on that tree: where a member's data ends, which field gives its name, whether `a/` is a
file, which of two copies wins. So a reviewer, scanner or SBOM tool can see one tree while the
installer extracts another: a *parser differential*, as in CVE-2025-62518 (tokio-tar),
GHSA-3pv8-6f4r-ffg2 (tar-rs) and CVE-2026-53655 (node-tar). A **strict parser** closes that gap
by rejecting every ambiguous archive instead of picking a tree. tar-minefield gives you what you
need to write one, or to check one:

- **[The test suite](suite/)**: cases, each an archive with a verdict and the tree it must extract.
  [The site](https://haampie-llms.github.io/tar-minefield/) has a page per case.
- **[The default policy](#the-default-policy)**: which ambiguities to reject, which names to
  normalize, and what to accept.
- **[The scans](contrib/data/STRICT.md)**: what that policy costs on every release tarball of Spack,
  nixpkgs, Guix and live-bootstrap.

[METHOD.md](METHOD.md#terms) defines the terms.

## Comparison

<!-- begin matrix.py -->
What 20 implementations make of the 55 cases: a row per case, by level, and a column per implementation, with the outcomes of all cases at the top. [The site](https://haampie-llms.github.io/tar-minefield/) has a page per case.

![What every implementation makes of every case of the test suite. Outcomes of all cases: strict.py: every criterion: ✅47 ⛔8; strict.py: default policy: ✅55; GNU tar: ✅23 ⚠️32; bsdtar: ✅26 ⚠️29; BusyBox tar: ✅23 ⚠️32; 7-Zip: ✅22 ⚠️31 ⛔1 ❌1; Python tarfile, filter=data: ✅26 ⚠️28 ⛔1; Python tarfile, filter=tar: ✅26 ⚠️29; Python tarfile, filter=fully_trusted: ✅25 ⚠️28 💥2; node-tar: ✅19 ⚠️35 ❌1; node-tar, strict: ✅27 ⚠️27 ⛔1; Java Commons Compress: ✅24 ⚠️30 ❌1; Go archive/tar: ✅22 ⚠️33; Go archive/tar, tarinsecurepath=0: ✅25 ⚠️30; Rust tar: ✅27 ⚠️28; Rust astral-tokio-tar: ✅27 ⚠️27 ⛔1; RubyGems: ✅19 ⚠️30 ⛔2 ❌4; Perl Archive::Tar: ✅26 ⚠️27 ⛔1 ❌1; Haskell tar: ✅30 ⚠️20 ⛔5; Julia Tar.jl: ✅32 ⚠️23; live-bootstrap untar: ✅17 ⚠️30 ❌6 💥2; live-bootstrap untar, --non-strict: ✅12 ⚠️35 ❌6 💥2](contrib/matrix/matrix.svg)
<!-- end matrix.py -->

## Strictness is affordable

<!-- begin strict.py -->
**The default policy rejects 151 of 62,622 release tarballs (0.24%); rejecting every criterion would reject 622 (0.99%).** The criterion that rejects the most tarballs on its own is `tree.duplicate.file-file` of the default policy, and `name.leading-dot-slash` of every criterion.

| ecosystem | tarballs | GB | rejected: every criterion | rejected: default policy |
|---|---:|---:|---:|---:|
| guix | 10,168 | 76.5 | 101 (0.99%) | 28 (0.28%) |
| live-bootstrap | 171 | 1.1 | 0 (0.00%) | 0 (0.00%) |
| nix | 18,990 | 77.7 | 157 (0.83%) | 70 (0.37%) |
| spack | 37,554 | 1,080.9 | 392 (1.04%) | 67 (0.18%) |
| **all, distinct** | 62,622 | 1,215.8 | 622 (0.99%) | 151 (0.24%) |

Tarballs: those downloaded and in a compression the scanner reads. Generated by `contrib/scanner/strict.py`; [contrib/data/STRICT.md](contrib/data/STRICT.md) has what was scanned, when the tarballs were made, and the cost of every criterion.
<!-- end strict.py -->

## The default policy

Strict where implementations can extract different trees, lenient where they cannot:

- **Reject** what implementations extract differently. F: a pax size on a member without data, or
  one that disagrees with the header; members after a zero block or after the end of the archive.
  N: a name from several sources; absolute names, `..`, `\`, control characters, names that are
  not UTF-8. K: a file named `a/`, a link target on a file. S: a file twice, even as identical
  copies (in fish 4.7.1 and logstash 8.15.2 they differ); a hardlink to itself or to a symlink; a
  member under a file or written through a symlink.
- **Normalize** names that are one path: `./a` is `a`, `.` is the root, `a/./b` and `a//b` are
  `a/b`. Duplicates are found after normalizing, so this hides none.
- **Accept** what cannot change the tree, or what the sha256 already settles: a global pax header
  with only a `comment`, as `git archive` writes; the magic `ustar\0\0\0`; newlines in xattrs;
  absolute symlinks, which are created but never written through; an archive that ends after a
  complete member without an end-of-archive marker, or with data after it that is not a header.

Everything else in the catalogue is rejected. A criterion that only a few old tarballs have stays
rejected: a package that needs such a tarball can allow it by its sha256. The policy is `DEFAULT`
in [contrib/scanner/strict.py](contrib/scanner/strict.py), argued in [METHOD.md](METHOD.md#the-default-policy),
and every rule of it has a case.

## Test an implementation

Every case is `suite/archives/<case>.tar`, with its verdict and manifest in `<case>.json` next to
it. A strict parser rejects every case to reject, extracts the manifest from every case to
accept, and either rejects a tolerated case or extracts its manifest. Extract them in a throwaway
directory, as some cases escape lenient implementations. [suite/](suite) describes the format,
and needs nothing else of this repository: copy it into the tests of an implementation.

## Contents

- [suite/](suite): the test suite: the archives, their manifests, and the scripts that write
  them byte by byte.
- [METHOD.md](METHOD.md): the terms, the method, the catalogue of ambiguities, the verdicts and
  the default policy, prior art, and open questions.
- [contrib/](contrib): how the data was made: the scanner and the scans of real tarballs, the
  matrix of implementations, and the site.
- [docs/](docs): the site, written by `contrib/site.py`.
