# 入力候補の words.txt を作る。1行目は「#よく使う語の数」、以降は候補の順。
#   1. FrequencyWords（OpenSubtitles 2018, CC-BY-SA）の頻度順のうち、OpenTaal に載っている語
#   2. OpenTaal basiswoorden-gekeurd（BSD / CC BY 3.0）の残り
# 発音記号があれば「語\t/IPA/」。出所は ipa-dict の nl.txt（INT, CC BY。ipa-dict 自体は MIT）。複数あるときは最初の1つ
# 取り直し: sh src/fetch.sh && python3 src/build_words.py
import re, pathlib
here = pathlib.Path(__file__).parent
ot = [l.strip() for l in open(here/'opentaal.txt', encoding='utf-8')]
ots = set(ot); seen = set(); out = []
for l in open(here/'nl_50k.txt', encoding='utf-8'):
    w = l.split()[0]
    if w in ots and len(w) >= 2 and w not in seen: seen.add(w); out.append(w)
nfreq = len(out)
pat = re.compile(r"^[a-zà-ÿ][a-zà-ÿ'\-]*$")
for w in ot:
    if w not in seen and pat.match(w) and len(w) >= 2: seen.add(w); out.append(w)
ipa = {}
for l in open(here/'ipa_nl.txt', encoding='utf-8'):
    w, _, p = l.rstrip('\n').partition('\t')
    p = p.split(',')[0].strip()
    if p and w not in ipa: ipa[w] = p
    if p and w.lower() not in ipa: ipa[w.lower()] = p
lines = [w + ('\t' + ipa[w] if w in ipa else '') for w in out]
(here.parent/'words.txt').write_text(f"#{nfreq}\n" + "\n".join(lines), encoding='utf-8')
print('ipa', sum(1 for w in out if w in ipa))
print(nfreq, len(out))
