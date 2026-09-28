# CLOUD SWEEP SLICE R04 - 11 PARENTS (FY26 SUBS FINANCIALS, 27-Sep-2026)
Standing instruction for this whole session; do not re-read it. Commit each parent before starting the next, on branch sweep/R04. If a site is unreachable say NETWORK BLOCKED. PRIORITY: FY26 files only; an FY25 file is listed as SUB_FS_FY25_FALLBACK only when the parent has NOT yet published its FY26 set at all.

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
### R SYSTEMS INTERNATIONAL LIMITED
CIN L74899DL1993PLC053579 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.rsystems.com/subsidiaries-financials/
TARGET FOLDER: L74899DL1993PLC053579__R SYSTEMS INTERNATIONAL LIMITED
MISSING SUBSIDIARIES TO FIND (27): R Systems, Inc., USA (United States); R Systems Computaris Europe SRL, Romania (Romania); R Systems (Singapore) Pte Limited, Singapore (Singapore); R Systems Computaris Poland Sp. z o.o., Poland (Poland); RSYS Technologies Ltd., Canada (Canada); R Systems IBIZCS Pte. Ltd., Singapore (Singapore); R Systems Consulting Services (M) Sdn. Bhd., Malaysia (Malaysia); R Systems Technologies Limited, USA (United States); R Systems Consulting Services (Thailand) Co. Ltd., Thailand (Thailand); R Systems Consulting Services Limited, Singapore (Singapore); R Systems Computaris S.R.L., Moldova (MOLDOVA, REPUBLIC OF); R Systems IBIZCS Sdn. Bhd., Malaysia (Malaysia); R Systems Computaris International Limited, UK (United Kingdom); PT. R Systems IBIZCS International, Indonesia (Indonesia); IBIZ Consulting (Thailand) Co. Ltd., Thailand (Thailand); R Systems Computaris Philippines Pte. Ltd. Inc., Philippines (Philippines); IBIZ Consulting Service Shanghai Co., Ltd., China (China); R Systems Computaris Malaysia Sdn. Bhd., Malaysia (Malaysia); R Systems Consulting Services (Shanghai) Co., Ltd., China (China); R Systems Computaris Suisse Sarl, Switzerland (Switzerland); IBIZ Consulting Service Limited, Hong Kong (Hong Kong); R Systems Consulting Services (Hong Kong) Limited, Hong Kong (Hong Kong); R Systems Consulting Services Kabushiki Kaisha, Japan (Japan); RSIL Mexico, S. de R.L. de C.V., Mexico (Mexico); R Systems Consulting Services Company Limited, Vietnam (Vietnam); Novigo for Information Technology (Saudi Arabia); Novigo Solutions Inc (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SIS LIMITED
CIN L75230BR1985PLC002083 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://sisindia.com/financials-subsidiary-companies/
TARGET FOLDER: L75230BR1985PLC002083__SIS LIMITED
MISSING SUBSIDIARIES TO FIND (21): SIS Australia Group Pty Ltd (Australia); MSS Security Pty Ltd (Australia); Southern Cross Protection Pty Ltd (Australia); MSS Strategic Medical and Rescue Pty Ltd (Australia); SIS Henderson Holdings Pte Ltd (Singapore); Platform 4 Group Limited (New Zealand); Safety Direct Solutions Pty Ltd (Australia); Triton Security Services Limited (New Zealand); Charter Security Protective Services Pty Ltd (Australia); Safety Direct Solutions Pty Ltd NZ (New Zealand); SIS MSS Security Holdings Pty Ltd (Australia); SIS Security International Holdings Pte. Ltd. (formerly SIS International Holdings Limited) (Singapore); Australian Security Connections Pty Ltd (Australia); SIS Security Asia Pacific Holdings Pte. Limited (formerly SIS Asia Pacific Holdings Limited) (Singapore); SIS Australia Holdings Pty Ltd (Australia); SIS Group International Holdings Pty Ltd (Australia); State Medical Assistance Holdings Pty Ltd (Australia); Western Australia Patient Transport Pty Ltd (Australia); State Medical Assistance - Victoria Pty Ltd (Australia); State Medical Assistance Pty Ltd (Australia); Clinical Governance Specialists Pty Ltd (Australia)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### VA TECH WABAG LIMITED
CIN L45205TN1995PLC030231 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.wabag.com/information-under-reg-46-of-sebilodr/
TARGET FOLDER: L45205TN1995PLC030231__VA TECH WABAG LIMITED
MISSING SUBSIDIARIES TO FIND (11): VA Tech Wabag (Singapore) Pte. Ltd., Singapore (Singapore); VA Tech Wabag Tunisie S.A.R.L., Tunisia (Tunisia); VA Tech Wabag (Philippines) Inc., Philippines (Philippines); Wabag Belhasa JV WLL, Bahrain (Bahrain); VA Tech Wabag Su Teknolojisi Ve Tic. A.S , Turkey (Turkey); VA Tech Wabag Muscat LLC., Oman (Oman); VA Tech Wabag Limited Pratibha Industries Limited JV, Nepal (Nepal); VA Tech Wabag Deutschland, GmbH.,Germany (Germany); VA Tech Wabag and Roots Contracting L.L.C. ,Qatar (Qatar); Wabag Muhibbah JV SDN. BHD., Malaysia (Malaysia); Wabag Limited, Thailand (Thailand)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### BIRLASOFT LIMITED
CIN L72200PN1990PLC059594 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.birlasoft.com/sites/default/files/resources/downloads/investors/annual-reports/
TARGET FOLDER: L72200PN1990PLC059594__BIRLASOFT LIMITED
MISSING SUBSIDIARIES TO FIND (7): Birlasoft Solutions Inc. (United States); Birlasoft Computer Corporation (United States); Birlasoft Consulting, Inc. (United States); Birlasoft Solutions France (France); Birlasoft Solutions GmbH (Germany); Birlasoft Solutions ME FZE (United Arab Emirates); Birlasoft GmbH, Germany (Germany)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### RENAISSANCE GLOBAL LIMITED
CIN L36911MH1989PLC054498 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://renaissanceglobal.com/subsidiary-accounts/
TARGET FOLDER: L36911MH1989PLC054498__RENAISSANCE GLOBAL LIMITED
MISSING SUBSIDIARIES TO FIND (6): Renaissance Jewelry N.Y Inc (United States); Verigold Jewellery FZCO (United Arab Emirates); RD2C Ventures Inc, USA (United States); Jean Dousset Jewelry LLc USA (Subsidiary of RD2C Ventures Inc) (United States); Renaissance FMI Inc., USA (Subsidiary of RD2C Ventures Inc) (United States); RD2C Ventures Inc (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### LMW LIMITED
CIN L29269TZ1962PLC000463 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.lmwglobal.com/investors/financial-and-meeting-information/subsidiaries.html
TARGET FOLDER: L29269TZ1962PLC000463__LMW LIMITED
MISSING SUBSIDIARIES TO FIND (6): NIL (NIL); LMW Global FZE, UAE (United Arab Emirates); LMW Textile Machinery (Suzhou) Co.Limited, China (China); LMW Textile Machinery (Suzhou) Co.Limited, China * (China); LMW Middle East FZE (United Arab Emirates); LMW Holding Limited, UAE (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### METROPOLIS HEALTHCARE LIMITED
CIN L73100MH2000PLC192798 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.metropolisindia.com/newdata/Investors/Subsidiary/subsidiary-financials-2023-2024/
TARGET FOLDER: L73100MH2000PLC192798__METROPOLIS HEALTHCARE LIMITED
MISSING SUBSIDIARIES TO FIND (4): Metropolis Star Lab Kenya Limited (Kenya); Metropolis Healthcare Lanka Pvt. Limited (Formerly known as Nawaloka Metropolis Laboratories Private Limited) (Sri Lanka); Metropolis Bramser Lab Services (Mtius) Limited (Mauritius); Metropolis Bramser Lab Services (Mtius) Ltd (Mauritius)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### NCC LIMITED
CIN L72200TG1990PLC011146 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.ncclimited.com/subsidiary-financials.html
TARGET FOLDER: L72200TG1990PLC011146__NCC LIMITED
MISSING SUBSIDIARIES TO FIND (4): Nagarjuna Construction Company International L.L.C. (OMAN); Al Mubarakia Contracting Co. L.L.C. (United Arab Emirates); NCCA International Kuwait General Contracts Company L.L.C. (KUWAIT); Nagarjuna Contracting Co. L.L.C. (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### DYNAMATIC TECHNOLOGIES LIMITED
CIN L72200KA1973PLC002308 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: http://www.dynamatics.com/annual-reports
TARGET FOLDER: L72200KA1973PLC002308__DYNAMATIC TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (4): Dynamatic Limited UK (United Kingdom); Eisenwerk Erla GmbH (Germany); Dynamatic LLC (United States); JKM Global Pte Limited (Réunion)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ROLTA INDIA LIMITED
CIN L74999MH1989PLC052384 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L74999MH1989PLC052384__ROLTA INDIA LIMITED
MISSING SUBSIDIARIES TO FIND (3): Rolta International Inc.(Consolidated) (United States); Rolta Saudi Arabia Ltd (Saudi Arabia); Rolta Middle East FZ-LLC (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### VERITAS (INDIA) LIMITED
CIN L23209MH1985PLC035702 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L23209MH1985PLC035702__VERITAS (INDIA) LIMITED
MISSING SUBSIDIARIES TO FIND (2): Veritas International FZE (United Arab Emirates); Verasco FZE (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.
