# CLOUD SWEEP SLICE R05 - 10 PARENTS (FY26 SUBS FINANCIALS, 27-Sep-2026)
Standing instruction for this whole session; do not re-read it. Commit each parent before starting the next, on branch sweep/R05. If a site is unreachable say NETWORK BLOCKED. PRIORITY: FY26 files only; an FY25 file is listed as SUB_FS_FY25_FALLBACK only when the parent has NOT yet published its FY26 set at all.

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
### SOLAR INDUSTRIES INDIA LIMITED
CIN L74999MH1995PLC085878 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://solargroup.com/Investor-relation.html
TARGET FOLDER: L74999MH1995PLC085878__SOLAR INDUSTRIES INDIA LIMITED
MISSING SUBSIDIARIES TO FIND (26): Solar Patlayici Maddeler San. Ve Tic. Ano Sirketi (Turkey); Solar Mining Services Pty Ltd-SA (South Africa); Solar Nigachem Limited (Nigeria); Problast BS (Pty) Ltd (South Africa); Solar Nitro Ghana Limited (Ghana); Solar Overseas Mauritius Limited (Mauritius); Solar Nitro Chemicals Limited (Tanzania); PT.Solar Mining Services (Indonesia); Solar Madencilik Hizmetleri A.S (Turkey); Solar Mining Services-Albania (ALBANIA); Frag Shared Services (Pty) Ltd (South Africa); Maxigear (Pty) Ltd (South Africa); Power Blast LLP (KAZAKHSTAN); Procapture (Pty) Ltd (South Africa); Solar Venture Company Limited (Tanzania); Solar Mining Services Cote d’Ivoire (COTE D'IVOIRE); Solar Nitro Kazakhstan Limited (Kazakhstan); Solar Industries Africa Limited (Mauritius); Solar Overseas Netherlands B.V. (Netherlands); Solar Overseas Netherlands Cooperatie U.A. (Netherlands); Solar Overseas Singapore Pte Limited (Singapore); Solar Nitro (SL) Limited (SIERRA LEONE); Solar Nitro SARL (COTE D'IVOIRE); Solar Mining Services-Burkina Faso (BURKINA FASO); Problast BBBEE Investment Co. (Pty) Ltd (South Africa); ASTRA Resources Pty Limited (BURKINA FASO)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### KPIT TECHNOLOGIES LIMITED
CIN L74999PN2018PLC174192 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://d1rz4ui464s6g7.cloudfront.net/wp-content/uploads/2020/08/07181608/
TARGET FOLDER: L74999PN2018PLC174192__KPIT TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (17): KPIT Technologies GK (Refer note iv below) (Japan); KPIT Technologies GmbH (Refer note ii below) (Germany); Technica Engineering GmbH (Germany); KPIT Technologies (UK) Limited (Refer note i below) (United Kingdom); KPIT Technologies S.A.S. (France); Technica Electronics Barcelona S.L. (Spain); KPIT Engineering SUARL (Tunisia); Technica Engineering Inc. (United States); KPIT (Shanghai) Software Technology Co. Limited (China); PathPartner Technology Inc. (United States); KPIT Tech (Thailand) Co., Ltd. (Refer note v below) (Thailand); KPIT Technologias Ltda. (Refer note iii below) (Brazil); Somit Solutions Limited (United Kingdom); Caresoft Global Technologies, Inc. (United States); CAREGLOTECH de RL de CV (Mexico); N-Dream AG (Switzerland); OXI S.R.L. (Italy)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ZENSAR TECHNOLOGIES LIMITED
CIN L72200PN1963PLC012621 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.zensar.com/sites/default/files/investor/annual/files/
TARGET FOLDER: L72200PN1963PLC012621__ZENSAR TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (10): Zensar Technologies Inc (United States); Zensar (South Africa) Proprietary Limited (South Africa); M3Bi LLC (United States); Foolproof (SG) Pte. Ltd (Singapore); Zensar Colombia S.A.S. (Colombia); Zensar Technologies (Canada) Inc (Canada); BridgeView Life Sciences LLC, USA (United States); Keystone Logic Mexico, S. DE R.L. DE C.V. (Mexico); Zensar Technologies GmbH (Germany); Zensar (Africa) Holdings Proprietary Limited (South Africa)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ALLIED DIGITAL SERVICES LIMITED
CIN L72200MH1995PLC085488 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.allieddigital.net/in/audited-financial-statements-of-subsidiaries-companies/
TARGET FOLDER: L72200MH1995PLC085488__ALLIED DIGITAL SERVICES LIMITED
MISSING SUBSIDIARIES TO FIND (8): Allied Digital Services, LLC (USA) (United States); Allied Digital IT Services (Beijing) Co., Ltd. (China); Allied Digital Services Japan G.K. (Japan); Allied Digital Services (Ireland) Limited (Ireland); Allied Digital Services Do Brazil Ltda. (Brazil); Allied Digital Singapore Pte Ltd (Singapore); Allied Digital INC (USA) (United States); Allied Digital Asia Pacific PTY LTD (Australia) (Australia)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### TVS MOTOR COMPANY LIMITED
CIN L35921TN1992PLC022845 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.tvsmotor.com/investors/financial-reports
TARGET FOLDER: L35921TN1992PLC022845__TVS MOTOR COMPANY LIMITED
MISSING SUBSIDIARIES TO FIND (6): PT TVS Motor Company Indonesia (Indonesia); Swiss E-Mobility Group (Holding) AG (Switzerland); Celerity Motor Gmbh (Germany); The GO Corporation (Switzerland); TVSM DMCC (United Arab Emirates); TVSM DMCC (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### LATENT VIEW ANALYTICS LIMITED
CIN L72300TN2006PLC058481 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.latentview.com/investor-relations/financial-results-reports/
TARGET FOLDER: L72300TN2006PLC058481__LATENT VIEW ANALYTICS LIMITED
MISSING SUBSIDIARIES TO FIND (8): LatentView Analytics Corporation (United States); Decision Point Latam SpA (Chile); Decision Point Analytics Inc (United States); LatentView Analytics Pte Limited (Singapore); LatentView AnalyticsGmbH (Germany); Decision Point Latam,Mexico (Mexico); LatentView Analytics B.V. (Netherlands); Decision Point Analytics L.L.C - FZ (United Arab Emirates)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ENDURANCE TECHNOLOGIES LIMITED
CIN L34102MH1999PLC123296 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.endurancegroup.com/investor-relation/annual-reports-of-subsidiaries/
TARGET FOLDER: L34102MH1999PLC123296__ENDURANCE TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (4): ENDURANCE CASTINGS SPA (Italy); ENDURANCE OVERSEAS SPA (Italy); Veicoli SrL, Italy (Wholly Owned Subsidiary of Endurance Overseas Srl) (Italy); GDS Sarl, Tunisia (TUNISIA)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### BAJAJ AUTO LIMITED.
CIN L65993PN2007PLC130076 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://investors.bajajauto.com/wp-content/uploads/2024/06/
TARGET FOLDER: L65993PN2007PLC130076__BAJAJ AUTO LIMITED.
MISSING SUBSIDIARIES TO FIND (4): Bajaj Do Brasil Comercio De Motocicletas Ltda (Brazil); Bajaj Auto Spain S.L.U. (Spain); Bajaj Auto (Thailand) Ltd. (Thailand); PT. Bajaj Auto Indonesia (Indonesia)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SYSTANGO TECHNOLOGIES LIMITED
CIN L51109MP2004PLC016959 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L51109MP2004PLC016959__SYSTANGO TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (3): Systango LLC (United States); Systango LLC (United States); Systango INC (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### INDO AMINES LIMITED
CIN L99999MH1992PLC070022 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://indoaminesltd.com/files/financials/
TARGET FOLDER: L99999MH1992PLC070022__INDO AMINES LIMITED
MISSING SUBSIDIARIES TO FIND (3): Indo Amines Americas LLC (United States); Indo Amines (Changzhou) Co. Ltd (China); Indo Amines (Malaysia) SDN & BHD (Malaysia)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.
