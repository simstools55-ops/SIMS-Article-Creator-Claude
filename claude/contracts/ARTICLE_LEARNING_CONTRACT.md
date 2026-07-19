# Article Learning Contract v1.0

## Per-article format
- format: SIMS_ARTICLE_LEARNING_RECORD_V1
- record_version: 1.0.0
- record_status: PROVISIONAL | CONFIRMED
- execution_id: Article Creator JSONと一致
- article_id: 任意。未指定時はexecution_idを使用
- generated_at: YYYY-MM-DD
- article_context: keyword / article_type / monetization / platform / blog_profile_id
- system_evaluation: publication_status / overall_score / warnings / successful_elements / suspected_defects
- human_review: publish_ready / published / manual_edit_minutes / edit_level / edited_components / reviewer_notes
- diagnosis: confirmed_defects / root_cause_candidates / recommended_changes

## Batch format
- format: SIMS_ARTICLE_LEARNING_REPORT_V1
- report_version: 1.0.0
- batch_size: 10
- source_record_ids: exactly 10 unique confirmed records
- metrics / recurring_defects / successful_patterns / change_candidates / next_uat_focus

## Validation rules
1. PROVISIONALではhuman_reviewの未確認値をnullとする。
2. CONFIRMEDにはpublish_readyとmanual_edit_minutesを必須とする。
3. edit_levelはNONE | MINOR | MODERATE | MAJOR | REWRITE。
4. root_cause targetはPROJECT_INSTRUCTIONS | RUNTIME | KNOWLEDGE | PATTERN | CONTRACT | TEMPLATE | INPUT_DATA | NONE。
5. 10件レポートはCONFIRMEDのみを集計する。
6. 同一execution_idの重複集計を禁止する。
7. 記事本文、認証情報、個人情報、完全なアフィリエイトURLを保存しない。
