# CLOUD SWEEP SLICE S16 - 25 PARENTS (27-Sep-2026)
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
### PRATHAM EPC PROJECTS LIMITED
CIN L45200GJ2014PLC081119 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45200GJ2014PLC081119__PRATHAM EPC PROJECTS LIMITED
Expected foreign subs (1): Pratham International Contracting LLC-OPC

### SWAN CORP LIMITED
CIN L17100MH1909PLC000294 | NSE SWANCORP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L17100MH1909PLC000294__SWAN CORP LIMITED
Expected foreign subs (1): Wilson Corporation FZE

### KOTHARI PRODUCTS LIMITED.
CIN L16008UP1983PLC006254 | NSE KOTHARIPRO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.kothariproducts.in/financialresults.htm
TARGET FOLDER: L16008UP1983PLC006254__KOTHARI PRODUCTS LIMITED.
Expected foreign subs (1): Kothari Products Singapore Pte. Limited

### GODFREY PHILLIPS INDIA LIMITED
CIN L16004MH1936PLC008587 | NSE GODFRYPHLP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L16004MH1936PLC008587__GODFREY PHILLIPS INDIA LIMITED
Expected foreign subs (1): Godfrey Phillips Middle East, DMCC

### AVANTI FEEDS LIMITED
CIN L16001AP1993PLC095778 | NSE AVANTIFEED | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L16001AP1993PLC095778__AVANTI FEEDS LIMITED
Expected foreign subs (1): Sealuxe B.V.

### K G DENIM LIMITED
CIN L17115TZ1992PLC003798 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: http://www.kgdenim.com/wp-content/uploads/2017/08/
TARGET FOLDER: L17115TZ1992PLC003798__K G DENIM LIMITED
Expected foreign subs (1): KG DENIM (USA) INC

### SHREE GANESH REMEDIES LIMITED
CIN L24230GJ1995PLC025661 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24230GJ1995PLC025661__SHREE GANESH REMEDIES LIMITED
Expected foreign subs (1): SGRL USA Inc.

### VST TILLERS TRACTORS LIMITED
CIN L34101KA1967PLC001706 | NSE VSTTILLERS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L34101KA1967PLC001706__VST TILLERS TRACTORS LIMITED
Expected foreign subs (1): VST Americas Inc.

### K.P.R. MILL LIMITED
CIN L17111TZ2003PLC010518 | NSE KPRMILL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.kprmilllimited.com/financial-result-subsidiary-cos
TARGET FOLDER: L17111TZ2003PLC010518__K.P.R. MILL LIMITED
Expected foreign subs (1): KPR EXPORTS PLC

### KAVERI SEED COMPANY LTD.
CIN L01120TG1986PLC006728 | NSE KSCL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.kaveriseeds.in/investors/subsidiaries-financials/
TARGET FOLDER: L01120TG1986PLC006728__KAVERI SEED COMPANY LTD.
Expected foreign subs (1): KAVERI SEED COMPANY BANGLADESH PRIVATE LIMITED

### Bil Vyapar Limited
CIN L24117WB1962PLC025584 | NSE BILVYAPAR | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24117WB1962PLC025584__BIL VYAPAR LIMITED
Expected foreign subs (1): GLOBAL COMPOSITE HOLDINGS INC

### VINATI ORGANICS LIMITED
CIN L24116MH1989PLC052224 | NSE VINATIORGA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://vinatiorganics.com/investors-home/
TARGET FOLDER: L24116MH1989PLC052224__VINATI ORGANICS LIMITED
Expected foreign subs (1): VINATI ORGANICSUSA INC

### PARAG MILK FOODS LIMITED
CIN L15204PN1992PLC070209 | NSE PARAGMILK | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.paragmilkfoods.com/investors.php
TARGET FOLDER: L15204PN1992PLC070209__PARAG MILK FOODS LIMITED
Expected foreign subs (1): Parag Foods Middle East FZE

### SUVEN LIFE SCIENCES LIMITED
CIN L24110TG1989PLC009713 | NSE SUVEN | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: http://www.suven.com/subsidiaryaccounts.aspx
TARGET FOLDER: L24110TG1989PLC009713__SUVEN LIFE SCIENCES LIMITED
Expected foreign subs (1): Suven Neurosciences Inc.,

### SUMITOMO CHEMICAL INDIA LIMITED
CIN L24110MH2000PLC124224 | NSE SUMICHEM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://sumichem.co.in/investors-relations.php
TARGET FOLDER: L24110MH2000PLC124224__SUMITOMO CHEMICAL INDIA LIMITED
Expected foreign subs (1): Excel Crop Care (Africa) Limited

### AEROFLEX INDUSTRIES LIMITED
CIN L24110MH1993PLC074576 | NSE AEROFLEX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.aeroflexindia.com/investor-relation/
TARGET FOLDER: L24110MH1993PLC074576__AEROFLEX INDUSTRIES LIMITED
Expected foreign subs (1): Aeroflex Industries Limited - U.K

### SADHANA NITRO CHEM LIMITED
CIN L24110MH1973PLC016698 | NSE SADHNANIQ | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24110MH1973PLC016698__SADHANA NITRO CHEM LIMITED
Expected foreign subs (1): Anuchem BVBA

### THEMIS MEDICARE LIMITED
CIN L24110GJ1969PLC001590 | NSE THEMISMED | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24110GJ1969PLC001590__THEMIS MEDICARE LIMITED
Expected foreign subs (1): Carpo Medical Limited

### CONCORD BIOTECH LIMITED
CIN L24230GJ1984PLC007440 | NSE CONCORDBIO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24230GJ1984PLC007440__CONCORD BIOTECH LIMITED
Expected foreign subs (1): Stellon Biotech Inc

### LIBAS CONSUMER PRODUCTS LIMITED
CIN L18101MH2004PLC149489 | NSE LIBAS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L18101MH2004PLC149489__LIBAS CONSUMER PRODUCTS LIMITED
Expected foreign subs (1): LIBAS DESIGNS FZE LLC

### SALZER ELECTRONICS LIMITED
CIN L03210TZ1985PLC001535 | NSE SALZERELEC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L03210TZ1985PLC001535__SALZER ELECTRONICS LIMITED
Expected foreign subs (1): Salzer Electronics (Arabia) Limited

### ROSSELL INDIA LIMITED
CIN L01132WB1994PLC063513 | NSE ROSSELLIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L01132WB1994PLC063513__ROSSELL INDIA LIMITED
Expected foreign subs (1): Rossell Techsys Inc. USA

### CIAN AGRO INDUSTRIES & INFRASTRUCTURE LIMITED
CIN L15142MH1985PLC037493 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L15142MH1985PLC037493__CIAN AGRO INDUSTRIES AND INFRASTRUCTURE LIMITED
Expected foreign subs (1): Cian Agro Limited - LLC

### HINDUSTAN UNILEVER LIMITED
CIN L15140MH1933PLC002030 | NSE HINDUNILVR | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.hul.co.in/investors/annual-reports-and-performance-highlights/annual-reports/hul-annual-report-related-documents/
TARGET FOLDER: L15140MH1933PLC002030__HINDUSTAN UNILEVER LIMITED
Expected foreign subs (1): UNILEVER NEPAL LIMITED

### NHC FOODS LIMITED
CIN L15122GJ1992PLC076277 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L15122GJ1992PLC076277__NHC FOODS LIMITED
Expected foreign subs (1): lntra Metal Trading LLC-FZ
