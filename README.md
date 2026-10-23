# tar-minefield

**A test suite for tar parsers that refuse to guess, and the data that shows refusing is affordable.**

A sha256 pins the bytes of a tarball, not the tree it extracts to. Tar leaves implementations room
to disagree on that tree: where a member's data ends, which field gives its name, whether `a/` is a
file, which of two copies wins. So a reviewer, scanner or SBOM tool can see one tree while the
installer extracts another: a *parser differential*, as in CVE-2025-62518 (tokio-tar),
GHSA-3pv8-6f4r-ffg2 (tar-rs) and CVE-2026-53655 (node-tar). A **strict parser** closes that gap
by rejecting every ambiguous archive instead of picking a tree. tar-minefield gives you what you
need to write one, or to check one:

- **[The corpus](corpus/)**: cases, each an archive with a verdict and the tree it must extract.
  [The site](https://haampie-llms.github.io/tar-minefield/) has a page per case.
- **[The default policy](#the-default-policy)**: which ambiguities to reject, which names to
  normalize, and what to accept.
- **[The scans](data/STRICT.md)**: what that policy costs on every release tarball of Spack,
  nixpkgs, Guix and live-bootstrap.

It follows Nicolas Seriot's [JSONTestSuite](https://github.com/nst/JSONTestSuite) and
[Parsing JSON is a Minefield](https://seriot.ch/projects/parsing_json.html), from which it takes
its name and its verdicts.

## Terms

| term | meaning |
|---|---|
| **implementation** | A program or library that turns a tar archive into a tree, by extracting it or by listing its members: GNU tar, Python `tarfile`, Go `archive/tar`, … |
| **member** | One entry of an archive: a header, its extended headers, and its data. |
| **tree** | What an implementation extracts: paths, each with a kind (file, directory, symlink, hardlink), the contents of a file or the target of a link, and whether a file is executable. Nothing else, such as mtimes and owners. |
| **ambiguity** | Something in an archive from which two implementations, each following a defensible reading of POSIX, GNU tar or practice, extract different trees. |
| **level** | The class of an ambiguity, from most to least damage it allows: **F** framing (where a member's data ends), **N** names, **K** kinds, **S** order and state (duplicates and links); and **G** global pax headers. |
| **strict parser** | An implementation that rejects an archive with an ambiguity, rather than extracting one of its trees. |
| **feature** | What the scanner reports of an archive, such as `name.leading-dot-slash`. |
| **criterion** | A feature that is an ambiguity, for which a strict parser may reject an archive. [METHOD.md](METHOD.md#initial-catalogue) lists them. |
| **policy** | The criteria a strict parser rejects: either *every criterion*, or the [default policy](#the-default-policy). |
| **case** | An archive of the corpus, with a code (its level and a number, such as `F15`), a verdict, and for `y_` and `i_` a manifest. |
| **verdict** | `n_`: a strict parser must reject it. `y_`: every implementation must accept it. `i_`: a strict parser may reject it, and the default policy accepts it. |
| **manifest** | The tree an implementation must extract from a `y_` or `i_` case, if it accepts it. |
| **outcome** | What an implementation makes of a case: ✅ as its verdict says, ⚠️ accepts an `n_` case, ⛔ rejects an `i_` case, ❌ rejects a `y_` case or extracts another tree than the manifest, 💥 writes outside its destination. |
| **tarball** | An archive released by a project and pinned by a package manager, as opposed to a case. |

## Implementations disagree

<!-- begin matrix.py -->
**Each of 20 implementations accepts between 20 and 35 of the 39 `n_` cases, and they extract different trees from 29 of them.** 2 cases make an implementation write outside its destination. Rows are the 55 cases, by level; columns are the implementations and the two policies of `scanner/strict.py`, with their outcomes of all cases at the top. [The site](https://haampie-llms.github.io/tar-minefield/) has a page per case: its blocks, a hex dump, how many scanned tarballs have it, and what every implementation makes of it. [corpus/MATRIX.md](corpus/MATRIX.md) has the matrix as a table.

![What every implementation makes of every case of the corpus. Outcomes of all cases: strict.py: every criterion: ✅47 ⛔8; strict.py: default policy: ✅55; GNU tar: ✅23 ⚠️32; bsdtar: ✅26 ⚠️29; live-bootstrap untar: ✅17 ⚠️30 ❌6 💥2; live-bootstrap untar, --non-strict: ✅12 ⚠️35 ❌6 💥2; BusyBox tar: ✅23 ⚠️32; 7-Zip: ✅22 ⚠️31 ⛔1 ❌1; Python tarfile, filter=fully_trusted: ✅25 ⚠️28 💥2; Python tarfile, filter=tar: ✅26 ⚠️29; Python tarfile, filter=data: ✅26 ⚠️28 ⛔1; Go archive/tar: ✅22 ⚠️33; Go archive/tar, tarinsecurepath=0: ✅25 ⚠️30; Rust tar: ✅27 ⚠️28; Rust astral-tokio-tar: ✅27 ⚠️27 ⛔1; Haskell tar: ✅30 ⚠️20 ⛔5; Java Commons Compress: ✅24 ⚠️30 ❌1; RubyGems: ✅19 ⚠️30 ⛔2 ❌4; Perl Archive::Tar: ✅26 ⚠️27 ⛔1 ❌1; Julia Tar.jl: ✅32 ⚠️23; node-tar: ✅19 ⚠️35 ❌1; node-tar, strict: ✅27 ⚠️27 ⛔1](corpus/matrix.svg)

Generated by `corpus/matrix.py` from `corpus/matrix.json`.
<!-- end matrix.py -->

## Strictness is affordable

<!-- begin strict.py -->
**The default policy rejects 151 of 62,622 release tarballs (0.24%); rejecting every criterion would reject 622 (0.99%).** The criterion that rejects the most tarballs on its own is `tree.duplicate.file-file` of the default policy, and `name.leading-dot-slash` of every criterion.

| ecosystem | tarballs | GB | rejected: every criterion | rejected: default policy | of latest versions |
|---|---|---|---|---|---|
| guix | 10,168 | 76.5 | 101 (0.99%) | 28 (0.28%) | 25 (0.26%) |
| live-bootstrap | 171 | 1.1 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| nix | 18,990 | 77.7 | 157 (0.83%) | 70 (0.37%) | 65 (0.36%) |
| spack | 37,554 | 1080.9 | 392 (1.04%) | 67 (0.18%) | 17 (0.22%) |
| **all, distinct** | 62,622 | 1215.8 | 622 (0.99%) | 151 (0.24%) | 95 (0.30%) |

Tarballs: those downloaded and in a compression the scanner reads. Latest: the latest version of each package, under the default policy. Generated by `scanner/strict.py`; [data/STRICT.md](data/STRICT.md) has what was scanned, when the tarballs were made, and the cost of every criterion.
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
in [scanner/strict.py](scanner/strict.py), argued in [METHOD.md](METHOD.md#the-default-policy),
and every rule of it has a case.

## Test an implementation

Extract every `corpus/archives/*.tar` in a throwaway directory, as some cases escape lenient
implementations. A strict parser rejects every `n_` case, and extracts from every `y_` and `i_` case
the manifest in the `.json` next to it, or rejects the `i_` case. To add an implementation to the
matrix, add it to `implementations()` in [corpus/matrix.py](corpus/matrix.py); [corpus/](corpus) has
the details.

## Contents

- [METHOD.md](METHOD.md): the method, the catalogue of ambiguities, the verdicts and the default
  policy, prior art, and open questions.
- [corpus/](corpus): the cases, the scripts that write them byte by byte, and the matrix.
- [scanner/](scanner): the scanner, and how to scan the tarballs of another ecosystem.
- [data/](data): the scans, each with a `RUN.md` on how it was made;
  [data/STRICT.md](data/STRICT.md) has the cost of every criterion, and
  [data/REPORT.md](data/REPORT.md) every feature found.
- [docs/](docs): the site, written by `corpus/site.py`.
