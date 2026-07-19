# Knowledge Load Runtime

## Step K0 Manifest validation
Manifest format、重複ID、ファイル存在、statusを確認する。

## Step K1 Core load
K-POLICY、K-INTENT、K-READER、K-HELPFUL、K-COVERAGE、K-SEO、K-READABILITY、K-EEATをロードする。

## Step K2 Conditional load
YMYL、time-sensitive claims、internal links、monetizationの入力条件に応じて追加する。

## Step K3 Precedence
KNOWLEDGE_PRECEDENCEに従って競合を解決する。

## Step K4 Runtime binding
- Intent/Reader/Coverage → Editorial Brief
- Evidence/Freshness/Safety → Evidence PlanとPublication Gate
- Helpful/SEO/Readability/Originality → DraftとEditorial Review
- Links/Monetization → Article Blueprintと最終監査

## Step K5 Audit
適用Knowledge ID、警告、未解決競合を記録する。未解決の重大競合はNEEDS_REVISION以上とする。
