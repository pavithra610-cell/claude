# CLOUD SWEEP SLICE S03 - 25 PARENTS (27-Sep-2026)
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
### 20 MICRONS LIMITED
CIN L99999GJ1987PLC009768 | NSE 20MICRONS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.20microns.com/annual-reports-of-all-subsidiaries
TARGET FOLDER: L99999GJ1987PLC009768__20 MICRONS LIMITED
Expected foreign subs (5): 20 Microns FZE; 20 Microns Vietnam; 20 Microns SDN BHD; Goh Teik Lim Quarry SDN BHD; IQ Marble SDN BHD

### ASIAN STAR COMPANY LIMITED
CIN L36910MH1995PLC086017 | NSE ASTAR | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.asianstargroup.com/investor-centre/
TARGET FOLDER: L36910MH1995PLC086017__ASIAN STAR COMPANY LIMITED
Expected foreign subs (5): Asian Star DMCC; Asian Star Co. Ltd. (USA); Asian Star Co. Ltd; Asian Star Trading (Hong Kong) Ltd; Asian Star Co. Ltd. N.Y.

### AGS TRANSACT TECHNOLOGIES LIMITED
CIN L72200MH2002PLC138213 | NSE AGSTRA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72200MH2002PLC138213__AGS TRANSACT TECHNOLOGIES LIMITED
Expected foreign subs (5): Novustech Transact Lanka (Private) Limited; Novus Technologies Pte.Ltd.; Novus Transact Philippines Corporation; Novus Technologies (Cambodia) Company Limited; Global Transact Services Pte Limited

### JYOTI CNC AUTOMATION LIMITED
CIN L29221GJ1991PLC014914 | NSE JYOTICNC | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://jyoti.co.in/investors/financial-reports-returns-and-notices/
TARGET FOLDER: L29221GJ1991PLC014914__JYOTI CNC AUTOMATION LIMITED
Expected foreign subs (5): Huron Frasmaschinen Gmbh; Huron Machinery Service and Foreign Trade Limited Company; Huron Graffenstanden SAS; Huron Canada Inc.; Jyoti SAS

### APAR INDUSTRIES LIMITED
CIN L91110GJ1989PLC012802 | NSE APARINDS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://apar.com/wp-content/uploads/2025/07/
TARGET FOLDER: L91110GJ1989PLC012802__APAR INDUSTRIES LIMITED
Expected foreign subs (5): Petroleum Specialities FZE, Sharjah; APAR Industries Latam Ltda, Brazil; Petroleum Specialities Pte. Limited, Singapore; APAR USA LLC (Earlier known as CEMA Wires & Cables LLC); Apar Industries Middle East Limited, Saudi Arabia

### OCTAWARE TECHNOLOGIES LIMITED
CIN L72200MH2005PLC153539 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://octaware.com/investors-relations/financial-data/
TARGET FOLDER: L72200MH2005PLC153539__OCTAWARE TECHNOLOGIES LIMITED
Expected foreign subs (5): Octaware Gulf FZE; Octaware Gulf (QFC Branch); Octaware Gulf QFC; Octaware Co, KSA; Octaware KSA

### ALUFLUORIDE LTD
CIN L24110AP1984PLC005096 | NSE n/a | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24110AP1984PLC005096__ALUFLUORIDE LTD
Expected foreign subs (5): Alufluoride International Private Limited; Jordanian Renewable Aluminium Fluoride Manufacturing Company P.S.C, (JV of the subsidiary); Alufluoride International Pte. Ltd., Singapore; Jordanian Renewable Aluminium Fluoride Manufacturing Company P.S.C, (JV of the subsidiary); Jordanian Reneweble Aluminium

### UNIHEALTH HOSPITALS LIMITED
CIN L85100MH2010PLC200491 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L85100MH2010PLC200491__UNIHEALTH HOSPITALS LIMITED
Expected foreign subs (5): Biohealth Limited; Aryavarta FZE; Unihealth Tanzania Ltd; Unihealth Holdings Limited; UMC Global Health Limited

### THEJO ENGINEERING LIMITED
CIN L27209TN1986PLC012833 | NSE THEJO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.thejo-engg.com/investors/
TARGET FOLDER: L27209TN1986PLC012833__THEJO ENGINEERING LIMITED
Expected foreign subs (5): Thejo Australia Pty Ltd; Thejo Hatcon Industrial Services Company; Thejo Engineering LatinoAmerica SpA; Thejo Brasil Comercio E Servicos Ltda; TE Global FZ-LLC

### ADITYA BIRLA NUVO LIMITED
CIN L17199GJ1956PLC001107 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L17199GJ1956PLC001107__ADITYA BIRLA NUVO LIMITED
Expected foreign subs (5): Aditya Birla Sun Life AMC Pte. Ltd. Singapore; Birla Sun Life AMC (Mauritius) Limited; Aditya Birla Sun Life AMC Limited, Dubai; International Opportunities Fund SPC; India Advantage Fund Limited

### EDUCOMP SOLUTIONS LIMITED
CIN L74999DL1994PLC061353 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74999DL1994PLC061353__EDUCOMP SOLUTIONS LIMITED
Expected foreign subs (5): Educomp Global FZE; Educomp Global Holding W.L.L.; Edumatics Corporation, usa; Savvica Inc. canada; Educomp Intelliprop Ventures Pte. Ltd. (Formerly known as Educomp Intelprop Ventures Pte. Ltd.)*

### VIKRAM SOLAR LIMITED
CIN L18100WB2005PLC106448 | NSE VIKRAMSOLR | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.vikramsolar.com/annual-financials/
TARGET FOLDER: L18100WB2005PLC106448__VIKRAM SOLAR LIMITED
Expected foreign subs (5): Vikram Solar US Inc.; Vikram Solar Pte. Ltd.; Vikram Solar GmbH; Solarcode Vikram Solarkraftwerk 1 GmbH & Co. KG; Solarcode Vikram Management GmbH

### MIDWEST LIMITED
CIN L14102TG1981PLC003317 | NSE MIDWESTLTD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://midwest.in/investors
TARGET FOLDER: L14102TG1981PLC003317__MIDWEST LIMITED
Expected foreign subs (5): Midwest Holdings Limited; Midwest Heavy Sands Private Limited; Midwest Heavy Sands Private Limited; Trinco Mineral Sands Private Limited; Trinco Minerals Private Limited

### ISMT LIMITED
CIN L27109PN1999PLC016417 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L27109PN1999PLC016417__ISMT LIMITED
Expected foreign subs (5): Structo Hydraulics AB; ISMT Europe AB; ISMT Enterprises SA; Indian Seamless Inc; PT ISMT Resources

### BIRLANU LIMITED
CIN L74999TG1955PLC000656 | NSE BIRLANU | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://birlanu.com/investor/subsidiaries-financials
TARGET FOLDER: L74999TG1955PLC000656__BIRLANU LIMITED
Expected foreign subs (5): Parador GmbH, Germany; Parador Parkettwerke GmbH, Germany; Parador UK Ltd., England; HIL International GmbH, Germany; Parador Holdings GmbH, Germany

### TIME TECHNOPLAST LIMITED
CIN L27203DD1989PLC003240 | NSE TIMETECHNO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L27203DD1989PLC003240__TIME TECHNOPLAST LIMITED
Expected foreign subs (5): GNXT Investment Holding PTE Ltd; Elan Incorporated Fze; Kompozit Praha S R O; Ikon Investment Holdings Limited; Schoeller Allibert Time Holding PTE Ltd

### ESSAR SHIPPING LIMITED.
CIN L61200GJ2010PLC060285 | NSE ESSARSHPNG | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.essar.com/compliance/
TARGET FOLDER: L61200GJ2010PLC060285__ESSAR SHIPPING LIMITED.
Expected foreign subs (4): Essar Shipping DMCC, Dubai; OGD Services Holdings Limited, Mauritius; Gargnano; Energy II Limited, Bermuda

### Euro Pratik Sales Limited
CIN L74110MH2010PLC199072 | NSE EUROPRATIK | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74110MH2010PLC199072__EURO PRATIK SALES LIMITED
Expected foreign subs (4): Euro Pratik Trade – FZCO Euro Pratik; Euro Pratik Trade – FZCO Euro Pratik; Euro Pratik Trade – FZCO; Euro Pratik Trade – FZCO; Euro Pratik USA LLC; Euro Pratik USA LLC; Euro Pratik C Corp INC; Euro Pratik C Corp INC; Euro Pratik EU D.O.O; Euro Pratik EU D.O.O

### UNIINFO TELECOM SERVICES LIMITED
CIN L64202MP2010PLC024569 | NSE UNIINFO | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L64202MP2010PLC024569__UNIINFO TELECOM SERVICES LIMITED
Expected foreign subs (4): Uni Info Telecom Services (Private) Limited; Uniinfo Technologies QFZ LLC; Uniinfo Technologies QFZ LLC Qatar; Uniinfo Telecom Services Private Limited Sri Lanka

### UNIPARTS INDIA LIMITED
CIN L74899DL1994PLC061753 | NSE UNIPARTS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.unipartsgroup.com/home/subsidiary_company_report
TARGET FOLDER: L74899DL1994PLC061753__UNIPARTS INDIA LIMITED
Expected foreign subs (4): Uniparts Olsen Inc.; Uniparts USA Limited; Uniparts India GmbH; Uniparts USA Ltd.

### CARE RATINGS LIMITED
CIN L67190MH1993PLC071691 | NSE CARERATING | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.careratings.com/Uploads/newsfiles/FinancialReports/
TARGET FOLDER: L67190MH1993PLC071691__CARE RATINGS LIMITED
Expected foreign subs (4): CARE Ratings (Africa) Private Limited; CARE Ratings Nepal Limited; CareEdge Global IFSC Limited; CARE Ratings South Africa (Pty) Limited

### AVT NATURAL PRODUCTS LIMITED
CIN L15142TN1986PLC012780 | NSE AVTNPL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.avtnatural.com/wp-content/uploads/2024/07/
TARGET FOLDER: L15142TN1986PLC012780__AVT NATURAL PRODUCTS LIMITED
Expected foreign subs (4): AVT Natural Europe Ltd., U.K.; AVT Natural FZCO, Dubai; AVT Natural North America, Inc.; AVT Natural S.A. DE C.V, Mexico

### SVP GLOBAL TEXTILES LIMITED
CIN L17290MH1982PLC026358 | NSE SVPGLOB | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.svpglobal.co.in/financial-statement.html
TARGET FOLDER: L17290MH1982PLC026358__SVP GLOBAL TEXTILES LIMITED
Expected foreign subs (4): SV PITTIE TRADING (FZC) LLC; SV PITTIE SOHAR TEXTILES(FZC) SAOC; SVP TEXTILES PLC; SV PITTIE GLOBAL CORPORATION

### J B CHEMICALS AND PHARMACEUTICALS LIMITED
CIN L24390MH1976PLC019380 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://jbpharma.com/download-category/subsidiary-accounts/
TARGET FOLDER: L24390MH1976PLC019380__J B CHEMICALS AND PHARMACEUTICALS LIMITED
Expected foreign subs (4): Biotech Laboratories (Pty.) Ltd., South Africa; LLC Unique Pharmaceutical Laboratories, Russia; Unique Pharmaceutical Laboratories FZE, Dubai; JBCPL Philippines Inc.

### ANUPAM RASAYAN INDIA LIMITED
CIN L24231GJ2003PLC042988 | NSE ANURAS | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.anupamrasayan.com/investors/results-reports
TARGET FOLDER: L24231GJ2003PLC042988__ANUPAM RASAYAN INDIA LIMITED
Expected foreign subs (4): Anupam General Trading FZE; Anupam Japan GK; Anupam General Trading FZE; Anupam Europe AG
