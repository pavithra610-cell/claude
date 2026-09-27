# CLOUD SWEEP SLICE S25 - 25 PARENTS (27-Sep-2026)
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
### L G BALAKRISHNAN & BROS LIMITED
CIN L29191TZ1956PLC000257 | NSE LGBBROSLTD | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L29191TZ1956PLC000257__L G BALAKRISHNAN AND BROS LIMITED
Expected foreign subs (1): LGB USA INC

### AVALON TECHNOLOGIES LIMITED
CIN L30007TN1999PLC043479 | NSE AVALON | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.avalontec.com/investor/financials/subsidiary-financials/
TARGET FOLDER: L30007TN1999PLC043479__AVALON TECHNOLOGIES LIMITED
Expected foreign subs (1): ABV Electronics (DBA) SIENNA Corporation

### SYRMA SGS TECHNOLOGY LIMITED
CIN L30007MH2004PLC148165 | NSE SYRMA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L30007MH2004PLC148165__SYRMA SGS TECHNOLOGY LIMITED
Expected foreign subs (1): SYRMA TECHNOLOGY, INC

### Shivalik Bimetal Controls Limited
CIN L27101HP1984PLC005862 | NSE SBCL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.shivalikbimetals.com/subsidiaries-financial-statement.php
TARGET FOLDER: L27101HP1984PLC005862__SHIVALIK BIMETAL CONTROLS LIMITED
Expected foreign subs (1): Shivalik Bimetals Europe SRL; Shivalik Bimetals Europe SRL; Shivalik Bimetals Europe SRL, Italy; Shivalik Bimetals Europe SRL, Italy

### Eraaya Lifespaces Limited
CIN L74899DL1967PLC004704 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74899DL1967PLC004704__ERAAYA LIFESPACES LIMITED
Expected foreign subs (1): ebix inc

### HINDUSTAN ADHESIVES LIMITED
CIN L74899DL1988PLC031191 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://bagla-group.com/about-us/investor-relations/
TARGET FOLDER: L74899DL1988PLC031191__HINDUSTAN ADHESIVES LIMITED
Expected foreign subs (1): Pt Bagla Group Indonesia

### B2B SOFTWARE TECHNOLOGIES LIMITED
CIN L72200TG1994PLC018351 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.b2bsoftech.com/SubsidiaryFinancials.html
TARGET FOLDER: L72200TG1994PLC018351__B2B SOFTWARE TECHNOLOGIES LIMITED
Expected foreign subs (1): B2B Softech Inc., USA

### KLJ RESOURCES LTD
CIN L67120WB1986PLC041487 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L67120WB1986PLC041487__KLJ RESOURCES LTD
Expected foreign subs (1): KLJ Resources, DMCC

### AKG EXIM LIMITED
CIN L00063HR2005PLC119497 | NSE AKG | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L00063HR2005PLC119497__AKG EXIM LIMITED
Expected foreign subs (1): ASRI Trade Pte. Ltd

### AION-TECH SOLUTIONS LIMITED
CIN L72200TG1994PLC017211 | NSE GOLDTECH | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200TG1994PLC017211__AION-TECH SOLUTIONS LIMITED
Expected foreign subs (1): STAYTOP SYSTEMS, INC.

### LUMAX INDUSTRIES LIMITED
CIN L74899DL1981PLC012804 | NSE LUMAXIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74899DL1981PLC012804__LUMAX INDUSTRIES LIMITED
Expected foreign subs (1): Lumax Industries Czech s.r.o.

### RITES LIMITED
CIN L74899DL1974GOI007227 | NSE RITES | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.rites.com/Subsidiaries
TARGET FOLDER: L74899DL1974GOI007227__RITES LIMITED
Expected foreign subs (1): RITES AFRIKA (PTY) LIMITED

### SANGHVI BRANDS LIMITED
CIN L74999PN2010PLC135586 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://sanghvibrands.com/subsidiaries-financial-results/
TARGET FOLDER: L74999PN2010PLC135586__SANGHVI BRANDS LIMITED
Expected foreign subs (1): Sanghvi Brands SL (Private) Limited

### STUDDS ACCESSORIES LTD.
CIN L25208HR1983PLC015135 | NSE STUDDS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L25208HR1983PLC015135__STUDDS ACCESSORIES LTD.
Expected foreign subs (1): Bikerz US INC

### ROSE MERC LIMITED
CIN L93190MH1985PLC035078 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L93190MH1985PLC035078__ROSE MERC LIMITED
Expected foreign subs (1): Emirates Holding FZ LLC (SSA)

### COMMERCIAL SYN BAGS LIMITED
CIN L25202MP1984PLC002669 | NSE COMSYN | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://comsyn.com/investor-relation/comsyn-india-private-limited/
TARGET FOLDER: L25202MP1984PLC002669__COMMERCIAL SYN BAGS LIMITED
Expected foreign subs (1): Smartlift Bulk Packaging Limited U.K

### CLEAN MAX ENVIRO ENERGY SOLUTIONS LIMITED
CIN L93090MH2010PLC208425 | NSE CLEANMAX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L93090MH2010PLC208425__CLEAN MAX ENVIRO ENERGY SOLUTIONS LIMITED
Expected foreign subs (1): Cleanmax Solar Mena FZCO

### MADHUCON PROJECTS LIMITED
CIN L74210TG1990PLC011114 | NSE MADHUCON | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74210TG1990PLC011114__MADHUCON PROJECTS LIMITED
Expected foreign subs (1): PT Madhucon Indonesia

### ALPHAGEO (INDIA) LIMITED
CIN L74210TG1987PLC007580 | NSE ALPHAGEO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74210TG1987PLC007580__ALPHAGEO (INDIA) LIMITED
Expected foreign subs (1): Alphageo International Limited

### DECCAN HEALTH CARE LIMITED
CIN L72200TG1996PLC024351 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200TG1996PLC024351__DECCAN HEALTH CARE LIMITED
Expected foreign subs (1): Deccan Better Living INC

### RESPONSE INFORMATICS LIMITED
CIN L72200TG1996PLC025871 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200TG1996PLC025871__RESPONSE INFORMATICS LIMITED
Expected foreign subs (1): Technologia Corporation, USA

### MADHUVEER COM 18 NETWORK LIMITED
CIN L93000GJ1995PLC026244 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L93000GJ1995PLC026244__MADHUVEER COM 18 NETWORK LIMITED
Expected foreign subs (1): Jojo Global Inc.

### PRIMA PLASTICS LIMITED
CIN L25206DD1993PLC001470 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.primaplastics.com/pages/financial-reports
TARGET FOLDER: L25206DD1993PLC001470__PRIMA PLASTICS LIMITED
Expected foreign subs (1): Prima Union Plasticos S.A.

### SEJAL GLASS LIMITED
CIN L26100MH1998PLC117437 | NSE SEJALLTD | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.sejalglass.co.in/subsidiary-financials.html
TARGET FOLDER: L26100MH1998PLC117437__SEJAL GLASS LIMITED
Expected foreign subs (1): M/s. Sejal Glass & Glass Manufacturing Products LLC

### MAHAMAYA LIFESCIENCES LIMITED
CIN L24233DL2002PLC115261 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24233DL2002PLC115261__MAHAMAYA LIFESCIENCES LIMITED
Expected foreign subs (1): Mahamaya Lifesciences FZE
