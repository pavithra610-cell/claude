# CLOUD SWEEP SLICE R06 - 10 PARENTS (FY26 SUBS FINANCIALS, 27-Sep-2026)
Standing instruction for this whole session; do not re-read it. Commit each parent before starting the next, on branch sweep/R06. If a site is unreachable say NETWORK BLOCKED. PRIORITY: FY26 files only; an FY25 file is listed as SUB_FS_FY25_FALLBACK only when the parent has NOT yet published its FY26 set at all.

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
### NEPHROCARE HEALTH SERVICES LIMITED
CIN L85100TG2009PLC066359 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L85100TG2009PLC066359__NEPHROCARE HEALTH SERVICES LIMITED
MISSING SUBSIDIARIES TO FIND (22): Nephrocare Health Services Central Asia (UZBEKISTAN); Nephrocare Health Services Central Asia (UZBEKISTAN); Nephrocare Health Care Services, Philippines Inc. (Philippines); Renal Therapy Solutions Inc. (Philippines); Anram Medical Group Inc. (Philippines); Medical Experts Group and Associates Inc. (Philippines); Cadiz Dialysis Hub Inc. (Philippines); Universe Dialysis and Kidney Care Centre Inc. (Philippines); Curis Cavite Renal Corporation Inc. (Philippines); People’s Center for Hemodialysis Care Inc. (Philippines); St. Margareth Dialysis and Biocare Centre Inc. (Philippines); Dialysis Asia and Patient Care Center Inc. (Philippines); Curis Hemodialysis Clinic Inc. (Philippines); Mega Health Dialysis Centre Inc. (Philippines); Rizal Dialysis and Wellness Center Inc (Philippines); Kolff Dialysis Inc (Philippines); Carmona Dialysis Systems Inc (Philippines); Bioregen Hemo Center Inc (Philippines); Nephrocare Health Services Saudi Arabia Company (Saudi Arabia); Infini Care health Systems Inc (Philippines); AIZ Hemodialysis Center Inc (Philippines); Nephrocare Health Services Nepal Private Limited (Nepal)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SONATA SOFTWARE LIMITED
CIN L72200MH1994PLC082110 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.sonata-software.com/about-us/investor-relations
TARGET FOLDER: L72200MH1994PLC082110__SONATA SOFTWARE LIMITED
MISSING SUBSIDIARIES TO FIND (14): Sonata Software North America Inc (United States); Quant Systems Inc. (United States); Sonata Australia Pty Ltd (Australia); Sonata Latin America S. DE R.L. DE C.V. (Mexico); Sonata Software Malaysia SDN BHD (Malaysia); Sonata Software GmbH (Germany); Sonata Software Japan KK (Japan); Sonata Software Intercontinental Limited (Ireland); GAPbuster Inc. (United States); Sonata Software Canada Limited (Canada); Sonata Software (Shanghai) Co., Ltd (China); Sonata Software Worldwide Malaysia SDN. BHD. (Malaysia); Sonata Software (Qatar) LLC (Qatar); Sonata Software Solutions (Egypt)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ARVIND LIMITED
CIN L17119GJ1931PLC000093 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.arvind.com/investors/annual_reports
TARGET FOLDER: L17119GJ1931PLC000093__ARVIND LIMITED
MISSING SUBSIDIARIES TO FIND (8): Arvind Worldwide Inc. USA (United States); Arvind Overseas (Mauritius) Limited (Mauritius); Arvind Niloy Exports Pvt. Ltd (Bosnia and Herzegovina); Arvind Envisol PLC (Ethiopia); Arvind Enterprises (FZC) (United Arab Emirates); Arvind Worldwide (M) Inc. (Mauritius); Arvind Spinning Limited (Mauritius); Arvind Textile Mills Limited (Bangladesh)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### MINDTECK (INDIA) LIMITED
CIN L30007KA1991PLC039702 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.mindteck.com/investors/subsidiaries-financials
TARGET FOLDER: L30007KA1991PLC039702__MINDTECK (INDIA) LIMITED
MISSING SUBSIDIARIES TO FIND (8): Mindteck Germany GmbH (Germany); Mindteck Middle East Ltd. WLL (Bahrain); Mindteck Inc. (United States); Mindteck Software Malaysia SDN. BHD. (Malaysia); Mindteck Singapore Pte. Ltd. (Singapore); Chendle Holdings Ltd. (VIRGIN ISLANDS, BRITISH); Mindteck Solutions Philippines, Inc. (Philippines); Mindteck Canada, Inc. (Canada)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### AXISCADES TECHNOLOGIES LIMITED
CIN L72200KA1990PLC084435 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.axiscades.com/investor-relation/
TARGET FOLDER: L72200KA1990PLC084435__AXISCADES TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (6): AXISCADES Inc. (USA) (United States); AXISCADES Technology Canada Inc. (Canada); add solution GmbH (Germany); Mistral Solutions Inc (United States); Axis Mechanical Engineering Design (Wuxi) Co. Ltd. (China); AXISCADES GmbH (Germany)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ADVANCED ENZYME TECHNOLOGIES LIMITED
CIN L24200MH1989PLC051018 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.advancedenzymes.com/investors/quarterly-updates/financial-results/
TARGET FOLDER: L24200MH1989PLC051018__ADVANCED ENZYME TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (6): Advanced Enzymes USA, Inc. (United States); evoxx technologies GmbH (Germany); Enzyme Innovation, Inc (Wholly owned subsidiary of Cal India Foods International) (United States); Advanced Supplementary Technologies Corporation (Wholly owned subsidiary of Advanced Enzymes USA, Inc.) (United States); Cal India Foods International (Wholly owned subsidiary of Advanced Enzymes USA, Inc.) (United States); Starya Labs Inc. (Wholly owned subsidiary of Advanced Enzymes USA, Inc. w.e.f. 9 December 2024) (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### KDDL LIMITED
CIN L33302HP1981PLC008123 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.kddl.com/financial-dashboard-yearly/
TARGET FOLDER: L33302HP1981PLC008123__KDDL LIMITED
MISSING SUBSIDIARIES TO FIND (4): Estima AG (Switzerland); Pylania S.A. (Switzerland); Silvercity Brands AG (Switzerland); Favre Leuba GmbH (Switzerland)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### MARKSANS PHARMA LIMITED
CIN L24110MH1992PLC066364 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L24110MH1992PLC066364__MARKSANS PHARMA LIMITED
MISSING SUBSIDIARIES TO FIND (3): Marksans Pharma Inc (United States); Nova Pharmaceuticals Australasia Pty Ltd (Australia); Access Healthcare For Medical Products LLC (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SETCO AUTOMOTIVE LIMITED
CIN L35999GJ1982PLC005203 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://setcoauto.com/financial-statements-of-subsidiaries/
TARGET FOLDER: L35999GJ1982PLC005203__SETCO AUTOMOTIVE LIMITED
MISSING SUBSIDIARIES TO FIND (3): Setco Automotive N.A. Inc. (United States); Setco MEA DMCC (United Arab Emirates); WEW Holdings Limited (Mauritius)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### HIMADRI SPECIALITY CHEMICAL LIMITED
CIN L27106WB1987PLC042756 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.himadri.com/home/performance
TARGET FOLDER: L27106WB1987PLC042756__HIMADRI SPECIALITY CHEMICAL LIMITED
MISSING SUBSIDIARIES TO FIND (3): Shangdong Dawn Himadri Chemical Industry Limited (China); SHANDONG DAWN HIMADRI CHEMICAL LIMITED (China); Shandong Dawn Himadri Chemical Industry Ltd (China)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.
