# 日本語→オランダ語の引き表 ja_nl.txt を作る。出所は JMdict（EDRDG ライセンス）の jmdict-simplified 版。
# 1行 = 見出し(,区切り)\t訳(;区切り)\t優先度（小さいほど先）
# 取り直し: sh src/fetch.sh && python3 src/build_ja.py
import json, glob, re, pathlib
here = pathlib.Path(__file__).parent
d = json.load(open(glob.glob(str(here/'jmdict-all*.json'))[0], encoding='utf-8'))
LATIN = re.compile(r'^[A-Z][a-z]+ [a-z]+$')
rows = []
for w in d['words']:
    gl = []
    for s in w['sense']:
        for x in s['gloss']:
            if x['lang'] != 'dut': continue
            t = re.sub(r'\{[^}]*\}', '', x['text']).strip(' ,;')
            if not t or '{' in t or '}' in t or LATIN.match(t) or len(t) > 32: continue
            if t not in gl: gl.append(t)
    if not gl: continue
    keys = [k['text'] for k in w['kanji']] + [k['text'] for k in w['kana']]
    common = any(k.get('common') for k in w['kanji'] + w['kana'])
    rows.append((0 if common else 1, ','.join(keys), ';'.join(gl[:4])))
rows.sort(key=lambda r: r[0])
(here.parent/'ja_nl.txt').write_text('\n'.join(f'{k}\t{g}\t{p}' for p, k, g in rows), encoding='utf-8')
print(len(rows), sum(1 for r in rows if r[0] == 0), 'common')
