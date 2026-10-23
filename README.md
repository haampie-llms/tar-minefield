# Tar file extraction test suite

This repo provides an extensive **[test suite for tar file extraction](suite/)**, with the goal to ensure implementations extract tar archives the same way.

There are dozens of implementations of tar file extraction out there, from command line tools to libraries for programming languages. Because the tar file format leaves room for interpretation, different implementations can extract certain crafted tar files in different ways.

This is a security concern: for example, a security scanner could see different files than what is ultimately extracted.

By assigning [identifiers](https://haampie-llms.github.io/tar-minefield/) to these ambiguities, and providing test cases and usage data, the hope is that tar implementations can converge on a strict parser and identical behavior.

This project proposes a **[default policy](https://haampie-llms.github.io/tar-minefield/#policy)** that rejects the vast majority of ambiguities in tar files that could make implementations extract different files, while ensuring that nearly every source tarball already published can still be extracted. <!-- begin strict.py -->Of the 62,622 source tarballs of Spack, nixpkgs, Guix and live-bootstrap, it accepts 99.76% ([per ecosystem](https://haampie-llms.github.io/tar-minefield/#tarballs)).<!-- end strict.py -->

## Examples

| case | the archive | what implementations make of it |
|---|---|---|
| [F12](https://haampie-llms.github.io/tar-minefield/F12.html) | a size field of `000000 1000`, with a space | GNU tar, BusyBox and node-tar read 0, and find a file `smuggled` in the data; bsdtar, Python, Go and Rust reject it |
| [F14](https://haampie-llms.github.io/tar-minefield/F14.html) | a pax header says the file is empty, its own header says 512 bytes | GNU tar, bsdtar, Python, Go, Rust and node-tar extract an empty `a` and a file `smuggled`; BusyBox, Perl and RubyGems extract `a` with 512 bytes |
| [F15](https://haampie-llms.github.io/tar-minefield/F15.html) | a pax size on a directory | GNU tar, 7-Zip and Rust extract `dir/`; bsdtar, Python, Go and node-tar extract `dir/smuggled` as well |
| [N20](https://haampie-llms.github.io/tar-minefield/N20.html) | one pax header with both `path=first` and `path=second` | most extract `second`; Rust's tar crate and Haskell's tar extract `first`; Perl and RubyGems ignore both |
| [K01](https://haampie-llms.github.io/tar-minefield/K01.html) | a regular file named `a/` | GNU tar, bsdtar and node-tar create a directory `a`; Python, Go, Rust and BusyBox an empty file `a` |
| [S10](https://haampie-llms.github.io/tar-minefield/S10.html) | a symlink `a` to `target`, then a file `a` | GNU tar, bsdtar, Go and Rust replace the link with the file; Python's tarfile writes through it, to `target` |

Use **[the test suite](suite/)** in your tests, or browse **[the website](https://haampie-llms.github.io/tar-minefield/)** for what each case means, what implementations make of it, and how often it occurs in source tarballs.

## Comparison

<!-- begin matrix.py -->
What 21 implementations make of the 55 cases: a row per case, by level, and a column per implementation, with the outcomes of all cases at the top. [The website](https://haampie-llms.github.io/tar-minefield/) has a page per case.

[![What every implementation makes of every case of the test suite. Outcomes of all cases: strict.py: ✅55; GNU tar: ✅23 ⚠️32; bsdtar: ✅26 ⚠️29; BusyBox tar: ✅23 ⚠️32; 7-Zip: ✅22 ⚠️31 ⛔1 ❌1; Python tarfile, filter=data: ✅26 ⚠️28 ⛔1; Python tarfile, filter=tar: ✅26 ⚠️29; Python tarfile, filter=fully_trusted: ✅25 ⚠️28 💥2; node-tar: ✅19 ⚠️35 ❌1; node-tar, strict: ✅27 ⚠️27 ⛔1; Java Commons Compress: ✅24 ⚠️30 ❌1; Go archive/tar: ✅22 ⚠️33; Go archive/tar, tarinsecurepath=0: ✅25 ⚠️30; Rust tar: ✅27 ⚠️28; Rust astral-tokio-tar: ✅27 ⚠️27 ⛔1; Rust tar-codec, as in uv: ✅40 ⚠️10 ⛔4 ❌1; RubyGems: ✅19 ⚠️30 ⛔2 ❌4; Perl Archive::Tar: ✅26 ⚠️27 ⛔1 ❌1; Haskell tar: ✅30 ⚠️20 ⛔5; Julia Tar.jl: ✅32 ⚠️23; live-bootstrap untar: ✅17 ⚠️30 ❌6 💥2; live-bootstrap untar, --non-strict: ✅12 ⚠️35 ❌6 💥2](contrib/matrix/matrix.svg)](https://haampie-llms.github.io/tar-minefield/)
<!-- end matrix.py -->

## Contents

- [suite/](suite): the test suite. Copy it into your tests; its README describes the format.
- [METHOD.md](METHOD.md): the terms, the catalogue of ambiguities, the verdicts and the default policy.
- [contrib/](contrib): how the data was made.
- [docs/](docs): the website.
