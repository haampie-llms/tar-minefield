"""List the tarballs of all versions in Spack's builtin repository, as JSON lines.

Run with `spack python scanner/spack_list.py > spack.jsonl`. Every line has the package, the
version, its sha256, its URL, the URLs to download it from (Spack's source mirror first), and
whether it is the latest version of the package with a checksum.
"""

import json
import sys

import spack.fetch_strategy
import spack.mirrors.layout
import spack.package_base
import spack.repo
import spack.spec

MIRROR = "https://mirror.spack.io/_source-cache/archive"
TAR_EXTENSIONS = ("tar", "tar.gz", "tgz", "tar.bz2", "tbz2", "tbz", "tar.xz", "txz")


def tarballs(pkg_cls):
    if getattr(pkg_cls, "manual_download", False):
        return []
    pkg = pkg_cls(spack.spec.Spec(pkg_cls.name))
    found = []
    for version, meta in pkg_cls.versions.items():
        if "sha256" not in meta or not meta.get("expand", True):
            continue
        fetcher = spack.package_base.for_package_version(pkg, version)
        if type(fetcher) is not spack.fetch_strategy.URLFetchStrategy or not fetcher.digest:
            continue
        ext = meta.get("extension") or spack.mirrors.layout._determine_extension(fetcher)
        if ext not in TAR_EXTENSIONS or not fetcher.url.startswith(("https://", "http://")):
            continue
        found.append(
            {
                "package": pkg_cls.name,
                "version": str(version),
                "sha256": fetcher.digest,
                "url": fetcher.url,
                "urls": [f"{MIRROR}/{fetcher.digest[:2]}/{fetcher.digest}.{ext}", fetcher.url],
                "deprecated": bool(meta.get("deprecated")),
            }
        )
    current = [t for t in found if not t["deprecated"]] or found
    if current:
        latest = max(current, key=lambda t: spack.version.Version(t["version"]))
        for t in found:
            t["latest"] = t is latest
    return found


def main():
    for pkg_cls in spack.repo.PATH.all_package_classes():
        try:
            for t in tarballs(pkg_cls):
                print(json.dumps(t))
        except Exception as e:
            print(f"{pkg_cls.name}: {type(e).__name__}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
