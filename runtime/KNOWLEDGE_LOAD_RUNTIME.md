# Knowledge Load Runtime v1.0.1

## Project Knowledge Binding
Knowledge資産はClaude Projectへ登録されたProject Knowledgeとして参照する。`knowledge/...`等の表記は論理識別名であり、ローカルファイルパスとしてopenしない。

## Step K0 Manifest validation
Project Knowledge内でManifest、重複ID、status、対応資産の存在を論理照合する。直接取得できない場合は一度再検索し、なお取得不能ならLOAD_WARNINGとして記録する。

## Step K1 Core load
K-POLICY、K-INTENT、K-READER、K-HELPFUL、K-COVERAGE、K-SEO、K-READABILITY、K-EEATを適用する。

## Step K2 Conditional load
YMYL、time-sensitive claims、internal links、monetizationの入力条件に応じて追加Knowledgeを適用する。

## Step K3 Precedence
Knowledge Precedenceに従って競合を解決する。

## Step K4 Runtime binding
- Intent/Reader/Coverage → Editorial Brief
- Evidence/Freshness/Safety → Evidence PlanとPublication Gate
- Helpful/SEO/Readability/Originality → DraftとEditorial Review
- Links/Monetization → Article Blueprintと最終監査

## Step K5 Fallback
個別Knowledgeを取得できない場合はProject Instructions内のSafety Core、Web Evidence Fallback、Editorial Opinion規則を必ず適用する。非YMYL記事では内部読込警告だけを理由に記事生成を停止しない。

## Step K6 Audit
適用Knowledge ID、警告、未解決競合を記録する。未解決の重大競合はNEEDS_REVISION以上とする。「資産が存在しない」と断定するのは、Project Knowledgeへの登録状況が明示的に確認できた場合に限る。
