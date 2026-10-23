# Lists of Spack's tarballs

Lists of all tarballs of Spack's builtin repository, from which samples can be drawn without
Spack. Each is made with `scanner/spack_list.py`, with Spack configured to use the
spack-packages commit in its name:

```console
$ cat > config/repos.yaml <<'YAML'
repos::
  builtin: /path/to/spack-packages/repos/spack_repo/builtin
YAML
$ spack -C config python scanner/spack_list.py > <commit>-<platform>.jsonl
```

A list depends on the platform it is made on: packages of prebuilt binaries have their versions
per operating system and architecture.

- `73b099d5c1-linux-x86_64.jsonl`: spack-packages `73b099d5c1118951de3ac69b91e6f73afc41690e`
  (2026-10-19), Spack `37c7f2646acbdf12bd3fae177e1daff3f2d7ce0b`, on Linux x86_64. The scan of
  `../2026-10-23` has all of its tarballs. Two earlier samples, now in the history of this
  repository, were drawn from a list of the same commits made on macOS arm64, which was not
  kept: a few of their tarballs, binaries for macOS or arm64, are not in this one.
