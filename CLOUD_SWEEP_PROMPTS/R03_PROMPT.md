# CLOUD SWEEP SLICE R03 - 11 PARENTS (FY26 SUBS FINANCIALS, 27-Sep-2026)
Standing instruction for this whole session; do not re-read it. Commit each parent before starting the next, on branch sweep/R03. If a site is unreachable say NETWORK BLOCKED. PRIORITY: FY26 files only; an FY25 file is listed as SUB_FS_FY25_FALLBACK only when the parent has NOT yet published its FY26 set at all.

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
### INDEGENE LIMITED
CIN L73100KA1998PLC102040 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://ir.indegene.com/en/investor-relations/financial-information/
TARGET FOLDER: L73100KA1998PLC102040__INDEGENE LIMITED
MISSING SUBSIDIARIES TO FIND (29): Indegene, Inc. (USA) (United States); Cult Health, LLC (USA) (United States); Trilogy Writing & Consulting GmbH (Germany) (Germany); Trilogy Writing & Consulting Inc. (USA) (United States); Services Indegene Aptilon Inc. (Canada) (Canada); DT Associates Research and Consulting Services Limited (UK) (United Kingdom); DT Associates Research and Consulting, Inc. (USA) (United States); Trilogy Writing & Consulting Limited (UK) (United Kingdom); Indegene Healthcare UK Limited (UK) (United Kingdom); Indegene Europe LLC (Switzerland) (Switzerland); Indegene Godo Kaisha, Japan LLC (Japan) (Japan); Trilogy Writing & Consulting ULC (Canada) (Canada); Indegene Ireland Limited (Ireland) (Ireland); Indegene Fareast Pte Ltd (Singapore) (Singapore); Indegene Healthcare Germany GmbH (Germany) (Germany); Indegene Healthcare Mexico S DE RL DE CV (Mexico) (Mexico); ILSL Holdings, Inc. (USA) (United States); Indegene Spain, S.L.U (Spain); Indegene Lifesystems Consulting (Shanghai) Co. Ltd. (China) (China); Biopharm Parent Holding Inc. (United States); Biopharm Communications, LLC (United States); Addressable Health LLC (United States); Cake Kommunikations GmbH (AT) (Austria); Cake Kommunikations AG (Switzerland) (Switzerland); Cake Kommunikations GmbH (DE) (Germany); Cake Kommunikations Holdings GmbH (Austria); Warn & Co Limited** (United Kingdom); Indegene Healthcare Canada, Inc (Canada); Warn & Co Limited (United Kingdom)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### Emcure Pharmaceuticals Limited
CIN L24231PN1981PLC024251 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.emcure.com/disclosure-under-reg/financial-statement-of-subsidiary-companies/
TARGET FOLDER: L24231PN1981PLC024251__EMCURE PHARMACEUTICALS LIMITED
MISSING SUBSIDIARIES TO FIND (18): Marcan Pharmaceuticals Inc (Canada); Mantra Pharma Inc. (Canada); Emcure Pharmaceuticals South Africa (Pty) Limited (South Africa); Tillomed Italia SRL (Italy); Tillomed Malta Ltd. (MALTA); Emcure Pharmaceuticals Mena FZ LLC (United Arab Emirates); Emcure Pharma Chile SpA (Chile); Tillomed Pharma GmbH (Germany); Emcure Pharma Peru S.A.C (PERU); Lazor Pharmaceuticals Ltd. (Kenya); Emcure Pharma Philippines Inc. (Philippines); Emcure Pharma Mexico S.A. DE C.V. (Mexico); Tillomed France SAS (France); Laboratorios Tillomed Spain SLU (Spain); Emcure Pharmaceuticals Pty Ltd (Australia); Emcure Brazil farmaceutica Ltda (Brazil); Emcure Nigeria Limited (Nigeria); Emcure Pharmaceuticals Dominicana (DOMINICAN REPUBLIC)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### Tata Consumer Products Limited
CIN L15491WB1962PLC031425 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.tataconsumer.com/investors/investor-relations/subsidiaries/subsidiary-financials
TARGET FOLDER: L15491WB1962PLC031425__TATA CONSUMER PRODUCTS LIMITED
MISSING SUBSIDIARIES TO FIND (20): Tata Coffee Vietnam Company Ltd. (Vietnam); Tata Consumer Products US Holdings Inc. (United States); Stansand (Africa) Ltd. (Kenya); Tata Consumer Products Polska.sp.zo.o (Poland); Tata Tea Extractions Inc. (under liquidation) (United States); Good Earth Teas Inc. (United States); Consolidated Coffee Inc. ( under liquidation) (United States); Onomento Co Ltd. (Non Operating entity) (Cyprus); Stansand Ltd. (Dormant) (United Kingdom); Good Earth Corporation (United States); Tata Global Beverages Holdings Ltd. (Dormant) (United Kingdom); Drassington Ltd. (Dormant) (United Kingdom); Tata Global Beverages Services Ltd. (Dormant) (United Kingdom); Tata Global Beverages Investment Ltd. (Dormant) (United Kingdom); Tata Global Beverages Overseas Ltd. (Dormant) (United Kingdom); Tata Waters LLC (United States); Stansand Brokers Ltd. (Dormant) (United Kingdom); Lyons Tetley Ltd. (Dormant) (United Kingdom); Suntyco Holdings Ltd. (Non Operating entity) (Cyprus); Eight O'Clock Holdings Inc. (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### EICHER MOTORS LIMITED
CIN L34102DL1982PLC129877 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L34102DL1982PLC129877__EICHER MOTORS LIMITED
MISSING SUBSIDIARIES TO FIND (7): Royal Enfield Brasil Comercio de Motocicletas Ltda (Brazil); Royal Enfield North America Limited (RENA) (United States); Royal Enfield (Thailand) Limited (Thailand); VECV South Africa (Pty) Ltd (South Africa); Royal Enfield Canada Limited (Canada); VECV Lanka (Private) Limited (Sri Lanka); PT VECV Automotive Indonesia (Indonesia)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SONA BLW PRECISION FORGINGS LIMITED
CIN L27300HR1995PLC083037 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://sonacomstar.com/investor-relations
TARGET FOLDER: L27300HR1995PLC083037__SONA BLW PRECISION FORGINGS LIMITED
MISSING SUBSIDIARIES TO FIND (6): Nirsen d.o.o. Beograd- Zvezdara (SERBIA); Novelic GmbH (Germany); Novelic SRL (Romania); Novelic Esc Dooel Skopje (North Macedonia); Comstar Hong Kong Mexico No. 1, LLC (United States); Comestel Automotive Technologies Mexicana, S. DE R.L. DE C.V. (Mexico)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### EXPLEO SOLUTIONS LIMITED
CIN L64202TN1998PLC066604 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L64202TN1998PLC066604__EXPLEO SOLUTIONS LIMITED
MISSING SUBSIDIARIES TO FIND (6): Expleo Solutions LLC. (United Arab Emirates); Expleo Solutions Inc. (United States); Expleo Solutions FZE, UAE (United Arab Emirates); Expleo Solutions FZE. (United Arab Emirates); Expleo Solutions Arabia Limited (Saudi Arabia); Expleo Solutions Arabia Limited (Saudi Arabia)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### TANLA PLATFORMS LIMITED
CIN L72200TG1995PLC021262 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.tanla.com/investor-relations/annual-reports
TARGET FOLDER: L72200TG1995PLC021262__TANLA PLATFORMS LIMITED
MISSING SUBSIDIARIES TO FIND (7): Karix Mobile FZ LLC (United Arab Emirates); Tanla Mobile Asia Pacific Pte Ltd (Singapore); ValueFirst Digital Media Pte Limited (Singapore); Tanla Mobile Middle East LLC (Saudi Arabia); PT Karix Communications Indonesia (Indonesia); Karix Mobile LLC, at Kingdom of Saudi Arabia (Saudi Arabia); Karix Brasil LTDA (Brazil)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### JASH ENGINEERING LTD
CIN L28910MP1973PLC001226 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://jashindia.com/investors/
TARGET FOLDER: L28910MP1973PLC001226__JASH ENGINEERING LTD
MISSING SUBSIDIARIES TO FIND (4): Rodney Hunt Inc. (United States); Jash USA INC (United States); Mahr Maschinenbau GmBH (Austria); Engineering and Manufacturing Jash Limited (Hong Kong)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### GODREJ INDUSTRIES LIMITED
CIN L24241MH1988PLC097781 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.godrejindustries.com/investors
TARGET FOLDER: L24241MH1988PLC097781__GODREJ INDUSTRIES LIMITED
MISSING SUBSIDIARIES TO FIND (5): Godrej International Trading & Investment Pte. Ltd. (Singapore); Godrej Fund Management Pte. Ltd. (Singapore); Godrej Properties Worldwide Inc., USA (United States); Comercializadora Agricola Agroastrachem Cia Ltda (Colombia); Astec Europe Sprl (Belgium)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### JUBILANT INGREVIA LIMITED
CIN L24299UP2019PLC122657 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.jubilantingrevia.com/investors/financials/subsidiaries-accounts
TARGET FOLDER: L24299UP2019PLC122657__JUBILANT INGREVIA LIMITED
MISSING SUBSIDIARIES TO FIND (3): Jubilant Life Sciences NV (Belgium); Jubilant Ingrevia (USA) Inc. (formerly known as Jubilant Life Sciences (USA) Inc.) (United States); Jubilant Life Sciences (Shanghai) Limited (China)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SRF LIMITED
CIN L18101DL1970PLC005197 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L18101DL1970PLC005197__SRF LIMITED
MISSING SUBSIDIARIES TO FIND (2): SRF Flexipak (South Africa)(Pty) Limited (South Africa); SRF Industex Belting (Pty) Limited (South Africa)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.
