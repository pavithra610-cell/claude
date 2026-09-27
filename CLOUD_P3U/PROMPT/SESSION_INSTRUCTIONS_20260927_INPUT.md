# CLOUD P3U — Prompt 3 + V18/V17 read of subsidiary financial statements (27-Sep-2026)

You work ONE batch folder: CLOUD_P3U/<BATCH>/ (50 PDFs or fewer), laid out as CLOUD_P3U/<BATCH>/<PARENT FOLDER>/<file>.pdf,
with CLOUD_P3U/<BATCH>/BATCH_<BATCH>_INPUT.tsv listing READ_ID, parent folder, file, list name, parent name, parent CIN.

1. Read CLOUD_P3U/PROMPT/PROMPT3_PLUS_V18_V17_20260927_INPUT.md in full. It is the reading prompt for EVERY PDF.
2. Split the batch into groups of 5 PDFs and give each group to one sub-agent (so up to 10 sub-agents, run in parallel). Each sub-agent,
   for each of its PDFs, one at a time:
   - reads the WHOLE PDF (all pages; scanned pages visually) and answers exactly as the prompt specifies — ONE complete
     JSON object, every section, up to 64,000 output tokens; never truncate, never summarise sections away.
   - writes it immediately to CLOUD_P3U/<BATCH>/<PARENT FOLDER>/<same file name without .pdf>__P3_V18_V17_OUTPUT.json
     (same company folder as the PDF), then moves to the next PDF.
   Items for the prompt's "THIS ITEM" block: FILE, LIST TITLE AS PUBLISHED BY THE PARENT, SOURCE = company website
   subsidiary financials, LISTED INDIAN PARENT OF THE GROUP (name + CIN). The legal name inside the document governs.
   TWO-CURRENCY RULE (compulsory): some PDFs print the full financial statements twice, in two currencies (e.g. local
   currency AND INR/USD translated set, or side-by-side currency columns for every statement). Before reading numbers:
   - state in the JSON field "DUAL_CURRENCY_CHECK": {"present": YES/NO, "currencies_seen": [...], "pages_per_currency":
     {"<CCY>": "p.a-b", ...}, "currency_chosen": "<CCY>", "reason": "..."}.
   - if YES: pick ONE currency set (prefer the entity's own functional/reporting currency as signed by the auditor;
     if only one set is audited, take that one) and take EVERY number in the whole JSON from that one set only.
   - never mix values from the two sets (no revenue in one currency and profit in the other); every number keeps its
     page cite from the chosen set, and the denomination is stated once.
   WRITE-TO-DISK RULE (compulsory): the JSON for each PDF is written to disk the moment it is complete — before the
   next PDF is opened. A PDF with no JSON file on disk counts as NOT DONE. If a read fails, still write
   <file>__P3_V18_V17_OUTPUT.json containing {"status":"FAILED","reason":"..."} so nothing is silently skipped.
3. After every PDF: git add that JSON, commit, and push to the branch you are on (p3u/<BATCH>). Never delete or modify PDFs.
4. When all PDFs are done, write CLOUD_P3U/<BATCH>/BATCH_<BATCH>_STATUS_OUTPUT.csv (READ_ID, file, status DONE/FAILED,
   legal_name, country, period_end) and push. Then stop.
