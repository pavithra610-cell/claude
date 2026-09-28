# A3 Lane 2 — Unseated 275: Ownership Verification Report

_Run date: 28-Sep-2026 · Branch `claude/modest-cray-e8hgnk` · Evidence files: `BLOCK01..11_EVIDENCE_OUTPUT.csv` · CIN audit: `A3_LANE2_CIN_CHANGES.csv`_

## 1. Summary

| Metric | Value |
|---|---|
| Rows processed | 275 / 275 |
| Seated with a verdict (non-UNVERIFIED) | 212 (77%) |
| Still UNVERIFIED | 63 |
| RETIRED (struck off / amalgamated / liquidation / converted) | 66 |
| Verdicts contradicting PROPOSAL | 24 |
| CIN pairs audited | 18 (10 confirmed CIN changes, 3 likely state shifts, 1 name reuse, 4 source typos) |

## 2. SEAT_VERDICT counts per block

| Block | CONFIRM_LABEL | CONFIRM_REGISTER | OTHER_HOUSE | JV_5050 | STANDALONE_INDIAN_PROMOTER | RETIRED | UNVERIFIED |
|---|---|---|---|---|---|---|---|
| 01 | 9 | 2 | 1 | 0 | 1 | 7 | 5 |
| 02 | 5 | 4 | 1 | 1 | 6 | 4 | 4 |
| 03 | 5 | 4 | 1 | 3 | 3 | 3 | 6 |
| 04 | 3 | 8 | 1 | 0 | 3 | 1 | 9 |
| 05 | 5 | 5 | 1 | 0 | 3 | 7 | 4 |
| 06 | 4 | 7 | 0 | 0 | 0 | 9 | 5 |
| 07 | 5 | 4 | 0 | 1 | 0 | 10 | 5 |
| 08 | 6 | 3 | 0 | 0 | 1 | 8 | 7 |
| 09 | 6 | 3 | 1 | 2 | 5 | 3 | 5 |
| 10 | 3 | 5 | 0 | 2 | 0 | 6 | 9 |
| 11 | 5 | 4 | 0 | 1 | 3 | 8 | 4 |
| **Total** | **56** | **49** | **6** | **10** | **25** | **66** | **63** |

## 3. Rows whose verdict contradicts PROPOSAL

Rule: LABEL_HOUSE contradicted by CONFIRM_REGISTER/OTHER_HOUSE; REGISTER_HOUSE by CONFIRM_LABEL/OTHER_HOUSE/STANDALONE_INDIAN_PROMOTER; CONFLICT/AMBIGUOUS by OTHER_HOUSE.

| Blk | CIN | Company | Proposal | Reg UID | Verdict | Proposed UID | Owner 2026 | Conf |
|---|---|---|---|---|---|---|---|---|
| 01 | U34300HR2018PTC114745 | Padmini Vna Emission Control System Private Limited | AMBIGUOUS | 16163 | OTHER_HOUSE | 6791 | Bhandari family (Sonia/Rahoul Kabir Bhandari, VNA Business Holding Trust) | MEDIUM |
| 02 | U86100OD2023PTC043198 | Bhadrak Arogyacare Private Limited | REGISTER_HOUSE | 5729 | STANDALONE_INDIAN_PROMOTER | - | Omnilink Technology Pvt Ltd (Dora family, Bhubaneswar IT SI) 74%; Cygnus Medicare 26% | MEDIUM |
| 02 | U86100OD2023PTC043093 | Jharsuguda Arogyacare Private Limited | REGISTER_HOUSE | 5729 | STANDALONE_INDIAN_PROMOTER | - | Omnilink Technology Pvt Ltd (Dora family) 74%; Cygnus Medicare 26% | MEDIUM |
| 02 | U51101DL2007PTC169442 | Cross Border Imports Private Limited | REGISTER_HOUSE | 49664 | STANDALONE_INDIAN_PROMOTER | - | Vineet Malik 50%; Kunal Singhal 50% (per FY2025 shareholding); directors Dinesh Rastogi &  | MEDIUM |
| 02 | U26931PN2012PTC142852 | Glazium Facades Private Limited | REGISTER_HOUSE | 8432 | STANDALONE_INDIAN_PROMOTER | - | Ashish Parakh 79%, Namrata Ashish Parakh 16%, Angelika Tawade 5% (individuals, per FY2025  | MEDIUM |
| 02 | U73100DL1981PTC012796 | Natwaraj Health Care Private Limited | REGISTER_HOUSE | 14349 | STANDALONE_INDIAN_PROMOTER | - | Vibrant Incorporation LLP (Bajaj family) | LOW |
| 02 | U73100MH2010NPL265172 | Broadcast Audience Research Council | REGISTER_HOUSE | 1821 | OTHER_HOUSE | - | Not-for-profit joint industry body; members are Indian Broadcasting and Digital Foundation | HIGH |
| 02 | U25209DL2022PTC401008 | R P Autostyles Private Limited | REGISTER_HOUSE | 49382 | STANDALONE_INDIAN_PROMOTER | - | Rajan Gandhi 80 pct, Vimmi Gandhi 10 pct, Siddharth Gandhi 10 pct per FY2025 filing | MEDIUM |
| 03 | U35999MH2015PTC268155 | Yeoman Marine Services Private Limited | REGISTER_HOUSE | 6847 | STANDALONE_INDIAN_PROMOTER | - | Mishra family | LOW |
| 03 | U74899DL1989PTC037976 | Caryaire Equipments India Private Limited | REGISTER_HOUSE | 11778 | STANDALONE_INDIAN_PROMOTER | - | Maheshwari family (Prabha Maheshwari 75.16%, Sachin Maheshwari 11.26%, Shruti Maheshwari 6 | MEDIUM |
| 03 | U40106TG2020PTC141183 | Abc Renewable Energy (Rj-02) Private Limited | AMBIGUOUS | 49067 | OTHER_HOUSE | 49748 | ABC Renewable Energy Pvt Ltd (Brookfield) | MEDIUM |
| 03 | U52330GA2013PTC007202 | Cmm Arena Retails Private Limited | REGISTER_HOUSE | 4761 | STANDALONE_INDIAN_PROMOTER | - | Cosme Matias Menezes Pvt Ltd (100% per SHP_HOLDERS), a Menezes-family-run Goa liquor compa | MEDIUM |
| 04 | L45203MH2008PLC178061 | Kesar Terminals & Infrastructure Limited | REGISTER_HOUSE | 49194 | OTHER_HOUSE | - | Harsh Kilachand family / Kesar Corporation Private Limited / Kesar Enterprises Limited (pr | HIGH |
| 04 | U35300MH1947PTC005720 | Afl Private Limited | REGISTER_HOUSE | 490 | STANDALONE_INDIAN_PROMOTER | - | Guzder family (Cyrus, Farokh, Manek Guzder; Statira Wadia; Erangal Comtrade & Consultancy  | HIGH |
| 05 | U67100TN2004PTC116303 | Ntc Engineering Services Private Limited | REGISTER_HOUSE | 7580 | STANDALONE_INDIAN_PROMOTER | - | Madhavan family | LOW |
| 05 | L25202MH2004PLC145548 | Sellowrap Industries Limited | REGISTER_HOUSE | 7865 | STANDALONE_INDIAN_PROMOTER | - | Poddar family | MEDIUM |
| 05 | U72200KA1994PTC016628 | Greytip Software Private Limited | REGISTER_HOUSE | 7121 | OTHER_HOUSE | - | Girish Rowjee and Ahmed Sayeed Anjum (founders) plus Apax Partners via Dorain Acquisition  | MEDIUM |
| 08 | U34300DL1999PLC099507 | Track Components Limited | REGISTER_HOUSE | 13681 | STANDALONE_INDIAN_PROMOTER | - | Rattan Kapur and Sandeep Chandhok (promoters); shareholders Chanson Shipping and Packing C | MEDIUM |
| 09 | U72400KA1996PTC020367 | Automated Workflow Private Limited | REGISTER_HOUSE | 1178 | OTHER_HOUSE | - | Sapiens International Corporation N.V. / Sapiens Technologies (1982) India Private Limited | HIGH |
| 09 | U51909HR2022PTC107323 | Clapjoy Innovations Private Limited | REGISTER_HOUSE | 10966 | STANDALONE_INDIAN_PROMOTER | - | Neha Aggarwal 47.51% and Pooja Arya 18.83% (individual Indian promoters, combined 66.34%); | LOW |
| 09 | U26999OR1992PTC003209 | Sarvesh Refractories Private Limited | REGISTER_HOUSE | 2652 | STANDALONE_INDIAN_PROMOTER | - | Thanwas group entities and individual (Thanwas Investment Pvt Ltd 27.6%, Thanwas Commercia | MEDIUM |
| 11 | U18101DL2021PTC388977 | Design Cellars Private Limited | REGISTER_HOUSE | 15500 | STANDALONE_INDIAN_PROMOTER | - | Founders | LOW |
| 11 | U32111GJ2012PTC122338 | Inddusinc Exim Private Limited | REGISTER_HOUSE | 15500 | STANDALONE_INDIAN_PROMOTER | - | Kapasiawala family (promoters) | LOW |
| 11 | U17299KA2016PTC096551 | Fonte Fashions India Private Limited | REGISTER_HOUSE | 15500 | STANDALONE_INDIAN_PROMOTER | - | Kala family (promoters) | LOW |

**Pattern:** 22 of 24 contradictions are REGISTER_HOUSE proposals; most are cases where the register edge is a *downstream* JV/associate stake (the company invests in a foreign-group JV) mis-read as the group owning the company — e.g. AFL (ASL Aviation), Sellowrap (Kaneka), NTC Engineering (Jinmyung), Yeoman Marine (IMS), Sarvesh (Chosun), Flipkart 10–19% minority stakes.

## 4. Other notable findings

| Finding | Rows |
|---|---|
| Ownership changed in 2025-26 | Automated Workflow → Sapiens (Jul-2025); CriticaLog → Shadowfax (Feb-2025); Scopfy/TGPEL → Shriram Pistons (Dec-2024); SVA India exits Future Group JV (2026); Equiniti still Siris (Bullish deal pending) |
| Label/register houses that look like the same family (merge candidates) | 9954 & 33056 (Sujan); 6747 & 49522 (Uppal); 1422 contains both Kirloskar and Atmus sides |
| Source data errors | Honos Asset Holding SHP lists ICRA Ltd CIN for Sammaan Capital; 4 typo CINs (Apollo Afinitas, Tablespace, Team India Managers, Cleardrive); IQVIA Health Transformation Foundation = same company as the Pvt Ltd row (now under liquidation) |
| Under insolvency (CIRP) | Payabhi Payments, 4B Networks, parents Umang Realtech, Sare Realty, Future Enterprises |

## 5. Method & evidence standard

| Pass | Method | Notes |
|---|---|---|
| Pass 1 | 11 parallel agents, WebSearch + WebFetch | Session web-search cap (~200) exhausted early; zaubacorp / tofler / thecompanycheck return 403 |
| Pass 2 (recheck of 168 UNVERIFIED) | Direct fetch of falconebiz.com MCA-sourced pages for the company **and** its owner/edge companies; matched directors by DIN and corporate email domain; combined with internal SHP/MGT % | 2025-26 dated (last AGM 2025, page updated 2026). Two fetched URLs per CONFIRM/OTHER/JV verdict |
| CIN audit | Same state+year+ROC-number with different CIN; same name with different CIN | Verified on instafinancials / falconebiz previous-CIN fields |

**Caveats:** (1) Pass-2 confirmations rest on director/email overlap from one aggregator (two separate pages) plus the internal shareholding %, so most are MEDIUM confidence. (2) Every previous-pass value is kept inside NOTE as `[prev pass: …]`; no rows or evidence were deleted. (3) 63 rows remain UNVERIFIED where control could not be shown (multi-party JVs, blank names, LLPs not indexed, dormant filers).
