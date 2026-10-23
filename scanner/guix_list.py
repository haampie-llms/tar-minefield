"""List the tarballs of Guix, as JSON lines.

    curl -o sources.json https://guix.gnu.org/sources.json
    python -I scanner/guix_list.py sources.json > guix.jsonl

sources.json, which Guix publishes for Software Heritage (it may be compressed with gzip), lists
the sources of the current revision of Guix. Only those fetched by URL that are tarballs with a
sha256 are listed. Their URLs are the content-addressed mirrors of Guix first, which sources.json
lists among the others, then tarballs.nixos.org, then at most three of the upstream URLs:
some sources list dozens of SourceForge mirrors. A package is the name of the tarball up to its
version, and its latest version is the highest version of it in Guix.
"""

import base64
import gzip
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nix_list import TAR, TARBALLS, package_version, version_key  # noqa: E402

MIRRORS = ("https://bordeaux.guix.gnu.org/file/", "https://ci.guix.gnu.org/file/")
UPSTREAM = 3


def basename(url):
    return url.split("?")[0].rstrip("/").rsplit("/", 1)[-1]


def main():
    with open(sys.argv[1], "rb") as f:
        data = f.read()
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    tarballs = {}
    for source in json.loads(data)["sources"]:
        if source.get("type") != "url" or not source.get("integrity", "").startswith("sha256-"):
            continue
        upstream = [u for u in source["urls"] if not u.startswith(MIRRORS)]
        named = [basename(u) for u in upstream if TAR.search(basename(u))]
        if not named:
            continue
        sha256 = base64.b64decode(source["integrity"][7:]).hex()
        if sha256 in tarballs:
            continue
        mirrors = [u for u in source["urls"] if u.startswith(MIRRORS)]
        upstream = [u for u in upstream if u.startswith(("https://", "http://", "ftp://"))]
        package, version = package_version(named[0])
        tarballs[sha256] = {
            "package": package,
            "version": version,
            "sha256": sha256,
            "url": upstream[0] if upstream else mirrors[0],
            "urls": mirrors + [f"{TARBALLS}/{sha256}"] + upstream[:UPSTREAM],
            "name": named[0],
        }
    latest = {}
    for t in tarballs.values():
        best = latest.get(t["package"])
        if best is None or version_key(t["version"]) > version_key(best["version"]):
            latest[t["package"]] = t
    for sha256 in sorted(tarballs):
        t = tarballs[sha256]
        t["latest"] = latest[t["package"]] is t
        print(json.dumps(t))


if __name__ == "__main__":
    main()
