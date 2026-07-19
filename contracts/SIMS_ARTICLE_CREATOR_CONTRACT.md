# SIMS Article Creator Contract v1.2

## 不変条件
1. formatはSIMS_ARTICLE_CREATOR_V1、contract_versionは1.2.0。
2. メインキーワード入力は記事生成Runtimeを開始する。
3. 本文生成前にEditorial BriefとMonetization判定を作成する。
4. 入力にない実体験を生成しない。
5. 事実、Editorial Opinion、User-provided Experienceを区分する。
6. 根拠未確認の重要主張を断定しない。
7. affiliate_url入力時はPR表記とリンク挿入を検証する。
8. body_markdownへ公開用完成記事全文を格納する。
9. 人間向け出力とJSONのタイトル、本文、リンク数、公開判定を一致させる。
10. BLOCKEDでも分析結果と不足情報を返す。

11. 記事生成完了時はSIMS_ARTICLE_LEARNING_RECORD_V1を別オブジェクトとして出力する。
12. Learning Recordに記事本文または秘密情報を複製しない。
