# CLOUD SWEEP SLICE S23 - 25 PARENTS (27-Sep-2026)
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
### ALPHALOGIC TECHSYS LIMITED
CIN L72501PN2018PLC180757 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72501PN2018PLC180757__ALPHALOGIC TECHSYS LIMITED
Expected foreign subs (1): Faraday Digital Inc.

### GODREJ PROPERTIES LIMITED
CIN L74120MH1985PLC035308 | NSE GODREJPROP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.godrejproperties.com/investors/financials
TARGET FOLDER: L74120MH1985PLC035308__GODREJ PROPERTIES LIMITED
Expected foreign subs (1): Godrej Properties Worldwide Inc., USA

### EKI ENERGY SERVICES LIMITED
CIN L74200MP2011PLC025904 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://enkingint.org/investor-relations/
TARGET FOLDER: L74200MP2011PLC025904__EKI ENERGY SERVICES LIMITED
Expected foreign subs (1): Enking International PTE LTD

### HOMESFY REALTY LIMITED
CIN L70100MH2011PLC217134 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L70100MH2011PLC217134__HOMESFY REALTY LIMITED
Expected foreign subs (1): Homesfy Global Realty L.L.C.

### SANDHAR TECHNOLOGIES LIMITED
CIN L74999DL1987PLC029553 | NSE SANDHAR | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://sandhargroup.com/investors/subsidiary-annual-reports
TARGET FOLDER: L74999DL1987PLC029553__SANDHAR TECHNOLOGIES LIMITED
Expected foreign subs (1): SANDHAR TECHNOLOGIES BARCELONA SL

### Astec LifeSciences Limited
CIN L99999MH1994PLC076236 | NSE ASTEC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.godrejastec.com/investors
TARGET FOLDER: L99999MH1994PLC076236__ASTEC LIFESCIENCES LIMITED
Expected foreign subs (1): Comercializadora Agricola Agroastrachem Cia Ltda

### SIGMA SOLVE LIMITED
CIN L72200GJ2010PLC060478 | NSE SIGMA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200GJ2010PLC060478__SIGMA SOLVE LIMITED
Expected foreign subs (1): Sigma Solve Inc

### ZEAL GLOBAL SERVICES LIMITED
CIN L74950DL2014PLC264849 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74950DL2014PLC264849__ZEAL GLOBAL SERVICES LIMITED
Expected foreign subs (1): Zeal Global Services LLC-FZ

### WINDLAS BIOTECH LIMITED
CIN L74899UR2001PLC033407 | NSE WINDLAS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74899UR2001PLC033407__WINDLAS BIOTECH LIMITED
Expected foreign subs (1): WINDLASS INC.

### OMAXE LIMITED
CIN L74899HR1989PLC051918 | NSE OMAXE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.omaxe.com/investor/audited-financial-statements-of-subsidiary-companies
TARGET FOLDER: L74899HR1989PLC051918__OMAXE LIMITED
Expected foreign subs (1): SHIKHAR LANDCON PRIVATE LIMITED

### ADITYA INFOTECH LIMITED
CIN L74899DL1995PLC066784 | NSE CPPLUS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74899DL1995PLC066784__ADITYA INFOTECH LIMITED
Expected foreign subs (1): Shenzhen CP Plus International Limited

### PETRONET LNG LIMITED
CIN L74899DL1998PLC093073 | NSE PETRONET | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.petronetlng.in/financials-subsidiaries
TARGET FOLDER: L74899DL1998PLC093073__PETRONET LNG LIMITED
Expected foreign subs (1): Petronet LNG Singapore Pte. Ltd.

### IDENTIXWEB LIMITED
CIN L72100GJ2017PLC098473 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72100GJ2017PLC098473__IDENTIXWEB LIMITED
Expected foreign subs (1): IDENTIXWEB LLC

### PROVENTUS AGROCOM LIMITED
CIN L74999MH2015PLC269390 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.proventusagro.com/investors-1
TARGET FOLDER: L74999MH2015PLC269390__PROVENTUS AGROCOM LIMITED
Expected foreign subs (1): Proventus Commodities DMCC

### KILITCH DRUGS (INDIA) LIMITED.
CIN L24239MH1992PLC066718 | NSE KILITCH | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://kilitch.com/investor-relations/
TARGET FOLDER: L24239MH1992PLC066718__KILITCH DRUGS (INDIA) LIMITED.
Expected foreign subs (1): Kilitch Estro Biotech PLC

### TEXEL INDUSTRIES LIMITED
CIN L29100GJ1989PLC012576 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L29100GJ1989PLC012576__TEXEL INDUSTRIES LIMITED
Expected foreign subs (1): Texel Industries (Africa) Ltd

### MACFOS LIMITED
CIN L29309PN2017PLC172718 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L29309PN2017PLC172718__MACFOS LIMITED
Expected foreign subs (1): Nuo Zhan Technologies Limited

### MEERA INDUSTRIES LIMITED
CIN L29298GJ2006PLC048627 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://meeraind.com/investors/
TARGET FOLDER: L29298GJ2006PLC048627__MEERA INDUSTRIES LIMITED
Expected foreign subs (1): MEERA INDUSTRIES USA, LLC

### INDIAN METALS AND FERRO ALLOYS LTD.
CIN L27101OR1961PLC000428 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L27101OR1961PLC000428__INDIAN METALS AND FERRO ALLOYS LTD.
Expected foreign subs (1): INDMET MINING PTE LTD

### ROSSELL TECHSYS LIMITED
CIN L29299WB2022PLC258641 | NSE ROSSTECH | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L29299WB2022PLC258641__ROSSELL TECHSYS LIMITED
Expected foreign subs (1): Rossell Techsys Inc. USA

### MANUGRAPH INDIA LIMITED
CIN L29290MH1972PLC015772 | NSE MANUGRAPH | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L29290MH1972PLC015772__MANUGRAPH INDIA LIMITED
Expected foreign subs (1): Manugraph Americas Inc

### JNK INDIA LIMITED
CIN L29268MH2010PLC204223 | NSE JNKINDIA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L29268MH2010PLC204223__JNK INDIA LIMITED
Expected foreign subs (1): JNK India Private FZE

### TEXMACO RAIL & ENGINEERING LIMITED
CIN L29261WB1998PLC087404 | NSE TEXRAIL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L29261WB1998PLC087404__TEXMACO RAIL AND ENGINEERING LIMITED
Expected foreign subs (1): Texmaco Middle East DMCC

### MAMATA MACHINERY LIMITED
CIN L29259GJ1979PLC003363 | NSE MAMATA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L29259GJ1979PLC003363__MAMATA MACHINERY LIMITED
Expected foreign subs (1): Mamata Enterprises Inc

### ERP SOFT SYSTEMS LIMITED
CIN L67120TN1994PLC029563 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L67120TN1994PLC029563__ERP SOFT SYSTEMS LIMITED
Expected foreign subs (1): Libertycom, LLC
