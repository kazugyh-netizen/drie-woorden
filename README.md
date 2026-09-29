# Drie Woorden（ドリーワード）

1日3語、身の回りのものを撮ってオランダ語で名前をつける。2026-09-29 作成。

- **採取**：撮る（または写真から選ぶ）→ 写真の真ん中に白帯＋黒文字 → 単語を入力 → 保存
  - 入力中、欄の下に候補（よく使う語の順）。押すと入って読み上げる
  - 欄の下に「✓ 辞書にある語／辞書に無い語」
  - 🔊 で端末のオランダ語音声（speechSynthesis, nl-NL）
- **ライブラリ**：日付ごとの一覧。1枚を押すと大きく出て読み上げ。写真に保存・削除
- 右上に今日の数（●●● 3/3）

## 作り

- サーバー不要の静的ファイルだけ（index.html ＋ words.txt ＋ sw.js ＋ manifest.json ＋ アイコン）
- 保存は端末のブラウザの IndexedDB（`drie-woorden` / `items`）。写真は合成済みの JPEG（長辺 1600px）
- sw.js で一式を端末に置くので、一度開けば圏外でも開ける。**中身を変えたら sw.js の VERSION を上げる**
- ライブラリの下に「控えを書き出す／控えから戻す」（写真ごと JSON）

## 単語リスト（words.txt）

1行目が `#よく使う語の数`、以降が候補の順。取り直しは `sh src/fetch.sh && python3 src/build_words.py`。

| 出所 | ライセンス | 使い方 |
| --- | --- | --- |
| [FrequencyWords](https://github.com/hermitdave/FrequencyWords) nl_50k（OpenSubtitles 2018） | CC-BY-SA | 並び順（頻度） |
| [OpenTaal](https://github.com/OpenTaal/opentaal-wordlist) basiswoorden-gekeurd | BSD / CC BY 3.0 | 正しい語かどうかの判定＋残りの候補 |

頻度表のうち OpenTaal に載っている語だけ（23,442 語）を先に、OpenTaal の残りを後ろに（計 195,134 語）。
人名や英語は OpenTaal で落ちる。縮小形（kopje など）は OpenTaal の基本語に無いので「辞書に無い語」と出る。

## 手元での確認

launch.json の `drie-woorden`（port 7926）。
