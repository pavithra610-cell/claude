# CLOUD SWEEP SLICE S09 - 25 PARENTS (27-Sep-2026)
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
### KRIDHAN INFRA LIMITED
CIN L27100MH2006PLC160602 | NSE KRIDHANINF | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L27100MH2006PLC160602__KRIDHAN INFRA LIMITED
Expected foreign subs (2): Readymade Steel Singapore PTE Limited; Readymade Steel Singapore PTE Ltd

### VIKAS LIFECARE LIMITED
CIN L25111DL1995PLC073719 | NSE VIKASLIFE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L25111DL1995PLC073719__VIKAS LIFECARE LIMITED
Expected foreign subs (2): Vikash Life Care Investment Management LLC; vikas lifecare investment management LLC

### SENORES PHARMACEUTICALS LIMITED
CIN L24290GJ2017PLC100263 | NSE SENORES | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://senorespharma.com/wp-content/uploads/2025/
TARGET FOLDER: L24290GJ2017PLC100263__SENORES PHARMACEUTICALS LIMITED
Expected foreign subs (2): Havix Group Inc. d/b/a Aavis Pharmaceuticals; Senores Pharmaceuticals INC.

### YASHO INDUSTRIES LIMITED
CIN L74110MH1985PLC037900 | NSE YASHO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.yashoindustries.com/uploads/7/9/4/9/7949862/
TARGET FOLDER: L74110MH1985PLC037900__YASHO INDUSTRIES LIMITED
Expected foreign subs (2): YASHO INDUSTRIES EUROPE B.V.; Yasho Inc.

### EVEREST INDUSTRIES LIMITED
CIN L74999MH1934PLC002093 | NSE EVERESTIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.everestind.com/investor-relations/subsidiaries-financial-statements
TARGET FOLDER: L74999MH1934PLC002093__EVEREST INDUSTRIES LIMITED
Expected foreign subs (2): Everestind FZE; Everest Building Products

### ZENITH STEEL PIPES & INDUSTRIES LIMITED
CIN L29220MH1960PLC011773 | NSE ZENITHSTL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.zenithsteelpipes.com
TARGET FOLDER: L29220MH1960PLC011773__ZENITH STEEL PIPES AND INDUSTRIES LIMITED
Expected foreign subs (2): Zenith Middle East FZ-LLC; Zenith (USA) Inc.

### EXHICON EVENTS MEDIA SOLUTIONS LIMITED
CIN L74990MH2010PLC208218 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://exhiconevents.in/investor-2/
TARGET FOLDER: L74990MH2010PLC208218__EXHICON EVENTS MEDIA SOLUTIONS LIMITED
Expected foreign subs (2): Green Branch Contracting & Land Scaping LLC; Maple Heights Business Centre LLC

### RAJRATAN GLOBAL WIRE LIMITED
CIN L27106MP1988PLC004778 | NSE RAJRATAN | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://rajratan.co.in/investors/
TARGET FOLDER: L27106MP1988PLC004778__RAJRATAN GLOBAL WIRE LIMITED
Expected foreign subs (2): Rajratan Thai Wire co. Limited; Rajratan Wire USA Inc.

### TEMBO GLOBAL INDUSTRIES LIMITED
CIN L24100MH2010PLC204331 | NSE TEMBO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://tembo.in/investors/
TARGET FOLDER: L24100MH2010PLC204331__TEMBO GLOBAL INDUSTRIES LIMITED
Expected foreign subs (2): Tembo LLC; United Global Industries Limited

### Meesho Limited
CIN L74900KA2015PLC082263 | NSE MEESHO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74900KA2015PLC082263__MEESHO LIMITED
Expected foreign subs (2): PT Fashnear Technology Indonesia, Indonesia; Fashnear Shenzhen Trading Co. Ltd, China

### BRIGHT BROTHERS LIMITED
CIN L25209MH1946PLC005056 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://brightbrothers.co.in/investor-relations/
TARGET FOLDER: L25209MH1946PLC005056__BRIGHT BROTHERS LIMITED
Expected foreign subs (2): Sintex Logistics LLC; Bright Brothers LLC

### AKUMS DRUGS AND PHARMACEUTICALS LIMITED
CIN L24239DL2004PLC125888 | NSE AKUMS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.akums.in/investors/subsidiary-accounts/
TARGET FOLDER: L24239DL2004PLC125888__AKUMS DRUGS AND PHARMACEUTICALS LIMITED
Expected foreign subs (2): AHL UK Ltd; Akums Healthcare UK Limited

### KANORIA CHEMICALS & INDUSTRIES LTD
CIN L24110WB1960PLC024910 | NSE KANORICHEM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.kanoriachem.com/investors/subsidiary-accounts
TARGET FOLDER: L24110WB1960PLC024910__KANORIA CHEMICALS AND INDUSTRIES LTD
Expected foreign subs (2): APAG Holding AG; Kanoria Africa

### LANCER CONTAINER LINES LIMITED
CIN L74990MH2011PLC214448 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.lancerline.com/investor-relations.php
TARGET FOLDER: L74990MH2011PLC214448__LANCER CONTAINER LINES LIMITED
Expected foreign subs (2): Argo Anchor Shipping Service LLC; LANCIA SHIPPING L.L.C

### WENDT INDIA LIMITED
CIN L85110KA1980PLC003913 | NSE WENDT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.wendtindia.com/investors/
TARGET FOLDER: L85110KA1980PLC003913__WENDT INDIA LIMITED
Expected foreign subs (2): Wendt Grinding Technologies Limited; Wendt Grinding GmbH (WGG)

### VETO SWITCHGEARS AND CABLES LIMITED
CIN L31401MH2007PLC171844 | NSE VETO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: http://www.vetoswitchgears.com/uploads/2024/
TARGET FOLDER: L31401MH2007PLC171844__VETO SWITCHGEARS AND CABLES LIMITED
Expected foreign subs (2): Veto Oversease Private FZE; Veto Overseas Private F.Z.E.

### EMMVEE PHOTOVOLTAIC POWER LIMITED
CIN L26101KA2007PLC042197 | NSE EMMVEE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L26101KA2007PLC042197__EMMVEE PHOTOVOLTAIC POWER LIMITED
Expected foreign subs (2): Emmvee Energy GmbH; Emmvee Energy Inc

### EXHICON EVENTS MEDIA SOLUTIONS LIMITED
CIN L74990PN2010PLC254841 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74990PN2010PLC254841__EXHICON EVENTS MEDIA SOLUTIONS LIMITED
Expected foreign subs (2): Green Branch Contracting & Land Scaping LLC; Maple Heights Business Centre LLC

### MRS.BECTORS FOOD SPECIALITIES LIMITED
CIN L74899PB1995PLC033417 | NSE BECTORFOOD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74899PB1995PLC033417__MRS.BECTORS FOOD SPECIALITIES LIMITED
Expected foreign subs (2): Mrs. Bectors Food International (FZE); Mrs. Bectors Food International (FZE)

### BALAXI PHARMACEUTICALS LIMITED
CIN L25191TG1942PLC121598 | NSE BALAXI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://balaxipharma.in/investor-landing-page
TARGET FOLDER: L25191TG1942PLC121598__BALAXI PHARMACEUTICALS LIMITED
Expected foreign subs (2): Balaxi Global DMCC,Dubai; Balaxi Healthcare

### SAI LIFE SCIENCES LIMITED
CIN L24110TG1999PLC030970 | NSE SAILIFE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.sailife.com/investors/
TARGET FOLDER: L24110TG1999PLC030970__SAI LIFE SCIENCES LIMITED
Expected foreign subs (2): Sai Life Sciences Inc.; Sai Life Sciences GmbH

### CHAMBAL FERTILISERS AND CHEMICALS LIMITED
CIN L24124RJ1985PLC003293 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://investor.chambalfertilisers.com/Disclosures_Under_Regulation_46.html
TARGET FOLDER: L24124RJ1985PLC003293__CHAMBAL FERTILISERS AND CHEMICALS LIMITED
Expected foreign subs (2): CFCL Ventures Limited; ISGN Corporation

### ABANS ENTERPRISES LIMITED
CIN L74120MH1985PLC035243 | NSE ABANSENT | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://abansenterprises.com/financial-statement-subsidiaries
TARGET FOLDER: L74120MH1985PLC035243__ABANS ENTERPRISES LIMITED
Expected foreign subs (2): Abans Gems and Jewels Trading FZC; Splendid International Limited

### DEEPAK NITRITE LIMITED
CIN L24110GJ1970PLC001735 | NSE DEEPAKNTR | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.godeepak.com/investors-overview/
TARGET FOLDER: L24110GJ1970PLC001735__DEEPAK NITRITE LIMITED
Expected foreign subs (2): Deepak NitriteCorporation, Inc.; Deepak Oman Industries (SFZ) LLC

### BEST AGROLIFE LIMITED
CIN L74110DL1992PLC116773 | NSE BESTAGRO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74110DL1992PLC116773__BEST AGROLIFE LIMITED
Expected foreign subs (2): BEST AGROLIFE GLOBAL; BEST AGROLIFE GLOBAL
