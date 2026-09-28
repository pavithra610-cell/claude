# CLOUD SWEEP SLICE S18 - 25 PARENTS (27-Sep-2026)
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
### SUMEET INDUSTRIES LIMITED
CIN L45200GJ1988PLC011049 | NSE SUMEETINDS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.sumeetindustries.com/investor-forms/
TARGET FOLDER: L45200GJ1988PLC011049__SUMEET INDUSTRIES LIMITED
Expected foreign subs (1): Sumeet Global Pte Ltd.

### TAKE Solutions Limited
CIN L63090TN2000PLC046338 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.takesolutions.com/investor-relation
TARGET FOLDER: L63090TN2000PLC046338__TAKE SOLUTIONS LIMITED
Expected foreign subs (1): Take Consultancy Services Inc

### WARDWIZARD INNOVATIONS & MOBILITY LIMITED
CIN L35100MH1982PLC264042 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://wardwizard.in/investor-relations/policies-and-strategy/incl-subsidiary-company-details/
TARGET FOLDER: L35100MH1982PLC264042__WARDWIZARD INNOVATIONS AND MOBILITY LIMITED
Expected foreign subs (1): Wardwizard Global PTE. LTD

### RAVINDRA ENERGY LIMITED
CIN L40104KA1980PLC075720 | NSE RELTD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: http://www.ravindraenergy.com/?page_id=824
TARGET FOLDER: L40104KA1980PLC075720__RAVINDRA ENERGY LIMITED
Expected foreign subs (1): Renuka Energy Resource Holdings FZE

### GROWINGTON VENTURES INDIA LIMITED
CIN L63090MH2010PLC363537 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L63090MH2010PLC363537__GROWINGTON VENTURES INDIA LIMITED
Expected foreign subs (1): Elementures Foodstuff Trading LLC

### SWAN DEFENCE AND HEAVY INDUSTRIES LIMITED
CIN L35110GJ1997PLC033193 | NSE SWANDEF | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L35110GJ1997PLC033193__SWAN DEFENCE AND HEAVY INDUSTRIES LIMITED
Expected foreign subs (1): PDOC PTE. LTD.

### THE SUPREME INDUSTRIES LIMITED
CIN L35920MH1942PLC003554 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.supreme.co.in/investor/archive/financial/subsidary-annual-reports
TARGET FOLDER: L35920MH1942PLC003554__THE SUPREME INDUSTRIES LIMITED
Expected foreign subs (1): The Supreme Industries Overseas (FZE)

### TOTAL TRANSPORT SYSTEMS LIMITED
CIN L63090MH1995PLC091063 | NSE TOTAL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L63090MH1995PLC091063__TOTAL TRANSPORT SYSTEMS LIMITED
Expected foreign subs (1): TOTAL TRANSPORT SYSTEMS PRIVATE LIMITED

### YATRA ONLINE LIMITED
CIN L63040DL2005PLC463461 | NSE YATRA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L63040DL2005PLC463461__YATRA ONLINE LIMITED
Expected foreign subs (1): Yatra Middle East L.L.C-FZ

### WHEELS INDIA LIMITED
CIN L35921TN1960PLC004175 | NSE WHEELS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://wheelsindia.com/annual-report/annual-report-of-subsidiary-company/
TARGET FOLDER: L35921TN1960PLC004175__WHEELS INDIA LIMITED
Expected foreign subs (1): WIL USA INC

### PREMIER ENERGIES LIMITED
CIN L40106TG1995PLC019909 | NSE PREMIERENE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40106TG1995PLC019909__PREMIER ENERGIES LIMITED
Expected foreign subs (1): Premier Energies Photovoltaic LLC

### FELIX INDUSTRIES LIMITED
CIN L40103GJ2012PLC072005 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40103GJ2012PLC072005__FELIX INDUSTRIES LIMITED
Expected foreign subs (1): Felix Industries LLC

### DEEP ENERGY RESOURCES LIMITED
CIN L63090GJ1991PLC014833 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L63090GJ1991PLC014833__DEEP ENERGY RESOURCES LIMITED
Expected foreign subs (1): Deep Energy LLC

### SENCO GOLD LIMITED
CIN L36911WB1994PLC064637 | NSE SENCO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://sencogold.com/financial-information
TARGET FOLDER: L36911WB1994PLC064637__SENCO GOLD LIMITED
Expected foreign subs (1): Senco Global Trading Jewellery LLC

### CHOWGULE STEAMSHIPS LIMITED
CIN L63090GA1963PLC000002 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L63090GA1963PLC000002__CHOWGULE STEAMSHIPS LIMITED
Expected foreign subs (1): CHOWGULE STEAMSHIPS OVERSEAS LTD

### PRABHA ENERGY LIMITED
CIN L40102GJ2009PLC057716 | NSE PRABHA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://prabhaenergy.com/financial-results/
TARGET FOLDER: L40102GJ2009PLC057716__PRABHA ENERGY LIMITED
Expected foreign subs (1): Deep Energy LLC

### LINC LIMITED
CIN L36991WB1994PLC065583 | NSE LINC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://linclimited.com/investor-subsidiary-annual-reports/
TARGET FOLDER: L36991WB1994PLC065583__LINC LIMITED
Expected foreign subs (1): Gelx Industries Ltd

### REFEX RENEWABLES & INFRASTRUCTURE LIMITED
CIN L40100TN1994PLC028263 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40100TN1994PLC028263__REFEX RENEWABLES AND INFRASTRUCTURE LIMITED
Expected foreign subs (1): Refex Renewables SL (Private) Limited

### THE K C P LIMITED
CIN L65991TN1941PLC001128 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.kcp.co.in/financials.html
TARGET FOLDER: L65991TN1941PLC001128__THE K C P LIMITED
Expected foreign subs (1): KCP Vietnam Industries Limited

### ZOTA HEALTH CARE LIMITED
CIN L24231GJ2000PLC038352 | NSE ZOTA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.zotahealthcare.com/wp-content/uploads/2025/09/
TARGET FOLDER: L24231GJ2000PLC038352__ZOTA HEALTH CARE LIMITED
Expected foreign subs (1): Zota Healthcare Lanka (Pvt) Ltd

### COASTAL CORPORATION LIMITED
CIN L63040AP1981PLC003047 | NSE COASTCORP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L63040AP1981PLC003047__COASTAL CORPORATION LIMITED
Expected foreign subs (1): SEACREST SEAFOODS INC.

### MAHINDRA HOLIDAYS & RESORTS INDIA LIMITED
CIN L55101MH1996PLC405715 | NSE MHRIL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L55101MH1996PLC405715__MAHINDRA HOLIDAYS AND RESORTS INDIA LIMITED
Expected foreign subs (1): Arabian Dreams Hotels Apartment LLC

### GMR AIRPORTS LIMITED
CIN L52231HR1996PLC113564 | NSE GMRAIRPORT | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://investor.gmraero.com/annual-account-of-subsidaries
TARGET FOLDER: L52231HR1996PLC113564__GMR AIRPORTS LIMITED
Expected foreign subs (1): GMR Airports (Mauritius) Limited

### Royal Orchid Hotels Limited
CIN L55101KA1986PLC007392 | NSE ROHLTD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.royalorchidhotels.com/investors
TARGET FOLDER: L55101KA1986PLC007392__ROYAL ORCHID HOTELS LIMITED
Expected foreign subs (1): Multi Hotels Limited

### CHL LIMITED
CIN L55101DL1979PLC009498 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L55101DL1979PLC009498__CHL LIMITED
Expected foreign subs (1): CHL International
