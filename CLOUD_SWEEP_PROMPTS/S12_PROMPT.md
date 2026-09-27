# CLOUD SWEEP SLICE S12 - 25 PARENTS (27-Sep-2026)
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
### GANDHAR OIL REFINERY (INDIA) LIMITED
CIN L23200MH1992PLC068905 | NSE GANDHAR | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://gandharoil.com/wp-content/uploads/2025/07/
TARGET FOLDER: L23200MH1992PLC068905__GANDHAR OIL REFINERY (INDIA) LIMITED
Expected foreign subs (2): Texol Lubritech FZC; Texol Lubricants Manufacturing LLC

### ANSAL HOUSING LIMITED
CIN L45201DL1983PLC016821 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.ansals.com/page/financial_subsidiary
TARGET FOLDER: L45201DL1983PLC016821__ANSAL HOUSING LIMITED
Expected foreign subs (2): HOUSING AND CONSTRUCTION LANKA (PRIVATE) LIMITED; HOUISNG AND CONSTRUCTION LANKA (PRIVATE) LIMITED

### NETTLINX LIMITED
CIN L67120TG1994PLC016930 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.nettlinx.com
TARGET FOLDER: L67120TG1994PLC016930__NETTLINX LIMITED
Expected foreign subs (2): Nettlinx, INC; SALION SE

### MUKKA PROTEINS LIMITED
CIN L10207KA2010PLC055771 | NSE MUKKA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L10207KA2010PLC055771__MUKKA PROTEINS LIMITED
Expected foreign subs (2): Ocean Aquatic Proteins LLC, Oman; United Gulf Fishery Products LLC

### ALLDIGI TECH LIMITED
CIN L72300TN1998PLC041033 | NSE ALLDIGI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.alldigitech.com/investor-relations-financial-information/
TARGET FOLDER: L72300TN1998PLC041033__ALLDIGI TECH LIMITED
Expected foreign subs (2): Alldigi Tech INC, USA; Alldigi Tech Manila Inc, Philippines

### GARWARE HI-TECH FILMS LIMITED
CIN L10889MH1957PLC010889 | NSE GRWRHITECH | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L10889MH1957PLC010889__GARWARE HI-TECH FILMS LIMITED
Expected foreign subs (2): Global Hi-Tech Films, Inc.; Garware Hi-Tech Films International Limited (GHFIL)

### COMPUTER AGE MANAGEMENT SERVICES LIMITED
CIN L65910TN1988PLC015757 | NSE CAMS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.camsonline.com/about-cams/shareholder-relations/subsidiary-annual-reports
TARGET FOLDER: L65910TN1988PLC015757__COMPUTER AGE MANAGEMENT SERVICES LIMITED
Expected foreign subs (2): Think 360AI INC; Sterling Software (Deutschland) GmbH

### POLY MEDICURE LIMITED
CIN L40300DL1995PLC066923 | NSE POLYMED | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.polymedicure.com/subsidiaries-financials/
TARGET FOLDER: L40300DL1995PLC066923__POLY MEDICURE LIMITED
Expected foreign subs (2): Poly Medicure BV,Netherlands; Poly Medicure (Laiyang) Co. Ltd., China

### XTGLOBAL INFOTECH LIMITED
CIN L72200TG1986PLC006644 | NSE XTGLOBAL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://xtglobal.com/investors/financial-information/
TARGET FOLDER: L72200TG1986PLC006644__XTGLOBAL INFOTECH LIMITED
Expected foreign subs (2): XTGlobal Inc; Network objects Inc

### ZUARI INDUSTRIES LIMITED
CIN L65921GA1967PLC000157 | NSE ZUARIIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.zuariindustries.in/investor-resources
TARGET FOLDER: L65921GA1967PLC000157__ZUARI INDUSTRIES LIMITED
Expected foreign subs (2): Zuari Infra Middle East Limited; Zuari Infraworld SJM properties LLC

### GREENPLY INDUSTRIES LTD
CIN L20211WB1990PLC268743 | NSE GREENPLY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://greenply.com/disclosures-u-r-46-of-lodr/subsidiaries-financials
TARGET FOLDER: L20211WB1990PLC268743__GREENPLY INDUSTRIES LTD
Expected foreign subs (2): Green Ply Holdings PTE Ltd. Singapore; Greenply Middle East Limited,

### TAMILNADU PETROPRODUCTS LIMITED
CIN L23200TN1984PLC010931 | NSE TNPETRO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.tnpetro.com/annualreports/annual-report-of-subsidiaries/
TARGET FOLDER: L23200TN1984PLC010931__TAMILNADU PETROPRODUCTS LIMITED
Expected foreign subs (2): Certus Investments and Trading Limited, Mauritius; Certus Investments and Trading Limited, Singapore

### DRC SYSTEMS INDIA LIMITED
CIN L72900GJ2012PLC070106 | NSE DRCSYSTEMS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.drcsystems.com/wp-content/uploads/2025/09/
TARGET FOLDER: L72900GJ2012PLC070106__DRC SYSTEMS INDIA LIMITED
Expected foreign subs (2): DRC Systems EMEA LLC-FZ; DRC Systems USA LLC

### UMA EXPORTS LTD
CIN L14109WB1988PLC043934 | NSE UMAEXPORTS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.umaexports.net
TARGET FOLDER: L14109WB1988PLC043934__UMA EXPORTS LTD
Expected foreign subs (2): UEL International FZE U.A.E; Graincomm Australia Pty Ltd

### LAXMI DENTAL LIMITED
CIN L51507MH2004PLC147394 | NSE LAXMIDENTL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.laxmidentallimited.com/financials/audited_financial_statement_of_group_company
TARGET FOLDER: L51507MH2004PLC147394__LAXMI DENTAL LIMITED
Expected foreign subs (2): Laxmi Dental Lab USA Inc; Illusion Dental Lab USA INC

### QUINT DIGITAL LIMITED
CIN L63122DL1985PLC373314 | NSE QUINT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L63122DL1985PLC373314__QUINT DIGITAL LIMITED
Expected foreign subs (2): Global Media Technologies Inc; Global Media Technologies Inc. (“GMT”)

### RESTAURANT BRANDS ASIA LIMITED
CIN L55204MH2013FLC249986 | NSE RBA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.burgerking.in/investorrelations
TARGET FOLDER: L55204MH2013FLC249986__RESTAURANT BRANDS ASIA LIMITED
Expected foreign subs (2): PT Sari Burger Indonesia; PT Sari Chicken Indonesia

### ASI INDUSTRIES LIMITED
CIN L14101MH1945PLC256122 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.asigroup.co.in/investors/
TARGET FOLDER: L14101MH1945PLC256122__ASI INDUSTRIES LIMITED
Expected foreign subs (2): ASI Global Limited; Al Rawasi Rock & Aggregate LLC

### Capitalnumbers Infotech Limited
CIN L72200WB2012PLC183599 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.capitalnumbers.com/investors-pdf/annual-accounts/
TARGET FOLDER: L72200WB2012PLC183599__CAPITALNUMBERS INFOTECH LIMITED
Expected foreign subs (2): Capital Numbers LLC; Capital Numbers Australia Pty. Ltd.

### SUTLEJ TEXTILES AND INDUSTRIES LIMITED
CIN L17124RJ2005PLC020927 | NSE SUTLEJTEX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.sutlejtextiles.com/investor-relations.html
TARGET FOLDER: L17124RJ2005PLC020927__SUTLEJ TEXTILES AND INDUSTRIES LIMITED
Expected foreign subs (2): American Silk Mills, LLC.; Sutlej Holdings, Inc.

### Elitecon International Limited
CIN L46305DL1987PLC396234 | NSE ELITECON | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L46305DL1987PLC396234__ELITECON INTERNATIONAL LIMITED
Expected foreign subs (2): Elitecon International FZ LLC; Elitecon International PTE LTD

### INDIAN EMULSIFIERS LIMITED
CIN L46691MH2020PLC351364 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L46691MH2020PLC351364__INDIAN EMULSIFIERS LIMITED
Expected foreign subs (2): SOUTHERN EMULSIFIER SOLUTIONS PTY LTD; SOUTHERN EMULSIFIER SOLUTIONS PTY LTD

### JET FREIGHT LOGISTICS LIMITED
CIN L63090MH2006PLC161114 | NSE JETFREIGHT | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L63090MH2006PLC161114__JET FREIGHT LOGISTICS LIMITED
Expected foreign subs (2): Jet Freight Logistics INC; Jet Freight Logistics B.V

### SAMPRE NUTRITIONS LIMITED
CIN L15499TG1991PLC013515 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L15499TG1991PLC013515__SAMPRE NUTRITIONS LIMITED
Expected foreign subs (2): Sampre Nutritions Holdings Limited; Sampre Nutritions FZCO

### PELATRO LIMITED
CIN L72100KA2013PLC068239 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72100KA2013PLC068239__PELATRO LIMITED
Expected foreign subs (2): Pelatro Pte limited; Pelatro Pte. Ltd.
