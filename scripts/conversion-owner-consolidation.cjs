const fs = require('node:fs');
const path = require('node:path');

module.exports = function consolidateConversionOwner(outputRoot) {
  const origin = 'https://www.stratumcostsegregation.com';
  const retired = origin + '/free-estimate/';
  const owner = origin + '/cost-seg-discovery/';
  const target = fs.readFileSync(path.join(outputRoot, 'cost-seg-discovery/index.html'), 'utf8');
  if (!target.includes('rel="canonical" href="' + owner + '"') || /<meta[^>]*content=["'][^"']*noindex/i.test(target)) {
    throw new Error('Discovery conversion owner must remain canonical and indexable');
  }
  const sitemapFile = path.join(outputRoot, 'sitemap.xml');
  const before = fs.readFileSync(sitemapFile, 'utf8');
  let removed = 0;
  const after = before.replace(/<url>\s*<loc>(.*?)<\/loc>[\s\S]*?<\/url>/g, (entry, url) => {
    if (url !== retired) return entry;
    removed++;
    return '';
  });
  // The existing canonical-discovery stage may already remove configured redirect sources.
  if (removed > 1 || after.includes('<loc>' + retired + '</loc>') || !after.includes('<loc>' + owner + '</loc>')) {
    throw new Error('Retired sitemap owner must be absent and discovery owner retained');
  }
  fs.writeFileSync(sitemapFile, after);
  // The hosting redirect is primary. Keep a useful non-indexable fallback in the static output.
  const fallback = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cost Segregation Discovery | Stratum</title><meta name="robots" content="noindex,follow"><link rel="canonical" href="' + owner + '"><link rel="stylesheet" href="/style.css"></head><body><header><a href="/">Stratum Cost Segregation</a></header><main><h1>Book a Cost Segregation Discovery Call</h1><p>Use the discovery page to review study scope, pricing and scheduling.</p><p><a href="/cost-seg-discovery/">Continue to the discovery page</a></p><p><a href="/pricing/">Review study pricing</a></p></main></body></html>';
  fs.writeFileSync(path.join(outputRoot, 'free-estimate/index.html'), fallback);
  console.log(JSON.stringify({retiredConversionOwner: retired, canonicalConversionOwner: owner, removedSitemapEntries: removed}));
};
