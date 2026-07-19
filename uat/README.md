# UAT Prototype Guide

## 目的
v0.6.0が、メインキーワードからEditorial Brief、Pattern選択、構成、本文、品質判定、JSONまで一貫して生成できるかを確認する。

## Claude Project設定
1. Claude用ZIPを解凍する。
2. `PROJECT_INSTRUCTIONS.md`をClaude Project Instructionsへ設定する。
3. `knowledge/`、`patterns/`、`runtime/`、`contracts/`、`templates/`、`uat/`をProject Filesへ登録する。
4. SIMS WriterのProjectへは登録しない。

## 1記事の試験
1. `UAT_REQUEST_TEMPLATE.md`へ入力する。
2. Claudeの回答全文を保存する。
3. `UAT_EVALUATION_SHEET.md`で人手評価する。
4. JSONを `tests/contract/validate_contract.py` で確認する。
5. `EDITORIAL_LEARNING_RECORD_TEMPLATE.json`へ指摘を記録する。

## 合格目安
- 重大な捏造: 0
- Contract違反: 0
- Primary Pattern誤選択: 0
- 必須論点の重大欠落: 0
- 公開判定と実際の品質が矛盾しない
