const fs = require('node:fs');
const path = require('node:path');

// Preserve the reviewed source guides through the existing production stages.
module.exports = function componentEvidenceReview(outputRoot) {
  const repository = path.resolve(__dirname, '..');
  const guides = {
    'security-cameras-report-review': 'fictional-camera-invoice-review.csv',
    'saunas-renovation-costs': 'fictional-sauna-cost-bridge.csv',
  };
  const owners = new Set();
  for (const [slug, csv] of Object.entries(guides)) {
    const owner = 'https://www.stratumcostsegregation.com/resources/components/' + slug + '/';
    const html = fs.readFileSync(path.join(outputRoot, 'resources/components', slug, 'index.html'), 'utf8');
    if (!html.includes('Reviewed November 22, 2026') || !html.includes('/assets/component-evidence/' + csv)) {
      throw new Error('Reviewed component content was overwritten: ' + slug);
    }
    const target = path.join(outputRoot, 'assets/component-evidence', csv);
    fs.mkdirSync(path.dirname(target), {recursive: true});
    fs.copyFileSync(path.join(repository, 'assets/component-evidence', csv), target);
    owners.add(owner);
  }
  const sitemap = path.join(outputRoot, 'sitemap.xml');
  let count = 0;
  const xml = fs.readFileSync(sitemap, 'utf8').replace(/<url>\s*<loc>(.*?)<\/loc>([\s\S]*?)<\/url>/g, (entry, url, tail) => {
    if (!owners.has(url)) return entry;
    count++;
    const updated = /<lastmod>/.test(tail)
      ? tail.replace(/<lastmod>.*?<\/lastmod>/, '<lastmod>2026-11-22</lastmod>')
      : tail + '<lastmod>2026-11-22</lastmod>';
    return '<url><loc>' + url + '</loc>' + updated + '</url>';
  });
  if (count !== owners.size) throw new Error('Reviewed component sitemap owners missing or duplicated');
  fs.writeFileSync(sitemap, xml);
  console.log(JSON.stringify({reviewedComponentGuides: count, fictionalCsvAssets: count}));
};
