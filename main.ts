// Entry for make.fun's "Sum up 24 November's world news in one image" bounty.
//
// The picture itself is entry.png, which sits beside this file in the
// repository: a broadsheet front page drawn in code (see generate.py)
// from the world news reported on Tuesday 24 November 2026. This program
// is the delivery step: it checks the picture is a whole PNG within the
// contest's size gate, then places it where the grader reads it.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const MAX_BYTES = 1_048_576; // the gate: at most 1 MiB
const PNG_SIGNATURE = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

const source = new URL('./entry.png', import.meta.url);
const bytes = readFileSync(source);

const isPng = PNG_SIGNATURE.every((b, i) => bytes[i] === b);
if (!isPng) throw new Error('entry.png does not start with a PNG signature');

// The gate also caps the canvas at 1024 by 1024 pixels; a PNG carries its
// width and height as two big-endian words in the IHDR chunk, at bytes
// 16..24, so read them straight from the header and refuse an oversize
// picture here rather than at the grader.
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 gate`);
}
if (bytes.length > MAX_BYTES) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB gate`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(source, join(outDir, 'entry.png'));
console.log(`entry.png delivered: ${bytes.length} bytes to ${outDir}`);
