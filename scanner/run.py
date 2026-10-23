"""Download a sample of tarballs and scan them.

    python -I scanner/run.py sample LIST N SEED > SAMPLE
    python -I scanner/run.py scan SAMPLE OUT [--untar PATH] [--jobs N] [--reuse FILE]...

`sample` takes the output of spack_list.py and picks N/2 latest versions of distinct packages,
and N/2 older versions of other distinct packages, in an order that is random but determined by
SEED and the names of packages and checksums of tarballs.

`scan` downloads each tarball from the first of its `urls` that works, scans it while it
downloads, checks its sha256, and appends a JSON line to OUT. Tarballs are never
written to disk, so tarballs of any size are scanned. Tarballs that are already in OUT
are skipped, so an interrupted run can continue. Every line records the version of the scanner,
and of untar, as the start of the sha256 of their source.

With --reuse FILE (repeatable), tarballs that FILE has results for, from the same versions of
the scanner and untar, are not downloaded: their results are copied. So ecosystems that share
tarballs are each sampled in full, while every tarball is downloaded once. With --untar, each tarball is also extracted by
untar from PATH, in a child process that reads the decompressed archive from a pipe, and its
error recorded. If untar runs out of disk space, that is recorded apart from its errors.
"""

import hashlib
import json
import lzma
import multiprocessing
import os
import subprocess
import shutil
import sys
import tempfile
import time
import traceback
import urllib.request
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tarscan  # noqa: E402

SCANNER = hashlib.sha256(open(tarscan.__file__, "rb").read()).hexdigest()[:12]
# Results of a scan, as opposed to the fields of the list entry of a tarball
SCAN_FIELDS = (
    "bytes",
    "members",
    "kinds",
    "features",
    "examples",
    "fingerprint",
    "mtime",
    "error",
    "compression",
    "compression_error",
    "untar_error",
    "untar_skipped",
    "scanner",
    "untar",
)
USER_AGENT = "tar-minefield-scanner (+https://github.com/haampie-llms/tar-minefield)"


def rank(seed, key):
    """A random but stable order: the order of most keys does not change when others are added
    or removed, so samples of later package lists overlap with earlier ones."""
    return hashlib.sha256(f"{seed}:{key}".encode()).hexdigest()


def sample(path, n, seed):
    seen = set()
    by_package = {}
    for line in open(path):
        t = json.loads(line)
        if t["sha256"] in seen:
            continue
        seen.add(t["sha256"])
        by_package.setdefault(t["package"], []).append(t)
    packages = sorted(by_package, key=lambda p: rank(seed, p))
    latest = [p for p in packages if any(t.get("latest") for t in by_package[p])][: n // 2]
    taken = set(latest)
    older = [
        p for p in packages if p not in taken and any(not t.get("latest") for t in by_package[p])
    ][: n - len(latest)]
    for p in latest:
        print(json.dumps(next(t for t in by_package[p] if t.get("latest"))))
    for p in older:
        versions = [t for t in by_package[p] if not t.get("latest")]
        print(json.dumps(min(versions, key=lambda t: rank(seed, t["sha256"]))))


# Extracts a tar archive from stdin with untar from argv[1], into argv[2]
UNTAR = """
import errno, sys
sys.path.insert(0, sys.argv[1])
import untar
try:
    untar.extract(sys.stdin.buffer, sys.argv[2])
except untar.Error as e:
    print(e, file=sys.stderr)
    sys.exit(10)
except OSError as e:
    # Out of disk space says nothing about the archive. Other errors do: untar never replaces
    # an entry (O_EXCL), so an archive with names that collide here fails with EEXIST.
    print(f"{type(e).__name__}: {e}", file=sys.stderr)
    sys.exit(11 if e.errno in (errno.ENOSPC, errno.EDQUOT) else 10)
"""


class Untar:
    """untar in a child process, extracting the decompressed archive written to it."""

    def __init__(self, untar_path, dest):
        self.dest = dest
        self.process = subprocess.Popen(
            [sys.executable, "-I", "-c", UNTAR, untar_path, dest],
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        self.stopped = False

    def write(self, chunk):
        if not self.stopped:
            try:
                self.process.stdin.write(chunk)
            except BrokenPipeError:
                # untar stopped reading: it rejected the archive
                self.stopped = True

    def result(self):
        """The outcome, as (error, skipped): error is None if untar extracted the archive."""
        try:
            self.process.stdin.close()
        except BrokenPipeError:
            pass
        stderr = self.process.stderr.read().decode(errors="replace").strip()
        code = self.process.wait()
        shutil.rmtree(self.dest, ignore_errors=True)
        if code == 0:
            return None, None
        if code == 10:
            return stderr, None
        if code == 11:
            return None, f"no disk space: {stderr}"
        return None, f"untar crashed: {stderr[-500:]}"


class Hashing:
    """A binary file that hashes and counts what is read from it."""

    def __init__(self, f):
        self.f = f
        self.sha256 = hashlib.sha256()
        self.size = 0
        self.failed = None

    def read(self, n=-1):
        try:
            data = self.f.read(n)
        except Exception as e:
            self.failed = e
            raise
        self.sha256.update(data)
        self.size += len(data)
        return data


def fetch_and_scan(url, t, untar_path, workdir):
    """Scan the tarball at url while it downloads, and extract it with untar if a path is given.
    Return the result, or an error if it could not be downloaded or its sha256 is wrong."""
    if not url.startswith(("https://", "http://")):
        return None, "not an http(s) URL"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    untar = Untar(untar_path, os.path.join(workdir, "untar")) if untar_path else None
    result = {}
    try:
        with urllib.request.urlopen(request, timeout=60) as r:
            f = Hashing(r)
            start = time.time()
            try:
                result.update(tarscan.scan(f, untar.write if untar else None))
            except Exception as e:
                if f.failed is not None:
                    return None, f"{type(e).__name__}: {e}"
                if isinstance(e, (EOFError, zlib.error, lzma.LZMAError, OSError)):
                    result["compression_error"] = f"{type(e).__name__}: {e}"
                else:
                    result["scan_crash"] = traceback.format_exc()
            while f.read(1 << 20):
                pass
            result["scan_seconds"] = round(time.time() - start, 2)
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"
    finally:
        if untar:
            result["untar_error"], skipped = untar.result()
            if skipped:
                result["untar_skipped"] = skipped
    if f.sha256.hexdigest() != t["sha256"]:
        return None, "sha256 mismatch"
    result["bytes"] = f.size
    return result, None


def scan_one(args):
    t, untar_path = args
    result = dict(t, scanner=SCANNER)
    if untar_path:
        result["untar"] = version(os.path.join(untar_path, "untar.py"))
    workdir = tempfile.mkdtemp(prefix="scan-")
    try:
        errors = []
        for url in t.get("urls") or [t["url"]]:
            scanned, error = fetch_and_scan(url, t, untar_path, workdir)
            if error is None:
                result["source"] = url
                result.update(scanned)
                return result
            errors.append(f"{url}: {error}")
        result["download_error"] = errors
        return result
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def version(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:12]


def reusable(paths, untar_path):
    """Results in paths, by sha256, from this scanner and untar."""
    untar = version(os.path.join(untar_path, "untar.py")) if untar_path else None
    found = {}
    for path in paths:
        for line in open(path):
            r = json.loads(line)
            if "features" in r and r.get("scanner") == SCANNER and r.get("untar") == untar:
                found.setdefault(r["sha256"], r)
    return found


def scan(sample_path, out_path, untar_path=None, jobs=8, reuse=()):
    done = set()
    if os.path.exists(out_path):
        done = {json.loads(line)["sha256"] for line in open(out_path)}
    todo = [json.loads(line) for line in open(sample_path)]
    todo = [t for t in todo if t["sha256"] not in done]
    known = reusable(reuse, untar_path)
    with open(out_path, "a") as out:
        for t in [t for t in todo if t["sha256"] in known]:
            r = known[t["sha256"]]
            copied = {k: r[k] for k in SCAN_FIELDS if k in r}
            out.write(json.dumps(dict(t, **copied, reused_from=r.get("source"))) + "\n")
    todo = [t for t in todo if t["sha256"] not in known]
    print(f"{len(done)} done, {len(todo)} to go", file=sys.stderr)
    with multiprocessing.Pool(jobs) as pool, open(out_path, "a") as out:
        for i, result in enumerate(
            pool.imap_unordered(scan_one, [(t, untar_path) for t in todo]), 1
        ):
            out.write(json.dumps(result) + "\n")
            out.flush()
            if i % 50 == 0:
                print(f"{len(done) + i} done", file=sys.stderr)


def main():
    args = sys.argv[1:]
    if args[0] == "sample":
        sample(args[1], int(args[2]), int(args[3]))
    elif args[0] == "scan":
        untar_path = args[args.index("--untar") + 1] if "--untar" in args else None
        jobs = int(args[args.index("--jobs") + 1]) if "--jobs" in args else 8
        reuse = [args[i + 1] for i, a in enumerate(args) if a == "--reuse"]
        scan(args[1], args[2], untar_path, jobs, reuse)


if __name__ == "__main__":
    main()
