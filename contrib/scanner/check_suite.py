"""Check the scanner and the default policy against the test suite.

    python -I contrib/scanner/check_suite.py

Every case must make tarscan.py report its features. The default policy of strict.py must reject
the cases to reject, accept the tolerated cases only by its rules, and accept the cases to accept
without them. And the letter of the identifier of a case must be the level of its features. That tests
the scanner and the policy against cases defined by their bytes, which a reviewer checks by
reading the scripts and dumps of suite/.
"""

import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import strict  # noqa: E402
import tarscan  # noqa: E402

ARCHIVES = os.path.join(HERE, "..", "..", "suite", "archives")


def check():
    """Problems with what tarscan.py and the default policy make of the cases."""
    problems = []
    for name in sorted(os.listdir(ARCHIVES)):
        if not name.endswith(".tar"):
            continue
        case = name[:-4]
        with open(os.path.join(ARCHIVES, f"{case}.json")) as f:
            expected = json.load(f)
        with open(os.path.join(ARCHIVES, name), "rb") as f:
            r = tarscan.scan(io.BytesIO(f.read()))
        found = set(r["features"])
        missing = set(expected["features"]) - found
        if missing:
            problems.append(f"{case}: tarscan.py does not report {sorted(missing)}")
        strict_found, rejected = strict.strict_features(r), strict.default_rejects(r)
        verdict = expected["verdict"]
        if verdict == "reject" and not rejected:
            problems.append(f"{case}: the default policy accepts it ({sorted(found)})")
        if verdict == "tolerate" and (rejected or not strict_found):
            problems.append(f"{case}: not accepted by a rule of the default policy: rejects "
                            f"{sorted(rejected)}, strict {sorted(strict_found)}")
        if verdict == "accept" and strict_found:
            problems.append(f"{case}: a strict criterion rejects it: {sorted(strict_found)}")
        levels = {strict.classify(f)[1] for f in expected["features"]} - {None} or {"framing"}
        level = strict.LEVELS["FNKSG".index(expected["id"][0])]
        if verdict != "accept" and level not in levels:
            problems.append(f"{case}: the identifier {expected['id']} is not of the level {levels}")
        print(f"{case}: {sorted(found)}")
    return problems


def main():
    problems = check()
    for p in problems:
        print(p)
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
