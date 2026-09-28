# CLOUD SWEEP SLICE S13 - 25 PARENTS (27-Sep-2026)
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
### GANESHA ECOSPHERE LIMITED
CIN L51109UP1987PLC009090 | NSE GANECOS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.ganeshaecosphere.com/subsidiary/
TARGET FOLDER: L51109UP1987PLC009090__GANESHA ECOSPHERE LIMITED
Expected foreign subs (2): GANESHA OVERSEAS PRIVATE LIMITED; Ganesa Overseas Private Limited

### IFB INDUSTRIES LTD
CIN L51109WB1974PLC029637 | NSE IFBIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.ifbindustries.com/assets/
TARGET FOLDER: L51109WB1974PLC029637__IFB INDUSTRIES LTD
Expected foreign subs (2): Global Automative & Appliances Pte Limited; Thai Automotive and Appliances Limited

### EMMBI INDUSTRIES LIMITED
CIN L17120DN1994PLC000387 | NSE EMMBI | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://emmbi.com/financial-results/
TARGET FOLDER: L17120DN1994PLC000387__EMMBI INDUSTRIES LIMITED
Expected foreign subs (2): ZASTIAN PTE. LTD; Zastian Europe GmbH

### KESAR INDIA LIMITED
CIN L51220MH2003PLC142989 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L51220MH2003PLC142989__KESAR INDIA LIMITED
Expected foreign subs (2): M/s DEJA VUE-FZCO; Kesar Middle East-FZCO

### I G PETROCHEMICALS LIMITED
CIN L51496GA1988PLC000915 | NSE IGPL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.igpetro.com/subsidiaries-financial-statements/
TARGET FOLDER: L51496GA1988PLC000915__I G PETROCHEMICALS LIMITED
Expected foreign subs (2): IGPL International Ltd.; IGPL Energy Ltd.

### INOX INDIA LIMITED
CIN L99999GJ1976PLC018945 | NSE INOXINDIA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://inoxcva.com/investor-relation.php
TARGET FOLDER: L99999GJ1976PLC018945__INOX INDIA LIMITED
Expected foreign subs (2): INOXCVA Europe B.V.; INOXCVA Comercio E Industria De Equipmentos Criogenicos Ltda. **

### McNALLY BHARAT ENGG CO LTD
CIN L45202WB1961PLC025181 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L45202WB1961PLC025181__MCNALLY BHARAT ENGG CO LTD
Expected foreign subs (2): MBE Minerals Zambia Limited; MBE Mineral Technologies Pte Ltd

### COSYN LIMITED
CIN L72200TG1994PLC017415 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.cosyn.in/content/annual-report/
TARGET FOLDER: L72200TG1994PLC017415__COSYN LIMITED
Expected foreign subs (2): COSYN LLC; WELL TO DESK

### NMDC LIMITED
CIN L13100TG1958GOI001674 | NSE NMDC | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.nmdc.co.in/investors/company-information
TARGET FOLDER: L13100TG1958GOI001674__NMDC LIMITED
Expected foreign subs (2): Legacy Iron Ore Limited; NMDC SARL

### PRADEEP METALS LIMITED
CIN L99999MH1982PLC026191 | NSE PRADPME | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.pradeepmetals.com/financial-reports/
TARGET FOLDER: L99999MH1982PLC026191__PRADEEP METALS LIMITED
Expected foreign subs (2): Pradeep Metals Limited, Inc.; Dimensional Machine Works, LLC

### DEV LABTECH VENTURE LIMITED
CIN L36100GJ1993PLC019374 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L36100GJ1993PLC019374__DEV LABTECH VENTURE LIMITED
Expected foreign subs (2): DEV LABTECH VENTURE INC.; DEV LABTECH VENTURE INC.

### FCS SOFTWARE SOLUTIONS LIMITED
CIN L72100DL1993PLC179154 | NSE FCSSOFT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://fcsltd.com/investors/financials/subsidiaries
TARGET FOLDER: L72100DL1993PLC179154__FCS SOFTWARE SOLUTIONS LIMITED
Expected foreign subs (2): FCS Software Solutions GmbH; FCS Software (Sanghai) Co., Ltd.

### SATTRIX INFORMATION SECURITY LIMITED
CIN L72200GJ2013PLC076845 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200GJ2013PLC076845__SATTRIX INFORMATION SECURITY LIMITED
Expected foreign subs (2): Sattrix Information Security DMCC; Sattrix Information Security Inc

### STRING METAVERSE LIMITED
CIN L62099TG1994PLC017207 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L62099TG1994PLC017207__STRING METAVERSE LIMITED
Expected foreign subs (2): String Fintech HK Limited; Kling Digital Assets FZCO

### FUTURE CONSUMER LIMITED
CIN L52602MH1996PLC192090 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L52602MH1996PLC192090__FUTURE CONSUMER LIMITED
Expected foreign subs (2): Aussee Oats Milling (Private) Limited; FCEL Overseas FZCO

### SUNDROP BRANDS LIMITED
CIN L15142TG1986PLC006957 | NSE SUNDROP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.sundropbrands.com/investor-relations.aspx
TARGET FOLDER: L15142TG1986PLC006957__SUNDROP BRANDS LIMITED
Expected foreign subs (2): Agro Tech Foods (Bangladesh) Pvt.Ltd.; Sundrop Foods Lanka (Private) Limited

### XCHANGING SOLUTIONS LIMITED
CIN L72200KA2002PLC030072 | NSE XCHANGING | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://dxc.com/in/en/about-us/xchanging-solutions-limited-investor-relations
TARGET FOLDER: L72200KA2002PLC030072__XCHANGING SOLUTIONS LIMITED
Expected foreign subs (2): Xchanging Solutions Singapore Pte Ltd.; Xchanging Solutions (USA), Inc.

### Coffee Day Enterprises Limited
CIN L55101KA2008PLC046866 | NSE COFFEEDAY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L55101KA2008PLC046866__COFFEE DAY ENTERPRISES LIMITED
Expected foreign subs (2): A N Coffeeday International Limited; Coffee Day Gastronomie Und Kaffeehandles GmbH

### TANVI FOODS (INDIA) LIMITED
CIN L15433TG2007PLC053406 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L15433TG2007PLC053406__TANVI FOODS (INDIA) LIMITED
Expected foreign subs (2): Tanvi Foods USA Inc; Tanvi Foods USA Inc

### MISHTANN FOODS LIMITED
CIN L15400GJ1981PLC004170 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L15400GJ1981PLC004170__MISHTANN FOODS LIMITED
Expected foreign subs (2): Grow and Grub Nutrients FZ-LLC; Grow & More Nutrifoods PTE LTD

### XELPMOC DESIGN AND TECH LIMITED
CIN L72200KA2015PLC082873 | NSE XELPMOC | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.xelpmoc.in/investorrelations
TARGET FOLDER: L72200KA2015PLC082873__XELPMOC DESIGN AND TECH LIMITED
Expected foreign subs (2): Xelpmoc Design and Tech UK Ltd; Xelpmoc Design and Tech UK Ltd

### TRIGYN TECHNOLOGIES LIMITED
CIN L72200MH1986PLC039341 | NSE TRIGYN | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.trigyn.com/investor-relations
TARGET FOLDER: L72200MH1986PLC039341__TRIGYN TECHNOLOGIES LIMITED
Expected foreign subs (2): TRIGYN TECCHNOLOGIES INC.; TRIGYN TECHNOLOGIES SCHWEIZ GMBH

### ZEN TECHNOLOGIES LIMITED
CIN L72200TG1993PLC015939 | NSE ZENTEC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.zentechnologies.com/investors.html
TARGET FOLDER: L72200TG1993PLC015939__ZEN TECHNOLOGIES LIMITED
Expected foreign subs (2): Zen Technologies INC; Zen UAE Defence LLC

### Quick Heal Technologies Limited
CIN L72200MH1995PLC091408 | NSE QUICKHEAL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.quickheal.co.in/media/documents/investors/
TARGET FOLDER: L72200MH1995PLC091408__QUICK HEAL TECHNOLOGIES LIMITED
Expected foreign subs (2): Seqrite Technologies DMCC; Quick Heal Technologies America Inc.

### TIMESCAN LOGISTICS (INDIA) LIMITED
CIN L60232TN2006PLC061351 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L60232TN2006PLC061351__TIMESCAN LOGISTICS (INDIA) LIMITED
Expected foreign subs (2): Timescan Logistics (Malaysia) Sdn. Bhd.; Timescan Logistics (Malaysia) Sdn. Bhd.
