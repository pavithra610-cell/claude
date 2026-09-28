# A3 Absent-Counterparty Lane — Run R1 Summary (paused 28-Sep-2026)

**Spec:** `A3_PROMPT_INPUT.md` · **Worklist:** `A3_LANE3_TRULY_ABSENT_4330_CLOUD_WORKLIST_20260928_INPUT.csv` (4,330 rows)
**Output:** `A3_EVIDENCE_CLOUD_R1_OUTPUT.csv` (combined) + `cloud_blocks/BLOCKNNN_OUTPUT.csv` (per block, originals kept)
**PR:** https://github.com/pavithra610-cell/claude/pull/2 (draft)

## 1. Progress

| Stage | Blocks | Rows | Status |
|---|---|---|---|
| HAS_MGT rows (priority set) | 001–077 | 1,914 | ✅ 100% done |
| Non-MGT rows | 078–095, 097 | 486 | ✅ done |
| Non-MGT, partial | 096 | 3 of 25 in block file (not merged) | ⏸ 22 rows to redo |
| Non-MGT, not started | 098–174 | 1,930 | ⏸ pending |
| **Total** | | **2,400 of 4,330 (55%)** | |

## 2. Results (2,400 rows in combined output)

| RELATION_TO_HOUSE | All | MGT rows | Non-MGT rows |
|---|---|---|---|
| PROMOTER_GROUP | 1,218 (51%) | 890 | 328 |
| ASSOCIATE | 383 (16%) | 355 | 28 |
| JV | 96 (4%) | 79 | 17 |
| SUB | 80 (3%) | 64 | 16 |
| NONE (exited / struck off / false link) | 69 (3%) | 55 | 14 |
| UNVERIFIED | 554 (23%) | 471 | 83 |

| CONFIDENCE | HIGH 287 (12%) | MED 1,464 (61%) | LOW 649 (27%) |
|---|---|---|---|

| STATUS_2026 | Active 2,063 · Struck off 52 · Amalgamated 50 · Liquidation/CIRP 20 · Converted 8 · Not found/other 207 |
|---|---|

## 3. Evidence rules applied (QC at merge)

| Rule | Effect |
|---|---|
| Two independent sources required; one URL = UNVERIFIED | per spec |
| Shared director / address / email alone ≠ ownership | → PROMOTER_GROUP, max MED, NOTE starts "DIRECTOR-OVERLAP ONLY" |
| PCT only when a source states it | internal MGT % moved to NOTE otherwise |
| Surname / name / brand match = name inference | → UNVERIFIED |
| Snippet-only sources | quote prefixed `[snippet]` |
| Min. 6 attempts before UNVERIFIED | NOTE ends `ATTEMPTS=n` |
| ~45 rows downgraded by merge-QC | each tagged `[MERGE-QC: …]` in NOTE |

## 4. User-approved fixes (all ✅)

| # | Fix | Result |
|---|---|---|
| 1 | Emami blocks 017/019 → RPT-disclosure evidence | 50 rows UNVERIFIED → PROMOTER_GROUP (all Active) |
| 2 | Status backfill 022–025 | 100/100 LLPs Active (indiafilings/addressadda) |
| 3 | Re-run low-effort UNVERIFIED (001–004, 009, 014, 029, 031, 034, 040, 041, 065, 066) | 163 rows re-checked, ~96 resolved |
| 4 | Jindal cluster (033) via DLF Towers lead | 7/7 → PROMOTER_GROUP |

All replacements logged in `cloud_blocks/RERUN_MERGE_LOG.csv` (320 entries); originals preserved in block files.

## 5. Side analyses

| File | Content |
|---|---|
| `A3_CIN_CHANGE_CHECK_R1.csv` | 27 CIN pairs: 17 same-company CIN changes (listing, PTC↔PLC, NIC, state shift, LLP), 6 blank names resolved, 1 different-company pair |
| `cloud_blocks/EMAMI_CLUSTER_EVIDENCE.csv` + `_SUMMARY.md` | 330 entities from Emami Realty Reg.23(9) RPT disclosures |
| `cloud_blocks/EMAMI_STATUS_BACKFILL_P1/P2.csv` | MCA status + designated partners for 100 Emami LLPs |

## 6. Data-quality flags for upstream

- Register edges pointing the **wrong direction** (absent co. holds the house, not vice-versa): e.g. Repro Enterprises, Patnaik Minerals, Zep Infratech, Paschim Chemicals/Mexin, Amisco Agro-Chem, Allen Infrastructures.
- **Stale** edges (stake sold/diluted/amalgamated): e.g. Bourton Consulting, Ashoka Sambalpur Tollway, Pankaj Polymers, Bigwin Buildsys, Athmar India, Fine Papyrus, Devansh/Godhuli LLPs, Walwhan SPVs (→ Tata Power), Welspun Urja.
- **CIN/name mismatches**: Current Technologies (≠ Redington's Currents Technology Retail), Asia Pacific Risk Mgmt (CIN = unrelated struck-off co.), Fiestta Fab, Tripura IDC, Hindustan Max-GB (Delhi CIN), Jangalpur Properties, Green Top Hotels.
- **Red flag**: house 26765 Grand Oak Canyons Distillery — dormant listed shell with ₹945cr→₹3,095cr "investments" jump; its 7 declared associates link only to each other.

## 7. Resume checklist

1. Block 096: redo 22 remaining rows (3 already in block file).
2. Blocks 098–174 (1,930 non-MGT rows), ~6 agents at a time (WebSearch quota is shared across concurrent agents; prefer direct fetch of indiafilings `/search/<slug>-cin-<CIN>` or `<slug>-llp-<LLPIN>`).
3. Optional re-runs of search-starved UNVERIFIED rows: 073 (5), 077 (4), 078 (13), 080 (2), 082 (1), 088 (1), 095 (1).
