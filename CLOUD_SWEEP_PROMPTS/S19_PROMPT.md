# CLOUD SWEEP SLICE S19 - 25 PARENTS (27-Sep-2026)
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
### AELEA COMMODITIES LIMITED
CIN L51909MH2018PLC316782 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L51909MH2018PLC316782__AELEA COMMODITIES LIMITED
Expected foreign subs (1): Supreme Commodities DMCC

### CES LIMITED.
CIN L55100TG1985PLC045963 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L55100TG1985PLC045963__CES LIMITED.
Expected foreign subs (1): CES USA INC

### AMBALAL SARABHAI ENTERPRISES LIMITED
CIN L52100GJ1978PLC003159 | NSE AMBALALSA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L52100GJ1978PLC003159__AMBALAL SARABHAI ENTERPRISES LIMITED
Expected foreign subs (1): ASENCE INC

### JUBILANT AGRI AND CONSUMER PRODUCTS LIMITED
CIN L52100UP2008PLC035862 | NSE JUBLCPL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L52100UP2008PLC035862__JUBILANT AGRI AND CONSUMER PRODUCTS LIMITED
Expected foreign subs (1): Jubilant Industries Inc. USA

### KOHINOOR FOODS LIMITED.
CIN L52110HR1989PLC070351 | NSE KOHINOOR | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L52110HR1989PLC070351__KOHINOOR FOODS LIMITED.
Expected foreign subs (1): KOHINOOR FOODS USA INC

### HALDYN GLASS LIMITED
CIN L51909GJ1991PLC015522 | NSE HALDYNGL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L51909GJ1991PLC015522__HALDYN GLASS LIMITED
Expected foreign subs (1): Haldyn Glass USA Inc.

### ORIENTAL HOTELS LIMITED
CIN L55101TN1970PLC005897 | NSE ORIENTHOT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://orientalhotels.co.in/investors/financial-results/
TARGET FOLDER: L55101TN1970PLC005897__ORIENTAL HOTELS LIMITED
Expected foreign subs (1): OHL International (HK) Limited

### COVANCE SOFTSOL LIMITED
CIN L62011TS2023PLC175979 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L62011TS2023PLC175979__COVANCE SOFTSOL LIMITED
Expected foreign subs (1): Softsol Resources Inc,

### LLOYDS METALS AND ENERGY LIMITED
CIN L40300MH1977PLC019594 | NSE LLOYDSME | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L40300MH1977PLC019594__LLOYDS METALS AND ENERGY LIMITED
Expected foreign subs (1): Lloyds Global Resources FZCO

### SINDHU TRADE LINKS LIMITED
CIN L63020DL1992PLC121695 | NSE SINDHUTRAD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://sindhutrade.com/investors-corner/
TARGET FOLDER: L63020DL1992PLC121695__SINDHU TRADE LINKS LIMITED
Expected foreign subs (1): Param Mitra Resources Pte. Limited

### ORBIT EXPORTS LTD
CIN L40300MH1983PLC030872 | NSE ORBTEXP | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://orbitexports.com/subsidiary-financial-statements
TARGET FOLDER: L40300MH1983PLC030872__ORBIT EXPORTS LTD
Expected foreign subs (1): Orbit Inc

### EXCEL REALTY N INFRA LIMITED
CIN L41001MH2003PLC138568 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L41001MH2003PLC138568__EXCEL REALTY N INFRA LIMITED
Expected foreign subs (1): excel info FZE

### Semac Construction Limited
CIN L42900TZ1977PLC000780 | NSE SEMAC | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L42900TZ1977PLC000780__SEMAC CONSTRUCTION LIMITED
Expected foreign subs (1): SEMAC & PARTNERS LLC

### VIRYA RESOURCES LIMITED
CIN L45100MH1987PLC042141 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45100MH1987PLC042141__VIRYA RESOURCES LIMITED
Expected foreign subs (1): PT Virya Resources Ltd

### ZUARI AGRO CHEMICALS LIMITED
CIN L65910GA2009PLC006177 | NSE ZUARI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.zuari.in/investor/financial_statements
TARGET FOLDER: L65910GA2009PLC006177__ZUARI AGRO CHEMICALS LIMITED
Expected foreign subs (1): Adventz Trading DMCC

### GENPHARMASEC LIMITED
CIN L24231MH1992PLC323914 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.genpharmasec.com/subsidiaries.html
TARGET FOLDER: L24231MH1992PLC323914__GENPHARMASEC LIMITED
Expected foreign subs (1): Genpharmasec Middle East DMCC

### GABRIEL INDIA LIMITED
CIN L34101PN1961PLC015735 | NSE GABRIEL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L34101PN1961PLC015735__GABRIEL INDIA LIMITED
Expected foreign subs (1): Gabriel Europe Engineering Centre

### ITC HOTELS LIMITED
CIN L55101WB2023PLC263914 | NSE ITCHOTELS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L55101WB2023PLC263914__ITC HOTELS LIMITED
Expected foreign subs (1): WelcomHotels Lanka (Private) Limited

### RACL GEARTECH LIMITED
CIN L34300DL1983PLC016136 | NSE RACLGEAR | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.raclgeartech.com/investors
TARGET FOLDER: L34300DL1983PLC016136__RACL GEARTECH LIMITED
Expected foreign subs (1): RACL GEARTECH GMBH

### UCAL LIMITED
CIN L31900TN1985PLC012343 | NSE UCAL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: http://www.ucalfuel.com/investor_information.asp
TARGET FOLDER: L31900TN1985PLC012343__UCAL LIMITED
Expected foreign subs (1): Ucal Holdings Inc.,

### AXIS SOLUTIONS LIMITED
CIN L43212GJ1985PLC029849 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L43212GJ1985PLC029849__AXIS SOLUTIONS LIMITED
Expected foreign subs (1): Brix Engineering GMBH

### CONFIDENCE PETROLEUM INDIA LIMITED
CIN L40200MH1994PLC079766 | NSE CONFIPET | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40200MH1994PLC079766__CONFIDENCE PETROLEUM INDIA LIMITED
Expected foreign subs (1): PT Surya Go Gas Indonesia

### GOBLIN INDIA LIMITED
CIN L51100GJ1989PLC012165 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L51100GJ1989PLC012165__GOBLIN INDIA LIMITED
Expected foreign subs (1): Globin France SARL

### Travel Food Services Limited
CIN L55209MH2007PLC176045 | NSE TRAVELFOOD | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L55209MH2007PLC176045__TRAVEL FOOD SERVICES LIMITED
Expected foreign subs (1): Travel Food Services Global Private Limited (Mauritius)

### LEELA PALACES HOTELS & RESORTS LIMITED
CIN L55209DL2019PLC347492 | NSE THELEELA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.theleela.com/investors
TARGET FOLDER: L55209DL2019PLC347492__LEELA PALACES HOTELS AND RESORTS LIMITED
Expected foreign subs (1): Aries Holdings (DIFC) Limited
