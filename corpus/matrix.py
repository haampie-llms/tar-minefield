"""Run every case of the corpus with every implementation, and tabulate what they make of it.

    python -I corpus/matrix.py WORK
    python -I corpus/matrix.py --readme README.md

Julia is found on PATH, or as $JULIA. WORK is a directory for builds and extractions: runners are built there, and every case is
extracted there in a directory of its own, two levels below a directory that catches what is
written outside it. Some cases do write outside the destination in lenient extractors, so WORK
should be a throwaway directory. Writes corpus/matrix.json, the results, and corpus/MATRIX.md,
the table made from them. With --readme, the summary between `<!-- begin matrix.py -->` and
`<!-- end matrix.py -->` in that file, and MATRIX.md, are generated again from matrix.json, and
nothing is run.

Each implementation either extracts a case, or, for libraries that have no extractor, lists its
members, which are then applied in order to an empty tree, as a program that uses it would. The
outcome is compared with the case's verdict:

- ✅ as the verdict says: rejects an `n_` case; extracts the tree in the manifest of a `y_` or
  `i_` case
- ⚠️ accepts an `n_` case: the letter says which tree, so that implementations that make
  different trees of one case have different letters
- ⛔ rejects an `i_` case, which a strict parser may
- ❌ rejects a `y_` case, or extracts another tree than the manifest of a `y_` or `i_` case
- 💥 writes outside the destination
"""

import hashlib
import io
import json
import os
import shutil
import stat
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARCHIVES = os.path.join(HERE, "archives")
RUNNERS = os.path.join(HERE, "runners")
TIMEOUT = 60


def run(cmd, **kw):
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=TIMEOUT, **kw)
        return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"


def first_line(cmd):
    code, out, err = run(cmd)
    return (out or err).strip().splitlines()[0] if (out or err).strip() else "?"


TARFILE = (
    "import sys, tarfile\n"
    "with tarfile.open(sys.argv[1]) as t:\n"
    "    t.extractall(sys.argv[2], filter=sys.argv[3])\n"
)
UNTAR = "import sys; sys.path.insert(0, sys.argv[3]); import untar; untar.extract(sys.argv[1], sys.argv[2])\n"


def implementations(work):
    """(name, version, kind, command) for every implementation found: kind is "extract", with a
    command of the archive and the destination, or "list", with a command of the archive."""
    found = []
    if shutil.which("tar"):
        found.append(("GNU tar", first_line(["tar", "--version"]), "extract",
                      lambda a, d: ["tar", "-xf", a, "-C", d]))
    if shutil.which("busybox"):
        found.append(("BusyBox tar", first_line(["busybox"]).split(" multi-call")[0], "extract",
                      lambda a, d: ["busybox", "tar", "-xf", a, "-C", d]))
    if shutil.which("7z"):
        version = first_line(["7z"]) if first_line(["7z"]) != "?" else "?"
        code, out, _ = run(["7z"])
        version = next((l for l in out.splitlines() if l.startswith("7-Zip")), "7-Zip").split(" :")[0]
        found.append(("7-Zip", version, "extract", lambda a, d: ["7z", "x", "-y", "-bd", f"-o{d}", a]))
    python = sys.executable
    pyversion = f"CPython {sys.version.split()[0]}"
    for f in ("fully_trusted", "tar", "data"):
        found.append((f"tarfile, filter={f}", pyversion, "extract",
                      lambda a, d, f=f: [python, "-I", "-c", TARFILE, a, d, f]))
    untar = os.path.expanduser("~/untar")
    if os.path.exists(os.path.join(untar, "untar.py")):
        commit = first_line(["git", "-C", untar, "rev-parse", "--short=12", "HEAD"])
        found.append(("untar", f"untar {commit}", "extract",
                      lambda a, d: [python, "-I", "-c", UNTAR, a, d, untar]))
    build = os.path.join(work, "build")
    os.makedirs(build, exist_ok=True)
    if shutil.which("go"):
        binary = os.path.join(build, "go-runner")
        code, _, err = run(["go", "build", "-o", binary, "."], cwd=os.path.join(RUNNERS, "go"))
        if code == 0:
            version = f"archive/tar of {first_line(['go', 'version']).split()[2]}"
            found.append(("Go archive/tar", version, "list", lambda a, b=binary: [b, a]))
            found.append(("Go archive/tar, tarinsecurepath=0", version, "list",
                          lambda a, b=binary: ["env", "GODEBUG=tarinsecurepath=0", b, a]))
        else:
            print("go runner:", err, file=sys.stderr)
    if shutil.which("cargo"):
        target = os.path.join(build, "rust")
        code, _, err = run(["cargo", "build", "--release", "--quiet", "--target-dir", target],
                           cwd=os.path.join(RUNNERS, "rust"))
        if code == 0:
            binary = os.path.join(target, "release", "runner")
            found.append(("Rust tar", "tar 0.4.46, unpack", "extract",
                          lambda a, d, b=binary: [b, "tar", a, d]))
            found.append(("Rust astral-tokio-tar", "astral-tokio-tar 0.7.0, unpack", "extract",
                          lambda a, d, b=binary: [b, "astral-tokio-tar", a, d]))
        else:
            print("rust runner:", err, file=sys.stderr)
    julia = os.environ.get("JULIA") or shutil.which("julia")
    if julia:
        script = os.path.join(RUNNERS, "julia", "extract.jl")
        code, out, _ = run([julia, "--startup-file=no", "-e",
                            'using Tar; print(VERSION, " ", pkgversion(Tar))'])
        version = "Tar {1} of Julia {0}".format(*out.split()) if code == 0 else "?"
        found.append(("Julia Tar.jl", version, "extract",
                      lambda a, d, j=julia, s=script: [j, "--startup-file=no", s, a, d]))
    if shutil.which("npm"):
        node = os.path.join(build, "node")
        shutil.copytree(os.path.join(RUNNERS, "node"), node, dirs_exist_ok=True)
        code, _, err = run(["npm", "ci", "--silent", "--no-audit", "--no-fund"], cwd=node)
        if code == 0:
            script = os.path.join(node, "extract.js")
            found.append(("node-tar", "tar 7.5.22", "extract",
                          lambda a, d, s=script: ["node", s, a, d]))
            found.append(("node-tar, strict", "tar 7.5.22", "extract",
                          lambda a, d, s=script: ["node", s, a, d, "strict"]))
        else:
            print("node runner:", err, file=sys.stderr)
    return found


def walk(top, dest=None):
    """The tree under top: {path: entry}, as in the manifests of the cases. Link targets in dest
    start with `DEST` instead, so that the results do not depend on where they were made."""
    tree = {}
    for dirpath, dirnames, filenames in os.walk(top):
        for name in dirnames + filenames:
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, top).replace(os.sep, "/")
            st = os.lstat(path)
            if stat.S_ISLNK(st.st_mode):
                target = os.readlink(path)
                if dest and (target == dest or target.startswith(dest + os.sep)):
                    target = "DEST" + target[len(dest):]
                tree[rel] = {"kind": "symlink", "target": target}
            elif stat.S_ISDIR(st.st_mode):
                tree[rel] = {"kind": "directory"}
            elif stat.S_ISREG(st.st_mode):
                with open(path, "rb") as f:
                    data = f.read()
                tree[rel] = {"kind": "file", "size": len(data),
                             "sha256": hashlib.sha256(data).hexdigest(),
                             "executable": bool(st.st_mode & stat.S_IXUSR)}
            else:
                tree[rel] = {"kind": "other"}
        dirnames[:] = [d for d in dirnames if not os.path.islink(os.path.join(dirpath, d))]
    return tree


def extract(command, archive, root):
    """Extract into root/x/y/dest; return (error, tree, outside), where outside is what was
    written in root but not under dest."""
    dest = os.path.join(root, "x", "y", "dest")
    os.makedirs(dest)
    code, out, err = run(command(archive, dest), cwd=dest)
    tree = walk(dest, dest)
    outside = {p: e for p, e in walk(root, dest).items()
               if p not in ("x", "x/y", "x/y/dest") and not p.startswith("x/y/dest/")}
    error = None
    if code != 0:
        error = (err.strip() or out.strip() or f"status {code}")
        error = error.replace(dest, "DEST").replace(root, "ROOT")[-300:]
    return error, tree, outside


def apply(members):
    """The tree that members make, applied in order to an empty tree: what a program that uses a
    library without an extractor would extract. Names keep a leading `/` and `..`."""
    tree, error = {}, None
    for m in members:
        if m["type"] == "g":
            continue  # a global pax header, which the library returns like a member
        absolute = m["name"].startswith("/")
        parts = [p for p in m["name"].split("/") if p not in ("", ".")]
        if not parts:
            continue
        path = ("/" if absolute else "") + "/".join(parts)
        for i in range(1, len(parts)):
            tree.setdefault(("/" if absolute else "") + "/".join(parts[:i]), {"kind": "directory"})
        t = m["type"]
        if t == "5":
            tree[path] = {"kind": "directory"}
        elif t == "2":
            tree[path] = {"kind": "symlink", "target": m.get("linkname", "")}
        elif t == "1":
            target = "/".join(p for p in m.get("linkname", "").split("/") if p not in ("", "."))
            if target in tree and target != path:
                tree[path] = dict(tree[target])
            elif target != path:
                error = error or f"hardlink to {target!r}, which is not there"
        elif t in ("0", "\0", "7"):
            tree[path] = {"kind": "file", "size": m["size"], "sha256": m.get("sha256", ""),
                          "executable": False}
        else:
            tree[path] = {"kind": "other"}
    return error, tree


def expected_tree(case):
    return {e["path"]: {k: v for k, v in e.items() if k != "path"} for e in case["tree"]}


def same(tree, manifest):
    """Whether a tree is the manifest's, comparing what the manifest says of each entry."""
    if set(tree) != set(manifest):
        return False
    for path, e in manifest.items():
        got = tree[path]
        if any(got.get(k) != v for k, v in e.items()):
            return False
    return True


def text(name):
    """A name as it can be shown in a table: other bytes than UTF-8, control characters and `|`
    escaped."""
    name = name.encode("utf-8", "surrogateescape").decode("utf-8", "backslashreplace")
    name = "".join(c if c.isprintable() else f"\\x{ord(c):02x}" for c in name)
    return name.replace("|", "\\|")


def describe(tree):
    """A tree as a short text, to tell trees apart in the table."""
    parts = []
    for path in sorted(tree):
        e = tree[path]
        path = text(path)
        if e["kind"] == "directory":
            parts.append(f"`{path}/`")
        elif e["kind"] == "symlink":
            parts.append(f"`{path}` → `{text(e['target'])}`")
        elif e["kind"] == "file":
            parts.append(f"`{path}` ({e['size']} B, {e['sha256'][:8]})")
        else:
            parts.append(f"`{path}` ({e['kind']})")
    return ", ".join(parts) or "nothing"


def policies():
    """The policies of scanner/strict.py, from what tarscan.py reports of each case."""
    sys.path.insert(0, os.path.join(HERE, "..", "scanner"))
    import strict
    import tarscan

    out = {}
    for name in sorted(os.listdir(ARCHIVES)):
        if name.endswith(".tar"):
            with open(os.path.join(ARCHIVES, name), "rb") as f:
                r = tarscan.scan(io.BytesIO(f.read()))
            out[name[:-4]] = {"every criterion": bool(strict.strict_features(r)),
                              "default policy": bool(strict.default_rejects(r))}
    return out


def load_cases():
    cases = {}
    for name in sorted(os.listdir(ARCHIVES)):
        if name.endswith(".json"):
            with open(os.path.join(ARCHIVES, name)) as f:
                cases[name[:-5]] = json.load(f)
    return cases


def main():
    if sys.argv[1] == "--readme":
        with open(os.path.join(HERE, "matrix.json")) as f:
            results = json.load(f)
        cases = load_cases()
        readme(sys.argv[2], results, cases)
        with open(os.path.join(HERE, "MATRIX.md"), "w") as f:
            f.write(table(results, cases))
        return
    work = os.path.abspath(sys.argv[1])
    cases = load_cases()
    impls = implementations(work)
    results = {"implementations": [{"name": n, "version": v, "kind": k} for n, v, k, _ in impls],
               "cases": {}}
    rejected_by = policies()
    runs = os.path.join(work, "runs")
    shutil.rmtree(runs, ignore_errors=True)
    for case, info in cases.items():
        archive = os.path.join(ARCHIVES, case + ".tar")
        row = {}
        for p, rejects in rejected_by[case].items():
            row[f"strict.py: {p}"] = {"error": "rejected" if rejects else None, "tree": None,
                                      "outside": {}}
        for i, (name, version, kind, command) in enumerate(impls):
            if kind == "extract":
                error, tree, outside = extract(command, archive, os.path.join(runs, str(i), case))
            else:
                code, out, err = run(command(archive))
                try:
                    listing = json.loads(out)
                    error, tree = apply(listing["members"])
                    error = listing.get("error") or error
                except ValueError:
                    error, tree = (err.strip() or f"status {code}")[-300:], {}
                outside = {}
            row[name] = {"error": error, "tree": tree, "outside": outside}
        results["cases"][case] = row
        print(case, file=sys.stderr)
    with open(os.path.join(HERE, "matrix.json"), "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)
        f.write("\n")
    with open(os.path.join(HERE, "MATRIX.md"), "w") as f:
        f.write(table(results, cases))


def outcome(case, r):
    """(symbol, tree or None) of one run."""
    if r["outside"]:
        return "💥", None
    if case["verdict"] == "n":
        return ("✅", None) if r["error"] else ("⚠️", r["tree"])
    if r["error"]:
        return ("⛔", None) if case["verdict"] == "i" else ("❌", None)
    if r["tree"] is None or same(r["tree"], expected_tree(case)):
        return "✅", None
    return "❌", r["tree"]


ORDER = ["✅", "⚠️", "⛔", "❌", "💥"]
LEGEND = [
    "- ✅ as the verdict says: rejects an `n_` case; extracts the manifest of a `y_` or `i_` case",
    "- ⚠️ accepts an `n_` case: the letter tells the trees apart",
    "- ⛔ rejects an `i_` case, which a strict parser may",
    "- ❌ rejects a `y_` case, or extracts another tree than the manifest of a `y_` or `i_` case",
    "- 💥 writes outside the destination",
]
# The cases in the summary of the README, with a short label
KEY = [
    ("n_pax_size_on_dir", "pax size on a dir"),
    ("n_pax_size_disagrees", "pax size disagrees"),
    ("n_end_zero_block_then_member", "member after a zero block"),
    ("n_end_archive_after", "archive after the end"),
    ("n_kind_trailing_slash_file", "file named `a/`"),
    ("n_tree_duplicate_file_differs", "a file twice"),
    ("n_name_dotdot", "`..` in a name"),
    ("n_tree_through_symlink", "through a symlink"),
    ("i_symlink_absolute", "absolute symlink"),
]


def columns(results):
    return ["strict.py: every criterion", "strict.py: default policy"] + [
        i["name"] for i in results["implementations"]]


def case_cells(info, row, names):
    """The cell of every implementation for one case, and the trees its letters stand for."""
    letters, cells = {}, {}
    for n in names:
        symbol, tree = outcome(info, row[n])
        cells[n] = symbol
        if tree is not None:
            key = describe(tree)
            letters.setdefault(key, chr(ord("A") + len(letters)))
            cells[n] = symbol + letters[key]
    return cells, letters


def totals(results, cases, names):
    counts = {n: {} for n in names}
    for case, info in cases.items():
        for n in names:
            symbol = outcome(info, results["cases"][case][n])[0]
            counts[n][symbol] = counts[n].get(symbol, 0) + 1
    return {n: " ".join(f"{s}{counts[n][s]}" for s in ORDER if counts[n].get(s)) for n in names}


def readme(path, results, cases):
    """The summary in the README: every implementation, on the cases of KEY and in total."""
    names = columns(results)
    cells = {case: case_cells(cases[case], results["cases"][case], names)[0] for case, _ in KEY}
    total = totals(results, cases, names)
    lines = [
        f"Every case of the corpus, {len(cases)} of them, extracted by every implementation: here a "
        "few that show how they differ, and the totals. "
        "[corpus/MATRIX.md](corpus/MATRIX.md) has every case, the versions, and which tree each "
        "letter is.",
        "",
        "| implementation | " + " | ".join(label for _, label in KEY) + " | all cases |",
        "|---|" + "---|" * (len(KEY) + 1),
    ]
    for n in names:
        lines.append(f"| {n} | " + " | ".join(cells[c][n] for c, _ in KEY) + f" | {total[n]} |")
    lines += [""] + LEGEND + ["", "Generated by `corpus/matrix.py` from `corpus/matrix.json`."]
    block = "\n".join(lines)
    text = open(path).read()
    begin, end = "<!-- begin matrix.py -->", "<!-- end matrix.py -->"
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    with open(path, "w") as f:
        f.write(f"{head}{begin}\n{block}\n{end}{tail}")


def table(results, cases):
    names = columns(results)
    lines = [
        "# What implementations make of the corpus",
        "",
        "Generated by `corpus/matrix.py` from `matrix.json`: every case of [archives/](archives),",
        "extracted by every implementation, or for libraries without an extractor listed and applied",
        "in order. The two policies of `scanner/strict.py` are from what `tarscan.py` reports.",
        "",
    ] + LEGEND + [
        "",
        "| implementation | version | how |",
        "|---|---|---|",
    ]
    for i in results["implementations"]:
        how = "extracts" if i["kind"] == "extract" else "lists, applied in order"
        lines.append(f"| {i['name']} | {i['version']} | {how} |")
    lines.append("")
    header = "| case | " + " | ".join(names) + " |"
    lines += [header, "|---|" + "---|" * len(names)]
    notes = []
    for case, info in cases.items():
        cells, letters = case_cells(info, results["cases"][case], names)
        lines.append(f"| `{case}` | " + " | ".join(cells[n] for n in names) + " |")
        if letters:
            notes.append(f"- `{case}`: " + "; ".join(f"{l}: {k}" for k, l in letters.items()))
    total = totals(results, cases, names)
    lines.append("| **total** | " + " | ".join(total[n] for n in names) + " |")
    lines += ["", "## Trees", "", "What the implementations that accept a case extract, where it is"
              " not its manifest: files by their size and the start of their sha256.", ""]
    lines += notes
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
