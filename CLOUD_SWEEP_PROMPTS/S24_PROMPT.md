# CLOUD SWEEP SLICE S24 - 25 PARENTS (27-Sep-2026)
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
### DALMIA REFRACTORIES LIMITED
CIN L24297TN1973PLC006372 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24297TN1973PLC006372__DALMIA REFRACTORIES LIMITED
Expected foreign subs (1): Dalmia Refractories Germany GmbH

### DE NEERS TOOLS LIMITED
CIN L29309DL2021PLC384229 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L29309DL2021PLC384229__DE NEERS TOOLS LIMITED
Expected foreign subs (1): DENEERS TOOLS TRADING LLC

### MANAKSIA COATED METALS & INDUSTRIES LIMITED
CIN L27100WB2010PLC144409 | NSE MANAKCOAT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.manaksiacoatedmetals.com
TARGET FOLDER: L27100WB2010PLC144409__MANAKSIA COATED METALS AND INDUSTRIES LIMITED
Expected foreign subs (1): MANAKSIA INTERNATIONAL FZE

### TOLINS TYRES LIMITED
CIN L25119KL2003PLC016289 | NSE TOLINS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.tolinstyres.com/investor-desk
TARGET FOLDER: L25119KL2003PLC016289__TOLINS TYRES LIMITED
Expected foreign subs (1): Tolins Tyres LLC

### TRITON VALVES LIMITED
CIN L25119KA1975PLC002867 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://tritonvalves.com/investors/
TARGET FOLDER: L25119KA1975PLC002867__TRITON VALVES LIMITED
Expected foreign subs (1): Triton Valves Hong Kong Limited

### TVS SRICHAKRA LIMITED
CIN L25111TN1982PLC009414 | NSE TVSSRICHAK | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://eurogriptyres.com/investor-relations/
TARGET FOLDER: L25111TN1982PLC009414__TVS SRICHAKRA LIMITED
Expected foreign subs (1): Super Grip Corporation

### NURECA LIMITED
CIN L24304MH2016PLC320868 | NSE NURECA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24304MH2016PLC320868__NURECA LIMITED
Expected foreign subs (1): Nureca Inc

### INDIAN ACRYLICS LIMITED
CIN L24301PB1986PLC006715 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.indianacrylics.com/financial_statements_of_foreign_subsidiary.htm
TARGET FOLDER: L24301PB1986PLC006715__INDIAN ACRYLICS LIMITED
Expected foreign subs (1): CARLIT TRADING EUROPE,S.L.U(SPAIN)

### ROCKINGDEALS CIRCULAR ECONOMY LIMITED
CIN L29305HR2002PLC135331 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L29305HR2002PLC135331__ROCKINGDEALS CIRCULAR ECONOMY LIMITED
Expected foreign subs (1): Rocking Deals General Trading L.L.C

### ORIENT CERATECH LIMITED
CIN L24299MH1971PLC366531 | NSE ORIENTCER | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24299MH1971PLC366531__ORIENT CERATECH LIMITED
Expected foreign subs (1): Orient Advanced Materials FZE

### Veranda Learning Solutions Limited
CIN L74999TN2018PLC125880 | NSE VERANDA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.verandalearning.com/web/index.php/investors-financials
TARGET FOLDER: L74999TN2018PLC125880__VERANDA LEARNING SOLUTIONS LIMITED
Expected foreign subs (1): Veranda Learning Solutions N.A,Inc.

### AUSTIN ENGINEERING COMPANY LIMITED
CIN L27259GJ1978PLC003179 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L27259GJ1978PLC003179__AUSTIN ENGINEERING COMPANY LIMITED
Expected foreign subs (1): AUSTIN ENGINEERING COMPANY

### LYPSA GEMS & JEWELLERY LIMITED
CIN L28990GJ1995PLC028270 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.lypsa.in/investors.htm
TARGET FOLDER: L28990GJ1995PLC028270__LYPSA GEMS AND JEWELLERY LIMITED
Expected foreign subs (1): Lypsa Gems & Jewellery DMCC

### HIND ALUMINIUM INDUSTRIES LIMITED
CIN L28920MH1987PLC043472 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: http://www.associatedgroup-investors.com/
TARGET FOLDER: L28920MH1987PLC043472__HIND ALUMINIUM INDUSTRIES LIMITED
Expected foreign subs (1): Hind Aluminium Industries (Kenya) Limited

### AMBER ENTERPRISES INDIA LIMITED
CIN L28910PB1990PLC010265 | NSE AMBER | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.ambergroupindia.com
TARGET FOLDER: L28910PB1990PLC010265__AMBER ENTERPRISES INDIA LIMITED
Expected foreign subs (1): AMBER ENTERPRISES USA INC

### D & H INDIA LIMITED
CIN L28900MH1985PLC035822 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L28900MH1985PLC035822__D AND H INDIA LIMITED
Expected foreign subs (1): D & H MIDDLE EAST FZE

### JOSTS ENGINEERING COMPANY LIMITED
CIN L28100MH1907PLC000252 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://josts.com/financials-of-subsidiary-company
TARGET FOLDER: L28100MH1907PLC000252__JOSTS ENGINEERING COMPANY LIMITED
Expected foreign subs (1): Josts Engineering INC, USA

### AEROFLEX INDUSTRIES LIMITED
CIN L27509MH1993PLC074576 | NSE AEROFLEX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L27509MH1993PLC074576__AEROFLEX INDUSTRIES LIMITED
Expected foreign subs (1): Aeroflex Industries Limited - U.K

### EUREKA FORBES LIMITED
CIN L27310MH2008PLC188478 | NSE EUREKAFORB | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.eurekaforbes.com/cms/assets/prod/
TARGET FOLDER: L27310MH2008PLC188478__EUREKA FORBES LIMITED
Expected foreign subs (1): Euro Forbes Limited, Dubai

### RATNAVEER PRECISION ENGINEERING LIMITED
CIN L27108GJ2002PLC040488 | NSE RATNAVEER | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L27108GJ2002PLC040488__RATNAVEER PRECISION ENGINEERING LIMITED
Expected foreign subs (1): Ratnaveer StainlessInox LLC

### RASHI PERIPHERALS LIMITED
CIN L30007MH1989PLC051039 | NSE RPTECH | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L30007MH1989PLC051039__RASHI PERIPHERALS LIMITED
Expected foreign subs (1): Rashi Peripherals PTE Limited, SINGAPORE

### KIRLOSKAR FERROUS INDUSTRIES LTD
CIN L27101PN1991PLC063223 | NSE KIRLFER | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.kirloskarferrous.com/investors/information-of-subsidiaries
TARGET FOLDER: L27101PN1991PLC063223__KIRLOSKAR FERROUS INDUSTRIES LTD
Expected foreign subs (1): ISMT Enterprises SA

### G N A AXLES LIMITED
CIN L29130PB1993PLC013684 | NSE GNA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://gnaaxles.in/reports-and-documents.php
TARGET FOLDER: L29130PB1993PLC013684__G N A AXLES LIMITED
Expected foreign subs (1): GNA AXLES INC

### CAPRIHANS INDIA LIMITED
CIN L29150PN1946PLC232362 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L29150PN1946PLC232362__CAPRIHANS INDIA LIMITED
Expected foreign subs (1): Bilcare Research GmbH

### PATELS AIRTEMP (INDIA) LIMITED
CIN L29190GJ1992PLC017801 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.patelsairtemp.com/investors/subsidiary-company-accounts/
TARGET FOLDER: L29190GJ1992PLC017801__PATELS AIRTEMP (INDIA) LIMITED
Expected foreign subs (1): Patels Airtemp (USA) Inc.
