// Extract a tar archive with node-tar, for corpus/matrix.py.
//
//     node extract.js ARCHIVE DEST [strict]
//
// With `strict`, node-tar's strict option makes its warnings errors. Exits with status 1 on an
// error, which is printed on stderr.
import * as tar from "tar";

const [file, cwd, mode] = process.argv.slice(2);
try {
  tar.x({ file, cwd, sync: true, strict: mode === "strict" });
} catch (e) {
  console.error(String(e));
  process.exit(1);
}
