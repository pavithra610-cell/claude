# CLOUD SWEEP SLICE S08 - 25 PARENTS (27-Sep-2026)
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
### KIRLOSKAR OIL ENGINES LIMITED
CIN L29100PN2009PLC133351 | NSE KIRLOSENG | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.kirloskaroilengines.com/investors/subsidiary-annual-report
TARGET FOLDER: L29100PN2009PLC133351__KIRLOSKAR OIL ENGINES LIMITED
Expected foreign subs (2): Kirloskar Americas Corporation; Kirloskar International ME FZE

### PAKKA LIMITED
CIN L24231UP1981PLC005294 | NSE PAKKA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L24231UP1981PLC005294__PAKKA LIMITED
Expected foreign subs (2): Pakka Inc; Pakka Pte Ltd

### SANGHVI MOVERS LIMITED
CIN L29150PN1989PLC054143 | NSE SANGHVIMOV | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://sanghvicranes.com/investor/investor-information/
TARGET FOLDER: L29150PN1989PLC054143__SANGHVI MOVERS LIMITED
Expected foreign subs (2): Sanghvi Movers Middle East Limited; Sanghvi Movers Vietnam Co. Ltd., Vietnam

### JAIN RESOURCE RECYCLING LIMITED
CIN L27320TN2022PLC150206 | NSE JAINREC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L27320TN2022PLC150206__JAIN RESOURCE RECYCLING LIMITED
Expected foreign subs (2): Jain Ikon Global Ventures (FZC); Jain Investment (Private) Limited

### MINAL INDUSTRIES LIMITED
CIN L32201MH1988PLC216905 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.minalindustrieslimited.in/investors
TARGET FOLDER: L32201MH1988PLC216905__MINAL INDUSTRIES LIMITED
Expected foreign subs (2): Minal International FZE; Minal international FZE UAE

### GEM AROMATICS LIMITED
CIN L24246MH1997PLC111057 | NSE GEMAROMA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24246MH1997PLC111057__GEM AROMATICS LIMITED
Expected foreign subs (2): Gem Aromatics LLC; Gem Aromatics FZ LLC

### EMERALD TYRE MANUFACTURERS LIMITED
CIN L25111TN2002PLC048665 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L25111TN2002PLC048665__EMERALD TYRE MANUFACTURERS LIMITED
Expected foreign subs (2): Emrald Tyres Europe BV; Emrald Middle East FZE

### GVK POWER & INFRASTRUCTURE LIMITED
CIN L74999TG2005PLC059013 | NSE GVKPIL | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74999TG2005PLC059013__GVK POWER AND INFRASTRUCTURE LIMITED
Expected foreign subs (2): GVK Airports International PTE Ltd; GVK Airports International PTE Ltd

### DRONEACHARYA AERIAL INNOVATIONS LIMITED
CIN L29308PN2017PLC224312 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://droneacharya.com/wp-content/uploads/2024/08/
TARGET FOLDER: L29308PN2017PLC224312__DRONEACHARYA AERIAL INNOVATIONS LIMITED
Expected foreign subs (2): DRONE ENTRY AERIAL SERVICES LLP; Drone Entry Aerial Services LLC

### LAURUS LABS LIMITED
CIN L24239AP2005PLC047518 | NSE LAURUSLABS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.lauruslabs.com/subsidary.html
TARGET FOLDER: L24239AP2005PLC047518__LAURUS LABS LIMITED
Expected foreign subs (2): Laurus Holidngs Limited; Laurus Generics SA PTY

### PLATINUM INDUSTRIES LIMITED
CIN L24299MH2020PLC341637 | NSE PLATIND | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://platinumindustriesltd.com/company-overview-governance/?tab=subsidiary-financials
TARGET FOLDER: L24299MH2020PLC341637__PLATINUM INDUSTRIES LIMITED
Expected foreign subs (2): Platinum Stabilizers Egypt LLC; Platinum Stabilizers Egypt LLC

### SKP BEARING INDUSTRIES LIMITED
CIN L29305GJ2022PLC128492 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L29305GJ2022PLC128492__SKP BEARING INDUSTRIES LIMITED
Expected foreign subs (2): SKP Bearing Industries Limited; SKP BEARINGS LIMITED FRANCE

### HALDER VENTURE LIMITED
CIN L74210WB1982PLC035117 | NSE HALDER | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74210WB1982PLC035117__HALDER VENTURE LIMITED
Expected foreign subs (2): Hal Exim PTE Ltd; Hal Exim PTE Ltd

### RAMKRISHNA FORGINGS LTD
CIN L74210WB1981PLC034281 | NSE RKFORGE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://ramkrishnaforgings.com/wp-content/uploads/2023/05/
TARGET FOLDER: L74210WB1981PLC034281__RAMKRISHNA FORGINGS LTD
Expected foreign subs (2): Ramkrishna Forgings LLC; RAMKRISHNA FORGINGSMEXICO S.A D.E C.V

### SUDEEP PHARMA LIMITED
CIN L24231GJ1989PLC013141 | NSE SUDEEPPHRM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24231GJ1989PLC013141__SUDEEP PHARMA LIMITED
Expected foreign subs (2): Sudeep Pharma USA Inc.; Sudeep Pharma B.V.

### DECIPHER LABS LIMITED
CIN L24230TG1986PLC006781 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://decipherlabs.in/wp-content/uploads/2024/09/
TARGET FOLDER: L24230TG1986PLC006781__DECIPHER LABS LIMITED
Expected foreign subs (2): Decipher Software Solutions LLC; Decipher Soft Middle East W.L.L.

### NACL INDUSTRIES LIMITED
CIN L24219TG1986PLC016607 | NSE NACLIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://naclind.com/investor-relations/financial-results/subsidiary-company/
TARGET FOLDER: L24219TG1986PLC016607__NACL INDUSTRIES LIMITED
Expected foreign subs (2): Nagarjuna Agrichem (Australia) Pty. Limited; NACL Industries (Nigeria) Limited

### Jai Balaji Industries Limited
CIN L27102WB1999PLC089755 | NSE JAIBALAJI | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://jaibalajigroup.com/audited-accounts-of-subsidiary-company/
TARGET FOLDER: L27102WB1999PLC089755__JAI BALAJI INDUSTRIES LIMITED
Expected foreign subs (2): Kesarisuta Industries Uganda Limited; Kesarisuta Industries Uganda Limited

### INDSIL HYDRO POWER AND MANGANESE LIMITED
CIN L27101TZ1990PLC002849 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.indsil.com/investors-relation/
TARGET FOLDER: L27101TZ1990PLC002849__INDSIL HYDRO POWER AND MANGANESE LIMITED
Expected foreign subs (2): INDSIL ENERGY GLOBAL (FZE); INDSIL ENERGY GLOBAL (FZE)

### SUNIL HEALTHCARE LIMITED
CIN L24302DL1973PLC189662 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.sunilhealthcare.com/investor/annual-reports-subsidiary
TARGET FOLDER: L24302DL1973PLC189662__SUNIL HEALTHCARE LIMITED
Expected foreign subs (2): Sunil Healthcare Mexico SA DE CV; Sunil Healthcare North America LLC

### BALASORE ALLOYS LIMITED
CIN L27101OR1984PLC001354 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://balweb.sparrowsys.com/regulation-disclosure
TARGET FOLDER: L27101OR1984PLC001354__BALASORE ALLOYS LIMITED
Expected foreign subs (2): MILTON HOLDINGS LIMITED; BALASORE METALS PTE. LTD.

### DCM SHRIRAM LIMITED
CIN L74899HR1989PLC137147 | NSE DCMSHRIRAM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L74899HR1989PLC137147__DCM SHRIRAM LIMITED
Expected foreign subs (2): Bioseed Research Philippines, INC; Bioseeds Holdings Pte. Ltd.

### DEV INFORMATION TECHNOLOGY LIMITED
CIN L30000GJ1997PLC033479 | NSE DEVIT | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.devitpl.com/investor-relations/investor-relations/subsidiary-companys-financials/
TARGET FOLDER: L30000GJ1997PLC033479__DEV INFORMATION TECHNOLOGY LIMITED
Expected foreign subs (2): DEV INFO TECH NORTH AMERICA LTD; DYNAMIC STARS LLC

### PI INDUSTRIES LIMITED
CIN L24211RJ1946PLC000469 | NSE PIIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.piindustries.com/investor/
TARGET FOLDER: L24211RJ1946PLC000469__PI INDUSTRIES LIMITED
Expected foreign subs (2): PI JAPAN COMPANY LIMITED; PI Industries Management Consultancies LLC

### KRISHCA STRAPPING SOLUTIONS LIMITED
CIN L74999TN2017PLC119939 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74999TN2017PLC119939__KRISHCA STRAPPING SOLUTIONS LIMITED
Expected foreign subs (2): Krishca Total Packaging Solutions FZCO; KRISHCA TOTAL PACKAGING & PRESERVATION SOLUTIONS PTE. LTD
