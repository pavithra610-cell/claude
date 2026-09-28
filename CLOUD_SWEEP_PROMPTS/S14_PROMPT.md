# CLOUD SWEEP SLICE S14 - 25 PARENTS (27-Sep-2026)
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
### KELLTON TECH SOLUTIONS LIMITED
CIN L72200TG1993PLC016819 | NSE KELLTONTEC | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.kellton.com/subsidiary-financials
TARGET FOLDER: L72200TG1993PLC016819__KELLTON TECH SOLUTIONS LIMITED
Expected foreign subs (2): Kellton Tech Solutions Inc; Kellton Tech Inc

### IND SWIFT LIMITED
CIN L24230CH1986PLC006897 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24230CH1986PLC006897__IND SWIFT LIMITED
Expected foreign subs (1): Indswift India Limited

### NECTAR LIFE SCIENCES LIMITED
CIN L21000PB1995PLC016664 | NSE NECLIFE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L21000PB1995PLC016664__NECTAR LIFE SCIENCES LIMITED
Expected foreign subs (1): Neclife PT Unipessoal LDA

### PANAMA PETROCHEM LIMITED
CIN L23209GJ1982PLC005062 | NSE PANAMAPET | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L23209GJ1982PLC005062__PANAMA PETROCHEM LIMITED
Expected foreign subs (1): Panol Industries RMC FZE

### HINDUSTAN PETROLEUM CORPORATION LIMITED
CIN L23201MH1952GOI008858 | NSE HINDPETRO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.hindustanpetroleum.com/financial
TARGET FOLDER: L23201MH1952GOI008858__HINDUSTAN PETROLEUM CORPORATION LIMITED
Expected foreign subs (1): HPCL Middle East FZCO

### COAL INDIA LTD GOVT OF INDIA UNDERTAKING
CIN L23109WB1973GOI028844 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L23109WB1973GOI028844__COAL INDIA LTD GOVT OF INDIA UNDERTAKING
Expected foreign subs (1): Coal India Africana Limitada

### EVEXIA LIFECARE LIMITED
CIN L23100GJ1990PLC014692 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L23100GJ1990PLC014692__EVEXIA LIFECARE LIMITED
Expected foreign subs (1): Evexia Lifecare Africa Limited

### UNIVERSUS PHOTO IMAGINGS LIMITED
CIN L22222UP2011PLC103611 | NSE UNIVPHOTO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L22222UP2011PLC103611__UNIVERSUS PHOTO IMAGINGS LIMITED
Expected foreign subs (1): JPF Netherland B.V.

### REPRO INDIA LIMITED
CIN L22200MH1993PLC071431 | NSE REPRO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L22200MH1993PLC071431__REPRO INDIA LIMITED
Expected foreign subs (1): REPRO DMCC

### THE INDIAN WOOD PRODUCTS CO LTD
CIN L20101WB1919PLC003557 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L20101WB1919PLC003557__THE INDIAN WOOD PRODUCTS CO LTD
Expected foreign subs (1): N.A

### KSS Limited
CIN L22100MH1995PLC092438 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L22100MH1995PLC092438__KSS LIMITED
Expected foreign subs (1): K SERA SERA PRODUCTIONS FZE

### THE WESTERN INDIA PLYWOODS LIMITED
CIN L20211KL1945PLC001708 | NSE WIPL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L20211KL1945PLC001708__THE WESTERN INDIA PLYWOODS LIMITED
Expected foreign subs (1): ERA & WIP Timber JV SDN BHD

### KHADIM INDIA LIMITED
CIN L19129WB1981PLC034337 | NSE KHADIM | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L19129WB1981PLC034337__KHADIM INDIA LIMITED
Expected foreign subs (1): Khadim Shoe Bangladesh Limited

### CHEMBOND MATERIAL TECHNOLOGIES LIMITED
CIN L24100MH1975PLC018235 | NSE CHEMBOND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.chembondindia.com/investor-relation/
TARGET FOLDER: L24100MH1975PLC018235__CHEMBOND MATERIAL TECHNOLOGIES LIMITED
Expected foreign subs (1): Chembond Water Technologies (Thailand) Co. Ltd

### REMEDIUM LIFECARE LIMITED
CIN L24100MH1988PLC343805 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24100MH1988PLC343805__REMEDIUM LIFECARE LIMITED
Expected foreign subs (1): Remlife Global PTE Ltd

### JUBILANT INDUSTRIES LIMITED
CIN L24100UP2007PLC032909 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24100UP2007PLC032909__JUBILANT INDUSTRIES LIMITED
Expected foreign subs (1): Jubilant Industries Inc. USA

### HIKAL LIMITED
CIN L24200MH1988PTC048028 | NSE HIKAL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24200MH1988PTC048028__HIKAL LIMITED
Expected foreign subs (1): Hikal LLC, USA

### KKALPANA INDUSTRIES (INDIA) LIMITED
CIN L19202WB1985PLC039431 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L19202WB1985PLC039431__KKALPANA INDUSTRIES (INDIA) LIMITED
Expected foreign subs (1): Kkalpana Plastic Reprocess Industries Middleeast FZE

### SANCO INDUSTRIES LIMITED
CIN L24100DL1989PLC035549 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24100DL1989PLC035549__SANCO INDUSTRIES LIMITED
Expected foreign subs (1): Sanjita Polymet Limited

### INTERGLOBE AVIATION LIMITED
CIN L62100DL2004PLC129768 | NSE INDIGO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L62100DL2004PLC129768__INTERGLOBE AVIATION LIMITED
Expected foreign subs (1): InterGlobe Aviation Financial Services IFSC Private Limited

### ESCONET TECHNOLOGIES LIMITED
CIN L62099DL2012PLC233739 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L62099DL2012PLC233739__ESCONET TECHNOLOGIES LIMITED
Expected foreign subs (1): Esconet Singapore Pte. Ltd

### CG VAK SOFTWARE AND EXPORTS LIMITED
CIN L30009TZ1994PLC005568 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L30009TZ1994PLC005568__CG VAK SOFTWARE AND EXPORTS LIMITED
Expected foreign subs (1): CG-VAK Software USA Inc

### TCI EXPRESS LIMITED
CIN L62200TG2008PLC061781 | NSE TCIEXP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.tciexpress.in/investor-analyst-corner.aspx?invid=13
TARGET FOLDER: L62200TG2008PLC061781__TCI EXPRESS LIMITED
Expected foreign subs (1): TCI Express Pte. Ltd

### MEP INFRASTRUCTURE DEVELOPERS LIMITED
CIN L45200MH2002PLC136779 | NSE MEP | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45200MH2002PLC136779__MEP INFRASTRUCTURE DEVELOPERS LIMITED
Expected foreign subs (1): MEPIDL Enterprises LLC

### PROZONE REALTY LIMITED
CIN L45200MH2007PLC174147 | NSE PROZONER | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://prozonerealty.com/investors-details
TARGET FOLDER: L45200MH2007PLC174147__PROZONE REALTY LIMITED
Expected foreign subs (1): PROZONE LIBERTY INTERNATIONAL LIMITED
