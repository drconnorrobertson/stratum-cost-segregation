// Package only public website files; source data, generators and audits stay in Git.
import {readdir, mkdir, rm, copyFile, readFile} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root = path.dirname(fileURLToPath(import.meta.url));
const output = path.join(root, 'public');
const excluded = new Set(['.git', '.github', 'public', 'content', '__pycache__', 'node_modules', 'cost-seg-discovery']);
const assets = new Set(['.css', '.js', '.csv', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.ico', '.woff', '.woff2']);
await rm(output, {recursive:true, force:true});
let pages = 0;
async function walk(dir, rel = '') {
  for (const entry of await readdir(dir, {withFileTypes:true})) {
    if (entry.name.startsWith('.') || excluded.has(entry.name)) continue;
    const child = path.join(rel, entry.name);
    if (entry.isDirectory()) { await walk(path.join(dir, entry.name), child); continue; }
    const ext = path.extname(entry.name);
    const allowed = entry.name === 'index.html' || (rel === '' && ['404.html','robots.txt','sitemap.xml','style.css'].includes(entry.name))
      || (rel === '' && /^(?:google[a-z0-9]+\.html|[a-f0-9]{32}\.txt)$/.test(entry.name))
      || (rel.split(path.sep)[0] === 'assets' && assets.has(ext));
    if (!allowed) continue;
    const target = path.join(output, child);
    await mkdir(path.dirname(target), {recursive:true});
    await copyFile(path.join(dir, entry.name), target);
    if (entry.name === 'index.html') pages++;
  }
}
await walk(root);
const sitemap = await readFile(path.join(output, 'sitemap.xml'), 'utf8');
const urls = [...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>m[1]);
if (urls.length !== pages || new Set(urls).size !== pages) throw new Error('Sitemap/page count mismatch');
for (const url of urls) {
  const pathname = new URL(url).pathname;
  const page = await readFile(path.join(output, pathname, 'index.html'), 'utf8');
  if (!page.includes(`rel="canonical" href="${url}"`)) throw new Error(`Canonical mismatch: ${url}`);
}
console.log(`Packaged ${pages} canonical pages and public assets. Source files excluded.`);
