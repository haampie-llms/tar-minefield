"""How many real tarballs a strict parser would accept, as Markdown.

    python -I scanner/strict.py RESULTS... > STRICT.md
    python -I scanner/strict.py --readme README.md RESULTS...

A strict parser rejects every archive with a feature that METHOD.md lists as an ambiguity: the
criteria below, each a pattern of feature names of tarscan.py. Features that METHOD.md lists as
`y_`, or that are confined to fields outside the tree it describes, are allowed. Names that some
filesystems cannot hold (`platform.*`) are neither: they are reported apart. A feature that none
of these patterns match is reported as unclassified, so that nothing is left out unseen.

Each results file is a dataset, and rates are given per dataset: each is a sample of its own
population. Tarballs in a compression that tarscan.py does not read are not assessed.

With --readme, the summary between the markers `<!-- begin strict.py -->` and
`<!-- end strict.py -->` in that file is generated again, and nothing else is printed: so that
no number in it is written by hand.
"""

import collections
import fnmatch
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from report import load, origin  # noqa: E402

LEVELS = ("framing", "name", "kind", "order and state", "global pax headers")

# (pattern, level, what it means), in order: the first pattern that matches a feature applies.
STRICT = [
    ("scan.error", "framing", "the scanner could not read past a header"),
    ("checksum.*", "framing", "a checksum that matches only one way of summing"),
    # Number fields that shape the tree are one criterion per problem: see criterion()
    ("number.[*].leading-space", "framing", "leading spaces in a size, mode or checksum"),
    ("number.[*].*", "framing", "a size, mode or checksum written in a way that readers differ on"),
    ("number.size.*", "framing", "a size written in a way that readers differ on"),
    ("number.chksum.*", "framing", "a checksum field written in a way that readers differ on"),
    ("magic.posix-with-odd-version", "framing", "POSIX magic with a version other than `00`"),
    ("magic.*", "framing", "a header that readers may not recognize as one"),
    ("type.unknown-*", "framing", "an unknown typeflag: data or no data"),
    ("type.gnu-sparse", "framing", "GNU's old sparse files"),
    ("type.contiguous", "framing", "contiguous files (7)"),
    ("pax.invalid-size", "framing", "a pax size that is not a number"),
    ("pax.size-on-*", "framing", "a pax size on a member without data"),
    ("pax.size-*", "framing", "a pax size that disagrees with the header"),
    ("extended.pax-size-before-gnu-long", "framing", "a pax size that a GNU long name may take"),
    ("extended.without-member", "framing", "an extended header without a member"),
    ("pax.newline-in-value.*", "framing", "a newline in a pax value, where readers split lines"),
    ("end.missing", "framing", "no end-of-archive marker"),
    ("end.lone-zero-block", "framing", "an end-of-archive marker of one zero block, not two"),
    ("end.data-after", "framing", "data other than zeros after the end-of-archive marker"),
    ("end.archive-after", "framing", "another archive after the end-of-archive marker"),
    ("end.zero-block-before-member", "framing", "a zero block, then more members"),
    ("end.*", "framing", "the end of the archive"),
    ("archive.empty", "framing", "no members at all"),
    ("name.leading-dot-slash", "name", "`./a`, which some readers make `a`"),
    ("name.dot", "name", "a member named `.` or `./`"),
    ("name.dot-component", "name", "`a/./b`"),
    ("name.double-slash", "name", "`a//b`"),
    ("name.trailing-slash-on-file", "kind", "a regular file named like a directory, `a/`"),
    ("name.absolute", "name", "an absolute name"),
    ("name.dotdot", "name", "`..` in a name"),
    ("name.empty", "name", "an empty name"),
    ("name.backslash", "name", "`\\`, a separator on Windows"),
    ("name.drive-letter", "name", "a drive letter"),
    ("name.control-character", "name", "a control character in a name"),
    ("name.not-utf8", "name", "a name that is not UTF-8"),
    ("name.bytes-after-nul", "name", "bytes after the NUL that ends a name"),
    ("name.*", "name", "a name that readers may normalize differently"),
    ("extended.*", "name", "several sources for one name or link target"),
    ("pax.hdrcharset", "name", "names that are not UTF-8 by declaration"),
    ("pax.path-not-utf8", "name", "a pax path that is not UTF-8"),
    ("pax.gnu-sparse", "name", "pax keys of GNU sparse files, which change the name"),
    ("pax.GNU.sparse.*", "name", "pax keys of GNU sparse files, which change the name"),
    ("pax.key-in-two-headers.*", "name", "a pax key in two extended headers of one member"),
    ("pax.nul-in-value.path", "name", "NUL in a pax path"),
    ("pax.nul-in-value.linkpath", "name", "NUL in a pax link path"),
    ("gnu.*", "name", "the prefix field of a GNU header, which GNU tar uses for times"),
    ("format.star", "name", "star's prefix field"),
    ("type.solaris-extended", "name", "Solaris X headers"),
    ("symlink.absolute", "name", "a symlink to an absolute path"),
    ("symlink.escapes", "name", "a symlink that points out of the archive"),
    ("symlink.*", "name", "a symlink target that readers may handle differently"),
    ("pax.SCHILY.filetype", "kind", "a pax key that changes the kind"),
    ("number.mode.*", "kind", "a mode written in a way that readers differ on"),
    ("tree.duplicate.file-file", "order and state", "the same file twice"),
    ("tree.duplicate.*", "order and state", "one path as two members"),
    ("tree.under-*", "order and state", "a member under a file or a symlink"),
    ("tree.through-symlink", "order and state", "a member written through a symlink"),
    ("tree.*", "order and state", "members that interact"),
    ("hardlink.to-itself", "order and state", "a hardlink to itself"),
    ("hardlink.to-symlink", "order and state", "a hardlink to a symlink"),
    ("hardlink.*", "order and state", "a hardlink to a later member, no member, or a misspelling"),
    ("pax-global.after-members", "global pax headers", "a global header after the first member"),
    ("pax-global.*", "global pax headers", "a global header with more than a comment"),
]

ALLOWED = [
    ("name.fills-field", "a name of exactly 100 bytes, without NUL (`y_`)"),
    ("linkname.no-nul", "a link name of exactly 100 bytes, without NUL"),
    ("name.non-ascii", "UTF-8 names"),
    ("name.not-nfc", "names not in NFC: one tree, which macOS may not hold"),
    ("name.dir-without-trailing-slash", "a directory without a trailing slash: the typeflag says"),
    ("ustar.prefix", "the ustar prefix field (`y_`)"),
    ("number.size.base256", "base-256 sizes of files over 8 GiB (`y_`)"),
    ("number.uid.*", "outside the tree"),
    ("number.gid.*", "outside the tree"),
    ("number.mtime.*", "outside the tree"),
    ("number.devmajor.*", "outside the tree"),
    ("number.devminor.*", "outside the tree"),
    ("type.nul", "the typeflag NUL of regular files, from before POSIX"),
    ("v7.bytes-after-linkname", "bytes in fields that v7 headers do not use"),
    ("tree.dir-after-contents", "directories after their contents (`y_`)"),
    ("tree.duplicate.dir-dir", "the same directory twice (`y_`)"),
    ("pax.SCHILY.*", "vendor pax keys outside the tree"),
    ("pax.LIBARCHIVE.*", "vendor pax keys outside the tree"),
    ("pax.nul-in-value.SCHILY.xattr.*", "NUL in xattrs, which are outside the tree"),
    ("pax.nul-in-value.LIBARCHIVE.xattr.*", "NUL in xattrs, which are outside the tree"),
]

# Compressions that tarscan.py does not read: it scans these as uncompressed tar
UNREAD = (".tar.lz", ".tar.zst", ".tzst", ".tar.lzma", ".tlz", ".tar.Z")


def classify(feature):
    """("platform" | "allowed" | "strict" | "unclassified", level, description)"""
    if feature.startswith("platform."):
        return "platform", None, None
    for pattern, reason in ALLOWED:
        if fnmatch.fnmatchcase(feature, pattern):
            return "allowed", None, reason
    for pattern, level, description in STRICT:
        if fnmatch.fnmatchcase(feature, pattern):
            return "strict", level, description
    return "unclassified", None, None


def assessed(r):
    if "features" not in r:
        return False
    name = r.get("name") or r.get("url", "")
    return not (r.get("error") and r["compression"]["format"] == "none" and name.endswith(UNREAD))


def criterion(feature):
    """The criterion of a strict feature: a problem of number fields that shape the tree is one
    criterion for all of them, as a parser has one rule for it."""
    return re.sub(r"^number\.(size|mode|chksum)\.", "number.*.", feature)


def strict_features(r):
    found = {criterion(f) for f in r["features"] if classify(f)[0] == "strict"}
    if r.get("error") or r.get("compression_error") or r.get("compression", {}).get("truncated"):
        found.add("scan.error")
    return found


def percent(n, total):
    return f"{100 * n / total:.2f}%" if total else "–"


def bound(total):
    """The 95% upper bound of a rate of which none of total were seen: the rule of three."""
    return f"<{300 / total:.2g}%" if total else "–"


def median_year(r):
    m = r.get("mtime")
    try:
        return time.gmtime(m[1]).tm_year if m else None
    except (OverflowError, OSError, ValueError):
        return None


def labels(names):
    """Datasets by their ecosystem, or by their directory where an ecosystem has several."""
    ecosystems = collections.Counter(n.split("/")[0] for n in names)
    return {n: n.split("/")[0] if ecosystems[n.split("/")[0]] == 1 else n for n in names}


def fixed_mtimes(rows):
    """mtimes that producers write in place of the real ones: those that all members of at least
    20 tarballs without a uname have, as producers that normalize mtimes also leave out names.
    Real dates, such as the commit that git archive writes, rarely repeat."""
    same = collections.Counter(
        r["mtime"][0]
        for r in rows
        if r.get("mtime")
        and r["mtime"][0] == r["mtime"][2]
        and set(r.get("fingerprint", {}).get("uname", {})) <= {""}
    )
    return {t for t, n in same.items() if n >= 20}


def histogram(datasets, union):
    """Tarballs by the median mtime of their members, in bins of two years, for each dataset."""
    names = list(datasets)
    fixed = fixed_mtimes(union)

    def bin_of(r):
        m = r.get("mtime")
        if m and m[0] == m[2] and m[0] in fixed and set(r["fingerprint"].get("uname", {})) <= {""}:
            return "fixed"
        y = median_year(r)
        if y is None or y <= 1980:
            return "unknown"
        if y < 1990:
            return "1981–1989"
        start = y - y % 2
        return f"{start}–{start + 1}"

    counts = {name: collections.Counter() for name in names}
    total = collections.Counter()
    for name, rows in datasets.items():
        for r in rows:
            if "features" in r:
                counts[name][bin_of(r)] += 1
    for r in union:
        if "features" in r:
            total[bin_of(r)] += 1
    bins = ["1981–1989"] + [f"{y}–{y + 1}" for y in range(1990, 2027, 2)] + ["fixed", "unknown"]
    bins = [b for b in bins if total[b]]
    widest = max(total.values())
    columns = [labels(names)[n] for n in names] + ["all"]
    widths = [max(len(c), 5) for c in columns]
    lines = ["years      " + " ".join(f"{c:>{w}}" for c, w in zip(columns, widths))]
    for b in bins:
        bar = "#" * max(1, round(40 * total[b] / widest))
        cells = [counts[n][b] for n in names] + [total[b]]
        row = " ".join(f"{c:>{w}}" for c, w in zip(cells, widths))
        lines.append(f"{b:<10} {row}  {bar}")
    return "\n".join(lines), fixed


def passes(r, allowed=()):
    return not (strict_features(r) - set(allowed))


def pass_table(names, short, rated, allowed=()):
    """Pass rates per dataset, and with the criteria allowed also allowed."""
    extra = f" | pass if `{'`, `'.join(allowed)}` were allowed" if allowed else ""
    lines = [
        f"| dataset | assessed | pass all criteria | of latest versions{extra} | untar extracts |",
        "|---|---|---|---|" + ("---|" if allowed else "") + "---|",
    ]
    for n in names:
        rs = rated[n]
        latest = [r for r in rs if r.get("latest")]
        passing = sum(passes(r) for r in rs)
        lp = sum(passes(r) for r in latest)
        tested = [r for r in rs if "untar_error" in r]
        extracted = sum(not r.get("untar_error") for r in tested)
        cells = [
            short[n],
            str(len(rs)),
            f"{passing} ({percent(passing, len(rs))})",
            f"{lp} ({percent(lp, len(latest))})",
        ]
        if allowed:
            p = sum(passes(r, allowed) for r in rs)
            cells.append(f"{p} ({percent(p, len(rs))})")
        cells.append(f"{extracted} ({percent(extracted, len(tested))})")
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def costliest(union):
    """The criterion that rejects the most tarballs on its own."""
    sole = collections.Counter()
    for r in union:
        found = strict_features(r)
        if len(found) == 1:
            sole[next(iter(found))] += 1
    return sole.most_common(1)[0][0] if sole else None


def readme(path, names, short, rated, union):
    top = costliest(union)
    allowed = (top,) if top else ()
    block = (
        f"Of {len(union)} distinct tarballs, {sum(passes(r) for r in union)} pass every criterion. "
        f"The criterion that rejects the most tarballs on its own is `{top}`.\n\n"
        + pass_table(names, short, rated, allowed)
        + f"\n\nGenerated by `scanner/strict.py` from {len(names)} scans: the details are in "
        "[data/STRICT.md](data/STRICT.md)."
    )
    text = open(path).read()
    begin, end = "<!-- begin strict.py -->", "<!-- end strict.py -->"
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    with open(path, "w") as f:
        f.write(f"{head}{begin}\n{block}\n{end}{tail}")


def main():
    args = sys.argv[1:]
    readme_path = None
    if args[:1] == ["--readme"]:
        readme_path, args = args[1], args[2:]
    rows, datasets = load(args)
    names = list(datasets)
    short = labels(names)
    rated = {n: [r for r in datasets[n] if assessed(r)] for n in names}
    union = [r for r in rows if assessed(r)]
    if readme_path:
        readme(readme_path, names, short, rated, union)
        return

    print("# Strict parsing of real tarballs\n")
    print(
        "How many release tarballs a strict tar parser would accept, if it rejected every "
        "ambiguity that [METHOD.md](../METHOD.md) lists. Generated by `scanner/strict.py` from the "
        "scans in this directory: see their `RUN.md` for how each was made.\n"
    )

    print("## What was scanned\n")
    print("| dataset | tarballs | scanned | not assessed | latest | GB | members | origins |")
    print("|---|---|---|---|---|---|---|---|")
    for n in names:
        scanned = [r for r in datasets[n] if "features" in r]
        gb = sum(r.get("bytes") or 0 for r in scanned) / 1e9
        members = sum(r.get("members") or 0 for r in scanned)
        latest = sum(1 for r in rated[n] if r.get("latest"))
        origins = collections.Counter(origin(r["url"]) for r in scanned)
        top = ", ".join(f"{k} {v}" for k, v in origins.most_common(3))
        print(
            f"| {short[n]} | {len(datasets[n])} | {len(scanned)} | "
            f"{len(scanned) - len(rated[n])} | {latest} | {gb:.1f} | {members:,} | {top} |"
        )
    gb = sum(r.get("bytes") or 0 for r in union) / 1e9
    print(f"| all, distinct | {len(rows)} | | | {sum(1 for r in union if r.get('latest'))} | "
          f"{gb:.1f} | {sum(r.get('members') or 0 for r in union):,} | |\n")
    print(
        "Not downloaded: tarballs that no URL serves any more. Not assessed: in a compression "
        "that the scanner does not read (`.tar.lz`, `.tar.zst`). Latest: the latest version "
        "of a package in its repository.\n"
    )
    print("Tarballs by the median mtime of their members, which dates most of them:\n")
    chart, fixed = histogram(datasets, rows)
    print("```")
    print(chart)
    print("```\n")
    print(
        "Fixed: every member has an mtime that a producer writes in place of the real one, such "
        "as `cabal sdist` (2001-09-09) on Hackage and hatchling (2020-02-02) on PyPI, so these "
        "tarballs are not dated: "
        + ", ".join(time.strftime("%Y-%m-%d %H:%M", time.gmtime(t)) for t in sorted(fixed))
        + ". Unknown: no mtime after 1980.\n"
    )

    print("## Pass rates\n")
    print(
        "A tarball passes if it has none of the strict criteria below. untar is the strict "
        "extractor of [untar](https://github.com/haampie/untar), as a policy that exists.\n"
    )
    top = costliest(union)
    print(pass_table(names, short, rated, (top,) if top else ()))
    print()

    failing = collections.defaultdict(lambda: collections.defaultdict(list))
    for n in names:
        for r in rated[n]:
            for f in strict_features(r):
                failing[f][n].append(r)
    sole = collections.Counter()
    examples = collections.defaultdict(list)
    for r in union:
        found = strict_features(r)
        if len(found) == 1:
            sole[next(iter(found))] += 1
        for f in found:
            if len(examples[f]) < 3:
                name = f"{r['package']}@{r['version']}" if r["version"] else r["package"]
                examples[f].append(name)

    print("## Criteria\n")
    print(
        "Tarballs that each criterion rejects, per dataset. Alone: tarballs of all datasets "
        "that only this criterion rejects, which allowing it would let through.\n"
    )
    print("| level | criterion | " + " | ".join(short[n] for n in names) + " | alone | examples |")
    print("|---|---|" + "---|" * len(names) + "---|---|")
    order = sorted(
        failing,
        key=lambda f: (
            LEVELS.index(classify(f)[1]) if f != "scan.error" else 0,
            -sum(len(v) for v in failing[f].values()),
        ),
    )
    for f in order:
        level, description = ("framing", STRICT[0][2]) if f == "scan.error" else classify(f)[1:]
        cells = " | ".join(
            f"{len(failing[f][n])} ({percent(len(failing[f][n]), len(rated[n]))})"
            if failing[f][n]
            else "0"
            for n in names
        )
        print(
            f"| {level} | `{f}`: {description} | {cells} | {sole[f]} | "
            f"{', '.join(examples[f])} |"
        )
    print()
    print(
        "Other criteria reject no tarball here. That is no proof that they cost nothing: with 95% "
        "confidence, each rejects less than "
        + ", ".join(f"{bound(len(rated[n]))[1:]} of {short[n]}" for n in names)
        + ".\n"
    )

    print("## Allowed features\n")
    print("Not ambiguous, or confined to fields outside the tree. Tarballs of all datasets:\n")
    print("| feature | why it is allowed | tarballs |")
    print("|---|---|---|")
    allowed = collections.Counter(
        f for r in union for f in r["features"] if classify(f)[0] == "allowed"
    )
    for f, count in allowed.most_common():
        print(f"| `{f}` | {classify(f)[2]} | {count} |")
    print()
    platform = collections.Counter(
        f for r in union for f in r["features"] if classify(f)[0] == "platform"
    )
    if platform:
        print(
            "Names that some filesystems cannot hold, so that extraction fails there only: "
            + ", ".join(f"`{f}` {c}" for f, c in platform.most_common())
            + ".\n"
        )
    unclassified = collections.Counter(
        f for r in union for f in r["features"] if classify(f)[0] == "unclassified"
    )
    if unclassified:
        print("## Unclassified features\n")
        print("Neither strict nor allowed yet: " + ", ".join(
            f"`{f}` {c}" for f, c in unclassified.most_common()) + ".\n")


if __name__ == "__main__":
    main()
