# CLOUD SWEEP SLICE S06 - 25 PARENTS (27-Sep-2026)
This message is your standing instruction for the whole session, sent once; do not re-read it. Requires FULL network access in this environment; if a company site is unreachable, stop and say NETWORK BLOCKED rather than guessing from search. Work the parents in order, one at a time; commit each parent before starting the next.

# FETCH-ONLY BRIEF (OPTION A: you FIND and VERIFY links, the user's machine downloads) - 27-Sep-2026
You are a document locator for Indian listed companies. You read nothing for values and you upload nothing. For each parent you produce ONE manifest of verified direct URLs. The user's Mac downloads every URL you list into an external drive. A URL that does not open as the right PDF wastes that lane, so verify each one.

WHAT TO LOCATE, PER PARENT (scope per parent is given below):
1. ANNUAL REPORT FY26 = year ended 31-Mar-2026, published Jul-Sep 2026 (integrated or full annual report with audited statements). Only if FY26 is not published anywhere on the site, NSE or BSE: FY25, labelled FY25_FALLBACK. Never quarterly results, never an older year.
2. AOC-1 PAGE RANGE inside that report: open the PDF, find Form AOC-1 (Part A subsidiaries, Part B associates and joint ventures, usually an annexure to the Board's Report). Record the PDF page numbers first..last covering BOTH parts completely, and the printed Sr. No. range you saw. If the AOC-1 is a separate PDF on the site, list that PDF too.
3. SUBSIDIARY FINANCIAL STATEMENTS: every subsidiary, domestic and foreign, full-year FY26 (31-Mar-2026) or calendar 2025 (31-Dec-2025) as published under s.136 / LODR Reg 46. Standalone and consolidated where both exist. Only if the FY26 set is not published: FY25 set, labelled FY25_FALLBACK. Step-downs consolidated inside an intermediate holding have no separate PDF: record them in NOT_FOUND with reason CONSOLIDATED_IN_<holding>.

HOW TO WORK: you have WebFetch/WebSearch and curl (no click browser). Fetch the raw HTML of the subsidiary page and grep it for PDF/zip links - year tabs and accordions are usually all present in the HTML; if a page uses a ?year= GET selector, request each year. Zip archives: download, list, and record each member file. Use a browser User-Agent and the page as Referer for curl. Only if a host truly blocks every route mark SITE_BLOCKED. Try the KNOWN SUBS PAGE first; if dead or stale, search the site per the patterns below, then a web search '<parent> subsidiary financials 2025-26'. Open each candidate PDF and look at its first page: confirm entity name and period before listing it. Record the exact click path you used.

OUTPUT PER PARENT (print as fenced CSV blocks in your reply; nothing else is a deliverable):
MANIFEST_OUTPUT.csv columns: parent_cin, parent_name, doc_type (AR_FY26 | AR_FY25_FALLBACK | AOC1_SEPARATE_PDF | SUB_FS_FY26 | SUB_FS_CY2025 | SUB_FS_FY25_FALLBACK), entity_name_as_printed, country_if_shown, period_end_as_printed, url, source_page_url, file_name_suggested, verified (YES = opened and first page checked), note.
AOC1_PAGES_OUTPUT.csv columns: parent_cin, ar_url, aoc1_part, pdf_page_first, pdf_page_last, printed_sr_first, printed_sr_last, unit_line_as_printed.
NOT_FOUND_OUTPUT.csv columns: parent_cin, entity_name_expected, reason (NOT_ON_SITE | CONSOLIDATED_IN_<holding> | ONLY_FY25 | SITE_BLOCKED | OTHER), pages_checked.
CASE.md: 5-10 lines: site, pages opened, year selector behaviour, anything the downloader must know (login walls, viewer-only links, redirects).
File name convention for file_name_suggested: <ENTITY NAME AS PRINTED>__<period>__<standalone|consolidated>.pdf; the AR as AR_FY26.pdf.

HARD RULE ON ROWS: one MANIFEST row per FILE you actually opened (or per zip member you actually listed), never one row per expected subsidiary. If a zip holds 5 PDFs, the manifest has 5 rows for that zip, each with the exact member name in file_name_suggested; the expected subsidiaries that have no file go to NOT_FOUND. Do not invent zip entries or file names. A row with verified=YES for a file you did not open is a defect.

RULES: FY26 means 2025-26. A calendar-2025 subsidiary statement inside the FY26 set is correct, label it SUB_FS_CY2025. Do not claim absence after one page; check the subsidiary page, the annual report page, the Reg 46 page and the site search. Exact company identity by CIN and printed name, never by ticker guess. Do not open anything unrelated to these parents. Write results per parent as soon as that parent is finished, then move on.
## HOW LISTED INDIAN PARENTS PUBLISH THESE DOCUMENTS (our experience, Jun-Sep 2026 - use it, do not guess)
1. Annual report FY26 (year ended 31-Mar-2026): Investors > Annual Reports / Reports & Filings / Financial Information. The FY26 report was published Jul-Sep 2026 (AGM season). An integrated report is one PDF of 200-500 pages; the AOC-1 is inside it as an ANNEXURE to the Board's Report (Part A subsidiaries, Part B associates & JVs), often placed just before the standalone financial statements or just after the Board's Report. Some parents publish the Board's Report BODY separately - that body only references the annexure and has no table; keep looking for the annexure or the full report.
2. Subsidiary financial statements (Companies Act s.136 / SEBI LODR Reg 46(2)(s)): a dedicated page under Investors named 'Subsidiary Companies', 'Financial Statements of Subsidiaries', 'Subsidiaries Financials', 'Reg 46 Disclosures', 'Annual Accounts of Subsidiaries'. Layouts seen: (a) one PDF per subsidiary per year, listed under an FY2025-26 tab or accordion; (b) one combined 'Subsidiary Annual Report Volume I/II' PDF (Tech Mahindra style); (c) one 'Financial Statements of Subsidiary Companies FY2025-26' page with per-company links (Tata Steel style); (d) a zip archive of all subsidiary accounts; (e) a year drop-down where the default view is FY2024-25 - switch it to FY2025-26; (f) subsidiaries with a Dec-2025 calendar year end sit in the FY26 set - keep them, label period as printed.
3. A step-down that is itself consolidated in an intermediate holding (Motherson/SMRPBV style) has no separate statement; record it in NOT_FOUND with reason CONSOLIDATED_IN_<holding>.
4. The subsidiary page is frequently a different domain or subdomain (insights.techmahindra.com, ir.<company>.com, investors.<company>.com). NSE/BSE carry the annual report only, never subsidiary financials.
5. A 403 to a bare fetch usually clears with a browser User-Agent + Referer header via curl; a viewer page (e.g. /viewer?file=...) carries the real PDF URL in its query string or HTML.
6. Verify each saved file is a real PDF of the right entity and period by opening its first pages; a successful request is not a saved file.
7. Every PDF name on Drive keeps the site's file name, prefixed by the subsidiary name as printed on the page when the site name is a code.




## HAND-BACK (MANDATORY, replaces printing): commit your outputs to the repository this session has open (chocka123/hello-world).
Path per parent: `SAGE_CLOUD_SWEEP/<TARGET FOLDER>/MANIFEST_OUTPUT.csv`, `AOC1_PAGES_OUTPUT.csv`, `NOT_FOUND_OUTPUT.csv`, `CASE.md`. Commit after EVERY parent (`git add SAGE_CLOUD_SWEEP && git commit -m "sweep <SLICE> <CIN>" && git push`), on branch `sweep/<SLICE>`. Never commit a PDF. Never delete or rewrite another parent's folder. If push fails, retry once, then keep committing locally and say so in the final report. At the end print a one-line summary per parent (files found / expected subs / not found).

## THE PARENTS
### ALICON CASTALLOY LIMITED
CIN L99999PN1990PLC059487 | NSE ALICON | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.alicongroup.co.in/annual-reports/
TARGET FOLDER: L99999PN1990PLC059487__ALICON CASTALLOY LIMITED
Expected foreign subs (3): Illichmann Castalloy S.R.O; Illichmann Castalloy GmbH; Alicon Holding GmbH

### NILKAMAL LIMITED
CIN L25209DN1985PLC000162 | NSE NILKAMAL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://nilkamal.com/financials/
TARGET FOLDER: L25209DN1985PLC000162__NILKAMAL LIMITED
Expected foreign subs (3): Nilkamal Eswaran Plastics Private Limited; Nilkamal Crates and Bins - FZE; Nilkamal Eswaran Marketing Private Limited

### EDVENSWA ENTERPRISES LIMITED
CIN L62099TS1980PLC176617 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://edvenswaenterprises.com/Investors
TARGET FOLDER: L62099TS1980PLC176617__EDVENSWA ENTERPRISES LIMITED
Expected foreign subs (3): Edvenswa Tech Inc; Omni Networks INC; Seltosoft LLC

### COHANCE LIFESCIENCES LIMITED
CIN L24299MH2018PLC422236 | NSE COHANCE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.cohance.com/financial-info/
TARGET FOLDER: L24299MH2018PLC422236__COHANCE LIFESCIENCES LIMITED
Expected foreign subs (3): NJ Bio, Inc.; Cohance Lifesciences Inc; NJ Biotherapeutics, LLC

### ICRA LIMITED
CIN L74999DL1991PLC042749 | NSE ICRA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.icra.in/InvestorRelation/Index
TARGET FOLDER: L74999DL1991PLC042749__ICRA LIMITED
Expected foreign subs (3): ICRA Nepal Limited; ICRA Lanka Limited; ICRA Employees Welfare Trust

### BSEL ALGO LIMITED
CIN L99999MH1995PLC094498 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: http://www.bsel.com/shareholderinfo.htm
TARGET FOLDER: L99999MH1995PLC094498__BSEL ALGO LIMITED
Expected foreign subs (3): BSEL INFRASTRUCTURE REALTY FZE; BSEL INFRASTRUCTURE REALTY SDN BHD; BSEL WATERFRONT SDN BHD

### VISHNU CHEMICALS LIMITED
CIN L85200TG1993PLC046359 | NSE VISHNU | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://vishnuchemicals.com/investors/
TARGET FOLDER: L85200TG1993PLC046359__VISHNU CHEMICALS LIMITED
Expected foreign subs (3): Vchem Trading FZE; Vishnu South Africa (Pty) Ltd; VCHEM Global Inc

### SANCODE TECHNOLOGIES LIMITED
CIN L74900MH2016PLC280315 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.sancodetech.com/group-entities
TARGET FOLDER: L74900MH2016PLC280315__SANCODE TECHNOLOGIES LIMITED
Expected foreign subs (3): Zsolt Ventures LLC; Dhruva Advisors USA INC; Zsolt Venture LLC

### TEJAS NETWORKS LIMITED
CIN L72900KA2000PLC026980 | NSE TEJASNET | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.tejasnetworks.com/financial-information-quarterly-results.php/
TARGET FOLDER: L72900KA2000PLC026980__TEJAS NETWORKS LIMITED
Expected foreign subs (3): Tejas Communication Pte Ltd.; Saankhya Labs Inc.; Tejas Communications (Nigeria) Limited

### OIL INDIA LIMITED
CIN L11101AS1959GOI001148 | NSE OIL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L11101AS1959GOI001148__OIL INDIA LIMITED
Expected foreign subs (3): Oil India International B.V.; Oil India Sweden AB; Oil India International Pte. Ltd.

### SAHAJ SOLAR LIMITED
CIN L35105GJ2010PLC059713 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L35105GJ2010PLC059713__SAHAJ SOLAR LIMITED
Expected foreign subs (3): Sahaj Renewable Power Limited; Sahaj Renewable Energy Trading FCZO (UAE Entity); Sahaj Renewable Energy Trading FCZO

### REMUS PHARMACEUTICALS LIMITED
CIN L24232GJ2015PLC084536 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24232GJ2015PLC084536__REMUS PHARMACEUTICALS LIMITED
Expected foreign subs (3): Espee Global Holdings LLC; Relius Pharma S.R.L; Relius Pharmaceuticals LTDA

### BAJAJ HINDUSTHAN SUGAR LIMITED
CIN L15420UP1931PLC065243 | NSE BAJAJHIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.bajajhindusthan.com/bajaj_hindusthan_(Singapore)_Private_Limited.php
TARGET FOLDER: L15420UP1931PLC065243__BAJAJ HINDUSTHAN SUGAR LIMITED
Expected foreign subs (3): Bajaj Hindusthan (Singapore) Pte. Ltd., Singapore; PT. Batu Bumi Persada, Indonesia; PT. Jangkar Prima, Indonesia

### JAY SHREE TEA AND INDUSTRIES LIMITED
CIN L15491WB1945PLC012771 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://jayshreetea.in/corporate/investor-relation/
TARGET FOLDER: L15491WB1945PLC012771__JAY SHREE TEA AND INDUSTRIES LIMITED
Expected foreign subs (3): Kijura Tea Company Limited; Bondo Tea Estate; Birla Holdings Limited

### HandsOn Global Management (HGM) Limited
CIN L72200PN1989PLC014448 | NSE HGM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L72200PN1989PLC014448__HANDSON GLOBAL MANAGEMENT (HGM) LIMITED
Expected foreign subs (3): HOVS Holdings Limited; HOVS LLC; HOV Environment LLC

### KEI INDUSTRIES LIMITED
CIN L74899DL1992PLC051527 | NSE KEI | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.kei-ind.com/investor-relations/financial-performance/balance-sheet-of-subsidiary/
TARGET FOLDER: L74899DL1992PLC051527__KEI INDUSTRIES LIMITED
Expected foreign subs (3): KEI Cables Australia PTY LTD; KEI CABLES AUSTRALIA PTY LIMITED; KEI CABLES AUSTRALIA PTY LTD

### PRAMARA PROMOTIONS LIMITED
CIN L51909MH2006PLC164247 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L51909MH2006PLC164247__PRAMARA PROMOTIONS LIMITED
Expected foreign subs (3): Pramara Promotions Pvt Ltd-Hongkong; Pramara – NA INC; Pramara Promotions Private Limited

### BLISS GVS PHARMA LIMITED
CIN L24230MH1984PLC034771 | NSE BLISSGVS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.blissgvs.com/financial-subsidiaries
TARGET FOLDER: L24230MH1984PLC034771__BLISS GVS PHARMA LIMITED
Expected foreign subs (3): Bliss GVS International Pte. Limited; ASTERISK LIFESCIENCES LTD; Greenlife Bliss Healthcare Ltd

### APL APOLLO TUBES LIMITED
CIN L74899DL1986PLC023443 | NSE APLAPOLLO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://aplapollo.com/investors/financial-performance
TARGET FOLDER: L74899DL1986PLC023443__APL APOLLO TUBES LIMITED
Expected foreign subs (3): A P L Apollo Tubes Company L.L.C. (Company incorporated on December 7, 2022); APL Apollo company LLC; APL Apollo Tubes FZE

### DECCAN GOLD MINES LIMITED
CIN L51900MH1984PLC034662 | NSE DECNGOLD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://deccangoldmines.com/disclosure-under-regulation-46/
TARGET FOLDER: L51900MH1984PLC034662__DECCAN GOLD MINES LIMITED
Expected foreign subs (3): Avelum Partner LLC; Deccan Gold FZCO; Deccan Gold (Tanzania) Private Limited

### AARVI ENCON LIMITED
CIN L29290MH1987PLC045499 | NSE AARVI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://aarviencon.com/investors
TARGET FOLDER: L29290MH1987PLC045499__AARVI ENCON LIMITED
Expected foreign subs (3): Aarvi Encon Resources Limited, UK; Aarvi Encon FZE, UAE; Aarvi Energy Company, Saudi Arabia

### SWELECT ENERGY SYSTEMS LIMITED
CIN L93090TN1994PLC028578 | NSE SWELECTES | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.swelectes.com/pdf/financial-information/audited-accounts-of-subsidiary-companies/2020-21/
TARGET FOLDER: L93090TN1994PLC028578__SWELECT ENERGY SYSTEMS LIMITED
Expected foreign subs (3): SWELECT Energy Systems Pte. Limited , Singapore; SWELECT Energy Systems Pte. Limited , Singapore; SWELECT Inc, USA

### KANSAI NEROLAC PAINTS LIMITED
CIN L24202MH1920PLC000825 | NSE KANSAINER | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.nerolac.com/investors/subsidiaries-financial-statements.html
TARGET FOLDER: L24202MH1920PLC000825__KANSAI NEROLAC PAINTS LIMITED
Expected foreign subs (3): Kansai Nerolac Paints (Bangladesh) Limited; KNP Japan Pvt. Ltd.; Kansai Paints Lanka Private Limited

### MAX HEALTHCARE INSTITUTE LIMITED
CIN L72200MH2001PLC322854 | NSE MAXHEALTH | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.maxhealthcare.in/investors
TARGET FOLDER: L72200MH2001PLC322854__MAX HEALTHCARE INSTITUTE LIMITED
Expected foreign subs (3): Max Healthcare FZ-LLC; MHC Global Healthcare (Nigeria) Limited; MHC Global Healthcare (Nigeria) Limited

### SHAKTI PUMPS (INDIA) LIMITED
CIN L29120MP1995PLC009327 | NSE SHAKTIPUMP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://shaktipumps.com/subsidiary-results/
TARGET FOLDER: L29120MP1995PLC009327__SHAKTI PUMPS (INDIA) LIMITED
Expected foreign subs (3): Shakti Pumps LLC USA; Shakti Pumps FZE; Shakti Pumps Bangladesh Limited
