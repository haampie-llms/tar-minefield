"""Summarize the output of run.py as Markdown.

python -I scanner/report.py OUT [TITLE] > REPORT.md
"""

import collections
import json
import re
import sys
import time


def origin(url):
    host = url.split("/")[2]
    if host in ("github.com", "codeload.github.com"):
        return "github-release" if "/releases/download/" in url else "github-archive"
    if host in ("gitlab.com",) or "gitlab" in host:
        return "gitlab"
    if host in ("files.pythonhosted.org", "pypi.io", "pypi.org"):
        return "pypi"
    if "cran" in host or "r-project.org" in host or "bioconductor" in host:
        return "cran/bioconductor"
    if "cpan" in host:
        return "cpan"
    if "gnu.org" in host:
        return "gnu"
    return "other"


def producer(r):
    fp = r.get("fingerprint", {})
    if fp.get("producer_hint", {}).get("git-archive"):
        return "git archive"
    pax = fp.get("pax_header_name", {})
    if any("PaxHeaders" in k for k in pax):
        return "GNU tar (pax)"
    if any("PaxHeader/" in k for k in pax):
        return "libarchive (pax)"
    if any("@PaxHeader" in k for k in pax):
        return "Python tarfile (pax)"
    magic = fp.get("magic", {})
    top = max(magic, key=magic.get) if magic else "none"
    return {"gnu": "GNU format", "posix": "ustar", "v7": "v7"}.get(top, top)


def year(r):
    m = r.get("mtime")
    if not m:
        return None
    try:
        return time.gmtime(m[1]).tm_year
    except (OverflowError, OSError, ValueError):
        return None


def untar_reason(error):
    error = re.sub(r"'[^']*'|\"[^\"]*\"", "'…'", error)
    error = re.sub(
        r"(symlink|path|contains|through|Archive contains) \S+(?= (twice|without|which|named|more))",
        r"\1 …",
        error,
    )
    error = re.sub(r"unsafe path .*", "unsafe path …", error)
    error = re.sub(r"\d+", "N", error)
    return error


def filesystem_only(r):
    """Whether untar failed only because the scanning machine's filesystem cannot hold the tree:
    names that collide there, and no duplicates in the archive itself."""
    features = r.get("features", {})
    collides = any(
        f in features for f in ("platform.case-collision", "platform.normalization-collision")
    )
    duplicates = any(f.startswith("tree.duplicate.") for f in features)
    error = r.get("untar_error") or ""
    return (
        collides
        and not duplicates
        and (error.startswith("FileExistsError") or "which is not a directory" in error)
    )


def counter(c, n=4):
    return ", ".join(f"{k} {v}" for k, v in c.most_common(n))


def main():
    rows = [json.loads(line) for line in open(sys.argv[1])]
    scanned = [r for r in rows if "features" in r]
    failed = [r for r in rows if "download_error" in r]
    crashed = [r for r in rows if "scan_crash" in r]
    latest = sum(1 for r in scanned if r.get("latest"))

    title = sys.argv[2] if len(sys.argv) > 2 else "Scan of tarballs"
    print(f"# {title}\n")
    print(
        f"- sampled: {len(rows)}, scanned: {len(scanned)} ({latest} latest versions, "
        f"{len(scanned) - latest} older)"
    )
    print(f"- not downloaded: {len(failed)}, scanner crashed: {len(crashed)}")
    first = sum(r.get("source") in ("mirror", (r.get("urls") or [None])[0]) for r in scanned)
    print(f"- downloaded from the first of their URLs (a mirror): {first}")
    print(f"- origins: {counter(collections.Counter(origin(r['url']) for r in scanned), 10)}")
    print(f"- producers: {counter(collections.Counter(producer(r) for r in scanned), 10)}")
    print(
        f"- compression: {counter(collections.Counter(r['compression']['format'] for r in scanned))}"
    )
    for r in scanned:
        if r.get("compression_error"):
            print(
                f"- compression error in {r['package']}@{r['version']}: {r['compression_error']}"
            )
    errors = [r for r in scanned if r.get("error")]
    print(f"- scanner stopped early: {len(errors)}")
    for r in errors:
        print(f"  - {r['package']}@{r['version']}: {r['error']}")

    if any("untar_error" in r for r in scanned):
        skipped = [r for r in scanned if r.get("untar_skipped")]
        for r in skipped:
            print(f"- untar skipped {r['package']}@{r['version']}: {r['untar_skipped'][:200]}")
        local = [r for r in scanned if r.get("untar_error") and filesystem_only(r)]
        if local:
            print(
                f"\nFailed only because of the case-insensitive filesystem of the scanning "
                f"machine, not counted as rejections: {len(local)}, "
                f"{sum(r.get('latest', False) for r in local)} latest "
                f"({'; '.join(r['package'] + '@' + r['version'] for r in local[:6])})."
            )
        rejected = [r for r in scanned if r.get("untar_error") and not filesystem_only(r)]
        rl = sum(1 for r in rejected if r.get("latest"))
        print(
            f"\n## untar\n\nRejects {len(rejected)} of {len(scanned)} "
            f"({100 * len(rejected) / len(scanned):.1f}%); "
            f"{rl} of {latest} latest versions ({100 * rl / max(latest, 1):.1f}%).\n"
        )
        print("| reason | tarballs | latest | origins | producers | examples |")
        print("|---|---|---|---|---|---|")
        by_reason = collections.defaultdict(list)
        for r in rejected:
            by_reason[untar_reason(r["untar_error"])].append(r)
        for reason, rs in sorted(by_reason.items(), key=lambda kv: -len(kv[1])):
            examples = "; ".join(f"{r['package']}@{r['version']}" for r in rs[:3])
            print(
                f"| {reason.replace('|', '/')} | {len(rs)} | {sum(r.get('latest', False) for r in rs)} | "
                f"{counter(collections.Counter(origin(r['url']) for r in rs), 3)} | "
                f"{counter(collections.Counter(producer(r) for r in rs), 3)} | {examples} |"
            )

    print("\n## Features\n")
    print(
        "Number of tarballs with each feature, of which latest versions; their origins, "
        "producers and median mtime years, and what untar did with them.\n"
    )
    print(
        "| feature | tarballs | latest | origins | producers | years | untar rejects | examples |"
    )
    print("|---|---|---|---|---|---|---|---|")
    by_feature = collections.defaultdict(list)
    for r in scanned:
        for f in r["features"]:
            by_feature[f].append(r)
    for f, rs in sorted(by_feature.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        years = sorted(y for y in map(year, rs) if y)
        span = f"{years[0]}–{years[-1]}" if years else ""
        examples = "; ".join(
            f"{r['package']}@{r['version']} `{(r['examples'].get(f) or [''])[0][:60]}`"
            for r in rs[:2]
        ).replace("|", "/")
        print(
            f"| `{f}` | {len(rs)} | {sum(r.get('latest', False) for r in rs)} | "
            f"{counter(collections.Counter(origin(r['url']) for r in rs), 3)} | "
            f"{counter(collections.Counter(producer(r) for r in rs), 3)} | {span} | "
            f"{sum(1 for r in rs if r.get('untar_error'))} | {examples} |"
        )

    print("\n## Fingerprints\n")
    for key in (
        "magic",
        "size",
        "mode",
        "checksum",
        "pax_header_name",
        "extended_sequence",
        "gnu_long_name",
        "end",
        "zero_blocks_after_end",
        "pax_keys",
        "pax_global_keys",
    ):
        c = collections.Counter()
        for r in scanned:
            for k in r.get("fingerprint", {}).get(key, {}):
                if key == "pax_header_name":
                    k = re.sub(r"[0-9a-fN]{16,}", "H", k)
                c[k] += 1
        print(f"- {key} (tarballs using each): {counter(c, 12)}")
    c = collections.Counter()
    for r in scanned:
        info = r["compression"]
        if info.get("streams", 0) > 1:
            c["several streams"] += 1
        if info.get("trailing_bytes"):
            c["trailing nonzero" if info.get("trailing_nonzero") else "trailing zeros"] += 1
        if info.get("truncated"):
            c["truncated"] += 1
    print(f"- compression layer: {counter(c)}")


if __name__ == "__main__":
    main()
