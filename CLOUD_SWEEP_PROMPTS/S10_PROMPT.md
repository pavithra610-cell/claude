# CLOUD SWEEP SLICE S10 - 25 PARENTS (27-Sep-2026)
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
### CAMLIN FINE SCIENCES LIMITED
CIN L74100MH1993PLC075361 | NSE CAMLINFINE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74100MH1993PLC075361__CAMLIN FINE SCIENCES LIMITED
Expected foreign subs (2): CFS Do Brasil Importacao E Exportacao De Aditivos Alimenticios LTDA.; CFS Europe S.p.A.

### GABION TECHNOLOGIES INDIA LIMITED
CIN L74999DL2008PLC195317 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74999DL2008PLC195317__GABION TECHNOLOGIES INDIA LIMITED
Expected foreign subs (2): Gabion Technologies Nepal Private Limited; Gabion Technologies BD Limited

### DMR ENGINEERING LIMITED
CIN L74900HR2009PLC039823 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.dmrengineering.net/financial-statement-of-subsidiaries/
TARGET FOLDER: L74900HR2009PLC039823__DMR ENGINEERING LIMITED
Expected foreign subs (2): DMR Consulting Inc.; DMR Consulting USA Inc.

### S & S POWER SWITCHGEAR LIMITED
CIN L31200TN1975PLC006966 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31200TN1975PLC006966__S AND S POWER SWITCHGEAR LIMITED
Expected foreign subs (2): Acrastyle Ltd., UK; Acrastyle Switchgear Ltd., UK

### SOLARA ACTIVE PHARMA SCIENCES LIMITED
CIN L24230MH2017PLC291636 | NSE SOLARA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://solara.co.in/investor-relations/subsidiary-financials/
TARGET FOLDER: L24230MH2017PLC291636__SOLARA ACTIVE PHARMA SCIENCES LIMITED
Expected foreign subs (2): Shasun USA Inc; Solara Active Pharma Sciences LTDA*

### DCM SHRIRAM LIMITED
CIN L74899DL1989PLC034923 | NSE DCMSHRIRAM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.dcmshriram.com/investors/annual-report
TARGET FOLDER: L74899DL1989PLC034923__DCM SHRIRAM LIMITED
Expected foreign subs (2): Bioseed Research Philippines, INC; Bioseeds Holdings Pte. Ltd.

### ELECTROTHERM (INDIA) LIMITED
CIN L29249GJ1986PLC009126 | NSE ELECTHERM | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.electrotherm.com/public/investors/
TARGET FOLDER: L29249GJ1986PLC009126__ELECTROTHERM (INDIA) LIMITED
Expected foreign subs (2): Jinhua Indus Enterprises Limited; Jinhua Jahari Enterprises Limited

### GLOBTIER INFOTECH LIMITED
CIN L72900UP2012PLC142156 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72900UP2012PLC142156__GLOBTIER INFOTECH LIMITED
Expected foreign subs (2): Globtier USA, LLC; Globtier USA, LLC

### UFLEX LIMITED
CIN L74899DL1988PLC032166 | NSE UFLEX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.uflexltd.com/investors.php
TARGET FOLDER: L74899DL1988PLC032166__UFLEX LIMITED
Expected foreign subs (2): Flex Films (USA) Inc.; Flex P. Films Egypt S.A.E.; Flex Americas S.A. de C.V.; Flex Americas Brasil Ltda; Flex Films Europa Sp. Z.o.o.; Flex Films RUS LLC; Flex Films Europa Korlatolt Felelossegu Tarsasag; Flex Films Africa Pvt Ltd.; Flex Middle East FZE; UFLEX Packaging Inc.; Flex Pet (Egypt) S.A.E.; Flex Foils Bangladesh Private Limited; UPET Holdings Limited; Flex Specialty Chemicals (Egypt) S.A.E.; Plastic Fix Europa Spolka Z Ograniczona Odpowiedzialnoscia (Poland); Uflex Woven Bags S.A. de C.V.; Flex Asepto (Egypt) S.A.E.; Flex FME Pte. Ltd.; Flex Films AZB AFEZCO; Flex Chemicals (P) Ltd. #

### MARSONS LIMITED
CIN L31102WB1976PLC030676 | NSE MARSONS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31102WB1976PLC030676__MARSONS LIMITED
Expected foreign subs (2): Cosol Developments Ltd, UK; COSOL DEVELPMENTS LTD

### BIRLA PRECISION TECHNOLOGIES LIMITED
CIN L29220MH1986PLC041214 | NSE BIRLAPREC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.birlaprecision.com/investor-section-subsidiaries.php
TARGET FOLDER: L29220MH1986PLC041214__BIRLA PRECISION TECHNOLOGIES LIMITED
Expected foreign subs (2): Birla Precision Technologies GmbH; Birla Precision USA Ltd

### SARLA PERFORMANCE FIBERS LIMITED
CIN L31909DN1993PLC000056 | NSE SARLAPOLY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.sarlafibers.com/investors/
TARGET FOLDER: L31909DN1993PLC000056__SARLA PERFORMANCE FIBERS LIMITED
Expected foreign subs (2): Sarlaflex Inc.; Sarla Overseas Holdings Limited

### DMCC SPECIALITY CHEMICALS LIMITED
CIN L24110MH1919PLC000564 | NSE DMCC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.dmcc.com/investor/statutory-information/subsidiaries-financials
TARGET FOLDER: L24110MH1919PLC000564__DMCC SPECIALITY CHEMICALS LIMITED
Expected foreign subs (2): DMCC (Europe) GmbH (Formerly know as Borax Morarji Europe GmbH); DMCC (Europe) GmbH (Formerly Borax Morarji (Europe) GmbH)

### PACE DIGITEK LIMITED
CIN L31909KA2007PLC041949 | NSE PACEDIGITK | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31909KA2007PLC041949__PACE DIGITEK LIMITED
Expected foreign subs (2): Lineage Power Holdings (Singapore) Pte. Ltd; Lineage Power (Myanmar) Limited

### ACCEDERE LIMITED
CIN L32000MH1983PLC030400 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L32000MH1983PLC030400__ACCEDERE LIMITED
Expected foreign subs (2): Accedere Tech Private Ltd; Accedere Tech Private Limited

### OMNITECH ENGINEERING LIMITED
CIN L26100GJ2021PLC124801 | NSE OMNI | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L26100GJ2021PLC124801__OMNITECH ENGINEERING LIMITED
Expected foreign subs (2): Omnitech Group, Inc.; Omnitech Group, Inc

### HLE GLASCOAT LIMITED
CIN L26100GJ1991PLC016173 | NSE HLEGLAS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.hleglascoat.com/audited-financial-statements-of-subsidiaries/
TARGET FOLDER: L26100GJ1991PLC016173__HLE GLASCOAT LIMITED
Expected foreign subs (2): THALETEC GmbH; THALETEC USA INC

### PIRAMAL ENTERPRISES LIMITED
CIN L24110MH1947PLC005719 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24110MH1947PLC005719__PIRAMAL ENTERPRISES LIMITED
Expected foreign subs (2): INDIAREIT Investment Management Co.; Piramal Technologies SA

### KERNEX MICROSYSTEMS (INDIA)LIMITED........
CIN L30007TG1991PLC013211 | NSE KERNEX | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.kernex.in/company/investor-relations/subsidiary-financials/
TARGET FOLDER: L30007TG1991PLC013211__KERNEX MICROSYSTEMS (INDIA)LIMITED........
Expected foreign subs (2): Avant-Grade Info Systems Inc; Avant-Garde Infosystems Inc

### Ramco Industries Limited
CIN L26943TN1965PLC005297 | NSE RAMCOIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://ramcoindltd.com/investors.html
TARGET FOLDER: L26943TN1965PLC005297__RAMCO INDUSTRIES LIMITED
Expected foreign subs (2): Sri Ramco Lanka (Private) Limited; Sri Ramco Roofings Lanka Private Limited

### CYBERTECH SYSTEMS AND SOFTWARE LIMITED
CIN L72100MH1995PLC084788 | NSE CYBERTECH | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://investors.cybertech.com/Investor
TARGET FOLDER: L72100MH1995PLC084788__CYBERTECH SYSTEMS AND SOFTWARE LIMITED
Expected foreign subs (2): CyberTech Systems and Software Inc. USA; Spatialitics LLC USA

### ZAGGLE PREPAID OCEAN SERVICES LIMITED
CIN L65999TG2011PLC074795 | NSE ZAGGLE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://ir.zaggle.in/wp-content/uploads/2025/05/
TARGET FOLDER: L65999TG2011PLC074795__ZAGGLE PREPAID OCEAN SERVICES LIMITED
Expected foreign subs (2): Zaggle Technologies Limited; Zaggle Technologies Limited

### UTI ASSET MANAGEMENT COMPANY LIMITED
CIN L65991MH2002PLC137867 | NSE UTIAMC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.utimf.com/uti-amc-shareholders/financials-filings/subsidiaries-financials
TARGET FOLDER: L65991MH2002PLC137867__UTI ASSET MANAGEMENT COMPANY LIMITED
Expected foreign subs (2): UTI International Ltd.; UTI Investments America Limited

### COUNTRY CLUB HOSPITALITY & HOLIDAYS LIMITED
CIN L70102TG1991PLC012714 | NSE CCHHL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L70102TG1991PLC012714__COUNTRY CLUB HOSPITALITY AND HOLIDAYS LIMITED
Expected foreign subs (2): Country Vacations International Limited; Country Club Babylon Resorts Private Limited

### INDIA POWER CORPORATION LIMITED
CIN L40105WB1919PLC003263 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40105WB1919PLC003263__INDIA POWER CORPORATION LIMITED
Expected foreign subs (2): IPCL Pte Limited; IPCL Pte. Ltd.
