# SIMS Article Creator Contract v1.0

## 不変条件
1. `format`は`SIMS_ARTICLE_CREATOR_V1`。
2. 本文生成前にEditorial Briefを作成する。
3. 入力にない実体験を生成しない。
4. 根拠未確認の重要主張を断定しない。
5. `BLOCKED`でも分析結果と不足情報を返す。
6. JSONはスキーマに適合させる。
7. 人間向け出力とJSONのタイトル、見出し、公開判定を一致させる。

## 実行結果
すべての実行は、成功・警告・差戻し・停止のいずれでも構造化結果を返す。
