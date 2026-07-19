# SIMS Article Creator

SIMS Article Creatorは、メインキーワードからEditorial Brief、Pattern、Coverage、Evidence、記事本文、編集審査、公開判定を生成する独立製品です。

## 現在のバージョン
`0.6.0 UAT Prototype`

## 今回の到達点
v0.5.0 Knowledge Architectureを基準に、8種類のPattern Library、Pattern Composer Runtime、UAT依頼テンプレート、評価票、Editorial Learning Record、検証テストを統合しました。本ZIPを使ってClaude Project上の実記事UATを開始できます。

## 中核フロー
入力検証 → Keyword Intelligence → Search Intent → Reader Model → Pattern Selection / Composer → Editorial Brief → Coverage Map → Evidence Plan → Blueprint → Writing → Editorial Review → Publication Gate → JSON

## 主要ディレクトリ
- `claude/knowledge/`：品質・安全・SEO・読者知識
- `claude/patterns/`：記事タイプ別設計ルール
- `claude/runtime/`：実行パイプライン
- `claude/contracts/`：入出力契約
- `claude/templates/`：成果物テンプレート
- `uat/`：UAT開始用一式
- `tests/`：静的検証と回帰テスト

## UAT開始
`uat/README.md`と`uat/UAT_REQUEST_TEMPLATE.md`を参照してください。

## 製品境界
SIMS Writerとは別リポジトリ・別Claude Projectとして運用し、実行時依存を持ちません。


## v0.7.0 Personal Blogger Edition
AdSense / Affiliate分岐、商品参照URL、アフィリエイトリンク挿入、Blog Profile、Author Profile、Editorial Voice、WordPress・はてな向けPublish Modeを追加。Golden Articleは「ピアノ講座 口コミ」。
