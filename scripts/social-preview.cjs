// Apply the default share image after every page generator has finished.
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const image = 'https://www.stratumcostsegregation.com/assets/stratum-share-20261012.png';
const alt = 'Stratum Cost Segregation — engineering-based studies built around your property';
const tags = `<meta property="og:image" content="${image}">
<meta property="og:image:secure_url" content="${image}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="${alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="${image}">
<meta name="twitter:image:alt" content="${alt}">`;
let count = 0;
function walk(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(file);
    else if (entry.name.endsWith('.html')) {
      const html = fs.readFileSync(file, 'utf8');
      if (!/<\/head>/i.test(html)) continue;
      const clean = html.replace(/<meta\s+[^>]*(?:property|name)=["'](?:og:image(?::[^"']+)?|twitter:image(?::[^"']+)?|twitter:card)["'][^>]*>\s*/gi, '');
      fs.writeFileSync(file, clean.replace(/<\/head>/i, tags + '\n</head>'));
      count++;
    }
  }
}
walk(path.join(root, 'public'));
if (!fs.existsSync(path.join(root, 'public/assets/stratum-share-20261012.png'))) throw new Error('Share image missing');
console.log(`Added social preview metadata to ${count} pages.`);
