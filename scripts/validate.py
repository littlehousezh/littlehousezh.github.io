#!/usr/bin/env python3
"""Validate generated content, all local links, and optional remote URLs."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from concurrent.futures import ThreadPoolExecutor
import argparse, json, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids=[]; self.links=[]; self.sections=[]; self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if tag=='section':self.sections.append(attrs.get('id'))
        for key in ['href','src']:
            if attrs.get(key):self.links.append(attrs[key])
def validate():
    subprocess.run([sys.executable,str(ROOT/'scripts/build.py'),'--check'],check=True)
    page=Page((ROOT/'index.html').read_text())
    assert len(page.ids)==len(set(page.ids)), 'Duplicate HTML IDs'
    assert page.sections==['about','news','publications','awards','service','teaching']
    for url in page.links:
        parsed=urlsplit(url)
        if parsed.scheme or parsed.netloc:continue
        if parsed.path:
            target=ROOT/unquote(parsed.path.lstrip('/'))
            assert target.is_file() or (target/'index.html').is_file(), f'Missing local target: {url}'
            if target.suffix=='.pdf':assert target.read_bytes().startswith(b'%PDF-'),f'Invalid PDF: {target}'
        if parsed.fragment:assert parsed.fragment in page.ids, f'Missing anchor: {url}'
    pubs=json.loads((ROOT/'data/publications.json').read_text())
    assert len({p['id'] for p in pubs})==len(pubs)
    assert all(p['id'] in page.ids and (p.get('pdf') or p.get('link')) for p in pubs)
    news=json.loads((ROOT/'data/news.json').read_text())
    assert [n['year'] for n in news]==[2026,2025,2024,2023]
    assert [len(n['items']) for n in news]==[10,5,3,2]
    for folder,anchor in [('about','about'),('publications','publications'),('Releases','teaching')]:
        assert f'url=/#{anchor}' in (ROOT/folder/'index.html').read_text()
    print(f'PASS: {len(pubs)} publications; 20 news entries; all local assets, PDFs, anchors, and legacy redirects.')
    return sorted({u for u in page.links if u.startswith(('http://','https://'))})
def remote(url):
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (academic website link check)'}),timeout=20) as r:
            return {'url':url,'status':r.status,'destination':r.url}
    except HTTPError as e:return {'url':url,'status':e.code,'destination':e.url}
    except (URLError,TimeoutError,OSError) as e:return {'url':url,'status':'unverified','reason':str(e)}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--external',action='store_true');parser.add_argument('--report');args=parser.parse_args()
    urls=validate()
    if args.external:
        with ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(remote,urls))
        for r in results: print(r['status'],r['url'])
        if args.report:Path(args.report).write_text(json.dumps(results,indent=2)+'\n')
        if any(r['status'] in [404,410] for r in results):sys.exit(1)
