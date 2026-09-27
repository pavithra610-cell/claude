# CLOUD SWEEP SLICE R01 - 11 PARENTS (FY26 SUBS FINANCIALS, 27-Sep-2026)
Standing instruction for this whole session; do not re-read it. Commit each parent before starting the next, on branch sweep/R01. If a site is unreachable say NETWORK BLOCKED. PRIORITY: FY26 files only; an FY25 file is listed as SUB_FS_FY25_FALLBACK only when the parent has NOT yet published its FY26 set at all.

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
### GODREJ CONSUMER PRODUCTS LIMITED
CIN L24246MH2000PLC129806 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.godrejcp.com/subsidiary-financials
TARGET FOLDER: L24246MH2000PLC129806__GODREJ CONSUMER PRODUCTS LIMITED
MISSING SUBSIDIARIES TO FIND (49): PT Godrej Consumer Products Indonesia (Indonesia); Subinite (Pty) Ltd. (South Africa); Strength of Nature LLC (United States); Laboratoria Cuenca S.A (Argentina); Beleza Mozambique LDA (Mozambique); Godrej Consumer Products International (FZCO) (United Arab Emirates); Lorna Nigeria Ltd. (Nigeria); Hair Trading (offshore) S. A. L (Lebanon); Godrej Global Mid East FZE (United Arab Emirates); Cosmetica Nacional (Chile); Weave Ghana Ltd (Ghana); Weave Mozambique Limitada (Mozambique); Godrej Tanzania Holdings Ltd (Mauritius); Godrej Household Products (Bangladesh) Pvt. Ltd. (Bangladesh); Canon Chemicals Limited (Kenya); Godrej Household Products (Lanka) Pvt. Ltd. (Sri Lanka); Hair Credentials Zambia Limited (Zambia); PT Indomas Susemi Jaya (Indonesia); Godrej Nigeria Limited (Nigeria); Godrej Holdings (Chile) Limitada (Chile); Godrej Consumer Investments (Chile) Spa (Chile); Deciral SA (Uruguay); Godrej SON Holdings INC (United States); PT Godrej Distribution Indonesia (Indonesia); Godrej Mauritius Africa Holdings Ltd. (Mauritius); PT Godrej Business Service Indonesia (Indonesia); Style Industries Limited (Kenya); PT Sarico Indah (Indonesia); Godrej Consumer Products Holding (Mauritius) Limited (Mauritius); Godrej South Africa Proprietary Ltd (South Africa); Godrej Indonesia IP Holding Ltd. (Mauritius); Issue Group Brazil Limited (Brazil); Weave IP Holdings Mauritius Pvt. Ltd. (Mauritius); Kinky Group (Pty) Limited (South Africa); Frika Weave (PTY) LTD (South Africa); Godrej West Africa Holdings Ltd. (Mauritius); Godrej MID East Holdings Limited (United Arab Emirates); Old Pro International Inc (United States); Panamar Producciones S.A. (Argentina); Weave Trading Mauritius Pvt. Ltd. (Mauritius); Godrej CP Malaysia SDN. BHD (Malaysia); Consell SA (Argentina) (Argentina); Consell SA (Argentina); Godrej Africa Holdings Limited (Mauritius); Charm Industries Limited (Kenya); Darling Trading Company Mauritius Ltd (Mauritius); DGH Phase Two Mauritius (Mauritius); DGH Tanzania Limited (Mauritius); Godrej Consumer Products Bangladesh Ltd (Bangladesh)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### TORRENT PHARMACEUTICALS LTD
CIN L24230GJ1972PLC002126 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.torrentpharma.com/investors/financial-info/subsidiary-reports/
TARGET FOLDER: L24230GJ1972PLC002126__TORRENT PHARMACEUTICALS LTD
MISSING SUBSIDIARIES TO FIND (22): Torrent Do Brasil Ltda. (Brazil) (Brazil); Torrent Pharma Inc. (USA) (United States); Heumann Pharma GmbH & Co. Generica KG (Germany); Torrent Pharma Philippines Inc. (Philippines) (Philippines); Heunet Pharma GmbH (Germany); Laboratorios Torrent, S.A. De C.V. (Mexico) (Mexico); Torrent Pharma (UK) Ltd (United Kingdom) (United Kingdom); Zao Torrent Pharma (Russia) (Russia); Laboratories Torrent (Malaysia) SDN. BHD. (Malaysia) (Malaysia); Torrent Pharma (Thailand) Co., Ltd. (Thailand) (Thailand); Curatio Inc. (Philippines); Torrent Pharma Gmbh (Germany) (Germany); Torrent Australasia Pty Ltd (Australia); Torrent Pharmaceuticals Chile SpA (Chile); Torrent International Lanka (Pvt) Ltd (Formerly known as Curatio International Lanka (Private) Ltd) (Sri Lanka); Curatio INC., Philippines (Philippines); Curatio International Lanka (Pvt) Ltd, Sri Lanka (Sri Lanka); Curatio International Lanka (Pvt) Ltd (Sri Lanka); OOO Unique Pharmaceutical Laboratories** (Russian Federation); Unique Pharmaceutical Laboratories FZE** (United Arab Emirates); JBCPL Philippines Inc.** (Philippines); Biotech Laboratories (Pty.) Ltd.** (South Africa)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SEQUENT SCIENTIFIC LIMITED
CIN L99999TS1985PLC196357 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://sequent.in/investor-relation/
TARGET FOLDER: L99999TS1985PLC196357__SEQUENT SCIENTIFIC LIMITED
MISSING SUBSIDIARIES TO FIND (14): Alivira Animal Health Limited (Ireland); Provet Veteriner Urunleri San. Ve Tic. A. S. (Turkey); Alivira Saude Animal Ltda. (formerly known as Evance Saude Animal Ltda) (Brazil); Topkim Topkapi Ilac premiks Sanayi Ve Ticaret A.S. (Turkey); Expeden Distribuidora De Produtos Veterinarios Ltda (formerly known as Evanvet Distribuidora De Produtos Veterinarios Ltda) (Brazil); Laboratorios Karizoo, S.A. DE C.V. (Mexico) (Mexico); Laboratorios Karizoo, S.A. (Spain); Phytotherapic Solutions S.L (Spain); Fendigo BV (Netherlands); Bremer Pharma GmbH (Germany); Vila Vina Participacions S.L. (Spain); Alivira France S.A.S. (France); Alivira Animal Health USA LLC (United States); Alviria Saude Animal Brasil Participacoes Ltda (Brazil)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### BERGER PAINTS INDIA LIMITED
CIN L51434WB1923PLC004793 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.bergerpaints.com/investors
TARGET FOLDER: L51434WB1923PLC004793__BERGER PAINTS INDIA LIMITED
MISSING SUBSIDIARIES TO FIND (8): Bolix S.A (Poland); BERGER JENSON & NICHOLSON (NEPAL) PVT LIMITED (Nepal); Soltherm Isolations Thermique Exterieure SAS (France); Berger Paints Overseas Limited (Russia); Bolix UKRAINE sp. z.o.o (Ukraine); Berger Paints (Cyprus) Limited (Cyprus); Build Trade sp. z.o.o (Poland); Lusako Trading Limited (Cyprus)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ELECTROSTEEL CASTINGS LTD
CIN L27310OR1955PLC000310 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.electrosteel.com/investor/accounts-of-subsidiaries.php
TARGET FOLDER: L27310OR1955PLC000310__ELECTROSTEEL CASTINGS LTD
MISSING SUBSIDIARIES TO FIND (7): Electrosteel Europe S.A. (France); Electrosteel Bahrain Holding W.L.L (Bahrain); Electrosteel USA, LLC (United States); Electrosteel Castings Gulf FZE (United Arab Emirates); Electrosteel Doha for Trading LLC (Qatar); Singardo International Pte. Ltd. (Singapore); Electrosteel Trading, S.A. (Spain)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ATUL LIMITED
CIN L99999GJ1975PLC002859 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L99999GJ1975PLC002859__ATUL LIMITED
MISSING SUBSIDIARIES TO FIND (6): Atul USA Inc (United States); Atul China Ltd (China); Atul Middle East FZ-LLC (United Arab Emirates); Atul Ireland Ltd (Ireland); Atul Brasil Quimicos Ltda (Brazil); Atul Deutschland GmbH (Germany)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ZODIAC CLOTHING COMPANY LIMITED
CIN L17100MH1984PLC033143 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.zodiaconline.com/pages/investorrelations
TARGET FOLDER: L17100MH1984PLC033143__ZODIAC CLOTHING COMPANY LIMITED
MISSING SUBSIDIARIES TO FIND (5): Zodiac Clothing Company INC - USA (United States); Zodiac Clothing Co. (U.A.E.) LLC (United Arab Emirates); Zodiac Clothing Bangladesh Limited (Bangladesh); Zela Technologies, Inc. (United States); Zodiac Clothing Co. S.A. - Switzerland (Switzerland)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ASHOK LEYLAND LIMITED
CIN L34101TN1948PLC000105 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.ashokleyland.com/investor/financialinfo/
TARGET FOLDER: L34101TN1948PLC000105__ASHOK LEYLAND LIMITED
MISSING SUBSIDIARIES TO FIND (4): Ashok Leyland (UAE) LLC (United Arab Emirates); Albonair GmbH (Germany); Ashok Leyland (Nigeria) Limited (Nigeria); ASHOK LEYLAND CHILE (Chile)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### GUJARAT FLUOROCHEMICALS LIMITED
CIN L24304HP2018PLC011898 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://gfl.co.in/Investor_Relations.php
TARGET FOLDER: L24304HP2018PLC011898__GUJARAT FLUOROCHEMICALS LIMITED
MISSING SUBSIDIARIES TO FIND (4): GFCL EV Products Americas LLC (United States); GFCL EV (SFZ) SPC (OMAN); GFCL EV Products Pte. Ltd (Singapore); GFCL EV Products GmbH (Germany)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### GOKALDAS EXPORTS LIMITED
CIN L18101MH2004PLC468826 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L18101MH2004PLC468826__GOKALDAS EXPORTS LIMITED
MISSING SUBSIDIARIES TO FIND (3): Amibros S.A., Panama (operating as a branch in the name of Atraco Industrial Enterprises in Dubai) (Panama); Gokaldas Exports Corporation (United States); Nava Apparels L.L.C-FZ (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SUNDRAM FASTENERS LIMITED
CIN L35999TN1962PLC004943 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L35999TN1962PLC004943__SUNDRAM FASTENERS LIMITED
MISSING SUBSIDIARIES TO FIND (3): Sundram Fasteners Zhejiang Limited (China); TVS Next Inc (United States); Sundram International Inc (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.
