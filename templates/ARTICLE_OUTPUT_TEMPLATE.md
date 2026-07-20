# SIMS Article Creator 出力テンプレート v1.2

## 1. 実行サマリー
## 2. 入力解釈・不足情報
## 3. Editorial Brief
## 4. 記事情報
- SEOタイトル
- H1タイトル
- メタディスクリプション
- パーマリンク候補
- カテゴリ候補
- タグ候補

## 5. コピー用完成記事（HTML）
PR表記からまとめ・CTAまでを単独の `html` コードブロックとして出力する。H1は記事情報として別出力し、本文HTMLは原則として導入の`<p>`から開始する。

## 6. 品質検査・公開判定
## 7. SIMS_ARTICLE_CREATOR_V1 JSON
## 8. SIMS_ARTICLE_LEARNING_RECORD_V1 JSON

完成記事の途中へEvidence、分析、JSONを混ぜない。JSONの`article.body_html`には省略なしのHTML全文を格納する。
