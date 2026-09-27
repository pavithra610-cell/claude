# CLOUD SWEEP SLICE S15 - 25 PARENTS (27-Sep-2026)
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
### K&R RAIL ENGINEERING LIMITED
CIN L45200TG1983PLC082576 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45200TG1983PLC082576__KANDR RAIL ENGINEERING LIMITED
Expected foreign subs (1): K&R GLOBAL L.L.C - FZ

### S J LOGISTICS (INDIA) LIMITED
CIN L63000MH2003PLC143614 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L63000MH2003PLC143614__S J LOGISTICS (INDIA) LIMITED
Expected foreign subs (1): SJL Group Singapore PTE LTD

### LE TRAVENUES TECHNOLOGY LIMITED
CIN L63000HR2006PLC071540 | NSE IXIGO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://investors-site-api.ixigo.workers.dev/files/
TARGET FOLDER: L63000HR2006PLC071540__LE TRAVENUES TECHNOLOGY LIMITED
Expected foreign subs (1): IXIGO EUROPE, S.L.

### ADVAIT ENERGY TRANSITIONS LIMITED
CIN L45201GJ2010PLC059878 | NSE ADVAIT | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45201GJ2010PLC059878__ADVAIT ENERGY TRANSITIONS LIMITED
Expected foreign subs (1): Advait Energy Holding AS

### TRANSVOY LOGISTICS INDIA LIMITED
CIN L63000GJ2015PLC084004 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L63000GJ2015PLC084004__TRANSVOY LOGISTICS INDIA LIMITED
Expected foreign subs (1): Transvoy Singapore PTE Limited

### PRIME URBAN DEVELOPMENT INDIA LIMITED
CIN L47990TZ1936PLC000001 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://ptlonline.com/subsidiaries-accounts/
TARGET FOLDER: L47990TZ1936PLC000001__PRIME URBAN DEVELOPMENT INDIA LIMITED
Expected foreign subs (1): Prime Urban North America INC

### TECHNO ELECTRIC & ENGINEERING COMPANY LIMITED
CIN L40108HR2005PLC142826 | NSE TECHNOE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40108HR2005PLC142826__TECHNO ELECTRIC AND ENGINEERING COMPANY LIMITED
Expected foreign subs (1): TECHNO ELECTRIC OVERSEAS PTE LTD

### SAR TELEVENTURE LIMITED
CIN L45202UP2019PLC213062 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45202UP2019PLC213062__SAR TELEVENTURE LIMITED
Expected foreign subs (1): SAR Televentures F.Z.E

### KBC GLOBAL LIMITED
CIN L45400MH2007PLC174194 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45400MH2007PLC174194__KBC GLOBAL LIMITED
Expected foreign subs (1): KBC GLOBAL FZCO

### SUUMAYA INDUSTRIES LIMITED
CIN L46411MH2011PLC220879 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L46411MH2011PLC220879__SUUMAYA INDUSTRIES LIMITED
Expected foreign subs (1): Suumaya Industries Pte. Limited

### JINKUSHAL INDUSTRIES LIMITED
CIN L46594CT2007PLC008170 | NSE JKIPL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L46594CT2007PLC008170__JINKUSHAL INDUSTRIES LIMITED
Expected foreign subs (1): Hexco Global FZE

### POWERICA LIMITED
CIN L31100MH1984PLC032825 | NSE POWERICA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31100MH1984PLC032825__POWERICA LIMITED
Expected foreign subs (1): POWERICA POWER SYSTEMS FZE

### IL&FS ENGINEERING AND CONSTRUCTION COMPANY LIMITED
CIN L45201TG1988PLC008624 | NSE IL&FSENGG | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45201TG1988PLC008624__ILANDFS ENGINEERING AND CONSTRUCTION COMPANY LIMITED
Expected foreign subs (1): Maytas Infra Saudi Arabia (MISA)

### ASHOKA BUILDCON LIMITED
CIN L45200MH1993PLC071970 | NSE ASHOKA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.ashokabuildcon.com/subsidiaries.php
TARGET FOLDER: L45200MH1993PLC071970__ASHOKA BUILDCON LIMITED
Expected foreign subs (1): Ashoka Buildcon (Guyana) INC

### SANWARIA CONSUMER LIMITED
CIN L15143MP1991PLC006395 | NSE SANWARIA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L15143MP1991PLC006395__SANWARIA CONSUMER LIMITED
Expected foreign subs (1): Sanwaria Singapore Pte. Ltd

### GSP CROP SCIENCE LIMITED
CIN L24120GJ1985PLC007641 | NSE GSPCROP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24120GJ1985PLC007641__GSP CROP SCIENCE LIMITED
Expected foreign subs (1): GSP Agroquimica Do Brasil LTDA

### JINDAL POLY FILMS LIMITED
CIN L17111UP1974PLC003979 | NSE JINDALPOLY | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.jindalpoly.com/download-reports
TARGET FOLDER: L17111UP1974PLC003979__JINDAL POLY FILMS LIMITED
Expected foreign subs (1): JPF Netherlands Investment B.V.

### ORIENTAL AROMATICS LIMITED
CIN L17299MH1972PLC285731 | NSE OAL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.orientalaromatics.com/investorrelations.php
TARGET FOLDER: L17299MH1972PLC285731__ORIENTAL AROMATICS LIMITED
Expected foreign subs (1): PT Oriental Aromatics

### BLACK ROSE INDUSTRIES LIMITED
CIN L17120MH1990PLC054828 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L17120MH1990PLC054828__BLACK ROSE INDUSTRIES LIMITED
Expected foreign subs (1): B.R. Chemicals Co. Ltd.

### ADITYA BIRLA REAL ESTATE LIMITED
CIN L17120MH1897PLC000163 | NSE ABREL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.adityabirlarealestate.com/investors
TARGET FOLDER: L17120MH1897PLC000163__ADITYA BIRLA REAL ESTATE LIMITED
Expected foreign subs (1): Birla Century International LLC

### THE BOMBAY DYEING AND MANUFACTURING COMPANY LIMITED
CIN L17120MH1879PLC000037 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://bombaydyeing.com/pdfs/disclosure/
TARGET FOLDER: L17120MH1879PLC000037__THE BOMBAY DYEING AND MANUFACTURING COMPANY LIMITED
Expected foreign subs (1): P. T. Five Star Textile Indonesia

### PENINSULA LAND LIMITED
CIN L17120MH1871PLC000005 | NSE PENINLAND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L17120MH1871PLC000005__PENINSULA LAND LIMITED
Expected foreign subs (1): Westgate Real Estate Developers LLP

### SIYARAM SILK MILLS LIMITED
CIN L17116MH1978PLC020451 | NSE SIYSIL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://siyaram-images.s3.ap-south-1.amazonaws.com/images/investor-relationship-doc/annual-reports/2023-2024/
TARGET FOLDER: L17116MH1978PLC020451__SIYARAM SILK MILLS LIMITED
Expected foreign subs (1): CADINI S. R. L.

### BIKAJI FOODS INTERNATIONAL LIMITED
CIN L15499RJ1995PLC010856 | NSE BIKAJI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.bikaji.com/financials
TARGET FOLDER: L15499RJ1995PLC010856__BIKAJI FOODS INTERNATIONAL LIMITED
Expected foreign subs (1): Bikaji Foods International USA Corp

### Britannia Industries Ltd
CIN L15412WB1918PLC002964 | NSE BRITANNIA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.britannia.co.in/investors/financial-performance/subsidiaries-accounts
TARGET FOLDER: L15412WB1918PLC002964__BRITANNIA INDUSTRIES LTD
Expected foreign subs (1): Strategic Food International Co. LLC; Al Sallan Food International Co. SAOC; Britannia Egypt LLC; Strategic Foods Uganda Limited; Britannia Dairy Holdings Private Limited
