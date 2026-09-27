# CLOUD SWEEP SLICE S04 - 25 PARENTS (27-Sep-2026)
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
### MAYUR UNIQUOTERS LIMITED
CIN L18101RJ1992PLC006952 | NSE MAYURUNIQ | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.mayuruniquoters.com/financial-results-of-subsidary.php
TARGET FOLDER: L18101RJ1992PLC006952__MAYUR UNIQUOTERS LIMITED
Expected foreign subs (4): Mayur Uniquoters Corp.; Mayur Uniquoters SA (Pty) Ltd.; Futura Textiles Inc.; UAB FUTURA TEXTILES EUROPE

### PENNAR INDUSTRIES LIMITED
CIN L27109TG1975PLC001919 | NSE PENIND | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.pennarindia.com/financial-information.php
TARGET FOLDER: L27109TG1975PLC001919__PENNAR INDUSTRIES LIMITED
Expected foreign subs (4): Pennar Global Inc; Pennar GmbH; Pennar FZCO; Pennar FZCO

### PRAVEG LIMITED
CIN L24231GJ1995PLC024809 | NSE PRAVEG | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.dizcoverpraveg.com/financial-reporting
TARGET FOLDER: L24231GJ1995PLC024809__PRAVEG LIMITED
Expected foreign subs (4): Praveg Communications USA Inc.; Praveg Communications (AUS) Pty Ltd; Praveg Safari Kenya Limited; Praveg Safari Tanzania Limited

### BALKRISHNA INDUSTRIES LIMITED
CIN L99999MH1961PLC012185 | NSE BALKRISIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.bkt-tires.com/en-us/download-category/investor-disclosures/?subcategory=financial-data
TARGET FOLDER: L99999MH1961PLC012185__BALKRISHNA INDUSTRIES LIMITED
Expected foreign subs (4): BKT EUROPE S.R.L; BKT TIRES INC.; BKT USA INC; BKT TIRES (CANADA) INC

### GRAUER AND WEIL (INDIA) LIMITED
CIN L74999MH1957PLC010975 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://growel.com/financial/AnnualReport/
TARGET FOLDER: L74999MH1957PLC010975__GRAUER AND WEIL (INDIA) LIMITED
Expected foreign subs (4): Growels Chemicals Co. Limited; Growel Chemicals Limited; Grauer and Weil Middle East FZE; Grauer & Weil (Shanghai) Limited

### SAREGAMA INDIA LIMITED
CIN L22213WB1946PLC014346 | NSE SAREGAMA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.saregama.com/static/investors#financialStat
TARGET FOLDER: L22213WB1946PLC014346__SAREGAMA INDIA LIMITED
Expected foreign subs (4): Saregama Inc, United States of America; Saregama Limited (Formerly Known as Saregama Plc), United Kingdom; Saregama FZE, Dubai; RPG Global Music Limited, Mauritius

### BAWEJA STUDIOS LIMITED
CIN L92112MH2001PLC131253 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L92112MH2001PLC131253__BAWEJA STUDIOS LIMITED
Expected foreign subs (4): Baweja Studios LLC; Three Knot Studio Ltd; Baweja Studios LLC; Three Knot Studio Ltd

### DUDIGITAL GLOBAL LIMITED
CIN L74110DL2007PLC171939 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74110DL2007PLC171939__DUDIGITAL GLOBAL LIMITED
Expected foreign subs (4): Dudigital Global LLC; Virtuworld Tourism LL.C; Duverify LLC FZ; Duverify LLC FZ

### AKSH OPTIFIBRE LIMITED
CIN L24305RJ1986PLC016132 | NSE AKSHOPTFBR | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.akshoptifibre.com/financial-results.php
TARGET FOLDER: L24305RJ1986PLC016132__AKSH OPTIFIBRE LIMITED
Expected foreign subs (4): Aksh Technologies (Mauritius) Limited; AOL FZE; AOL Composites (Jiangsu) Co. Ltd.; AOL Technologies FZE

### TRANSPORT CORPORATION OF INDIA LIMITED
CIN L70109TG1995PLC019116 | NSE TCI | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://tcil.com/disclosures/
TARGET FOLDER: L70109TG1995PLC019116__TRANSPORT CORPORATION OF INDIA LIMITED
Expected foreign subs (4): TCI Nepal Pvt. Ltd.; TCI Bangladesh Limited; TCIL Middle East Logistics Services LLC; TCI Holdings Asia Pacific Pte. Limited

### CRANES SOFTWARE INTERNATIONAL LIMITED
CIN L05190KA1984PLC031621 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L05190KA1984PLC031621__CRANES SOFTWARE INTERNATIONAL LIMITED
Expected foreign subs (4): Systat Software GmbH; Cranes Software International Pte. Ltd.; Systat Software Inc,. USA; Cranes Software Inc.,(Earlier known as NISA Software Inc)

### HAPPIEST MINDS TECHNOLOGIES LIMITED
CIN L72900KA2011PLC057931 | NSE HAPPSTMNDS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.happiestminds.com/investors/Financial%20Results/2024-2025-Q4/
TARGET FOLDER: L72900KA2011PLC057931__HAPPIEST MINDS TECHNOLOGIES LIMITED
Expected foreign subs (4): Happiest Minds Inc; InnovazIT Technologies LLC; GAVS Technologies LLC; GAVS Technologies Saudi Arabia for Telecommunications and Information Technology

### BOROSIL RENEWABLES LIMITED
CIN L26100MH1962PLC012538 | NSE BORORENEW | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://borosilrenewables.com/investor/subsidiaries-financials
TARGET FOLDER: L26100MH1962PLC012538__BOROSIL RENEWABLES LIMITED
Expected foreign subs (4): Interfloat Corporation; Laxman AG; GMB Glasmanufaktur Brandenburg GmbH; Geosphere Glassworks GmbH

### ADVANCE METERING TECHNOLOGY LIMITED
CIN L31401DL2011PLC271394 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://pkrgroup.in/index.php/investor-release/
TARGET FOLDER: L31401DL2011PLC271394__ADVANCE METERING TECHNOLOGY LIMITED
Expected foreign subs (4): P K R TECHNOLOGIES CANADA LIMITED; Advance Power and Trading GmbH; Global Power and Trading (GPAT) PTE Lt d . Singapore; PKR Canada Technology Limited

### BAJAJ STEEL INDUSTRIES LIMITED
CIN L27100MH1961PLC011936 | NSE BAJAJST | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://bajajngp.com/investor-relations/
TARGET FOLDER: L27100MH1961PLC011936__BAJAJ STEEL INDUSTRIES LIMITED
Expected foreign subs (4): Bajaj Coneagle LLC; Bajaj Continental LTDA; Bajaj Services LTDA; Bajaj Steel Industries (U) Limited

### MAXIMUS INTERNATIONAL LIMITED
CIN L51900GJ2015PLC085474 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.maximusinternational.in/investors.php
TARGET FOLDER: L51900GJ2015PLC085474__MAXIMUS INTERNATIONAL LIMITED
Expected foreign subs (4): Maximus Lubricants LLC; Maximus Global FZE; Quantum Lubricants (E.A.) Limited; MX Africa Limited

### SAKSOFT LIMITED
CIN L72200TN1999PLC054429 | NSE SAKSOFT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.saksoft.com/investor-relations/financials-annual-reports/
TARGET FOLDER: L72200TN1999PLC054429__SAKSOFT LIMITED
Expected foreign subs (4): Saksoft Inc & its subsidiaries; Saksoft Solutions Ltd and its subsidiaries; Saksoft Pte Ltd and its subsidiaries; DreamOrbit Inc

### WANBURY LIMITED
CIN L51900MH1988PLC048455 | NSE WANBURY | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.wanbury.com/wanbury/www/fin-result.html
TARGET FOLDER: L51900MH1988PLC048455__WANBURY LIMITED
Expected foreign subs (4): WANBURY HOLDING B.V; WANBURY GLOBAL FZE; NINGXIA WANBURY FINE CHEMICALS CO.LTD; Wanbury Holding B.V (Netherland)

### SIMPLEX INFRASTRUCTURES LIMITED
CIN L45209WB1924PLC004969 | NSE SIMPLEXINF | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.simplexinfra.com/page.aspx?mid=27
TARGET FOLDER: L45209WB1924PLC004969__SIMPLEX INFRASTRUCTURES LIMITED
Expected foreign subs (4): SIMPLEX (MIDDLE EAST) LIMITED; SIMPLEX INFRASTRUCTURES LIBYA JOINT VENTURE CO.; Simplex Infrastructures Libiya Joint Venture Co.; Simplex Infrastructures Libya Joint Venture Co.

### McLEOD RUSSEL INDIA LIMITED
CIN L51109WB1998PLC087076 | NSE MCLEODRUSS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.mcleodrussel.com/investors/subsidiaries-reports-and-accounts.aspx
TARGET FOLDER: L51109WB1998PLC087076__MCLEOD RUSSEL INDIA LIMITED
Expected foreign subs (4): McLeod Russel Uganda Limited (MRUL); McLeod Russel Africa Limited (MRAL); McLeod Russel Middle East DMCC (MRME); Borelli Tea Holdings Limited (BTHL)

### MAZAGON DOCK SHIPBUILDERS LIMITED
CIN L35100MH1934GOI002079 | NSE MAZDOCK | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L35100MH1934GOI002079__MAZAGON DOCK SHIPBUILDERS LIMITED
Expected foreign subs (4): Colombo Dockyard PLC; DOCKYARD GENERAL ENGINEERING SERVICES LIMITED; DOCKYARD TOTAL SOLUTION (PRIVATE) LIMITED; CEYLON SHIPPING AGENCY (PRIVATE) LIMITED

### R.P.P INFRA PROJECTS LIMITED
CIN L45201TZ1995PLC006113 | NSE RPPINFRA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.rppipl.com/investor.php
TARGET FOLDER: L45201TZ1995PLC006113__R.P.P INFRA PROJECTS LIMITED
Expected foreign subs (4): RPP Infra Projects (Lanka) Limited; RPP Infra Overseas PLC; RPP Infra Projects Gabon; RPP Realtors Pvt Ltd

### MARINE ELECTRICALS (INDIA) LIMITED
CIN L31907MH2007PLC176443 | NSE MARINE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://marineelectricals.com
TARGET FOLDER: L31907MH2007PLC176443__MARINE ELECTRICALS (INDIA) LIMITED
Expected foreign subs (4): STI Company SRL; STI SRL; MEL Power Systems FZC; Xanatos Marine Ltd

### PROTEAN EGOV TECHNOLOGIES LIMITED
CIN L72900MH1995PLC095642 | NSE PROTEAN | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://cms.proteantech.in/sites/default/files/2025-05/
TARGET FOLDER: L72900MH1995PLC095642__PROTEAN EGOV TECHNOLOGIES LIMITED
Expected foreign subs (4): Protean International DMCC; NSDL e-Governance (Malaysia) Sdn. Bhd.; Protean eGov Technologies Australia Pty Ltd; NSDL e-Governance (Malaysia) Sdn. Bhd.

### APTECH LIMITED
CIN L72900MH2000PLC123841 | NSE APTECHT | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.aptech-worldwide.com/pages/investor-relations/investorrelations_subsidiary_companies.aspx
TARGET FOLDER: L72900MH2000PLC123841__APTECH LIMITED
Expected foreign subs (4): APTECH TRAINING LIMITED, FZE; AGLSM SDN.BHD MALAYSIA; APTECH VENTURES LIMITED; APTECH INVESTMENT ENHANCERS LIMITED
