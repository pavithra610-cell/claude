# CLOUD SWEEP SLICE S20 - 25 PARENTS (27-Sep-2026)
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
### ALPS INDUSTRIES LIMITED
CIN L51109UP1972PLC003544 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L51109UP1972PLC003544__ALPS INDUSTRIES LIMITED
Expected foreign subs (1): ALPS USA Inc.

### DREAMFOLKS SERVICES LIMITED
CIN L51909DL2008PLC177181 | NSE DREAMFOLKS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://dreamfolks.in/financial
TARGET FOLDER: L51909DL2008PLC177181__DREAMFOLKS SERVICES LIMITED
Expected foreign subs (1): Dreamfolks Services PTE. Ltd.

### TARSONS PRODUCTS LIMITED
CIN L51109WB1983PLC036510 | NSE TARSONS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.tarsons.com/financial-reports/
TARGET FOLDER: L51109WB1983PLC036510__TARSONS PRODUCTS LIMITED
Expected foreign subs (1): Tarsons Life Science Pte. Ltd.

### COMFORT COMMOTRADE LIMITED
CIN L51311MH2007PLC175688 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L51311MH2007PLC175688__COMFORT COMMOTRADE LIMITED
Expected foreign subs (1): ANJALI TRADELINK FZE

### SHAILY ENGINEERING PLASTICS LIMITED
CIN L51900GJ1980PLC065554 | NSE SHAILY | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://shaily.com/investors/compliances-policies/shaily-uk-ltd-wholly-owned-subsidiary
TARGET FOLDER: L51900GJ1980PLC065554__SHAILY ENGINEERING PLASTICS LIMITED
Expected foreign subs (1): Shaily (UK) Limited

### STEELMAN TELECOM LIMITED
CIN L55101WB2003PLC096195 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: http://steelmantelecom.com/investors-relations.php
TARGET FOLDER: L55101WB2003PLC096195__STEELMAN TELECOM LIMITED
Expected foreign subs (1): STEELMAN INSTALLATION SERVICES PLC

### M LAKHAMSI INDUSTRIES LIMITED
CIN L51900MH1985PLC034994 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L51900MH1985PLC034994__M LAKHAMSI INDUSTRIES LIMITED
Expected foreign subs (1): Lakhamsi FZE

### BANG OVERSEAS LIMITED
CIN L51900MH1992PLC067013 | NSE BANG | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L51900MH1992PLC067013__BANG OVERSEAS LIMITED
Expected foreign subs (1): Bang HK Limited

### SPACE INCUBATRICS TECHNOLOGIES LIMITED
CIN L17100UP2016PLC084473 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L17100UP2016PLC084473__SPACE INCUBATRICS TECHNOLOGIES LIMITED
Expected foreign subs (1): SYBLY INTERNATIONAL FZE

### TRENT LIMITED
CIN L24240MH1952PLC008951 | NSE TRENT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://trentlimited.com/pages/subsidiary-financials
TARGET FOLDER: L24240MH1952PLC008951__TRENT LIMITED
Expected foreign subs (1): Trent Global Holdings Limited

### MAHANAGAR TELEPHONE NIGAM LIMITED
CIN L32101DL1986GOI023501 | NSE MTNL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.mtnl.in
TARGET FOLDER: L32101DL1986GOI023501__MAHANAGAR TELEPHONE NIGAM LIMITED
Expected foreign subs (1): Mahanagar Telephone (Mauritius) Limited

### MINDPOOL TECHNOLOGIES LIMITED
CIN L72900PN2011PLC138607 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.mindpooltech.com/investors
TARGET FOLDER: L72900PN2011PLC138607__MINDPOOL TECHNOLOGIES LIMITED
Expected foreign subs (1): Mindpool Technologies Inc.

### HITECH CORPORATION LIMITED
CIN L28992MH1991PLC168235 | NSE HITECHCORP | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.hitechgroup.com/investor/
TARGET FOLDER: L28992MH1991PLC168235__HITECH CORPORATION LIMITED
Expected foreign subs (1): Hitech Global Inc.

### DELAPLEX LIMITED
CIN L72900MH2004PLC144498 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72900MH2004PLC144498__DELAPLEX LIMITED
Expected foreign subs (1): Delaplex Software Limited

### PREVEST DENPRO LIMITED
CIN L85199JK1999PLC001969 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L85199JK1999PLC001969__PREVEST DENPRO LIMITED
Expected foreign subs (1): Axiodent INC.

### TRANSGENE BIOTEK LIMITED.
CIN L85195TG1990PLC011065 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L85195TG1990PLC011065__TRANSGENE BIOTEK LIMITED.
Expected foreign subs (1): Transgene Biotek HK Ltd

### DUCON INFRATECHNOLOGIES LIMITED
CIN L72900MH2009PLC191412 | NSE DUCON | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72900MH2009PLC191412__DUCON INFRATECHNOLOGIES LIMITED
Expected foreign subs (1): Ducon Combustion Equipments INC

### TECHKNOWGREEN SOLUTIONS LIMITED
CIN L90000PN2023PLC217501 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L90000PN2023PLC217501__TECHKNOWGREEN SOLUTIONS LIMITED
Expected foreign subs (1): Techknowgreen Solutions PTE LTD

### CYBER MEDIA (INDIA) LIMITED
CIN L92114DL1982PLC014334 | NSE CYBERMEDIA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L92114DL1982PLC014334__CYBER MEDIA (INDIA) LIMITED
Expected foreign subs (1): Cyber Media Services Pte. Ltd.*

### SYNGENE INTERNATIONAL LIMITED
CIN L85110KA1993PLC014937 | NSE SYNGENE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.syngeneintl.com/investors/share-holder-services/subsidiary-financials-fy-2023-24/
TARGET FOLDER: L85110KA1993PLC014937__SYNGENE INTERNATIONAL LIMITED
Expected foreign subs (1): Syngene USA Inc., USA

### ATHENA GLOBAL TECHNOLOGIES LIMITED
CIN L74140TG1992PLC014182 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://athenagt.com
TARGET FOLDER: L74140TG1992PLC014182__ATHENA GLOBAL TECHNOLOGIES LIMITED
Expected foreign subs (1): ATHENA GLOBAL TECHNOLOGIES INC

### INFOLLION RESEARCH SERVICES LIMITED
CIN L73100HR2009PLC126450 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L73100HR2009PLC126450__INFOLLION RESEARCH SERVICES LIMITED
Expected foreign subs (1): Infollion Research Services Corp

### RODIUM REALTY LIMITED
CIN L85110MH1993PLC206012 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://rodium.net/investor/
TARGET FOLDER: L85110MH1993PLC206012__RODIUM REALTY LIMITED
Expected foreign subs (1): Rodium Digital Inc

### SUN PHARMA ADVANCED RESEARCH COMPANY LIMITED
CIN L73100GJ2006PLC047837 | NSE SPARC | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L73100GJ2006PLC047837__SUN PHARMA ADVANCED RESEARCH COMPANY LIMITED
Expected foreign subs (1): SPARCLIFE Inc.

### MOBAVENUE AI TECH LIMITED
CIN L73100MP2010PLC023011 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L73100MP2010PLC023011__MOBAVENUE AI TECH LIMITED
Expected foreign subs (1): Mobavenue Global Holdings Limited
