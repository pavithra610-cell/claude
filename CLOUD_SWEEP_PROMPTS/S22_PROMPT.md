# CLOUD SWEEP SLICE S22 - 25 PARENTS (27-Sep-2026)
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
### TRIDENT TECHLABS LIMITED
CIN L74899DL2000PLC105611 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74899DL2000PLC105611__TRIDENT TECHLABS LIMITED
Expected foreign subs (1): Trident Techlabs L.L.C-FZ

### MEDICAMEN ORGANICS LIMITED.
CIN L74899DL1995PLC066416 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74899DL1995PLC066416__MEDICAMEN ORGANICS LIMITED.
Expected foreign subs (1): Depot Pharmacy Yego Limited

### C.E. INFO SYSTEMS LIMITED
CIN L74899DL1995PLC065551 | NSE MAPMYINDIA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.mapmyindia.com/investor/
TARGET FOLDER: L74899DL1995PLC065551__C.E. INFO SYSTEMS LIMITED
Expected foreign subs (1): CE Info Systems International INC., USA

### VASCON ENGINEERS LIMITED
CIN L70100PN1986PLC175750 | NSE VASCONEQ | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L70100PN1986PLC175750__VASCON ENGINEERS LIMITED
Expected foreign subs (1): GMP Technical Solutions Middle East (FZE)

### SMARTWORKS COWORKING SPACES LIMITED
CIN L74900DL2015PLC310656 | NSE SMARTWORKS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.smartworksoffice.com/investors/
TARGET FOLDER: L74900DL2015PLC310656__SMARTWORKS COWORKING SPACES LIMITED
Expected foreign subs (1): Smartworks Space Pte. Ltd.

### ESCORTS KUBOTA LIMITED
CIN L74899HR1944PLC039088 | NSE ESCORTS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.escortskubota.com/investors/regulation-46-of-sebi/subsidiary-financial-statements
TARGET FOLDER: L74899HR1944PLC039088__ESCORTS KUBOTA LIMITED
Expected foreign subs (1): Farmtrac Tractors Europe Sp. Z.o.o, Poland

### SICAGEN INDIA LIMITED
CIN L74900TN2004PLC053467 | NSE SICAGEN | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.sicagen.com/investors/financials-for-subsidiaries/
TARGET FOLDER: L74900TN2004PLC053467__SICAGEN INDIA LIMITED
Expected foreign subs (1): Wilson Cables Private Limited

### EYANTRA VENTURES LIMITED
CIN L72100TG1984PLC167149 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://eyantraventures.com/
TARGET FOLDER: L72100TG1984PLC167149__EYANTRA VENTURES LIMITED
Expected foreign subs (1): EYANTRA VENTURES FZE

### ABM KNOWLEDGEWARE LIMITED
CIN L67190MH1993PLC113638 | NSE ABMKNO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L67190MH1993PLC113638__ABM KNOWLEDGEWARE LIMITED
Expected foreign subs (1): INSTASAFE INC.

### RISA INTERNATIONAL LIMITED
CIN L99999MH1993PLC071062 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L99999MH1993PLC071062__RISA INTERNATIONAL LIMITED
Expected foreign subs (1): RISA UNIVERSAL LIMITED

### SHRYDUS INDUSTRIES LIMITED
CIN L67190WB1983PLC035658 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L67190WB1983PLC035658__SHRYDUS INDUSTRIES LIMITED
Expected foreign subs (1): Roopyaa General Trading Co. L.L.C

### JBM AUTO LIMITED
CIN L74899HR1996PLC123264 | NSE JBMA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.jbmgroup.com/investors/jbm-auto-ltd/financial-of-subsidiary-company/
TARGET FOLDER: L74899HR1996PLC123264__JBM AUTO LIMITED
Expected foreign subs (1): JBM ELECTRIC VEHICLES TRADING MIDDLE EAST LLC

### SHIPWAVES ONLINE LIMITED
CIN L74900KA2015PLC079072 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74900KA2015PLC079072__SHIPWAVES ONLINE LIMITED
Expected foreign subs (1): Shipwaves Online LLC

### AGARWAL INDUSTRIAL CORPORATION LIMITED
CIN L99999MH1995PLC084618 | NSE AGARIND | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L99999MH1995PLC084618__AGARWAL INDUSTRIAL CORPORATION LIMITED
Expected foreign subs (1): AICL Overseas FZ LLC

### SHEMAROO ENTERTAINMENT LIMITED
CIN L67190MH2005PLC158288 | NSE SHEMAROO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.shemarooent.com/investors
TARGET FOLDER: L67190MH2005PLC158288__SHEMAROO ENTERTAINMENT LIMITED
Expected foreign subs (1): Shemaroo Media & Entertainment LLC

### MAN INFRACONSTRUCTION LIMITED
CIN L70200MH2002PLC136849 | NSE MANINFRA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.maninfra.com/subsidiaries-annual-report/
TARGET FOLDER: L70200MH2002PLC136849__MAN INFRACONSTRUCTION LIMITED
Expected foreign subs (1): MICL Global INC

### PVR INOX LIMITED
CIN L74899MH1995PLC387971 | NSE PVRINOX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74899MH1995PLC387971__PVR INOX LIMITED
Expected foreign subs (1): PVR Inox Lanka Limited

### ACTION CONSTRUCTION EQUIPMENT LIMITED
CIN L74899HR1995PLC053860 | NSE ACE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.ace-cranes.com/home/annual-results-of-subsidiaries
TARGET FOLDER: L74899HR1995PLC053860__ACTION CONSTRUCTION EQUIPMENT LIMITED
Expected foreign subs (1): SC Forma SA

### DIGIKORE STUDIOS LIMITED
CIN L92112PN2000PLC157681 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L92112PN2000PLC157681__DIGIKORE STUDIOS LIMITED
Expected foreign subs (1): Digikore Visual Effects Inc

### INTERIORS & MORE LIMITED
CIN L74120MH2012PLC233915 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74120MH2012PLC233915__INTERIORS AND MORE LIMITED
Expected foreign subs (1): Interiors & More Limited LLC

### RELIANCE INFRASTRUCTURE LIMITED
CIN L75100MH1929PLC001530 | NSE RELINFRA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.rinfra.com
TARGET FOLDER: L75100MH1929PLC001530__RELIANCE INFRASTRUCTURE LIMITED
Expected foreign subs (1): Reliance Global Limited

### MEDICAMEN BIOTECH LIMITED
CIN L74899DL1993PLC056594 | NSE MEDICAMEQ | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.medicamen.com/investor/view/2
TARGET FOLDER: L74899DL1993PLC056594__MEDICAMEN BIOTECH LIMITED
Expected foreign subs (1): OPAL Pharmaceuticals Pty Ltd

### IRONWOOD EDUCATION LIMITED
CIN L68100MH1983PLC030838 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L68100MH1983PLC030838__IRONWOOD EDUCATION LIMITED
Expected foreign subs (1): EMDI (Overseas) FZ LLC

### CYBER MEDIA RESEARCH & SERVICES LIMITED
CIN L74130DL1996PLC081509 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74130DL1996PLC081509__CYBER MEDIA RESEARCH AND SERVICES LIMITED
Expected foreign subs (1): Cyber Media Services Pte Limited

### MUKTA ARTS LIMITED
CIN L92110MH1982PLC028180 | NSE MUKTAARTS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L92110MH1982PLC028180__MUKTA ARTS LIMITED
Expected foreign subs (1): Mukta A2 Multiplex W.L.L
