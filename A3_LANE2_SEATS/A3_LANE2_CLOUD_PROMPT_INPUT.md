# A3 LANE 2 — UNSEATED 275 — cloud ownership verification (28-Sep-2026)

Blocks: `A3_LANE2_SEATS/BLOCK01..11_INPUT.csv` (25 rows each). Each row is an Indian company that sits in the MASTERGROUP spine without a house. Columns: CIN, NAME, current label PROMOTER_GROUP, IMM_NAME, LABEL_HOUSE_UID / REGISTER_HOUSE_UID (candidate houses), REGISTER_EDGES (which spine house declared it as a related party and how), SHP_HOLDERS (shareholders on file, FY), MGT (group declarations), PROPOSAL, SHP_vs_LABEL, SHP_vs_REGISTER (internal agreement flags).

## Task per row — WebSearch / WebFetch only (registries return 403 from cloud; use bing/google cached snippets, thecompanycheck, tofler, falconebiz, company sites, parent annual reports, exchange filings, CCI orders, rating rationales, reputable press)
1. Status today: active / amalgamated / struck off / liquidated / renamed to X. Cite URL.
2. Who owns it in 2025-2026: parent (%), or JV partners (%), or standalone Indian promoter. Say whether that owner belongs to the house named in REGISTER_EDGES / PROMOTER_GROUP.
3. TWO independent URLs actually fetched per row for any CONFIRM / OTHER_HOUSE verdict. One URL = UNVERIFIED. Owner facts must be dated 2025-2026; older facts are noted but do not confirm.
4. Never infer from the name or from the register edge alone. Never write a URL you did not fetch.

## Output — append after EVERY row: `A3_LANE2_SEATS/BLOCK<NN>_EVIDENCE_OUTPUT.csv`
CIN,NAME,OWNER_2026,OWNER_PCT,OWNER_CIN_OR_ID,SEAT_VERDICT,PROPOSED_HOUSE_UID,URL1,QUOTE1,URL2,QUOTE2,ASOF,STATUS_2026,CONFIDENCE,NOTE
SEAT_VERDICT in {CONFIRM_LABEL, CONFIRM_REGISTER, OTHER_HOUSE, JV_5050, STANDALONE_INDIAN_PROMOTER, RETIRED, UNVERIFIED}.
Work block by block in order (BLOCK01 holds the conflicts). Commit + push after every block: `git add A3_LANE2_SEATS && git commit -m "A3 lane2 block NN" && git push`. Log "Saved k/25" after each row. No sub-agents. Final report: counts per SEAT_VERDICT per block and every row whose verdict contradicts PROPOSAL.
