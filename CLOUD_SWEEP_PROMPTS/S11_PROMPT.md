# CLOUD SWEEP SLICE S11 - 24 PARENTS (27-Sep-2026)
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
### E TO E TRANSPORTATION INFRASTRUCTURE LIMITED
CIN L45201KA2010PLC052810 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45201KA2010PLC052810__E TO E TRANSPORTATION INFRASTRUCTURE LIMITED
Expected foreign subs (2): E to E Rail Private Limited; E to E Rail Pte. Limited-Singapore

### THE RAMARAJU SURGICAL COTTON MILLS LIMITED
CIN L17111TN1939PLC002302 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L17111TN1939PLC002302__THE RAMARAJU SURGICAL COTTON MILLS LIMITED
Expected foreign subs (2): Taram Textiles, LLC; Taram Textiles Online, Inc

### IFB AGRO INDUSTRIES LTD.
CIN L01409WB1982PLC034590 | NSE IFBAGRO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.ifbagro.in/investor_relations/audited-financial-statement-of-subsidiary
TARGET FOLDER: L01409WB1982PLC034590__IFB AGRO INDUSTRIES LTD.
Expected foreign subs (2): IFB AGRO MARINE (FZE); IFB AGRO HOLDINGS PTE. LTD.

### FIEM INDUSTRIES LIMITED
CIN L36999DL1989PLC034928 | NSE FIEMIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://fiemindustries.com/investor-presentation/
TARGET FOLDER: L36999DL1989PLC034928__FIEM INDUSTRIES LIMITED
Expected foreign subs (2): Fiem Research & Technology S.R.L.; Fiem Industries Japan Co., Ltd.

### NISUS FINANCE SERVICES CO LIMITED
CIN L65923MH2013PLC247317 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://nisusfin.com/investor-relations
TARGET FOLDER: L65923MH2013PLC247317__NISUS FINANCE SERVICES CO LIMITED
Expected foreign subs (2): NISUS FINANCE INVESTMENT CONSULTANCY FZCO; NIFCO MANAGEMENT CONSULTANCIES LLC

### VADILAL INDUSTRIES LIMITED
CIN L91110GJ1982PLC005169 | NSE VADILALIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://vadilalgroup.com/wp-content/uploads/2024/08/
TARGET FOLDER: L91110GJ1982PLC005169__VADILAL INDUSTRIES LIMITED
Expected foreign subs (2): Vadilal Industries (USA) Inc; Vadilal Industries Pty Ltd.


### INTEGRATED HITECH LIMITED
CIN L72300TN1993PLC024583 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72300TN1993PLC024583__INTEGRATED HITECH LIMITED
Expected foreign subs (2): INTEGRATED HITECH SINGAPORE PTE LTD; INTEGRATED HITECH SINGAPORE PTE LTD

### D S KULKARNI DEVELOPERS LTD
CIN L45201PN1991PLC063340 | NSE DSKULKARNI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://dskcirp.com
TARGET FOLDER: L45201PN1991PLC063340__D S KULKARNI DEVELOPERS LTD
Expected foreign subs (2): DSK Developers Corporation USA; DSK Woods LLC

### DOLPHIN OFFSHORE ENTERPRISES (INDIA) LIMITED
CIN L11101MH1979PLC021302 | NSE DOLPHIN | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://dolphinoffshore.com/subsidiaries-associates/
TARGET FOLDER: L11101MH1979PLC021302__DOLPHIN OFFSHORE ENTERPRISES (INDIA) LIMITED
Expected foreign subs (2): Beluga International DMCC; Dolphin Offshore Enterprises (Mauritius) Pvt Ltd

### MAGELLANIC CLOUD LIMITED
CIN L72100TG1981PLC169991 | NSE MCLOUD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://magellanic-cloud.com/investors/subsidiary-financials/
TARGET FOLDER: L72100TG1981PLC169991__MAGELLANIC CLOUD LIMITED
Expected foreign subs (2): JNIT Technologies, INC.; Motivity Inc

### CADSYS ( INDIA ) LIMITED
CIN L72200TG1992PLC014558 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200TG1992PLC014558__CADSYS ( INDIA ) LIMITED
Expected foreign subs (2): Apex Advanced Technology LLC; Cadsys Technologies LLC

### SAYAJI INDUSTRIES LIMITED
CIN L99999GJ1941PLC000471 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.sayajigroup.in
TARGET FOLDER: L99999GJ1941PLC000471__SAYAJI INDUSTRIES LIMITED
Expected foreign subs (2): Sayaji Industries FZC; Sayaji Industries FZC-UAE

### WISE TRAVEL INDIA LIMITED
CIN L63090DL2009PLC189594 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L63090DL2009PLC189594__WISE TRAVEL INDIA LIMITED
Expected foreign subs (2): WTI RENT A CAR LLC; PT WTI Trading and Mining Ventures

### SPACENET ENTERPRISES INDIA LIMITED
CIN L68100TG2010PLC068624 | NSE SPCENET | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.spacenetent.com/Investor-Relations.html
TARGET FOLDER: L68100TG2010PLC068624__SPACENET ENTERPRISES INDIA LIMITED
Expected foreign subs (2): Spacenet Tradetech HK Limited; Spacenet Enterprises FZCO

### SAATVIK GREEN ENERGY LIMITED
CIN L40106HR2015PLC075578 | NSE SAATVIKGL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40106HR2015PLC075578__SAATVIK GREEN ENERGY LIMITED
Expected foreign subs (2): Saatvik Green Energy USA Inc.; Saatvik Green Energy USA Inc.

### ORCHASP LIMITED
CIN L72200TG1994PLC017485 | NSE ORCHASP | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://orchasp.com/investors/
TARGET FOLDER: L72200TG1994PLC017485__ORCHASP LIMITED
Expected foreign subs (2): Cybermate Infotek Limited Inc; Cybermate International, Unipessoal, LDA

### WINSOL ENGINEERS LIMITED
CIN L40100GJ2015PLC085516 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40100GJ2015PLC085516__WINSOL ENGINEERS LIMITED
Expected foreign subs (2): Winsol Engineers Zambia Limited; Winsol Engineers Zambia Limited

### GNG ELECTRONICS LIMITED
CIN L72900MH2006PLC165194 | NSE EBGNG | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72900MH2006PLC165194__GNG ELECTRONICS LIMITED
Expected foreign subs (2): Elecronics Bazaar FZC; Electronics Bazaar FZC

### KSOLVES INDIA LIMITED
CIN L72900DL2014PLC269020 | NSE KSOLVES | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72900DL2014PLC269020__KSOLVES INDIA LIMITED
Expected foreign subs (2): KSOLVES LLC; Kingpin Technology Consultants LLC

### JYOTI STRUCTURES LIMITED
CIN L45200MH1974PLC017494 | NSE JYOTISTRUC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://content.app-sources.com/s/82347095277189258/uploads/Financial_Results/
TARGET FOLDER: L45200MH1974PLC017494__JYOTI STRUCTURES LIMITED
Expected foreign subs (2): Jyoti Structures FZE; Jyoti Structures Africa (Pty.) Ltd.

### SHREE RENUKA SUGARS LIMITED
CIN L01542KA1995PLC019046 | NSE RENUKA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://renukasugars.com/disclosure-under-reg-46-and-62-of-sebi-lodr/
TARGET FOLDER: L01542KA1995PLC019046__SHREE RENUKA SUGARS LIMITED
Expected foreign subs (2): Renuka Commodities DMCC, Dubai; Shree Renuka East Africa Agriventures PLC

### RANE HOLDINGS LIMITED
CIN L35999TN1936PLC002202 | NSE RANEHOLDIN | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://ranegroup.com/investors/rane-holdings-limited/
TARGET FOLDER: L35999TN1936PLC002202__RANE HOLDINGS LIMITED
Expected foreign subs (2): Rane Holdings America Inc.; Rane Holdings Europe GmbH

### KRBL LIMITED
CIN L01111DL1993PLC052845 | NSE KRBL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://krblrice.com/investor-relations/
TARGET FOLDER: L01111DL1993PLC052845__KRBL LIMITED
Expected foreign subs (2): KRBL DMCC; KRBL DMCC GROUP

### BAJAJ CONSUMER CARE LIMITED
CIN L01110RJ2006PLC047173 | NSE BAJAJCON | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://bajajconsumercare.com/pdf/general-meeting-agm/
TARGET FOLDER: L01110RJ2006PLC047173__BAJAJ CONSUMER CARE LIMITED
Expected foreign subs (2): BAJAJ CORP INTERNATIONAL(FZE); BAJAJ BANGLADESH LIMITED
