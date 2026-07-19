# Changelog

## 0.7.1 - Learning Foundation
- Added per-article SIMS_ARTICLE_LEARNING_RECORD_V1 output.
- Added provisional and confirmed UAT record states.
- Added ten-record SIMS_ARTICLE_LEARNING_REPORT_V1 aggregation.
- Added human feedback template and asset-level root-cause routing.
- Added governance rules preventing unapproved automatic self-modification.
- Updated Article Creator contract to 1.2.0.

## 0.7.0 - 2026-07-19
- Personal Blogger Edition基盤を追加
- Runtime Lock、Monetization Router、Editorial Voice、Publish Modeを追加
- Blog Profile / Author Profile / Affiliate Inputテンプレートを追加
- Review Pattern 2.0とGolden Article「ピアノ講座 口コミ」回帰テストを追加
- Input/Output Contractを1.1.0へ拡張
- PR表記、アフィリエイトリンク、body_markdown完全性の品質ゲートを強化

## 0.6.0 - UAT Prototype
- 8種類のPattern Libraryを実装
- Pattern Manifest / Routing / Composer Rulesを追加
- Pattern Composer RuntimeをEditorial Pipelineへ統合
- UAT Request、Evaluation Sheet、Editorial Learning Recordを追加
- Pattern/UAT静的検証を追加
- Claude Project投入用プロトタイプを整備


## [0.5.0] - 2026-07-19

### Added
- Knowledge Architecture v1.0
- Knowledge Index、Manifest、Routing、Precedence、Conflict Resolution
- Search Intent、Reader Model、Helpful Content、E-E-A-T、SEO、Evidence、Freshness、Safety、YMYL、Readability、Originality、Internal Link、Monetization Knowledge
- Claim ClassificationとSource Quality階層
- Knowledge Load Runtime
- KnowledgeテストとManifest検証
- Claude Project Instructions

### Changed
- READMEの版表示と開発状況を修正
- Runtimeのロード順序をKnowledge Architecture対応へ更新
- Editorial CoreからKnowledgeへの参照境界を明文化

## [0.4.0] - 2026-07-19

### Added
- Editorial Core、Coverage Engine、Reader Journey Engine
- Evidence Gate、Fabrication Prevention
- Editorial Review、Publication Readiness Gate
- Quality Frameworkと関連テスト

## [0.3.0] - 2026-07-19

### Added
- Input / Output Specification
- SIMS_ARTICLE_CREATOR_V1 JSON Contract
- JSON Schema、Reason Codes、Warning Codes、Examples、Contract Test