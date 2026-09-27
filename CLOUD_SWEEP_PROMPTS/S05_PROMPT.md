# CLOUD SWEEP SLICE S05 - 25 PARENTS (27-Sep-2026)
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
### INFOBEANS TECHNOLOGIES LIMITED
CIN L72200MP2011PLC025622 | NSE INFOBEAN | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://infobeans.ai/investors/
TARGET FOLDER: L72200MP2011PLC025622__INFOBEANS TECHNOLOGIES LIMITED
Expected foreign subs (4): InfoBeans Technologies INC; InfoBeans Technologies Europe GMBH; Infobeans Technologies LLC; InfoBeans Technologies Technologies DMCC

### GKB OPHTHALMICS LIMITED
CIN L26109GA1981PLC000469 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://gkb.net/en/financials/
TARGET FOLDER: L26109GA1981PLC000469__GKB OPHTHALMICS LIMITED
Expected foreign subs (4): GKB OPHTHALMICS PRODUCTS FZE; Lensco - The Lens Company , N.J. USA; Prescription Optical Products LLC, Dubai; Prime Ophthalmics Products PTY Limited, South Africa

### TD POWER SYSTEMS LIMITED
CIN L31103KA1999PLC025071 | NSE TDPOWERSYS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.tdps.co.in/investor-relations/subsidiary/financial-statements
TARGET FOLDER: L31103KA1999PLC025071__TD POWER SYSTEMS LIMITED
Expected foreign subs (4): TD Power Systems Europe GMBH; TD Power Systems USA Inc; TD Power Systems Jenerator Sanayi Anonim Sirketi; TD Power Systems Japan Limited

### IKIO TECHNOLOGIES LIMITED
CIN L31401DL2016PLC292884 | NSE IKIO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L31401DL2016PLC292884__IKIO TECHNOLOGIES LIMITED
Expected foreign subs (3): Royalux LLC; Royalux LLC; Ritech Holding Limited, UAE

### IP RINGS LIMITED
CIN L28920TN1991PLC020232 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L28920TN1991PLC020232__IP RINGS LIMITED
Expected foreign subs (3): IPR North America Inc; IPR North America Inc.; IPR North America Inc.

### FACOR ALLOYS LIMITED
CIN L27101AP2004PLC043252 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.facoralloys.in/investor.php
TARGET FOLDER: L27101AP2004PLC043252__FACOR ALLOYS LIMITED
Expected foreign subs (3): Facor Minerals (Netherlands) B.V.; Facor Turkkrom Mining (Netherlands) B.V.; Cati Mandencilik Ithalat ve Ihracat A.S.

### RATNAMANI METALS AND TUBES LIMITED
CIN L70109GJ1983PLC006460 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://ratnamani.com/investors_relations.html
TARGET FOLDER: L70109GJ1983PLC006460__RATNAMANI METALS AND TUBES LIMITED
Expected foreign subs (3): Ratnamani Trade EU AG, Switzerland; Ratnamani Inc.,USA; Ratnamani Middle East Pipe Trading LLC OPC, UAE

### DEEP INDUSTRIES LIMITED
CIN L14292GJ2006PLC049371 | NSE DEEPINDS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L14292GJ2006PLC049371__DEEP INDUSTRIES LIMITED
Expected foreign subs (3): BelugaInternationalDMCC; SAARInternationalFZLLC; Deep International DMCC

### DIFFUSION ENGINEERS LIMITED
CIN L99999MH2000PLC124154 | NSE DIFFNKG | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.diffusionengineers.com/investor
TARGET FOLDER: L99999MH2000PLC124154__DIFFUSION ENGINEERS LIMITED
Expected foreign subs (3): Diffusion Wear Solutions Inc. (Philippines); Diffusion Engineers Singapore Pte. Ltd.; F. Diffusion Eurasia Mühendislik Sanayi Ve Ticaret Anonim Sirketi

### CUPID LIMITED
CIN L25193MH1993PLC070846 | NSE CUPID | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.cupidlimited.com/investors-info/
TARGET FOLDER: L25193MH1993PLC070846__CUPID LIMITED
Expected foreign subs (3): Cupid Invesco Limited (100 Shares @ AED 1000); Cupid Invesco Limited (UAE); M/s Cupid Invesco Limited

### MANAKSIA STEELS LIMITED
CIN L27101WB2001PLC138341 | NSE MANAKSTEEL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.manaksiasteels.com/web/annual-report-of-subsidiary-companies
TARGET FOLDER: L27101WB2001PLC138341__MANAKSIA STEELS LIMITED
Expected foreign subs (3): FEDERATED STEEL MILLS LIMITED; SUMO AGROCHEM LIMITED; FAR EAST STEEL INDUSTRIES LIMITED

### STYRENIX PERFORMANCE MATERIALS LIMITED
CIN L25200GJ1973PLC002436 | NSE STYRENIX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://styrenix.com/quarterly-results-31/
TARGET FOLDER: L25200GJ1973PLC002436__STYRENIX PERFORMANCE MATERIALS LIMITED
Expected foreign subs (3): Styrenix Performance Materials (Thailand) Ltd.; Styrenix Performance Materials FZE; Styrenix Polymers

### Delta Corp Limited
CIN L65493MH1990PLC436790 | NSE DELTACORP | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://deltacorp.in/investors/investor-reports.php?cat=Subsidiaries+Accounts+from+Financial+section
TARGET FOLDER: L65493MH1990PLC436790__DELTA CORP LIMITED
Expected foreign subs (3): Delta Hotels Lanka (Private) Limited; Delta Hospitality and Entertainment Mauritius Limited; Delta Offshore Developers Limited

### RESPONSIVE INDUSTRIES LIMITED
CIN L65100MH1982PLC027797 | NSE RESPONIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.responsiveindustries.com/subsidiary-companies
TARGET FOLDER: L65100MH1982PLC027797__RESPONSIVE INDUSTRIES LIMITED
Expected foreign subs (3): RESPONSIVE INDUSTRIES LIMITED; RESPONSIVE INDUSTRIES LLC; AXIOM CORDAGES LIMITED

### DEEPAK FERTILISERS AND PETROCHEMICALS CORPORATION LTD
CIN L24121MH1979PLC021360 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.dfpcl.com/subsidiaries
TARGET FOLDER: L24121MH1979PLC021360__DEEPAK FERTILISERS AND PETROCHEMICALS CORPORATION LTD
Expected foreign subs (3): PLATINUM BLASTING SERVICES PTY. LIMITED; Platinum Blasting Services (Logistics) Pty Ltd; DEEPAK NITROCHEM PTY.

### EROS INTERNATIONAL MEDIA LIMITED
CIN L99999MH1994PLC080502 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://erosmediaworld.com/investor-relations-eros/eiml-sebi-listing-regulation-46/
TARGET FOLDER: L99999MH1994PLC080502__EROS INTERNATIONAL MEDIA LIMITED
Expected foreign subs (3): BIG SCREEN ENTERTAINMENT PRIVATE LIMITED; Digicine PTE Limited; Eros International Limited

### VIVIMED LABS LIMITED
CIN L02411KA1988PLC009465 | NSE VIVIMEDLAB | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.vivimedlabs.com/financials/
TARGET FOLDER: L02411KA1988PLC009465__VIVIMED LABS LIMITED
Expected foreign subs (3): Vivimed Holdings Limited; Vivimed Labs USA; Vivimed Labs Mauritius Limited

### ZIM LABORATORIES LIMITED.
CIN L99999MH1984PLC032172 | NSE ZIMLAB | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.zimlab.in/investors/subsidiaries
TARGET FOLDER: L99999MH1984PLC032172__ZIM LABORATORIES LIMITED.
Expected foreign subs (3): ZIM Laboratories FZE; SIA ZIM Laboratories Limited; ZIM Scientific Office LLC

### GODAVARI BIOREFINERIES LIMITED
CIN L67120MH1956PLC009707 | NSE GODAVARIB | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.godavaribiorefineries.com/our-company-investors
TARGET FOLDER: L67120MH1956PLC009707__GODAVARI BIOREFINERIES LIMITED
Expected foreign subs (3): Godavari Biorefineries BV; Godavari Biorefineries INC; Cayuga Investments BV

### THE INDIA CEMENTS LIMITED
CIN L26942TN1946PLC000931 | NSE INDIACEM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.indiacements.co.in/subsidiaries-financial-statements.html
TARGET FOLDER: L26942TN1946PLC000931__THE INDIA CEMENTS LIMITED
Expected foreign subs (3): PT Coromandel Mineral Resources; Coromandel Minerals Pte Limited; Raasi Minerals Pte Limited

### MAN INDUSTRIES (INDIA) LIMITED
CIN L99999MH1988PLC047408 | NSE MANINDS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://mangroup.com/investor-relations/
TARGET FOLDER: L99999MH1988PLC047408__MAN INDUSTRIES (INDIA) LIMITED
Expected foreign subs (3): Man Overseas Metals DMCC; Man USA Inc.; Man International Steel Industrial Company

### INDOKEM LIMITED
CIN L31300MH1964PLC013088 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L31300MH1964PLC013088__INDOKEM LIMITED
Expected foreign subs (3): Tex care Middle East LLC; Refnol Overseas Limited; Indokem Bangladesh Pvt. Ltd

### BSE LIMITED
CIN L67120MH2005PLC155188 | NSE BSE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L67120MH2005PLC155188__BSE LIMITED
Expected foreign subs (3): India International Exchange (IFSC) Limited; India International Clearing Corporation (IFSC) Limited; India INX Global Access IFSC Limited

### J B CHEMICALS AND PHARMACEUTICALS LIMITED
CIN L24390GJ1976PLC173077 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24390GJ1976PLC173077__J B CHEMICALS AND PHARMACEUTICALS LIMITED
Expected foreign subs (3): Biotech Laboratories (Pty.) Ltd., South Africa; LLC Unique Pharmaceutical Laboratories, Russia; Unique Pharmaceutical Laboratories FZE, Dubai

### ALLCARGO LOGISTICS LIMITED
CIN L63010MH2004PLC073508 | NSE ALLCARGO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.allcargologistics.com/cms/pdfs/December2025/
TARGET FOLDER: L63010MH2004PLC073508__ALLCARGO LOGISTICS LIMITED
Expected foreign subs (3): Flamingo Line Chile S.A.; Ports International, Inc.; FMA Line Agencies Do Brasil Ltda
