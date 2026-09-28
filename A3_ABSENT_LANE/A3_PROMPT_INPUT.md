# A3 ABSENT-COUNTERPARTY LANE — cloud evidence pull (28-Sep-2026)

Worklist: `A3_ABSENT_LANE/A3_LANE3_TRULY_ABSENT_4330_CLOUD_WORKLIST_20260928_INPUT.csv` (4,330 Indian companies/LLPs named as related parties by spine houses but absent from the spine).
Columns: ABSENT_CIN, ABSENT_NAME, REGISTER_EDGES (which spine house X declared it, relationship), SHP_HOLDERS (its own shareholders, FY), SHP_HOLDS_IN (spine companies it holds shares in), MGT (MGT-7 group declarations).

## Task per row (WebSearch/WebFetch only; no shell network tricks; registries 403 from cloud — use press, company sites, exchange filings, rating rationales, tofler/zaubacorp cached snippets)
1. Confirm the company exists under this name today: current status (active / amalgamated / struck off / liquidated / renamed to X). Cite URL.
2. Find the CURRENT (2025-2026) ownership relationship to the declaring house in REGISTER_EDGES: subsidiary (%), JV (partners %), associate (%), promoter-group company, or NO CURRENT RELATIONSHIP (deal exited / only a customer-vendor RPT). Cite at least TWO independent URLs (company site, annual report/AOC-1 page, exchange filing, CCI order, rating rationale, reputable press). One URL = UNVERIFIED.
3. If the house is not the owner, name the actual owner/promoter and cite.
4. Never infer from the name or from the register edge alone. Never invent URLs; only URLs actually fetched.

## Output (append-only, write after EVERY row): `A3_ABSENT_LANE/A3_EVIDENCE_CLOUD_<run>_OUTPUT.csv`
ABSENT_CIN, ABSENT_NAME, STATUS_2026, RENAMED_TO, RELATION_TO_HOUSE (SUB/JV/ASSOCIATE/PROMOTER_GROUP/NONE/UNVERIFIED), PCT, HOUSE_UID, ACTUAL_OWNER, SOURCE_URL_1, QUOTE_1, SOURCE_URL_2, QUOTE_2, ASOF_DATE, CONFIDENCE (HIGH/MED/LOW), NOTE
Work in blocks of 25 rows, commit + push after every block (`git add A3_ABSENT_LANE && git commit -m "A3 block N" && git push`). Start with rows where HAS_MGT or HAS_SHP_HOLDS_IN is True (strongest internal lead), then the rest in file order. Log "Saved X/4330" after each row.
