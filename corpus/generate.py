"""Write the archives of the corpus from the scripts in cases/, and check them.

    python -I corpus/generate.py            # write archives/
    python -I corpus/generate.py --check    # fail if archives/ is not what the scripts write
    python -I corpus/generate.py --scan     # also check what scanner/tarscan.py makes of them

For each case `<case>.py`, archives/ has `<case>.tar`, the dump of its blocks `<case>.txt`, a
map of them `<case>.svg`, and `<case>.json`: its verdict, the features of tarscan.py that it is about, and for the cases that a
parser accepts, `y_` and `i_`, the tree it must extract.

--scan checks that tarscan.py reports the features of every case, and that the default policy
of scanner/strict.py rejects the `n_` cases, accepts the `i_` cases only by its rules, and
accepts the `y_` cases without them. That tests the scanner and the policy against cases defined
by their bytes, which a reviewer checks by reading the scripts and dumps.
"""

import hashlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blocks import Archive, block_map  # noqa: E402

CASES = os.path.join(HERE, "cases")
ARCHIVES = os.path.join(HERE, "archives")
VERDICTS = {"n": "rejected", "y": "accepted", "i": "accepted by the default policy"}
# The letter of a code is the level of the catalogue: of METHOD.md, and LEVELS of strict.py
LETTERS = {"F": "framing", "N": "name", "K": "kind", "S": "order and state",
           "G": "global pax headers"}


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tree(entries):
    """The tree of a case as data: contents as their size and sha256."""
    out = []
    for e in entries:
        e = dict(e)
        if "contents" in e:
            contents = e.pop("contents")
            e["size"] = len(contents)
            e["sha256"] = hashlib.sha256(contents).hexdigest()
        out.append(e)
    return out


def generate():
    """{file name: bytes} of every case."""
    files, codes = {}, {}
    for name in sorted(os.listdir(CASES)):
        if not name.endswith(".py"):
            continue
        case = name[:-3]
        module = load(os.path.join(CASES, name))
        assert case.startswith(module.VERDICT + "_"), f"{case}: the name starts with its verdict"
        assert re.fullmatch(r"[FNKSG]\d\d", module.CODE), f"{case}: a code such as F01"
        assert module.CODE not in codes, f"{case}: the code of {codes.get(module.CODE)}"
        codes[module.CODE] = case
        archive = Archive()
        module.build(archive)
        expected = {
            "code": module.CODE,
            "verdict": module.VERDICT,
            "description": module.__doc__.strip().split("\n")[0],
            "features": getattr(module, "FEATURES", []),
        }
        if module.VERDICT in ("y", "i"):
            expected["tree"] = tree(module.TREE)
        header = f"{module.CODE} {case}: {VERDICTS[module.VERDICT]}\n\n{module.__doc__.strip()}\n\n"
        files[f"{case}.tar"] = archive.bytes()
        files[f"{case}.txt"] = (header + archive.dump()).encode()
        files[f"{case}.svg"] = block_map(
            archive, f"{module.CODE} {case}: every block of the archive").encode()
        files[f"{case}.json"] = (json.dumps(expected, indent=1) + "\n").encode()
    return files


def scan(files):
    """Problems with what tarscan.py and the default policy make of the cases."""
    sys.path.insert(0, os.path.join(HERE, "..", "scanner"))
    import strict
    import tarscan

    problems = []
    for name, data in files.items():
        if not name.endswith(".tar"):
            continue
        case = name[:-4]
        expected = json.loads(files[f"{case}.json"])
        r = tarscan.scan(io.BytesIO(data))
        found = set(r["features"])
        missing = set(expected["features"]) - found
        if missing:
            problems.append(f"{case}: tarscan.py does not report {sorted(missing)}")
        strict_found, rejected = strict.strict_features(r), strict.default_rejects(r)
        verdict = expected["verdict"]
        if verdict == "n" and not rejected:
            problems.append(f"{case}: the default policy accepts it ({sorted(found)})")
        if verdict == "i" and (rejected or not strict_found):
            problems.append(f"{case}: not accepted by a rule of the default policy: rejects "
                            f"{sorted(rejected)}, strict {sorted(strict_found)}")
        if verdict == "y" and strict_found:
            problems.append(f"{case}: a strict criterion rejects it: {sorted(strict_found)}")
        levels = {strict.classify(f)[1] for f in expected["features"]} - {None} or {"framing"}
        if verdict != "y" and LETTERS[expected["code"][0]] not in levels:
            problems.append(f"{case}: the code {expected['code']} is not of the level {levels}")
        print(f"{case}: {sorted(found)}")
    return problems


def main():
    args = sys.argv[1:]
    files = generate()
    if "--check" in args:
        on_disk = set(os.listdir(ARCHIVES)) if os.path.isdir(ARCHIVES) else set()
        differ = [n for n in sorted(files) if n not in on_disk
                  or open(os.path.join(ARCHIVES, n), "rb").read() != files[n]]
        extra = sorted(on_disk - set(files))
        for n in differ:
            print(f"archives/{n}: not what the scripts write")
        for n in extra:
            print(f"archives/{n}: no script writes it")
        if differ or extra:
            sys.exit(1)
    else:
        os.makedirs(ARCHIVES, exist_ok=True)
        for n, data in files.items():
            with open(os.path.join(ARCHIVES, n), "wb") as f:
                f.write(data)
    if "--scan" in args:
        problems = scan(files)
        for p in problems:
            print(p)
        if problems:
            sys.exit(1)


if __name__ == "__main__":
    main()
