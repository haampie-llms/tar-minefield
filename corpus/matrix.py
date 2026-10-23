"""Run every case of the corpus with every implementation, and tabulate what they make of it.

    python -I corpus/matrix.py WORK
    python -I corpus/matrix.py --readme README.md

Programs are found on PATH, or in an environment variable of their name in capitals, such as
$JULIA or $BSDTAR. WORK is a directory for builds and extractions: runners are built there, and every case is
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


def tool(name):
    """A program from the environment variable of its name in capitals, or from PATH."""
    return os.environ.get(name.upper()) or shutil.which(name)


def fetch_jars(listing, into):
    """The jars that listing names, from Maven Central into a directory, checked by their sha1."""
    import urllib.request

    os.makedirs(into, exist_ok=True)
    for line in open(listing):
        if line.strip() and not line.startswith("#"):
            path, sha1 = line.split()
            target = os.path.join(into, os.path.basename(path))
            if not os.path.exists(target):
                with urllib.request.urlopen(f"https://repo1.maven.org/maven2/{path}") as r:
                    data = r.read()
                if hashlib.sha1(data).hexdigest() != sha1:
                    raise ValueError(f"{path}: sha1 mismatch")
                with open(target, "wb") as f:
                    f.write(data)


def build_mescc_untar(build):
    """The untar of mescc-tools-extra, compiled from the commits of its source.txt, or None."""
    binary = os.path.join(build, "untar")
    if os.path.exists(binary):
        return binary
    sources = {}
    for line in open(os.path.join(RUNNERS, "mescc-tools-extra", "source.txt")):
        if line.strip() and not line.startswith("#"):
            name, url, commit = line.split()
            sources[name] = (url, commit)
    src = os.path.join(build, "src")
    for name, (url, commit) in sources.items():
        path = src if name == "mescc-tools-extra" else os.path.join(src, name)
        shutil.rmtree(path, ignore_errors=True)
        for cmd in (["git", "clone", "-q", "--filter=blob:none", "--no-checkout", url, path],
                    ["git", "-C", path, "checkout", "-q", commit]):
            code, _, err = run(cmd)
            if code != 0:
                print("mescc-tools-extra:", err, file=sys.stderr)
                return None
    # C99: M2libc names a variable bool, which C23 makes a keyword
    code, _, err = run([tool("cc"), "-std=gnu99", "-Wno-implicit-function-declaration", "untar.c",
                        "M2libc/bootstrappable.c", "-o", binary], cwd=src)
    if code != 0:
        print("mescc-tools-extra:", err, file=sys.stderr)
        return None
    return binary


def implementations(work):
    """(name, version, kind, command) for every implementation found: kind is "extract", with a
    command of the archive and the destination, or "list", with a command of the archive."""
    found = []
    if shutil.which("tar"):
        found.append(("GNU tar", first_line(["tar", "--version"]), "extract",
                      lambda a, d: ["tar", "-xf", a, "-C", d]))
    bsdtar = tool("bsdtar")
    if bsdtar:
        found.append(("bsdtar", first_line([bsdtar, "--version"]).split(" zlib")[0], "extract",
                      lambda a, d, b=bsdtar: [b, "-xf", a, "-C", d]))
    if shutil.which("git") and tool("cc"):
        binary = build_mescc_untar(os.path.join(work, "build", "mescc-tools-extra"))
        if binary:
            commit = open(os.path.join(RUNNERS, "mescc-tools-extra", "source.txt")).read().split(
                "mescc-tools-extra https://github.com/oriansj/mescc-tools-extra ")[1][:12]
            version = f"mescc-tools-extra {commit}, built with cc"
            found.append(("live-bootstrap untar", version, "extract",
                          lambda a, d, b=binary: [b, "--file", a]))
            found.append(("live-bootstrap untar, --non-strict", version, "extract",
                          lambda a, d, b=binary: [b, "--non-strict", "--file", a]))
    if shutil.which("busybox"):
        found.append(("BusyBox tar", first_line(["busybox"]).split(" multi-call")[0], "extract",
                      lambda a, d: ["busybox", "tar", "-xf", a, "-C", d]))
    if shutil.which("7z"):
        code, out, _ = run(["7z"])
        version = next((l for l in out.splitlines() if l.startswith("7-Zip")), "7-Zip").split(" :")[0]
        found.append(("7-Zip", version, "extract", lambda a, d: ["7z", "x", "-y", "-bd", f"-o{d}", a]))
    python = sys.executable
    pyversion = f"CPython {sys.version.split()[0]}"
    for f in ("fully_trusted", "tar", "data"):
        found.append((f"Python tarfile, filter={f}", pyversion, "extract",
                      lambda a, d, f=f: [python, "-I", "-c", TARFILE, a, d, f]))
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
    cabal = tool("cabal")
    if cabal:
        target = os.path.join(build, "haskell")
        code, out, err = run([cabal, "install", "--installdir", target, "--overwrite-policy=always",
                              "--install-method=copy", f"--builddir={target}/dist"],
                             cwd=os.path.join(RUNNERS, "haskell"))
        if code == 0:
            version = first_line([os.path.join(target, "runner"), "--version"])
            found.append(("Haskell tar", version, "extract",
                          lambda a, d, b=os.path.join(target, "runner"): [b, a, d]))
        else:
            print("haskell runner:", (err or out)[-2000:], file=sys.stderr)
    java = tool("java")
    if java:
        jars = os.path.join(build, "java")
        fetch_jars(os.path.join(RUNNERS, "java", "jars.txt"), jars)
        java_version = first_line([java, "-version"]).split('"')[1]
        found.append(("Java Commons Compress", f"Commons Compress 1.28.0, Expander, on Java {java_version}",
                      "extract", lambda a, d, j=java, c=os.path.join(jars, "*"):
                      [j, "-cp", c, os.path.join(RUNNERS, "java", "Extract.java"), a, d]))
    ruby = tool("ruby")
    if ruby:
        code, out, _ = run([ruby, "-e", 'require "rubygems"; print Gem::VERSION, " ", RUBY_VERSION'])
        version = "RubyGems {} of Ruby {}, extract_tar_gz".format(*out.split()) if code == 0 else "?"
        found.append(("RubyGems", version, "extract", lambda a, d, r=ruby:
                      [r, os.path.join(RUNNERS, "ruby", "extract.rb"), a, d]))
    perl = tool("perl")
    if perl:
        code, out, _ = run([perl, "-MArchive::Tar", "-e", 'print "$Archive::Tar::VERSION $^V"'])
        version = "Archive::Tar {} of Perl {}".format(*out.split()) if code == 0 else "?"
        found.append(("Perl Archive::Tar", version, "extract", lambda a, d, p=perl:
                      [p, os.path.join(RUNNERS, "perl", "extract.pl"), a, d]))
    julia = tool("julia")
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


GROUPS = {
    "y": "accepted by every parser",
    "i": "accepted by the default policy",
    "framing": "rejected: framing",
    "name": "rejected: names",
    "kind": "rejected: kinds",
    "order and state": "rejected: order and state",
    "global pax headers": "rejected: global pax headers",
}


def category(info):
    """The group of a case: its verdict, and for n_ cases the level of the catalogue that
    scanner/strict.py gives its features; a case without any is one the scanner cannot read
    past, which is framing."""
    if info["verdict"] != "n":
        return info["verdict"]
    sys.path.insert(0, os.path.join(HERE, "..", "scanner"))
    import strict

    levels = [strict.classify(f)[1] for f in info["features"] if strict.classify(f)[0] == "strict"]
    return levels[0] if levels else "framing"


def load_cases():
    """The cases, in the order of GROUPS, and by name in each group."""
    cases = {}
    for name in sorted(os.listdir(ARCHIVES)):
        if name.endswith(".json"):
            with open(os.path.join(ARCHIVES, name)) as f:
                cases[name[:-5]] = json.load(f)
    order = list(GROUPS)
    return dict(sorted(cases.items(), key=lambda kv: (order.index(category(kv[1])), kv[0])))


def main():
    if sys.argv[1] == "--readme":
        with open(os.path.join(HERE, "matrix.json")) as f:
            results = json.load(f)
        cases = load_cases()
        readme(sys.argv[2], results, cases)
        write_outputs(results, cases)
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
    write_outputs(results, cases)


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
    "- ⚠️ accepts an `n_` case. The letter is the tree it extracts: in one row, the same letter is"
    " the same tree, and different letters are trees that differ; [MATRIX.md](MATRIX.md#trees)"
    " lists them",
    "- ⛔ rejects an `i_` case, which a strict parser may",
    "- ❌ rejects a `y_` case, or extracts another tree than the manifest of a `y_` or `i_` case",
    "- 💥 writes outside the destination",
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


# SVG: the classes of outcomes; their colours in light and dark mode, as (cell, mark): pale cells,
# as a grid of saturated ones flickers at its crossings; what they mean; and a mark that tells
# them apart without colour
CLASSES = {
    "✅": ("ok", ("#b4f1c3", "#116329"), ("#1a4a2b", "#56d364"),
          "as the verdict says: rejects an n_ case, extracts the tree of the others", "✓"),
    "⚠️": ("warn", ("#ffe08a", "#7d4e00"), ("#5a4310", "#e3b341"),
           "accepts an n_ case, which a strict parser rejects", "!"),
    "⛔": ("stop", ("#d0d7de", "#424a53"), ("#3a424c", "#b1bac4"),
           "rejects an i_ case, which a strict parser may", "–"),
    "❌": ("bad", ("#ffc1ba", "#a40e26"), ("#5e1d26", "#ff7b72"),
           "rejects a y_ case, or extracts another tree than its manifest", "✗"),
    "💥": ("boom", ("#dcc8ff", "#6639ba"), ("#45307a", "#bc8cff"),
           "writes outside the destination", "↑"),
}
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def group(name):
    """The group of an implementation, which the SVG separates from the next by a gap: the
    policies, the command-line tools, and then the libraries of each language."""
    if name.startswith("strict.py"):
        return "policy"
    if name in ("GNU tar", "bsdtar", "BusyBox tar", "7-Zip") or name.startswith("live-bootstrap"):
        return "tool"
    return name.split()[0].replace("RubyGems", "Ruby").replace("node-tar,", "node-tar")


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_style():
    light = "".join(f".{c[0]}{{fill:{c[1][0]}}}.{c[0]}-ink{{fill:{c[1][1]}}}" for c in CLASSES.values())
    dark = "".join(f".{c[0]}{{fill:{c[2][0]}}}.{c[0]}-ink{{fill:{c[2][1]}}}" for c in CLASSES.values())
    return (
        f"<style>text{{font-family:{FONT};font-size:12px;fill:#1f2328}}.head{{font-weight:600}}"
        ".cell{font-size:11px;font-weight:700;text-anchor:middle}"
        f".rule{{stroke:#d0d7de}}{light}"
        "@media (prefers-color-scheme: dark){text{fill:#e6edf3}.rule{stroke:#30363d}"
        f"{dark}}}</style>"
    )


def cell_svg(x, y, w, h, symbol, title):
    """A cell, coloured and marked by its outcome. The letters of trees are left to MATRIX.md,
    which lists the trees: the hover title names the tree."""
    base = next(c for c in CLASSES if symbol.startswith(c))
    cls, mark = CLASSES[base][0], CLASSES[base][4]
    return (f'<g><title>{esc(title)}</title><rect class="{cls}" x="{x}" y="{y}" width="{w}" '
            f'height="{h}" rx="3"/><text class="cell {cls}-ink" x="{x + w / 2}" y="{y + h / 2 + 4}">{mark}'
            "</text></g>")


def legend_svg(x, y):
    out = []
    for c in CLASSES.values():
        out.append(f'<rect class="{c[0]}" x="{x}" y="{y - 12}" width="16" height="16" rx="3"/>'
                   f'<text class="cell {c[0]}-ink" x="{x + 8}" y="{y}">{c[4]}</text>'
                   f'<text x="{x + 22}" y="{y}">{esc(c[3])}</text>')
        y += 21
    return "".join(out), y


def svg(results, cases):
    """Every implementation in columns; in rows, the outcomes of all cases first, as a bar per
    implementation, then every case."""
    names = columns(results)
    counts = {n: {} for n in names}
    for case, info in cases.items():
        for n in names:
            symbol = outcome(info, results["cases"][case][n])[0]
            counts[n][symbol] = counts[n].get(symbol, 0) + 1
    left = 20 + 7 * max(len(c) for c in cases)
    cw, ch, gap, top = 22, 16, 2, 230
    xs, x, previous = {}, left, None
    for n in names:
        if previous is not None and group(n) != group(previous):
            x += 10
        xs[n], previous, x = x, n, x + cw + gap
    out, y = [], top
    for n in names:
        out.append(f'<text transform="translate({xs[n] + cw / 2 + 4},{top - 8}) rotate(-60)">{esc(n)}</text>')
    # the bars: outcomes stacked from the bottom, with the number of each where it fits
    bar = 2 * len(cases)
    out.append(f'<text x="{left - 10}" y="{y + bar / 2 + 4}" text-anchor="end">all {len(cases)} cases</text>')
    for n in names:
        bottom = y + bar
        for symbol in ORDER:
            k = counts[n].get(symbol, 0)
            if not k:
                continue
            h = bar * k / len(cases)
            out.append(f'<g><title>{esc(n)}: {k} of {len(cases)}, {esc(CLASSES[symbol][3])}</title>'
                       f'<rect class="{CLASSES[symbol][0]}" x="{xs[n]}" y="{bottom - h:.1f}" '
                       f'width="{cw}" height="{h:.1f}"/>')
            if h >= 14:
                out.append(f'<text class="cell {CLASSES[symbol][0]}-ink" x="{xs[n] + cw / 2}" '
                           f'y="{bottom - h / 2 + 4:.1f}">{k}</text>')
            out.append("</g>")
            bottom -= h
    y += bar
    previous = None
    for case, info in cases.items():
        if category(info) != previous:
            previous = category(info)
            out.append(f'<line class="rule" x1="10" x2="{x - gap}" y1="{y + 10}" y2="{y + 10}"/>'
                       f'<text class="head" x="10" y="{y + 26}">{esc(GROUPS[previous])}</text>')
            y += 34
        out.append(f'<text x="{left - 10}" y="{y + ch / 2 + 4}" text-anchor="end">{esc(case)}</text>')
        cells, letters = case_cells(info, results["cases"][case], names)
        trees = {v: k for k, v in letters.items()}
        for n in names:
            letter = cells[n].lstrip("✅⚠️⛔❌💥\ufe0f")
            title = f"{n}: {case}" + (f", tree {letter}: {trees[letter]}" if letter in trees else "")
            out.append(cell_svg(xs[n], y, cw, ch, cells[n], title.replace("`", "")))
        y += ch + gap
    legend, y = legend_svg(left, y + 24)
    out.append(legend)
    # the rotated name of the last column reaches past it, by the cosine of 60°
    width, height = int(x + 20 + 7 * len(names[-1]) / 2), y + 4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img"><title>What implementations make of every '
            f'case of the corpus</title>{svg_style()}{"".join(out)}</svg>\n')


def write_outputs(results, cases):
    """MATRIX.md and matrix.svg, from the results."""
    for name, data in (("MATRIX.md", table(results, cases)), ("matrix.svg", svg(results, cases))):
        with open(os.path.join(HERE, name), "w") as f:
            f.write(data)


def readme(path, results, cases):
    """The summary in the README: matrix.svg, with the outcomes of every implementation as text."""
    names = columns(results)
    total = totals(results, cases, names)
    lines = [
        f"Every case of the corpus, {len(cases)} of them, extracted by every implementation, and "
        "the outcomes of all cases at the top. [corpus/MATRIX.md](corpus/MATRIX.md) has the same as "
        "a table, with the versions and which tree each letter is.",
        "",
        "![What every implementation makes of every case of the corpus. Outcomes of all cases: "
        + "; ".join(f"{n}: {total[n]}" for n in names) + "](corpus/matrix.svg)",
        "",
        "Generated by `corpus/matrix.py` from `corpus/matrix.json`.",
    ]
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
        "![Every case of the corpus, in rows, and what every implementation makes of it, in columns:"
        " the table below as a picture](matrix.svg)",
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
    previous = None
    for case, info in cases.items():
        if category(info) != previous:
            previous = category(info)
            lines.append(f"| **{GROUPS[previous]}** |" + " |" * len(names))
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
