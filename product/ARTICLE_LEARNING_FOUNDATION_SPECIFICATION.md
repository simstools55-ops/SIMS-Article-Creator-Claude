# Article Learning Foundation Specification v1.0

Release: v0.7.1

## Scope
- Per-article Learning Record
- Human feedback confirmation
- Ten-record aggregation
- Asset-level change candidate routing

## Non-goals
- Claudeのモデル再訓練
- 会話を越えた無保証の自動保存
- KnowledgeやRuntimeの無承認自動変更

## Acceptance criteria
- 記事生成時にprovisional recordを出力
- 人間評価後にconfirmed recordを出力
- confirmed 10件だけを重複なしで集計
- 本文・秘密情報を学習記録に複製しない
