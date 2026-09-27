# CLOUD SWEEP SLICE S21 - 25 PARENTS (27-Sep-2026)
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
### TOYAM SPORTS LIMITED
CIN L74110MH1985PLC285384 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74110MH1985PLC285384__TOYAM SPORTS LIMITED
Expected foreign subs (1): Pacific Star Sports Services L.L.C.

### SOUTH ASIAN ENTERPRISES LIMITED
CIN L91990UP1990PLC011753 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L91990UP1990PLC011753__SOUTH ASIAN ENTERPRISES LIMITED
Expected foreign subs (1): CHAI THELA PRIVATE LIMITED

### NET AVENUE TECHNOLOGIES LIMITED
CIN L72900TN2001PLC047220 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72900TN2001PLC047220__NET AVENUE TECHNOLOGIES LIMITED
Expected foreign subs (1): Cbazaar.com Inc

### FAZE THREE LIMITED
CIN L99999DN1985PLC000197 | NSE FAZE3Q | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L99999DN1985PLC000197__FAZE THREE LIMITED
Expected foreign subs (1): Faze Three US LLC

### DR. AGARWAL'S HEALTH CARE LIMITED
CIN L85100TN2010PLC075403 | NSE AGARWALEYE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L85100TN2010PLC075403__DR. AGARWAL'S HEALTH CARE LIMITED
Expected foreign subs (1): Orbit Health Care Services (Mauritius) Limited

### SILLY MONKS ENTERTAINMENT LIMITED
CIN L92120TG2013PLC090132 | NSE SILLYMONKS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://sillymonks.com/financials-of-subsidiary-companys
TARGET FOLDER: L92120TG2013PLC090132__SILLY MONKS ENTERTAINMENT LIMITED
Expected foreign subs (1): DREAM BOAT ENTERTAINMENT LLC

### BOMBAY METRICS SUPPLY CHAIN LIMITED
CIN L74999MH2015PLC263148 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74999MH2015PLC263148__BOMBAY METRICS SUPPLY CHAIN LIMITED
Expected foreign subs (1): METRICS VIETNAM COMPANY LIMITED

### BLUE CLOUD SOFTECH SOLUTIONS LIMITED
CIN L72200TG1991PLC013135 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200TG1991PLC013135__BLUE CLOUD SOFTECH SOLUTIONS LIMITED
Expected foreign subs (1): IT Corpz INC

### SUPREME INFRASTRUCTURE INDIA LIMITED
CIN L74999MH1983PLC029752 | NSE SUPREMEINF | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74999MH1983PLC029752__SUPREME INFRASTRUCTURE INDIA LIMITED
Expected foreign subs (1): SUPREME INFRASTRUCTURE OVERSEAS LLC

### INDOGULF CROPSCIENCES LIMITED
CIN L74899DL1993PLC051854 | NSE IGCL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74899DL1993PLC051854__INDOGULF CROPSCIENCES LIMITED
Expected foreign subs (1): Indogulf Cropsciences Australia PTY Ltd.

### LYKIS LIMITED
CIN L74999MH1984PLC413247 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74999MH1984PLC413247__LYKIS LIMITED
Expected foreign subs (1): Lykis Export LLC

### B.A.G. FILMS AND MEDIA LIMITED
CIN L74899DL1993PLC051841 | NSE BAGFILMS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74899DL1993PLC051841__B.A.G. FILMS AND MEDIA LIMITED
Expected foreign subs (1): BAG Network Limited

### MICROPRO SOFTWARE SOLUTIONS LIMITED
CIN L72200MH1996PLC102385 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200MH1996PLC102385__MICROPRO SOFTWARE SOLUTIONS LIMITED
Expected foreign subs (1): Microsync Information Technology Co. L.L.C.

### URAVI DEFENCE AND TECHNOLOGY LIMITED
CIN L84220MH2004PLC145760 | NSE URAVIDEF | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L84220MH2004PLC145760__URAVI DEFENCE AND TECHNOLOGY LIMITED
Expected foreign subs (1): Bharat Technology Limited

### VALECHA ENGINEERING LIMITED
CIN L74210MH1977PLC019535 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74210MH1977PLC019535__VALECHA ENGINEERING LIMITED
Expected foreign subs (1): Valecha International FZE

### Aries Agro Limited (Cn)
CIN L99999MH1969PLC014465 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://ariesagro.com/investors-agm-information/
TARGET FOLDER: L99999MH1969PLC014465__ARIES AGRO LIMITED (CN)
Expected foreign subs (1): Golden Harvest Middle East FZC

### GREAVES COTTON LIMITED
CIN L99999MH1922PLC000987 | NSE GREAVESCOT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://greavescotton.com/wp-content/uploads/2025/07/
TARGET FOLDER: L99999MH1922PLC000987__GREAVES COTTON LIMITED
Expected foreign subs (1): Greaves Technologies Inc.

### FIDEL SOFTECH LIMITED
CIN L72200PN2004PLC020061 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200PN2004PLC020061__FIDEL SOFTECH LIMITED
Expected foreign subs (1): Fidelsoft Inc

### NIRMITEE ROBOTICS INDIA LIMITED
CIN L74999MH2016PLC284731 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74999MH2016PLC284731__NIRMITEE ROBOTICS INDIA LIMITED
Expected foreign subs (1): Nirmitee Robotics AC Maintenance LLC

### VIRINCHI LIMITED
CIN L72200TG1990PLC011104 | NSE VIRINCHI | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.virinchi.com/subsidiaryReports.php
TARGET FOLDER: L72200TG1990PLC011104__VIRINCHI LIMITED
Expected foreign subs (1): KSoft Systems Inc

### WINDSOR MACHINES LIMITED
CIN L99999GJ1963PLC168458 | NSE WINDMACHIN | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L99999GJ1963PLC168458__WINDSOR MACHINES LIMITED
Expected foreign subs (1): Wintal Machines

### R S SOFTWARE (INDIA) LTD.
CIN L72200WB1987PLC043375 | NSE RSSOFTWARE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: http://www.rssoftware.com/home/investors
TARGET FOLDER: L72200WB1987PLC043375__R S SOFTWARE (INDIA) LTD.
Expected foreign subs (1): Responsive Solutions, INC.

### MUKAND LIMITED
CIN L99999MH1937PLC002726 | NSE MUKANDLTD | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L99999MH1937PLC002726__MUKAND LIMITED
Expected foreign subs (1): MUKAND INTERNATIONAL FZE

### DEE DEVELOPMENT ENGINEERS LIMITED
CIN L74140HR1988PLC030225 | NSE DEEDEV | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.deepiping.com/financial-reports.php
TARGET FOLDER: L74140HR1988PLC030225__DEE DEVELOPMENT ENGINEERS LIMITED
Expected foreign subs (1): DEE Piping Sy s t ems (Thailand) Co., Ltd.

### TIL LIMITED
CIN L74999WB1974PLC041725 | NSE TIL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74999WB1974PLC041725__TIL LIMITED
Expected foreign subs (1): TIL OVERSEAS PTE LTD
