# Section Depth Weighting Pattern v1.0

## Purpose
検索意図上の重要度に応じて、各見出しの解説量を調整する。全見出しを同じ深さで書かず、読者が最初に必要とする情報へ文章量を配分する。

## Internal importance levels
- `★★★★★` — Primary answer / decision-critical section
  - 結論、主要な判断基準、中心手順、重要な注意点を十分に説明する。
  - 比較表、手順、具体例、条件分岐を必要に応じて含める。
- `★★★★☆` — Supporting decision section
  - Primary answerを補強する要素を、重複を避けて中程度の深さで説明する。
- `★★★☆☆` — Context / supplementary section
  - 読者理解に必要な背景や補助情報を簡潔に扱う。

## Rules
1. 重要度は内部設計用であり、通常は公開記事へ星印を表示しない。
2. ユーザー指定の見出しは、重要度が低くても勝手に削除・統合しない。
3. 文字数を固定しない。検索意図、Evidence、記事タイプ、読者負荷で調整する。
4. 同じ説明を複数見出しで繰り返さない。
5. Primary answerは記事前半へ配置し、★★★★★の内容を後半へ埋没させない。
6. FAQは本文の再掲ではなく、残存疑問に限定する。

## Quality check
- 最重要の疑問が最も詳しく説明されているか。
- 補助トピックが本題より長くなっていないか。
- 読者が結論へ到達する前に背景説明が過剰になっていないか。
