"""List the tarballs of live-bootstrap, as JSON lines.

Run with `python -I scanner/live_bootstrap_list.py path/to/live-bootstrap > list.jsonl`. Each
`steps/<step>/sources` has lines `f <url> <sha256> [<name>]` for files, and
`g <repo>~<ref> <url> <sha256> [<name>]` for tarballs of a git reference, where the URL is `_` if
the tarball is made with `git archive` and has no upstream. live-bootstrap's mirrors serve every
file by its name, so they come first in `urls`, and the upstream URL last.

Every tarball is listed once, with the steps that use it. A package is the name of the tarball up
to its version, and its latest version is the one that the last step in `steps/manifest` builds:
the version that the bootstrapped system ends up with.
"""

import json
import os
import re
import sys

MIRRORS = ("https://live-bootstrap.stikonas.eu", "https://samuelt.me/pub/live-bootstrap")
TAR_EXTENSIONS = ("tar", "tar.gz", "tgz", "tar.bz2", "tbz2", "tar.xz", "txz", "tar.lzma")


def sources(root, step):
    path = os.path.join(root, "steps", step, "sources")
    if not os.path.exists(path):
        return
    for line in open(path, encoding="utf-8"):
        fields = line.split()
        if not fields:
            continue
        if fields[0] in ("g", "git"):
            kind, repo, url, sha256, *name = fields
        else:
            kind, url, sha256, *name = fields
            repo = None
        name = name[0] if name else os.path.basename(url)
        yield {"kind": kind, "repo": repo, "url": url, "sha256": sha256, "name": name}


VERSION = r"(v?\d.*|[0-9a-f]{6,40})"


def package_version(s, step):
    """The package and version of a tarball, from its name, or if it is named by its version only
    (`v2.0.22.tar.gz`, a commit), from its repository or the name of its step."""
    for ext in TAR_EXTENSIONS:
        if s["name"].endswith("." + ext):
            stem = s["name"][: -len(ext) - 1]
            if re.match(rf"^{VERSION}$", stem):
                m = re.match(r"^https://github\.com/[^/]+/([^/]+)/archive/", s["url"])
                if s["repo"]:
                    package = re.sub(r"\.git$", "", os.path.basename(s["repo"].split("~")[0]))
                elif m:
                    package = m.group(1)
                else:
                    package = re.match(r"^(.+?)(-[\d.]+.*)?$", step).group(1)
                return package, stem
            m = re.match(rf"^(.+?)-{VERSION}$", stem) or re.match(rf"^([a-z]+){VERSION}$", stem)
            return (m.group(1), m.group(2)) if m else (stem, "")
    return None


def main():
    root = sys.argv[1]
    manifest = []
    for line in open(os.path.join(root, "steps", "manifest"), encoding="utf-8"):
        if line.startswith("build: "):
            step = line.split()[1].split("#")[0].strip()
            if step not in manifest:
                manifest.append(step)
    others = sorted(
        s for s in os.listdir(os.path.join(root, "steps")) if s not in manifest
    )
    by_sha256 = {}
    for step in manifest + others:
        for s in sources(root, step):
            pv = package_version(s, step)
            if pv is None:
                continue
            if s["sha256"] in by_sha256:
                by_sha256[s["sha256"]]["steps"].append(step)
                continue
            urls = [f"{m}/{s['name']}" for m in MIRRORS]
            if s["url"] != "_":
                urls.append(s["url"])
            by_sha256[s["sha256"]] = {
                "package": pv[0],
                "version": pv[1],
                "sha256": s["sha256"],
                "url": s["url"] if s["url"] != "_" else s["repo"],
                "urls": urls,
                "name": s["name"],
                "git_archive": s["url"] == "_",
                "steps": [step],
                "in_manifest": step in manifest,
            }
    tarballs = list(by_sha256.values())
    # The last tarball of each package that a step in the manifest uses
    latest = {}
    for t in tarballs:
        if t["in_manifest"]:
            latest[t["package"]] = t
    for t in tarballs:
        t["latest"] = latest.get(t["package"]) is t
        print(json.dumps(t))


if __name__ == "__main__":
    main()
