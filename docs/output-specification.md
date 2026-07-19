# 出力仕様 v1.0

## 1. 出力の二層構造

### Human-readable Output
1. 実行サマリー
2. 入力解釈と前提
3. 検索意図・読者課題
4. Editorial Brief
5. SEOタイトルとメタディスクリプション
6. H2・H3構成
7. 完成記事
8. FAQ
9. 内部リンク候補
10. 広告・CTA設計
11. 根拠・不足情報
12. 品質検査と公開判定

### Machine-readable Output
`SIMS_ARTICLE_CREATOR_V1`形式のJSONを出力する。

## 2. 公開判定
- `PASS`: 公開可能
- `PASS_WITH_WARNING`: 注意点確認後に公開可能
- `NEEDS_REVISION`: 修正後に再検査
- `NEEDS_EVIDENCE`: 根拠追加が必要
- `NEEDS_EXPERT_REVIEW`: 専門家または人による確認が必要
- `BLOCKED`: 現状では公開不可

## 3. 本文と警告の関係
本文が生成されても公開可能とは限らない。警告、未確認主張、YMYLリスクは削除せずJSONに保持する。

## 4. Markdown記事
完成記事は、原則としてタイトルを除き、導入、H2/H3、本文、FAQ、まとめの順で出力する。記事タイプにより不要な章は省略できる。

## 5. JSON整合性
- `format`は固定値`SIMS_ARTICLE_CREATOR_V1`
- `contract_version`はSemVer
- `article.main_keyword`と入力のメインキーワードは一致
- `publication_gate.status`と警告・blocking issueに矛盾がない
- 実体験がない場合、`first_party_experience.used=false`
- 未確認の重要主張は`evidence_items`に存在する

正式スキーマは`claude/contracts/schemas/article-creator-output.schema.json`を正とする。
