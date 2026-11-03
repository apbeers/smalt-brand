// Copies the brand files the site uses into public/media/, so the site always shows the
// committed logos, badges and social cards rather than copies of them. public/media is not committed.
import { cpSync, rmSync, mkdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const site = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const repo = path.resolve(site, '..');
const out = path.join(site, 'public', 'media');
rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
for (const dir of ['logos', 'badges', 'social']) cpSync(path.join(repo, dir), path.join(out, dir), { recursive: true });
// GitHub Pages serves the custom domain from this file when the site is deployed by Actions too.
writeFileSync(path.join(site, 'public', 'CNAME'), 'smaltworks.dev\n');
console.log('copied logos, badges and social into public/media');
