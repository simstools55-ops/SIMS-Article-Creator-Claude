from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[2]
required=[
 root/'claude/runtime/ARTICLE_LEARNING_RUNTIME.md',
 root/'claude/contracts/ARTICLE_LEARNING_CONTRACT.md',
 root/'claude/templates/ARTICLE_LEARNING_RECORD_TEMPLATE.json',
 root/'claude/templates/ARTICLE_LEARNING_REPORT_TEMPLATE.json',
 root/'uat/UAT_HUMAN_FEEDBACK_TEMPLATE.md'
]
missing=[str(p) for p in required if not p.exists()]
if missing:
 print('MISSING', *missing, sep='\n'); sys.exit(1)
r=json.loads((root/'claude/templates/ARTICLE_LEARNING_RECORD_TEMPLATE.json').read_text(encoding='utf-8'))
b=json.loads((root/'claude/templates/ARTICLE_LEARNING_REPORT_TEMPLATE.json').read_text(encoding='utf-8'))
assert r['format']=='SIMS_ARTICLE_LEARNING_RECORD_V1'
assert r['record_status']=='PROVISIONAL'
assert b['format']=='SIMS_ARTICLE_LEARNING_REPORT_V1' and b['batch_size']==10
inst=(root/'claude/PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
assert 'ARTICLE_LEARNING_RUNTIME.md' in inst and 'SIMS_ARTICLE_LEARNING_RECORD_V1' in inst
contract=(root/'claude/contracts/SIMS_ARTICLE_CREATOR_CONTRACT.md').read_text(encoding='utf-8')
assert '1.2.0' in contract
print('Learning Foundation validation: PASS')
