# Article Learning Runtime v1.0

## Purpose
実記事UATの結果を記事単位で構造化し、10件ごとに再発問題と成功パターンを集計する。記事生成品質を自己改変ではなく、監査可能な改善候補として蓄積する。

## Trigger
- 記事生成がR18まで完了したとき: provisional Learning Recordを生成する。
- ユーザーが公開可否、修正内容、修正時間を返したとき: confirmed Learning Recordへ更新する。
- confirmed recordが10件入力されたとき: Batch Learning Reportを生成する。

## Per-article workflow
1. article_id / execution_id / keyword / article_type / monetizationを記録。
2. 自動評価値をsystem_evaluationへ転記。
3. 初回はrecord_status=PROVISIONALとする。
4. human_reviewは未入力項目をnullにし、推測で埋めない。
5. ユーザー評価後はrecord_status=CONFIRMEDとし、manual_edit_minutes、publish_ready、edited_components、defectsを更新。
6. root_cause_candidatesをProject Instructions / Runtime / Knowledge / Patterns / Contract / Templates / Input Dataへ分類。
7. 記事本文・個人情報・アフィリエイトURL全文はLearning Recordに複製しない。識別に必要な最小情報だけを保持する。

## Ten-record aggregation
10件のCONFIRMED recordのみを正式集計対象とする。
- article type別件数と合格率
- 平均・中央値の人手修正時間
- defect codeの発生回数
- edited componentの発生回数
- successful elementの再現回数
- root cause target別の改善候補
- Priority A/B/C

Priority A: 10件中5件以上、または公開阻害が1件以上。
Priority B: 10件中2〜4件。
Priority C: 10件中1件、または観察継続。

## Safety and governance
- 1記事だけの印象でRuntimeやKnowledgeの変更を確定しない。
- 記録にない事実を補完しない。
- 学習はモデル再訓練ではなく、製品資産の改善候補抽出である。
- 自動適用は禁止。変更提案には対象ファイル、根拠件数、期待効果、回帰リスクを含める。

## Output
記事ごと: SIMS_ARTICLE_LEARNING_RECORD_V1 JSON
10記事ごと: SIMS_ARTICLE_LEARNING_REPORT_V1 JSON + 人間向け要約
