# CLOUD AOC-1 READ — session instructions (28-Sep-2026) — wave F02

Repo files: CLOUD_AOC1/PROMPT/PROMPT_V20_AOC1_FULLPRINT_INPUT.txt (the doctrine + output schema; read ONCE in full) and
CLOUD_AOC1/F02/BATCH_F02_INPUT.tsv (25 carve PDFs, 1-5 pages each; columns: agent, cin, filer_name, pdf, expected_part_a_rows, pages, output_json).

TOKEN DISCIPLINE — these carves are tiny; do not explore:
1. Launch exactly 5 sub-agents (A01..A05); each gets the rows whose `agent` column matches, in TSV order. Sub-agents may use ONLY Read (the carve PDF pages) and Write (the JSON). No Bash/Python/OCR/web/grep/TOC hunting/sub-sub-agents; never re-read a page.
2. Per carve, the sub-agent's task message is: "FILER: <filer_name> | CIN: <cin> | FILE: <pdf> | expected Part A rows: <n>". Read every page of that PDF once, then Write ONE JSON object — the prompt's §5 schema — to the `output_json` path. ONE JSON PER COMPANY, never combined. In "filer" add "input_filer_name" and "input_cin" (from the TSV) beside "name_as_printed"/"cin_as_printed" (from the page); if they disagree, say so in completion.sr_sequence_note.
3. If part_a_rows_emitted < expected_part_a_rows, re-check the pages (spreads, transposed columns, continuation pages) before finishing; a real difference is recorded, never padded.
4. No prose between carves; the sub-agent's final message = one line per carve: cin | filer | part_a_count_printed | rows_emitted | format_class | truncated.
5. Main session, after all sub-agents finish: git add CLOUD_AOC1/F02/*_OUTPUT.json ; git commit -m "AOC1 F02 outputs" ; git push origin aoc1/F02. One commit. Stop.
6. MODEL: this session and every sub-agent run on Fable (claude-fable-5-1). Each JSON must add "completion.model_used": the exact model id you are running as, and "completion.read_mode": "visual page read, Read tool". A JSON without model_used is rejected.
7. Never edit the PDFs, the prompt or the TSV. null / NOT_FOUND where the page prints nothing; nothing invented.
