# CLOUD SWEEP SLICE R02 - 11 PARENTS (FY26 SUBS FINANCIALS, 27-Sep-2026)
Standing instruction for this whole session; do not re-read it. Commit each parent before starting the next, on branch sweep/R02. If a site is unreachable say NETWORK BLOCKED. PRIORITY: FY26 files only; an FY25 file is listed as SUB_FS_FY25_FALLBACK only when the parent has NOT yet published its FY26 set at all.

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
### SUDARSHAN CHEMICAL INDUSTRIES LIMITED
CIN L24119PN1951PLC008409 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.sudarshan.com/subsidiaries-financial-reports/
TARGET FOLDER: L24119PN1951PLC008409__SUDARSHAN CHEMICAL INDUSTRIES LIMITED
MISSING SUBSIDIARIES TO FIND (49): Inventories Frankfurt GmbH (Germany); Sudarshan North America, Inc. (United States); Sudarshan Germany Horizons GmbH (Formerly known as Blitz F24-522 GmbH) (Germany); Inventories Langelsheim GmbH (Germany); Sudarshan Mexico S. de R.L. de CV. (Mexico); Sudarshan Switzerland HLD1 AG (Formerly known as Heubach Holding Switzerland AG) (Switzerland); Sudarshan USA SLO LLC (Formerly known as Heubach Colorants USA LLC) (United States); Sudarshan Langelsheim PLT GmbH (Formerly known as Blitz F24-523 GmbH) (Germany); Sudarshan Brasil MFG Ltda. (Formerly known as Heubach Colorants Brasil Ltda.) (Brazil); Heubach Colorants (Shanghai) Ltd. (China); Heubach Colorants México, S.A. de C.V. (Mexico); Sudarshan Japan MFG K.K. (Formerly known as Heubach Colorants Japan K.K.) (Japan); Sudarshan Fairless Hills MFG Ltd., LP (Heubach Ltd.) (United States); VP4 Frankfurt GmbH (Germany); Heubach Colorants Iberica, S.L.U. (Spain); Sudarshan Belgium SLO SRL (Formerly known as Heubach Colorants Belgium SRL) (Belgium); Sudarshan Switzerland SLO AG (Formerly known as Heubach Colorants Switzerland AG) (Switzerland); Heubach Colorants Pigment Preparations (Tianjin) Ltd. (China); Sudarshan Southern Africa MFG (Pty) Ltd. (Formerly known as Heubach Colorants Southern Africa (Pty) Ltd) (South Africa); P.T. Heubach Colorants Coatings Indonesia (Indonesia); Sudarshan Italy SLO S.r.l. (Formerly known as Heubach Colorants Italy S.r.l.) (Italy); P.T. Heubach Colorants Indonesia (Indonesia); Sudarshan Malaysia SLO Sdn. Bhd. (Formerly known as Heubach Colorants Malaysia Sdn. Bhd.) (Malaysia); Heubach Colorants France SAS (France); Heubach Colorants Colombia S.A.S. (Colombia); Sudarshan Chile Industria Química Limitada (Formerly known as Heubach Colorants Chile Industria Química Limitada) (Chile); Sudarshan MFG (Thailand) Ltd. (Formerly known as Heubach Colorants (Thailand) Limited.) (Thailand); Heubach Colorants Argentina S.A.U. (Argentina); Sudarshan Canada SLO Inc. (Formerly known as Heubach Colorants Canada Inc.) (Canada); Sudarshan (Shanghai) Trading Company Limited (China); Sudarshan Osaka SLO K.K. (Formerly known as Heubach Japan K.K.) (Japan); Sudarshan Turkey SLO Boya Sanayi ve Ticaret A.Ş. (Formerly known as Heubach Colorants Turkey Boya Sanayi ve Ticaret A.S.) (Turkey); Sudarshan Japan Limited (Japan); Sudarshan Brasil Ltda. (Brazil); Sudarshan Europe Management GmbH (Formerly known as Blitz F24-526 GmbH) (Germany); Sudarshan Middle East General Trading L.L.C.# (United Arab Emirates); Sudarshan Switzerland HLD2 AG (Formerly known as Heubach EBITO Chemiebeteiligungen AG) (Switzerland); Heubach Colorants Middle East FZE (United Arab Emirates); Sudarshan Switzerland Consulting AG (Formerly known as Heubach Colorants Consulting Switzerland AG) (Switzerland); Heubach Colorants Korea Ltd. (KOREA, REPUBLIC OF); Heubach Colorants Peru S.A.C. (PERU); Heubach Colorants Scandinavia AB (Sweden); Heubach Colorants Taiwan Co., Ltd. (Taiwan); Heubach Europa EWIV (Germany); Heubach Colorants México Productos Químicos, S.A. de C.V. (Mexico); Sudarshan Lux Holding S.à r.l (Formerly known as Heubach Holdings S.a r.l) (Luxembourg); Sudarshan USA HLD1 LLC (Formerly known as Heubach Holding USA LLC) (United States); Heubach Research Centre s.r.o (Czech Republic); Sudarshan Langelsheim RE GmbH (Formerly known as Blitz F24-524 GmbH) (Germany)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### Rain Industries Limited
CIN L26942TG1974PLC001693 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.rain-industries.com/annual-report-2024/pdf/
TARGET FOLDER: L26942TG1974PLC001693__RAIN INDUSTRIES LIMITED
MISSING SUBSIDIARIES TO FIND (20): Rain CII Carbon LLC (United States); Rain Carbon Germany GmbH (Germany); RAIN CARBON BV (Belgium); OOO RÜTGERS Severtar (Russia); Rain Carbon Canada Inc. (Canada); Rain Carbon Poland Sp. z. o. o (Poland); Rain Carbon (Shanghai) Trading Co. Ltd (China); Rain Carbon Gewerbeimmobilien GmbH & Co. KG (Germany); Rain Carbon Wohnimmobilien GmbH & Co. KG (Germany); RAIN Carbon GmbH (Germany); Rain Commodites FZCO (United Arab Emirates); VFT France S.A (France); Rain Holding Limited (United Arab Emirates); Rain Commodities (USA) Inc. (United States); Rain Carbon Inc. (United States); Rain Global Services LLC (United States); Rumba Invest BVBA & Co. KG (Germany); Severtar Holding Ltd. (Cyprus); OOO Rain Carbon LLC (Russia); Severtar Holding ILLC (Russia)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SUPRAJIT ENGINEERING LIMITED
CIN L29199KA1985PLC006934 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://suprajit.com/financials/subsidiary-accounts/
TARGET FOLDER: L29199KA1985PLC006934__SUPRAJIT ENGINEERING LIMITED
MISSING SUBSIDIARIES TO FIND (13): Suprajit Brownsville, LLC (United States); Wescon Controls LLC (United States); Suprajit Hungary Kft. (Hungary); Suprajit Mexico S de RLde CV (Mexico); Suprajit Germany GmbH (Germany); Luxlite Lamps SARL, Luxembourg (Luxembourg); Suprajit Morocco SARL (MOROCCO); Shanghai Lone Star Cable Co., Ltd. (China); SCS Polska Sp. Z.o.o. (Poland); Suprajit (Jiaxing) Automotive Systems Company Limited (China); Suprajit USA, Inc (United States); Suprajit Canada Limited (Canada); Trifa Lamps Germany, GmbH (Germany)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### ELECON ENGINEERING COMPANY LIMITED
CIN L29100GJ1960PLC001082 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.elecon.com/investors/audited-financial-statements-of-subsidiaries-companies
TARGET FOLDER: L29100GJ1960PLC001082__ELECON ENGINEERING COMPANY LIMITED
MISSING SUBSIDIARIES TO FIND (10): Radicon Drive Systems Inc. (United States); AB Benzlers (Sweden); Benzlers TBA B.V. (Netherlands); Elecon Singapore Pte. Limited (Singapore); Benzlers Antriebstechnik G.m.b.h (Germany); OY Benzlers AB (Finland); Benzlers Italia s.r.l. (Italy); Benzlers Transmission A.S. (Denmark); Elecon Radicon Africa Pty. Limited (South Africa); Benzlers Systems AB (Sweden)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### IPCA LABORATORIES LIMITED
CIN L24239MH1949PLC007837 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://ipca.com/investors-subsidiary-accounts/
TARGET FOLDER: L24239MH1949PLC007837__IPCA LABORATORIES LIMITED
MISSING SUBSIDIARIES TO FIND (8): Bayshore Pharmaceuticals LLC, USA (United States); Ipca Laboratories (UK) Ltd., UK (United Kingdom); Onyx Scientific Ltd., UK (United Kingdom); Pisgah Laboratories Inc., USA (United States); Ipca Pharma Nigeria Ltd., Nigeria (Nigeria); Ipca Pharma (Australia) Pty. Ltd., Australia (Australia); Ipca Pharma (NZ) Pty. Ltd., New Zealand (New Zealand); Ipca Pharmaceuticals Ltd.,SA de CV (Mexico)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### VERTOZ LIMITED
CIN L74120MH2012PLC226823 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://vertoz.com/ir/financials/
TARGET FOLDER: L74120MH2012PLC226823__VERTOZ LIMITED
MISSING SUBSIDIARIES TO FIND (6): Vertoz INC (United States); Admeridian Inc (United States); Ownregistrar Inc (United States); Hueads Inc (United States); Vokut Inc (United States); Qualispace Inc (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SASKEN TECHNOLOGIES LIMITED
CIN L72100KA1989PLC014226 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://www.sasken.com/investors/financials-subsidiaries
TARGET FOLDER: L72100KA1989PLC014226__SASKEN TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (6): Sasken Technologies Japan Co. Ltd (Japan); Sasken Communication Technologies Mexico S.A De C.V (Mexico); Sasken Design Solutions Pte Ltd (Singapore); Borqs International Holding Corp (Cayman Islands); New Borqs Technologies (Beijing) Company Limited (China); Borqs Technologies (HK) Limited (Hong Kong)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### SUPERHOUSE LIMITED
CIN L24231UP1980PLC004910 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: http://superhouse.in/pdf/
TARGET FOLDER: L24231UP1980PLC004910__SUPERHOUSE LIMITED
MISSING SUBSIDIARIES TO FIND (4): Linea De Seguridad SLU (Spain); LA Compagnie Francaise De Protection SRL (France); Superhouse Middle East FZC Azman (United Arab Emirates); Superhouse (USA) International Inc (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### FERMENTA BIOTECH LIMITED
CIN L99999MH1951PLC008485 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://fermentabiotech.com/investor_relations.php
TARGET FOLDER: L99999MH1951PLC008485__FERMENTA BIOTECH LIMITED
MISSING SUBSIDIARIES TO FIND (3): Fermenta USA LLC (United States); Fermenta Biotech GmbH (Germany); Fermenta Biotech USA LLC (United States)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### GRAPHITE INDIA LIMITED
CIN L10101WB1974PLC094602 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | subs page not known - find it (Investors > Subsidiaries / Reg 46)
TARGET FOLDER: L10101WB1974PLC094602__GRAPHITE INDIA LIMITED
MISSING SUBSIDIARIES TO FIND (3): Bavaria Carbon Specialities GmbH (Germany); General Graphene Corporation (United States); Bavaria Electrodes GmbH (Germany)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.

### KFIN TECHNOLOGIES LIMITED
CIN L72400MH2017PLC444072 | SCOPE: SUBS FINANCIALS ONLY - FY26 (31-Mar-2026) or CY2025 full-year; we already hold the FY26 annual report, so record its URL and AOC-1 page range but do not list the AR as a download | KNOWN SUBS PAGE: https://investor.kfintech.com/subsidiaries/
TARGET FOLDER: L72400MH2017PLC444072__KFIN TECHNOLOGIES LIMITED
MISSING SUBSIDIARIES TO FIND (3): KFin Technologies (Malaysia) Sendirian Berhad (Malaysia); KFin Technologies (Thailand) Limited (Thailand); KFin Global Technologies (IFSC) Limited (India)
Also list any OTHER subsidiary FY26 file on the page (domestic or foreign) - one row per file.
