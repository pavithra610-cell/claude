# CLOUD SWEEP SLICE S01 - 20 PARENTS (27-Sep-2026)
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
### PATEL ENGINEERING LIMITED
CIN L99999MH1949PLC007039 | NSE PATELENG | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L99999MH1949PLC007039__PATEL ENGINEERING LIMITED
Expected foreign subs (29): Waterfront Developers Ltd.; Patel Engineering (Singapore) Pte Ltd. (Standalone); Patel Engineering (Mauritius) Ltd. (Standalone); Patel Engineering Inc.; Patel Engineering Lanka (Pvt.) Ltd.; Les Salines Development Ltd.; La Bourgade Development Ltd.; Ville Magnifique Development Ltd.; Sur La Plage Development Ltd.; PT Patel Surya Jaya; PT Patel Surya Minerals; PT Surpat Geo Minerals; PT PEL Minerals Resources; PT Surya Geo Minerals; PT Patel Engineering Indonesia; Patel Mining (Mauritius) Ltd.; Acoord Mines Venture Lda; Patel Assignment Mozambique, Lda; Chivarro Mines Mozambique Lda; Enrich Mining Vision Lda; Fortune Mines Concession Lda; Metalline Mines Works Lda; Netcore Mining Operations Lda; Omini Mines Enterprises Lda; Patel Infrastructure, Lda; Patel Mining Priviledge, Lda; Quest Mining Activities, Lda; Trend Mining Projects Lda; ASI Global LLC

### ETERNAL LIMITED
CIN L93030DL2010PLC198141 | NSE ETERNAL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.eternal.com/investor-relations/
TARGET FOLDER: L93030DL2010PLC198141__ETERNAL LIMITED
Expected foreign subs (26): Zomato Middle East FZ - LLC; Zomato Media (Private) Limited, Srilanka; Zomato NZ Media Pvt. Ltd.; PT. Zomato Media Indonesia; Zomato Chile SpA; Zomato Media Portugal, Unipessoal, Lda; Delivery 21 Inc.; Zomato Ireland Limited; Lunchtime. cz s.r.o; Zomato Internet LLC; Zomato Vietnam Company Limited; Zomato Australia PTY Limited; Lunchtime . Cz s.r.o; Zomato Media Portugal , Unipessoal, Lda; Zomato NZ Media Pvt. Ltd.; Zomato Internet LLC; Zomato Slovakia s.r.o; Zomato Slovakia s.r.o; Zomato Philippines Inc.; Zomato Vietnam Company Limited; Zomato Internet Hizmetleri Ticaret Anonim Sirketi; Zomato Netherlands B.V.; Zomato Inc.; Zomato Australia PTY Limited; Zomato Malaysia Sdn. Bhd.; Gastronauci Sp z.o.o

### NAVA LIMITED
CIN L27101TG1972PLC001549 | NSE NAVA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.navalimited.com/investors/
TARGET FOLDER: L27101TG1972PLC001549__NAVA LIMITED
Expected foreign subs (22): Maamba Energy Limited; Nava Energy Pte. Limited; Nava Energy Zambia Limited; Nava Resources CI.; Nava Resources CI.; Compai Healthcare SDN.BHD.; The Iron Suites Pte. Ltd.; Compai Pharma Pte. Ltd.; Integrative Health Services Pte.; Maamba Solar Energy Limited; Nava Avocado Ltd.; Nava Alloys CI; Nava Health Care Pte Ltd; Kawambwa Sugar Ltd.; Nava Alloys CI; Maamba Solar Energy Limited; Nava Avocado Ltd.; Nava Agro Pte. Ltd.; Kawambwa Sugar Ltd.; Nava Bharat (Singapore) Pte. Limited; Integrative Health Services Pte. Limited; Tiash Pte. Limited

### GRASIM INDUSTRIES LTD
CIN L17124MP1947PLC000410 | NSE GRASIM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.grasim.com/investors/results-reports-and-presentations
TARGET FOLDER: L17124MP1947PLC000410__GRASIM INDUSTRIES LTD
Expected foreign subs (20): Star Super Cement Industries LLC(SSCILLC); Star Cement Co. LLC, Dubai; Star Cement Co. LLC, Ras AI Khaimah; Arabian Cement Industry LLC, Abu Dhabi; UltraTech Cement Lanka Pvt. Ltd.; RAS AL KHAIMAH CO.FOR WHITE CEMENT AND CONSTRUCTION MATERIALS P.S.C; RAS AL KHAIMAH LIME CO NOORA LLC; Ultra Tech Cement Bahrain Company WLL, Bahrain; Modern Block Factory Establishment; Al Nakhla Crushers LLC, Fujairah; COROMANDEL MINERALS PTE. LTD.; RAASI MINERALS PTE. LTD.; PT Coromandel Mineral Resources; Duqm Cement Project International, LLC, Oman; PT Anggana Energy Resources; Binani Cement (Uganda) Ltd; Bhumi Resources (Singapore) Pte. Ltd (Bhumi); BC Tradelink Limited; Binani Cement Tanzania Limited; UltraTech Cement Middle East Investment Ltd.

### UltraTech Cement Limited
CIN L26940MH2000PLC128420 | NSE ULTRACEMCO | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.grasim.com/Upload/PDF/
TARGET FOLDER: L26940MH2000PLC128420__ULTRATECH CEMENT LIMITED
Expected foreign subs (18): Star Super Cement Industries LLC (SSCILLC); Star Cement Co. LLC, Dubai; Star Cement Co LLC, Ras Al Khaimah; Arabian Cement Industry LLC, Abu Dhabi; UltraTech Cement Lanka (Private) Limited (UCLPL); Ras Al Khaimah Co. for White Cement & Construction Materials P.S.C, U.A.E (RAKWCT); Ras Al Khaimah Lime Co, Noora LLC; UltraTech Cement Bahrain Company WLL, Bahrain; Modern Block Factory Establishment; Al Nakhla Crusher Co. LLC, Fujairah; PT Coromandel Mineral Resources (CMR); Coromandel Minerals Pte Ltd. (CMP); Binani Cement (Tanzania) Limited; BC Tradelink Limited, Tanzania; Duqm Cement Project International, LLC, Oman; Raasi Minerals Pte Ltd. (RMP); UltraTech Cement Middle East Investments Limited (UCMEIL); Binani Cement (Uganda) Limited

### QUESS CORP LIMITED
CIN L74140KA2007PLC043909 | NSE QUESS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.quesscorp.com/investor-other-information/
TARGET FOLDER: L74140KA2007PLC043909__QUESS CORP LIMITED
Expected foreign subs (18): Quesscorp Manpower Supply Services LLC; Quess Selection and Services Pte Ltd; Quess (Philippines) Corp.; Quesscorp Holdings Pte Ltd.; Quess Corp NA LLC; Quesscorp Solutions Pte Ltd.; Quess Recruit, Inc.; Quesscorp Management Consultancies; Agensi Pekerjaan Quess Recruit Sdn. Bhd.; Quess Malaysia Digital Sdn. Bhd; Quesscorp Consulting Pte Ltd.; Quess Corp Vietnam LLC; Quess Services Limited; Quesscorp Singapore Pte Ltd; Quess Corp Lanka (Private) Limited; QuessCorp Manpower Supply Services - L.L.C-S.P.C; Quess Engineering Pte. Ltd; Quessglobal (Malaysia) Sdn. Bhd.

### SAGILITY LIMITED
CIN L72900KA2021PLC150054 | NSE SAGILITY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://sagility.com/investor-relations/financial-summary/
TARGET FOLDER: L72900KA2021PLC150054__SAGILITY LIMITED
Expected foreign subs (15): Sagility Provider Solutions LLC; Sagility (Jamaica) Limited; Sagility Payment Integrity Solutions LLC; Broadpath LLC; Sagility LLC; Sagility (Colombia) S.A.S.; Broadpath Global Services Inc.; Sagility Technologies LLC; Birch Technologies Inc.; BHive Holdings LLC; Sagility Care Management LLC; Sagility Operations Inc.; Sagility (US) Holdings Inc.; Sagility (US) Inc.; Sagility Philippines B.V.

### KEC INTERNATIONAL LIMITED
CIN L45200MH2005PLC152061 | NSE KEC | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.kecrpg.com/annual-accounts-of-subsidiaries
TARGET FOLDER: L45200MH2005PLC152061__KEC INTERNATIONAL LIMITED
Expected foreign subs (14): Al-Sharif Group and KEC Ltd. Co, Saudi Arabia; SAE Towers Holdings LLC, USA; KEC EPC LLC, Dubai, UAE; KEC Towers LLC, Dubai, UAE; KEC International (Malaysia) SDN. BHD, Malaysia; SAE Towers Brasil Torres de Transmissao Ltda, Brazil; SAE Towers Mexico S de RL de CV, Mexico; SAE Towers Brazil Subsidiary Company LLC, USA; SAE Towers Mexico Subsidiary Holding Company LLC, USA; KEC Engineering & Construction Services S de RL de CV, Mexico; RPG Transmission Nigeria Limited, Nigeria; SAE Prestadora de Servicios Mexico, S de RL de CV, Mexico; SAE Towers Ltd, USA; KEC Investment Holdings, Mauritius


### GAMMON INDIA LIMITED
CIN L74999MH1922PLC000997 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L74999MH1922PLC000997__GAMMON INDIA LIMITED
Expected foreign subs (13): ATSL Holdings BV, Netherlands; Gammon Holdings B.V., Netherlands; Gammon International B.V., Netherlands; Gammon Holdings (Mauritius) Limited; P.Van Eerd Beheersmaatsc-happaji B.V.,Netherlands; Associated Transrail Structures Limited., Nigeria; Gammon Italy Srl; SAE Powerlines Srl; Franco Tosi Meccanica S.p.A; Gammon International FZE; Sofinter S.p.A.; Gammon International FZE; Sofinter S.p.A.

### KALPATARU PROJECTS INTERNATIONAL LIMITED
CIN L40100GJ1981PLC004281 | NSE KPIL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://kalpataruprojects.com/investors/financials/annual-reports
TARGET FOLDER: L40100GJ1981PLC004281__KALPATARU PROJECTS INTERNATIONAL LIMITED
Expected foreign subs (13): Linjemontage i Grastorp Aktiebolag; Fasttel Engenharia S.A.; Kalpataru IBN Omairah Company Limited; Linjemontage Service Nordic AB; Kalpataru Power DMCC, UAE; Linjemontage AS; Kalpataru Power Chile SpA; Kalpataru Power Senegal SARL; Kalpataru Power Transmission - USA, Inc.; Kalpataru Power do Brasil Participacoes S.A.; Kalpataru Power Transmission (Mauritius) Limited; LLC Kalpataru Power Transmission Ukraine; Kalpataru Power Transmission Sweden AB

### INTERNATIONAL GEMMOLOGICAL INSTITUTE (INDIA) LIMITED
CIN L46591MH1999PLC118476 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://investor.igi.org/annual-reports/subsidiary-company/
TARGET FOLDER: L46591MH1999PLC118476__INTERNATIONAL GEMMOLOGICAL INSTITUTE (INDIA) LIMITED
Expected foreign subs (13): International Gemmological Institute Inc.; IGI (Shanghai) Gemological Research and Testing Limited; International Gemmological Institute BV; International Gemmological Institute DMCC; IGI (Shenzhen) Jewelry; IGI (Shanghai) Business Consulting Co., Ltd.; International Gemmological Institute (Israel) Ltd; International Gemological Institute (HK) Limited; IGI (Shanghai) Gemological Training Company Limited; International Gemmological Identification (Thailand) Limited; IGI Netherlands B.V .; IGI Gemmological Institute Türkiye Precious Stone Certification Services Joint Stock Company; International Gemological Institute for Jewelry and Precious Stones (IGI)

### KAYA LIMITED
CIN L85190MH2003PLC139763 | NSE KAYA | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.kaya.in/investors
TARGET FOLDER: L85190MH2003PLC139763__KAYA LIMITED
Expected foreign subs (12): Kaya Skin Care Clinic LLC; Kaya Skin Care Clinic - Sole Proprietorship LLC; Kaya Middle East FZE; Kaya Middle East DMCC; Sakr AL Majd International Company; Kaya Trading LLC; Kaya Beauty Clinic - Sole Proprietorship LLC; Kaya Medical Complex LLC; Kaya Skin Medical Centre; Kaya Beauty Clinic LLC SP; IRIS Medical Centre LLC; KME Holdings Pte Ltd.

### AIA ENGINEERING LIMITED
CIN L29259GJ1991PLC015182 | NSE AIAENG | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://aiaengineering.com/investor-financials/
TARGET FOLDER: L29259GJ1991PLC015182__AIA ENGINEERING LIMITED
Expected foreign subs (11): Vega Industries (Middle East) FZC - UAE; Vega Industries Ltd. – USA; Vega Middle East (DFTZ) FZE - UAE; VEGA Industries Australia Pty Ltd. - Australia; AIA Ghana Ltd. Ghana; Wuxi Vega Trade Co. Ltd. - China; VEGA Industries Chile SPA - Chile; Vega Steel Industries (RSA) (Pty) Ltd. -South Africa; PT Vega Industries Indonesia - Indonesia; Vega Industries Ltd. – UK; Vega Industries Peru Limited, Peru

### VAIBHAV GLOBAL LIMITED
CIN L36911RJ1989PLC004945 | NSE VAIBHAVGBL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.vaibhavglobal.com/financial_reporting/financial-results-of-subsidiary
TARGET FOLDER: L36911RJ1989PLC004945__VAIBHAV GLOBAL LIMITED
Expected foreign subs (11): Shop TJC Limited, UK; STS Global Supply Limited, Hong Kong; Shop LC GmbH, Germany; STS (Guangzhou) Trading Limited Company, China; STS Jewels Inc., USA; Mindful Souls B.V., Netherlands; PT. STS Bali, Indonesia; VGL Retail Ventures Limited, Mauritius; STS Global Limited, Thailand; STS Global Limited, Japan; Shop LC Global Inc., USA

### POLYPLEX CORPORATION LIMITED
CIN L25209UR1984PLC011596 | NSE POLYPLEX | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://investor.polyplex.com/financial-subsidiaries.aspx
TARGET FOLDER: L25209UR1984PLC011596__POLYPLEX CORPORATION LIMITED
Expected foreign subs (11): Polyplex USA LLC; Polyplex (Thailand) Public Company Ltd.; Polyplex Europa Polyester Film Sanayi Ve Ticaret A.S; PT Polyplex Films Indonesia (PT PFI); EcoBlue Limited; Polyplex Paketleme Cozumleri Sanayi Ve Ticaret Anonim Sirketi (PP); Polyplex (Asia) Pte. Ltd.; Polyplex Europe B.V. (PEBV); Polyplex (Singapore) Pte. Ltd.; PAR LLC; Polyplex America Holdings Inc.


### CAPILLARY TECHNOLOGIES INDIA LIMITED
CIN L72200KA2012PLC063060 | NSE CAPILLARY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L72200KA2012PLC063060__CAPILLARY TECHNOLOGIES INDIA LIMITED
Expected foreign subs (10): Capillary Technologies LLC (Formerly known as Pursuade Loyalty LLC); Capillary Brierley Inc.; Capillary Brierley Inc. (formerly known as Brierley & Partners, Inc) (w.e.f. April 1, 2023); Capillary Technologies Europe Limited; Capillary Technologies Europe Limited (Formerly Known as Brierley Europe Limited); Capillary Pte. Ltd. (CPL); Capillary Technologies DMCC (Capillary Dubai); Capillary Technologies Inc,USA; Capillary Technologies (Malaysia) SDN BHD; PT Capillary Technologies Indonesia (Capillary Indonesia)

### RAIL VIKAS NIGAM LIMITED
CIN L74999DL2003GOI118633 | NSE RVNL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://rvnl.org/investor
TARGET FOLDER: L74999DL2003GOI118633__RAIL VIKAS NIGAM LIMITED
Expected foreign subs (10): RVNL Infra Middle East (Oman); RVNL Middle East Contracting L.L.C. (Dubai); Rail Vikas Nigam LLC (Uzbekistan); RVNL Infra South Africa; Rail Vikas Nigam Company Ltd. (One Person Company) (Kingdom of Saudi Arabia); Rail Vikas Nigam LLC (Uzbekistan); RVNL Middle East Contracting L.L.C. (Dubai); RVNL Infra Middle East (Oman); RVNL Infra South Africa; Rail Vikas Nigam Ltd. Company (One Person) (Kingdom of Saudi Arabia)

### FINEOTEX CHEMICAL LIMITED
CIN L24100MH2004PLC144295 | NSE FCL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L24100MH2004PLC144295__FINEOTEX CHEMICAL LIMITED
Expected foreign subs (10): BT Chemicals SDN. BHD; BT Biotex SDN.BHD; Rovatex SDN BHD; Fineotex Malaysia Limited; Fineotex Biotex Healthguard FZE; Crude Chem Technology LLC; Frackmex Equipments LLC; Oil Pro Advantage Inc; Lonester Technoboost LLC; BT Biotex Limited

### VINSYS IT SERVICES INDIA LIMITED
CIN L72200PN2008PLC131274 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.vinsys.com/investor/subsidiaries-accounts
TARGET FOLDER: L72200PN2008PLC131274__VINSYS IT SERVICES INDIA LIMITED
Expected foreign subs (9): Vinsys Information Technology Consultancy, Dubai (Step-Down Subsidiary of the Company); Vinsys Information Technology Consultancy Sole Proprietorship LLC, Abu Dhabi; Vinsys Information Technology Services LLC, Dubai; Vinsys Arabia Information Technology Company, Saudi Arabia; Vinsys IT Services LLC Qatar; Vinsys International Limited, UAE Dubai; Vinsys Corporation, USA; Vinsys IT Services LLC (Dubai); Vinsys Corporation (US)

### SECUREKLOUD TECHNOLOGIES LIMITED
CIN L72300TN1993PLC101852 | NSE SECURKLOUD | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.securekloud.com/subsidiary-financials
TARGET FOLDER: L72300TN1993PLC101852__SECUREKLOUD TECHNOLOGIES LIMITED
Expected foreign subs (8): Healthcare Triangle Inc, USA; SecureKloud Technologies Inc., USA; Blockedge Technologies Inc., USA; Devcool Inc, USA; SecureKloud Technologies Inc, Canda; SecureKloudTechnologies Inc, Canada; Nexage Technologies Inc; Mentor Minds Solutions and Services Inc. USA
