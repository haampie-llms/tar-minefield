// Extract a tar archive with tar-fs, on tar-stream, for contrib/matrix/matrix.py. Yarn 1
// unpacks packages with it.
//
//     node tar-fs.js ARCHIVE DEST
//
// Exits with status 1 on an error, which is printed on stderr. Some errors are thrown from
// callbacks of tar-fs rather than passed to the stream, so uncaught exceptions are errors too.
import { createReadStream } from "node:fs";
import { pipeline } from "node:stream/promises";
import tarFs from "tar-fs";

function fail(e) {
  console.error(String(e));
  process.exit(1);
}

process.on("uncaughtException", fail);
const [file, cwd] = process.argv.slice(2);
await pipeline(createReadStream(file), tarFs.extract(cwd)).catch(fail);
