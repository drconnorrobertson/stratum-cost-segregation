"""Read-only public release checks; no credentials, submissions or indexing requests."""
import concurrent.futures
import json
from pathlib import Path
import urllib.request

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'outputs/owner-growth-manifest.json').read_text())
base='https://www.stratumcostsegregation.com'

def check(url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Stratum-owner-release-verification/1.0'})
        with urllib.request.urlopen(req,timeout=30) as response:
            body=response.read().decode('utf-8')
            if url.endswith('.csv'):
                passed=response.status==200 and '"' in body and len(body.splitlines())>=2
            else:
                passed=response.status==200 and f'rel="canonical" href="{url}"' in body
                if url in manifest['newPages']:
                    passed=passed and 'owner-main' in body and 'data-owner-cta' in body
                else:
                    passed=passed and 'data-owner-growth' in body
            return {'url':url,'status':response.status,'finalUrl':response.url,'passed':passed}
    except Exception as error:
        return {'url':url,'passed':False,'error':str(error)}

targets=manifest['newPages']+manifest['updatedPages']+[base+p for p in manifest['templates']]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results=list(pool.map(check,targets))
report={'checkedAt':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'checked':len(results),'passed':sum(r['passed'] for r in results),'results':results}
(root/'outputs/owner-production-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='results'}))
for r in results:
    if not r['passed']:print(json.dumps(r))
if not all(r['passed'] for r in results):raise SystemExit(1)
