#!/usr/bin/env python3
"""Generate the GitHub Pages homepage; Python 3 standard library only."""
from pathlib import Path
from string import Template
from html import escape
from itertools import groupby
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
def read(name):
    return json.loads((ROOT / 'data' / (name + '.json')).read_text())
def e(value):
    return escape(str(value), quote=True)
def inline(value, new_tab=False):
    """Small, escaped Markdown subset: links, bold, italic. No raw HTML."""
    value = e(value)
    target = ' target="_blank" rel="noopener"' if new_tab else ''
    value = re.sub(r'\[([^\]]+)\]\(((?:https?://|mailto:)[^)]+)\)', rf'<a href="\2"{target}>\1</a>', value)
    value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
    return re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', value)
def link(label, url, cls='', title=None):
    assert url.startswith(('https://', 'http://', 'mailto:', '/')), url
    extra = ' target="_blank" rel="noopener"' if not url.startswith('mailto:') else ''
    accessible = f' aria-label="{e(label + ": " + title)}"' if title else ''
    return f'<a class="{cls}" href="{e(url)}"{extra}{accessible}>{e(label)}</a>'
def render():
    profile = read('profile')
    pubs = sorted(read('publications'), key=lambda x: -x['year'])
    publication_html = []
    for year, papers in groupby(pubs, key=lambda x: x['year']):
        rows = []
        for p in papers:
            actions = ''.join(link(label, p[key], 'paper-link', p['title']) for key, label in [('link','Link'),('pdf','PDF')] if p.get(key))
            award = f'<p class="paper-award">{e(p["award"])}</p>' if p.get('award') else ''
            rows.append(f'<li class="publication" id="{e(p["id"])}"><div class="venue-badge">{e(p["venue"])}</div><div class="paper-content"><h4>{e(p["title"])}</h4><p class="paper-venue">{e(p["venue"])} · {year}</p>{award}<div class="paper-actions">{actions}</div></div></li>')
        publication_html.append(f'<div class="publication-year"><h3>{year}</h3><ol>{"".join(rows)}</ol></div>')
    news = []
    for group in sorted(read('news'), key=lambda x:-x['year']):
        items = ''.join(f'<li>{inline(item, new_tab=True)}</li>' for item in group['items'])
        news.append(f'<div class="news-year"><h3>{group["year"]}</h3><ul>{items}</ul></div>')
    awards = ''.join(f'<li><span class="item-date">{a["year"]}</span><div><strong>{e(a["title"])}</strong>'+ (f'<span class="item-detail">{e(a["institution"])}</span>' if a['institution'] else '')+'</div></li>' for a in sorted(read('awards'), key=lambda x:-x['year']))
    service = ''.join(f'<li><div><strong>{e(s["venue"])}</strong>'+ (f'<span class="item-detail">{e(s["detail"])}</span>' if s.get('detail') else '')+f'</div><span class="role">{e(s["role"])}</span></li>' for s in read('service'))
    teaching = ''.join(f'<li><span class="item-date">{e(t["terms"])}</span><div><strong>{e(t["course"])}</strong><span class="item-detail">{e(t["code"])} · {e(t["role"])} · {e(t["institution"])}</span></div></li>' for t in read('teaching'))
    education = ''.join(f'<li><span class="item-date">{e(x["term"])}</span><span>{e(x["degree"])}<span class="item-detail">{e(x["institution"])}</span></span></li>' for x in profile['education'])
    values = {k:e(v) for k,v in profile.items() if isinstance(v,str)}
    values.update(biography=''.join(f'<p>{inline(p)}</p>' for p in profile['biography']),profile_links=''.join(link(x['label'],x['url']) for x in profile['links']),footer_links=''.join(link(x['label'],x['url']) for x in profile['links'] if x['label'] not in ['Email','X']), education=education,news=''.join(news),publications=''.join(publication_html),awards=awards,service=service,teaching=teaching,year=max(g['year'] for g in read('news')))
    return Template((ROOT/'templates/index.html').read_text()).substitute(values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if committed HTML is stale')
    args = parser.parse_args()
    content = render()
    if args.check:
        assert (ROOT/'index.html').read_text() == content, 'Run python3 scripts/build.py and commit index.html.'
        print('Generated homepage is up to date.')
    else:
        (ROOT/'index.html').write_text(content)
        print('Built index.html (all content is available without JavaScript).')
