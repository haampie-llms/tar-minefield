# The corpus

Tar archives, each with a verdict, as [METHOD.md](../METHOD.md) describes: `n_` cases a strict
implementation rejects, `y_` cases every implementation accepts, and `i_` cases that the default
policy accepts. [MATRIX.md](MATRIX.md) shows what implementations make of each case.

Every case has a code, such as `F15`, whose letter is its level in METHOD.md: F framing, N names,
K kinds, S order and state, G global pax headers. A code stays with its case, and a new case gets
the next free number of its letter. The [site](https://haampie-llms.github.io/tar-minefield/) has
a page per code.

**Some archives escape the directory they are extracted to in lenient extractors.** Their files
are harmless, and say in their names and contents what happened, but extract them in a
throwaway directory.

## Layout

- `archives/<case>.tar`: the archive, uncompressed.
- `archives/<case>.json`: its code, its verdict, the features of `scanner/tarscan.py` it is about, and for
  `y_` and `i_` cases the tree an implementation must extract: path, kind, and for files their size,
  sha256 and whether they are executable.
- `archives/<case>.txt`: what the case is about, and every block of the archive with its offset
  and, for headers, every field with its raw bytes.
- `archives/<case>.svg`: a map of its blocks, every one 512 bytes to scale, with the fields of
  headers where they are, and the bytes that the case writes itself marked.
- `cases/<case>.py`: the script that writes it, whose docstring explains the case: the decision
  point where implementations differ, where the scans saw it, and what implementations do with it.
- `blocks.py`: writes archives from raw 512-byte blocks, and describes each block as it writes
  it. It uses no tar implementation, so that the corpus does not test one against itself.

## Generating and checking

```console
$ python -I corpus/generate.py            # write archives/
$ python -I corpus/generate.py --check    # fail if archives/ is not what the scripts write
$ python -I corpus/generate.py --scan     # check the scanner and the default policy against it
```

Generation is deterministic, with the Python standard library only. `--scan` checks that
`tarscan.py` reports the features of each case, and that the default policy of
`scanner/strict.py` rejects the `n_` cases and accepts the others.

A new case is a script in `cases/`, named for its verdict and level, with `VERDICT`, `CODE`, `FEATURES`,
`TREE` for `y_` and `i_` cases, and a `build(archive)` function.

## What implementations make of it

```console
$ python -I corpus/matrix.py WORK
```

extracts every case with every implementation it finds, and writes `matrix.json` and the table
in `MATRIX.md` from it. Libraries without an extractor, such as Go's `archive/tar`, list the
members, which are then applied in order. WORK holds the builds of the programs in `runners/`,
whose dependencies are pinned, and the extractions: each in a directory of its own, two levels
below a directory that catches what is written outside it. Run it in a throwaway directory, or a
container, as some cases escape in lenient extractors. It uses what is installed: GNU tar,
the untar of live-bootstrap (with git and a C compiler), bsdtar, BusyBox, 7-Zip, CPython's
`tarfile` with each of its filters, Go, Rust, Haskell
(cabal), Java (with the jars of `runners/java/jars.txt`, which it downloads and checks), Ruby,
Perl, Julia and Node.js: each on PATH, or in an environment variable of its name in capitals,
such as `$JULIA`.

## The site

```console
$ python -I corpus/site.py docs data/*/*/results.jsonl
```

writes `docs/`, which GitHub Pages serves: an index with the matrix, and a page per case with its
explanation, its block map and dump, how many tarballs of the scans have its feature and how many
of those the default policy rejects, and what every implementation makes of it, from
`matrix.json`. Plain HTML and CSS, without scripts, all of it generated. The `Seen in:` of a
case is written by hand: site.py fails if it says no tarball where the scans have its feature, or
names tarballs where they have none.
