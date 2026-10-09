#!/usr/bin/env python3
"""Editorial inventory and overlap review for the new resource library."""
from pathlib import Path
from collections import Counter
import html,json,re,statistics
ROOT=Path(__file__).resolve().parent
def main():
    items=json.loads((ROOT/'content/resource-expansion-manifest.json').read_text())
    assert len(items)==500 and len({m['path'] for m in items})==500
    words=[];shingles=[];errors=[]
    for m in items:
        s=(ROOT/m['path']/'index.html').read_text()
        assert '<link rel="canonical" href="https://www.stratumcostsegregation.com/'+m['path']+'/'+'">' in s
        assert 'reviewedBy' not in s and 'Tax review by' not in s
        main=re.search(r'<main\b.*?</main>',s,re.S)[0]
        main=re.sub(r'<script.*?</script>|<nav.*?</nav>','',main,flags=re.S)
        main=re.sub(r'<section class="source-panel".*','',main,flags=re.S)
        tokens=re.findall('[a-z0-9]+',html.unescape(re.sub('<[^>]+>',' ',main)).lower())
        words.append(len(tokens));shingles.append(set(zip(*(tokens[i:] for i in range(5)))))
        for source in m['sources']:
            if source not in s:errors.append(m['path']+': missing declared source')
        if len(tokens)<450:errors.append(m['path']+': insufficient developed evidence content')
    nearest=[]
    for i,a in enumerate(shingles):
        value,j=max((len(a&b)/len(a|b),j) for j,b in enumerate(shingles) if j!=i)
        nearest.append({'page':items[i]['path'],'nearest':items[j]['path'],'five_word_jaccard':round(value,4)})
        if value>=.65:errors.append(items[i]['path']+': similarity needs editorial review: '+str(round(value,3)))
    report={'guides':500,'category_counts':dict(Counter(x['category'] for x in items)),
      'main_content_word_count':{'minimum':min(words),'median':statistics.median(words),'maximum':max(words)},
      'similarity_method':'Pairwise five-word Jaccard, excluding navigation, sources, related links, and CTA. 0.65 is an internal review flag, not a search engine policy or ranking threshold.',
      'maximum_nearest_similarity':max(x['five_word_jaccard'] for x in nearest),'errors':errors,'nearest':nearest}
    (ROOT/'content/resource-expansion-quality.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='nearest'},indent=2))
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
