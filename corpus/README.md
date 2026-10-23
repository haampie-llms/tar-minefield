# The corpus

Tar archives, each with a verdict, as [METHOD.md](../METHOD.md) describes: `n_` cases a strict
parser rejects, `y_` cases every parser accepts, and `i_` cases that the default policy accepts.
It has its first cases; the others of the catalogue follow.

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
