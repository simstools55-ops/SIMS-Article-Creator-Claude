# Article Learning Foundation

Article Learning Foundationは、実記事UATの人手修正結果を監査可能なJSONとして保存し、10記事ごとに製品改善候補を抽出する仕組みです。モデルの自動再学習ではありません。

## Records
- Provisional: 記事生成直後の自動評価
- Confirmed: 利用者の公開判定・修正時間・修正箇所を反映
- Batch Report: Confirmed 10件の集計

## Governance
変更候補は自動適用せず、対象資産・根拠件数・回帰リスクを示して承認を受けます。
