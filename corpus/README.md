# The corpus

Tar archives, each with a verdict, as [METHOD.md](../METHOD.md) describes: `n_` cases a strict
parser rejects, `y_` cases every parser accepts, and `i_` cases that the default policy accepts.
[MATRIX.md](MATRIX.md) shows what implementations make of each case.

**Some archives escape the directory they are extracted to in lenient extractors.** Their files
are harmless, and say in their names and contents what happened, but extract them in a
throwaway directory.

## Layout

- `archives/<case>.tar`: the archive, uncompressed.
- `archives/<case>.json`: its verdict, the features of `scanner/tarscan.py` it is about, and for
  `y_` and `i_` cases the tree a parser must extract: path, kind, and for files their size,
  sha256 and whether they are executable.
- `archives/<case>.txt`: what the case is about, and every block of the archive with its offset
  and, for headers, every field with its raw bytes.
- `cases/<case>.py`: the script that writes it, whose docstring explains the case: the decision
  point where readers differ, where the scans saw it, and what implementations do with it.
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

A new case is a script in `cases/`, named for its verdict and level, with `VERDICT`, `FEATURES`,
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
BusyBox, 7-Zip, CPython's `tarfile` with each of its filters, untar (in `~/untar`), Go, Rust,
Node.js, and Julia (on PATH, or as `$JULIA`).
