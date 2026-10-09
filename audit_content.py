#!/usr/bin/env python3
"""Flag similar market body text for editorial review; not a Google policy score."""
from pathlib import Path
import re,html,json,statistics,argparse
ROOT=Path(__file__).resolve().parent

def body(path):
    text=path.read_text()
    match=re.search(r'<main\b[^>]*>(.*?)</main>',text,re.S)
    text=match[1] if match else text
    text=re.sub(r'<(?:script|style)\b.*?</(?:script|style)>','',text,flags=re.S)
    text=re.sub(r'<div class="cta-banner">.*','',text,flags=re.S)
    text=html.unescape(re.sub('<[^>]+>',' ',text)).lower()
    return re.findall(r'[a-z0-9]+',text)

def audit():
    files=[p for p in ROOT.glob('cost-segregation-*/index.html') if p.parent.name not in {'cost-segregation-calculator','cost-segregation-resources'}]
    shingles={p.parent.name:set(zip(*(body(p)[i:] for i in range(5)))) for p in files}
    rows=[]
    for name,a in shingles.items():
        nearest,score=max(((other,len(a&b)/len(a|b) if a|b else 0) for other,b in shingles.items() if other!=name),key=lambda x:x[1])
        rows.append({'page':name,'nearest_page':nearest,'five_word_jaccard':round(score,4),'review_flag':score>=0.65})
    return {'method':'Five-word Jaccard similarity of main body; shared navigation excluded. 0.65 is an internal editorial flag, not a Google threshold.','market_count':len(rows),'flagged_count':sum(x['review_flag'] for x in rows),'median_nearest_similarity':round(statistics.median(x['five_word_jaccard'] for x in rows),4),'pages':sorted(rows,key=lambda x:-x['five_word_jaccard'])}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args();result=audit()
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='pages'},indent=2))
