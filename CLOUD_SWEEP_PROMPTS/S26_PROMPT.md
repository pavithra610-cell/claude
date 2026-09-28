# CLOUD SWEEP SLICE S26 - 18 PARENTS (27-Sep-2026)
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
### NECTAR LIFE SCIENCES LIMITED
CIN L24232PB1995PLC016664 | NSE NECLIFE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24232PB1995PLC016664__NECTAR LIFE SCIENCES LIMITED
Expected foreign subs (1): Neclife PT Unipessoal LDA

### Suraj Products Limited
CIN L26942OR1991PLC002865 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L26942OR1991PLC002865__SURAJ PRODUCTS LIMITED
Expected foreign subs (1): SURAJ IRON & STEEL MANUFACTURERS - L.L.C.- S.P.C

### KWALITY PHARMACEUTICALS LIMITED
CIN L24232PB1983PLC005426 | NSE KPL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24232PB1983PLC005426__KWALITY PHARMACEUTICALS LIMITED
Expected foreign subs (1): Kwality Pharmaceuticals Africa Limitada

### PRECISION CAMSHAFTS LIMITED
CIN L24231PN1992PLC067126 | NSE PRECAM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://pclindia.in/index.php/financials_new/
TARGET FOLDER: L24231PN1992PLC067126__PRECISION CAMSHAFTS LIMITED
Expected foreign subs (1): PCL (International)Holding B.V. (Consolidated) Basis

### PUNJAB CHEMICALS AND CROP PROTECTION LIMITED
CIN L24231PB1975PLC047063 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.punjabchemicals.com/annual-reports/
TARGET FOLDER: L24231PB1975PLC047063__PUNJAB CHEMICALS AND CROP PROTECTION LIMITED
Expected foreign subs (1): SD Agchem (Europe) NV

### UNIMECH AEROSPACE AND MANUFACTURING LIMITED
CIN L30305KA2016PLC095712 | NSE UNIMECH | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L30305KA2016PLC095712__UNIMECH AEROSPACE AND MANUFACTURING LIMITED
Expected foreign subs (1): Unimech Global Manufacturing Solutions Inc.(With effect from May 29, 2024)

### Aeroflex Enterprises Limited
CIN L25199MH1984PLC034632 | NSE AEROENTER | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L25199MH1984PLC034632__AEROFLEX ENTERPRISES LIMITED
Expected foreign subs (1): ITALICA GLOBAL FZC

### TEXMO PIPES AND PRODUCTS LIMITED
CIN L25200MP2008PLC020852 | NSE TEXMOPIPES | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://texmopipe.com/investors/
TARGET FOLDER: L25200MP2008PLC020852__TEXMO PIPES AND PRODUCTS LIMITED
Expected foreign subs (1): Tapti Pipes and Products Limited FZE

### NILE LIMITED
CIN L27029AP1984PLC004719 | NSE NILE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: http://www.nilelimited.com/subsidiary-reports.html
TARGET FOLDER: L27029AP1984PLC004719__NILE LIMITED
Expected foreign subs (1): Nile Overseas Enterprise FZE


### GSS INFOTECH LIMITED
CIN L72200TG2003PLC041860 | NSE GSS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200TG2003PLC041860__GSS INFOTECH LIMITED
Expected foreign subs (1): GSS Infotech Inc (Delaware)

### KAJARIA CERAMICS LIMITED
CIN L26924HR1985PLC056150 | NSE KAJARIACER | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.kajariaceramics.com/investor?tab=report-11
TARGET FOLDER: L26924HR1985PLC056150__KAJARIA CERAMICS LIMITED
Expected foreign subs (1): Kajaria International DMCC

### SHANKARA BUILDING PRODUCTS LIMITED
CIN L26922KA1995PLC018990 | NSE SHANKARA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L26922KA1995PLC018990__SHANKARA BUILDING PRODUCTS LIMITED
Expected foreign subs (1): Steel Network Holdings Pte Limited

### NITCO LIMITED
CIN L26920MH1966PLC016547 | NSE NITCO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.nitco.in/corporate/investors/subsidiary-companies
TARGET FOLDER: L26920MH1966PLC016547__NITCO LIMITED
Expected foreign subs (1): Reliant Properties and Realty LLP

### SHREE RAMA MULTI-TECH LIMITED
CIN L25200GJ1993PLC020880 | NSE SHREERAMA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L25200GJ1993PLC020880__SHREE RAMA MULTI-TECH LIMITED
Expected foreign subs (1): SHREE RAMA (MAURITIUS) LIMITED

### GRINDWELL NORTON LIMITED
CIN L26593MH1950PLC008163 | NSE GRINDWELL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.grindwellnorton.co.in/investors
TARGET FOLDER: L26593MH1950PLC008163__GRINDWELL NORTON LIMITED
Expected foreign subs (1): Saint-Gobain Ceramic Materials Bhutan Private Limited

### XPRO INDIA LIMITED
CIN L25209WB1997PLC085972 | NSE XPROINDIA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L25209WB1997PLC085972__XPRO INDIA LIMITED
Expected foreign subs (1): Xpro Dielectric Films FZ-LLC

### SHISH INDUSTRIES LIMITED
CIN L25209GJ2017PLC097273 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L25209GJ2017PLC097273__SHISH INDUSTRIES LIMITED
Expected foreign subs (1): GreenEnergy International INC.

### TECHNO ELECTRIC & ENGINEERING COMPANY LIMITED
CIN L40108UP2005PLC094368 | NSE TECHNOE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L40108UP2005PLC094368__TECHNO ELECTRIC AND ENGINEERING COMPANY LIMITED
Expected foreign subs (1): TECHNO ELECTRIC OVERSEAS PTE LTD
