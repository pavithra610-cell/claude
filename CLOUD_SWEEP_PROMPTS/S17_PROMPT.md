# CLOUD SWEEP SLICE S17 - 25 PARENTS (27-Sep-2026)
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
### UVS HOSPITALITY AND SERVICES LIMITED
CIN L15100WB1989PLC046886 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L15100WB1989PLC046886__UVS HOSPITALITY AND SERVICES LIMITED
Expected foreign subs (1): UVS Australia Pty Ltd

### DHAMPUR BIO ORGANICS LIMITED
CIN L15100UP2020PLC136939 | NSE DBOL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.dhampur.com/subsidiary/
TARGET FOLDER: L15100UP2020PLC136939__DHAMPUR BIO ORGANICS LIMITED
Expected foreign subs (1): Dhampur International Pte Limited

### PACIFIC INDUSTRIES LIMITED
CIN L14101RJ1989PLC099253 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.pacificindustriesltd.com/subsidiary.php
TARGET FOLDER: L14101RJ1989PLC099253__PACIFIC INDUSTRIES LIMITED
Expected foreign subs (1): Taanj quartz INC

### Hindustan Oil Exploration Company Limited
CIN L11100GJ1996PLC029880 | NSE HINDOILEXP | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://hoec.com/financial-results/
TARGET FOLDER: L11100GJ1996PLC029880__HINDUSTAN OIL EXPLORATION COMPANY LIMITED
Expected foreign subs (1): Geopetrol International Inc.

### YATRA ONLINE LIMITED
CIN L63040MH2005PLC158404 | NSE YATRA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L63040MH2005PLC158404__YATRA ONLINE LIMITED
Expected foreign subs (1): Yatra Middle East L.L.C-FZ

### SPICEJET LIMITED
CIN L51909DL1984PLC288239 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L51909DL1984PLC288239__SPICEJET LIMITED
Expected foreign subs (1): AS AIR LEASE 41 (IRELAND) LIMITED

### CYIENT DLM LIMITED
CIN L31909TG1993PLC141346 | NSE CYIENTDLM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.cyientdlm.com/investors/
TARGET FOLDER: L31909TG1993PLC141346__CYIENT DLM LIMITED
Expected foreign subs (1): Cyient DLM Inc.

### M & B ENGINEERING LIMITED
CIN L45200GJ1981PLC004437 | NSE MBEL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.mbel.in/investors/
TARGET FOLDER: L45200GJ1981PLC004437__M AND B ENGINEERING LIMITED
Expected foreign subs (1): Phenix Construction Technologies Inc.

### WORTH PERIPHERALS LIMITED
CIN L67120MP1996PLC010808 | NSE WORTHPERI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L67120MP1996PLC010808__WORTH PERIPHERALS LIMITED
Expected foreign subs (1): Worth India Pack Private Limited

### GEOJIT FINANCIAL SERVICES LIMITED
CIN L67120KL1994PLC008403 | NSE GEOJITFSL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L67120KL1994PLC008403__GEOJIT FINANCIAL SERVICES LIMITED
Expected foreign subs (1): Qurum Business Group Geojit Securities LLC

### SHARE INDIA SECURITIES LIMITED.
CIN L67120GJ1994PLC115132 | NSE SHAREINDIA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.shareindia.com/about-us/investor-relations
TARGET FOLDER: L67120GJ1994PLC115132__SHARE INDIA SECURITIES LIMITED.
Expected foreign subs (1): Share India Global Pte. Ltd.

### USHA MARTIN LIMITED
CIN L31400WB1986PLC091621 | NSE USHAMART | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://ushamartin.com/investor-relations
TARGET FOLDER: L31400WB1986PLC091621__USHA MARTIN LIMITED
Expected foreign subs (1): Usha Siam Steel Industries Public Company Limited; Brunton Wolf Wire Ropes FZCO; Usha Martin Singapore Pte. Limited; De Ruiter Staalkabel BV Sliedrecht; Usha Martin Australia Pty Limited; Usha Siam Speciality Wire Rope Company Limited; Usha Martin Europe B.V.; Usha Martin Italia S.R.L.; Brunton Wire Ropes Industrial Company Limited; Usha Martin Espana S.L.; Usha Martin Espana; European Management and Marine Corporation Limited; Usha Martin China Company Limited

### IDEAFORGE TECHNOLOGY LIMITED
CIN L31401MH2007PLC167669 | NSE IDEAFORGE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://ideaforgetech.com/investor-relations/audited-financial-statements
TARGET FOLDER: L31401MH2007PLC167669__IDEAFORGE TECHNOLOGY LIMITED
Expected foreign subs (1): ideaForge Technology Inc

### AMARA RAJA ENERGY & MOBILITY LIMITED
CIN L31402AP1985PLC005305 | NSE ARE&M | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.amararajaeandm.com/Investors/
TARGET FOLDER: L31402AP1985PLC005305__AMARA RAJA ENERGY AND MOBILITY LIMITED
Expected foreign subs (1): Amara Raja Batteries Middle East (FZE)

### EVEREADY INDUSTRIES INDIA LTD
CIN L31402WB1934PLC007993 | NSE EVEREADY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.evereadyindia.com/investors/reports-accounts/account-of-subsidiary-companies/
TARGET FOLDER: L31402WB1934PLC007993__EVEREADY INDUSTRIES INDIA LTD
Expected foreign subs (1): Everspark Hong Kong Private Limited

### SHERA ENERGY LIMITED
CIN L31102RJ2009PLC030434 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31102RJ2009PLC030434__SHERA ENERGY LIMITED
Expected foreign subs (1): SHERA ZAMBIA LIMITED

### INSECTICIDES (INDIA) LIMITED
CIN L65991DL1996PLC083909 | NSE INSECTICID | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L65991DL1996PLC083909__INSECTICIDES (INDIA) LIMITED
Expected foreign subs (1): IIL Overseas DMCC (Dubai)

### AIMTRON ELECTRONICS LIMITED
CIN L31900GJ2011PLC065011 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31900GJ2011PLC065011__AIMTRON ELECTRONICS LIMITED
Expected foreign subs (1): Aimtron Electronics LLC

### DECCAN TRANSCON LEASING LIMITED
CIN L63090TG2007PLC052599 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L63090TG2007PLC052599__DECCAN TRANSCON LEASING LIMITED
Expected foreign subs (1): DECCAN SHIPPING AND LOGISTICS

### CWD LIMITED
CIN L31900MH2016PLC281796 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31900MH2016PLC281796__CWD LIMITED
Expected foreign subs (1): CWD HK Limited

### CESC LTD
CIN L31901WB1978PLC031411 | NSE CESC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L31901WB1978PLC031411__CESC LTD
Expected foreign subs (1): Bantal Singapore Pte. Ltd

### ABATE AS INDUSTRIES LIMITED
CIN L65990TZ1991PLC029162 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L65990TZ1991PLC029162__ABATE AS INDUSTRIES LIMITED
Expected foreign subs (1): Sky International Trading WLL

### VAKRANGEE LIMITED
CIN L65990MH1990PLC056669 | NSE VAKRANGEE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.vakrangee.in/Annual_Reports_Subsidiaries.html
TARGET FOLDER: L65990MH1990PLC056669__VAKRANGEE LIMITED
Expected foreign subs (1): Vakrangee e-Solutions Inc.

### MIC ELECTRONICS LIMITED
CIN L31909TG1988PLC008652 | NSE MICEL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L31909TG1988PLC008652__MIC ELECTRONICS LIMITED
Expected foreign subs (1): SOA Electronics Trading LLC

### OPERATIONAL ENERGY GROUP INDIA LIMITED
CIN L40100TN1994PLC028309 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40100TN1994PLC028309__OPERATIONAL ENERGY GROUP INDIA LIMITED
Expected foreign subs (1): OEG Bangladesh Private Limited
