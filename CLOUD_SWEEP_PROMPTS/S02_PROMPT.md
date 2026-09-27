# CLOUD SWEEP SLICE S02 - 25 PARENTS (27-Sep-2026)
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
### TAC INFOSEC LIMITED
CIN L72900PB2016PLC045575 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L72900PB2016PLC045575__TAC INFOSEC LIMITED
Expected foreign subs (8): TAC Security INC; Sandia IT & Cybersecurity Services, LLC; TAC Cyber Security Consultancy LLC; VulMan Ltd; CyberScope I.K.E.; Sandia IT & Cybersecurity Services, LLC; VULMAN LIMITED; Sandia IT & Cybersecuirty L.L.C

### AFCONS INFRASTRUCTURE LIMITED
CIN L45200MH1976PLC019335 | NSE AFCONS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.afcons.com/sites/default/files/2025-06/
TARGET FOLDER: L45200MH1976PLC019335__AFCONS INFRASTRUCTURE LIMITED
Expected foreign subs (8): Afcons Construction Mideast LLC; Afcons Overseas Singapore Pte Ltd.; Afcons Mauritius Infrastructure Ltd; Afcons Infrastructures Kuwait for Building, Roads and Marine Contracting WLL; Afcons Infra Projects Kazakhstan LLP; Afcons Gulf International Project Services FZE; Afcons Overseas Project Gabon SARL; Afcons Contracting Company Saudi Arabia

### RELIANCE POWER LIMITED
CIN L40101MH1995PLC084687 | NSE RPOWER | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.reliancepower.co.in/financial-statements-of-subsidiaries
TARGET FOLDER: L40101MH1995PLC084687__RELIANCE POWER LIMITED
Expected foreign subs (8): Reliance Power Holding FZC, Dubai (RFZC) (w.e.f. May 15, 2016); Reliance Power Netherlands BV (RPN); PT Heramba Coal Resources (PTH); PT Avaneesh Coal Resources (PTA); Reliance Natural Resources (Singapore) Pte Limited (RNRL- Singapore); PT Sumukha Coal Services (PTS); PT Brayan Bintang Tiga Energi (BBE); PT Sriwijiya Bintang Tiga Energi (SBE)

### CYIENT LIMITED
CIN L72200TG1991PLC013134 | NSE CYIENT | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L72200TG1991PLC013134__CYIENT LIMITED
Expected foreign subs (8): Cyient Europe Limited, UK; Cyient Australia Pty Ltd, Australia; Cyient GmbH, Germany; Cyient KK, Japan; Cyient Singapore Private Limited, Singapore; Cyient Project Management Consultancy LLC SPC; Cyient Israel India Limited, Israel*; Cyient Inc., USA

### VOLTAS LIMITED
CIN L29308MH1954PLC009371 | NSE VOLTAS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.voltas.in/investors/disclosure-under-regulation-46-lodr/audited-financials-of-subsidiaries
TARGET FOLDER: L29308MH1954PLC009371__VOLTAS LIMITED
Expected foreign subs (8): Saudi Ensas Company for Engineering Services & Trading W.L.L. (Saudi Ensas); Universal MEP Contracting Services & Trading W.L.L. (UMCST) (Formerly known as Voltas Qatar W.L.L.); Universal Lalbuksh Engineering Services Trading L.L.C. (ULAL) (Formerly known as Lalbuksh Voltas Engineering Services & Trading L.L.C.); Universal Oman SPC (UOSPC) (Formerly known as Voltas Oman SPC); Weathermaker FZE (WMF); Universal MEP Projects Pte Limited (UMPPL); Voltas Netherlands B.V. (VNBV); Universal MEP Contracting L.L.C. (UMCL)

### MANORAMA INDUSTRIES LIMITED
CIN L15142MH2005PLC243687 | NSE MANORAMA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://manoramagroup.co.in/investors-financial
TARGET FOLDER: L15142MH2005PLC243687__MANORAMA INDUSTRIES LIMITED
Expected foreign subs (8): Manorama Savanna Limited; Manorama Latin America LTDA; Manorama Savanna Togo SARL; Manorama Mena Trading LLC; Manorama Africa Benin; Manorama Africa Savanna IVC; Manorama Burkina SARL; Manorama Savanna Ghana Limited

### DIGITIDE SOLUTIONS LIMITED
CIN L62099KA2024PLC184626 | NSE DIGITIDE | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.digitide.com/investors/financial-subsidaries-associate-companies-fy25/
TARGET FOLDER: L62099KA2024PLC184626__DIGITIDE SOLUTIONS LIMITED
Expected foreign subs (8): Alldigi Tech Inc, USA; MFXchange US, Inc; Mindwire Systems Limited; Alldigi Tech Manila Inc, Philippines; Brainhunter Systems Limited; MFXchange Holdings, Inc.; Quess Corp (USA) Inc.; Quess GTS Canada Holding Inc.

### ALOK INDUSTRIES LIMITED
CIN L17110DN1986PLC000334 | NSE ALOKINDS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | subs page not known - find it
TARGET FOLDER: L17110DN1986PLC000334__ALOK INDUSTRIES LIMITED
Expected foreign subs (7): Mileta a.s; Alok Singapore Pte Ltd.; Alok International, Inc.; Alok World Wide Limited; Alok International (middle east) FZE; Grabal Alok International Limited; Alok Industries International Limited

### JINDAL STAINLESS LIMITED
CIN L26922HR1980PLC010901 | NSE JSL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.jindalstainless.com/financials/financials-statements/
TARGET FOLDER: L26922HR1980PLC010901__JINDAL STAINLESS LIMITED
Expected foreign subs (7): Iberjindal S.L.; Sungai Lestari Investment Pte. Ltd.; PT. Jindal Stainless Indonesia; Sulawesi Nickel Processing Industries Holdings Pte. Ltd.; Evergreat International Investment Pte. Ltd.; JSL Group Holdings Pte. Ltd.; Jindal Stainless FZE

### Symphony Limited
CIN L32201GJ1988PLC010331 | NSE SYMPHONY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://symphonylimited.com/investor/results/
TARGET FOLDER: L32201GJ1988PLC010331__SYMPHONY LIMITED
Expected foreign subs (7): Climate Technologies Pty. Ltd.; Guangdong Symphony Keruilai Air Coolers Co., Ltd; IMPCO S DE RL DE CV; Symphony Climatizadores Ltda; Bonaire USA LLC, USA; Dongguan GSK Appliances Co. Limited; Symphony AU Pty. Ltd., Australia

### LAXMI ORGANIC INDUSTRIES LIMITED
CIN L24200MH1989PLC051736 | NSE LXCHEM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.laxmi.com/investors/subsidiary-financials
TARGET FOLDER: L24200MH1989PLC051736__LAXMI ORGANIC INDUSTRIES LIMITED
Expected foreign subs (7): Laxmi Organic Industries (Europe) BV, Netherlands (LOBV); Laxmi Speciality Chemicals (Shanghai) Co. Limited; Laxmi Italy Srl (LISRL); Laxmi U.S.A. LLC; Laxmi Italy Srl; Laxmi Italy Srl; Laxmi Petrochem Middle East FZE

### WINSOME YARNS LTD
CIN L17115CH1990PLC010566 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | subs page not known - find it
TARGET FOLDER: L17115CH1990PLC010566__WINSOME YARNS LTD
Expected foreign subs (7): Winsome Yarns (Cyprus) Ltd, Cyprus; Winsome Yarns FZE, UAE; S.C. WINSOME ROMANIA S.R.L; IMM WINSOME ITALIA S.R.L.; S.C. TEXTILE S.R.L; WINSOME YARNS CYPRUS LIMITED; WINSOME YARNS FZE

### ASHAPURA MINECHEM LTD
CIN L14108MH1982PLC026396 | NSE ASHAPURMIN | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.ashapura.com/investor-corner.php
TARGET FOLDER: L14108MH1982PLC026396__ASHAPURA MINECHEM LTD
Expected foreign subs (7): Ashapura Holdings (UAE) FZE; Ashapura Midgulf NV; Ashapura Guinea Resources SARL; Ashapura Fareast SDN BHD; PT Ashapura Bentoclay Fareast; Ashapura Holding Fareast Pte Ltd; Ashapura Minechem (UAE) FZE

### EMBASSY DEVELOPMENTS LIMITED
CIN L45101HR2006PLC095409 | NSE EMBDL | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://embassyindia.com/investor-relations/financial-other-reports/audited-financial-statements-of-subsidiary-companies/
TARGET FOLDER: L45101HR2006PLC095409__EMBASSY DEVELOPMENTS LIMITED
Expected foreign subs (7): M Holdco 1 Limited; M Holdco 2 Limited; M Holdco 3 Limited; Navilith Holdings Limited; Brenformexa Limited; Dev Property Development Limited; Ariston Investments Limited

### Kerala Ayurveda Limited
CIN L24233KL1992PLC006592 | NSE n/a | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://keralaayurveda.com/pages/investors
TARGET FOLDER: L24233KL1992PLC006592__KERALA AYURVEDA LIMITED
Expected foreign subs (6): Ayu Natural Medicine Clinic, P.S.; Ayu Natural Medicine Clinic, P.S.; Ayurvedic Academy Inc.; Ayurvedic Academy Inc.; Suveda Inc.; Suveda Inc.; Nutraveda PTE Ltd; Nutraveda PTE Ltd; CMS Katra Holdings LLC; CMS Katra Holdings LLC; CMS Katra Nursing LLC; CMS Katra Nursing LLC; Ayu Natual Medicine Clinic PS; Ayu Natual Medicine Clinic PS; CMS Katra Holding LLC USA; CMS Katra Holding LLC USA

### NIIT LIMITED
CIN L74899HR1981PLC107123 | NSE NIITLTD | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.niit.com/india/investors/pages/subsidiaries-financials/
TARGET FOLDER: L74899HR1981PLC107123__NIIT LIMITED
Expected foreign subs (6): NIIT China (Shanghai) Limited, Shanghai; NIIT (Guizhou) Education Technology Co., Limited, China; Chongqing NIIT Enterprises Management Consulting Co., Ltd; PT NIIT Indonesia, Indonesia; NIIT GC Limited, Mauritius; Guizhou NIIT Information Technology Consulting Co., Limited, China

### KAVVERI DEFENCE & WIRELESS TECHNOLOGIES LIMITED
CIN L85110KA1996PLC019627 | NSE KAVDEFENCE | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.kavveridefence.com/investor/
TARGET FOLDER: L85110KA1996PLC019627__KAVVERI DEFENCE AND WIRELESS TECHNOLOGIES LIMITED
Expected foreign subs (6): TIL TEK ANTENNAE INC; Kavveri Realty 5 Inc.; KAVVERI TECHNOLOGIES INC; KAVVERI TECHNOLOGIES AMERICA INC; KAVVERI REALITY 5 INC; DCI- DIGITAL COMMUNICATIONS LTD

### RISHABH INSTRUMENTS LIMITED
CIN L31100MH1982PLC028406 | NSE RISHABH | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://rishabh.co.in/investor-relation
TARGET FOLDER: L31100MH1982PLC028406__RISHABH INSTRUMENTS LIMITED
Expected foreign subs (6): Sifam Tinsley Instrumentation Limited, UK; Lumel Alucast Sp. Z.o.o (Earlier ECO 1 Sp. Z.o.o.), Poland; LUMEL S.A., Poland; Shanghai VA Instruments Co. Ltd. China; Sifam Tinsley Instrumentation Inc., USA; Dhruv Enterprises Limited, Cyprus

### MATRIMONY.COM LIMITED
CIN L63090TN2001PLC047432 | NSE MATRIMONY | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.matrimony.com/investors/investor-reports?search=financial_fillings&cat=Subsidiary%20financials
TARGET FOLDER: L63090TN2001PLC047432__MATRIMONY.COM LIMITED
Expected foreign subs (6): Bangladeshi Matrimony Private Limited; Bangladeshi Matrimony Private Limited; Matrimony DMCC; Matrimony DMCC; Consim Info USA; Consim Info USA Inc

### SHREE CEMENT LIMITED
CIN L26943RJ1979PLC001935 | NSE SHREECEM | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.shreecement.com/investors
TARGET FOLDER: L26943RJ1979PLC001935__SHREE CEMENT LIMITED
Expected foreign subs (6): Union Cement Company PrJSC; U C N Co Ltd. L.L.C. (Indirect Subsidiary Company) (Liquidated on 18 March, 2025); U C N Co Ltd. L.L.C.; Shree Enterprises Management Ltd.; Shree International Holding Ltd.; Shree Global FZE

### NARAYANA HRUDAYALAYA LIMITED
CIN L85110KA2000PLC027497 | NSE NH | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.narayanahealth.org/stakeholder-relations/subsidiary-companies-financial-statements
TARGET FOLDER: L85110KA2000PLC027497__NARAYANA HRUDAYALAYA LIMITED
Expected foreign subs (6): HEALTH CITY CAYMAN ISLANDS LTD.; ENT in Cayman Ltd; Cayman Integrated Healthcare Ltd; NARAYANA HEALTH NORTH AMERICA, LLC; NH HEALTH BANGLADESH PRIVATE LIMITED.; NARAYANA HOLDINGS PRIVATE LIMITED

### Brainbees Solutions Limited
CIN L51100PN2010PLC136340 | NSE FIRSTCRY | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.firstcry.com/investor-relations/subsidiaries
TARGET FOLDER: L51100PN2010PLC136340__BRAINBEES SOLUTIONS LIMITED
Expected foreign subs (6): Firstcry Retail DWC-LLC; Firstcry General Trading L.L.C; Firstcry Trading Company; Globalbees Brands DWC; Firstcry Management DWC LLC; Shenzhen Starbees Services Ltd

### PRAJ INDUSTRIES LIMITED
CIN L27101PN1985PLC038031 | NSE PRAJIND | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://www.praj.net/investors-type/financial-reports-of-subsidiaries/
TARGET FOLDER: L27101PN1985PLC038031__PRAJ INDUSTRIES LIMITED
Expected foreign subs (6): Praj Americas Inc. USA; Praj Americas Inc; Praj Far East Co., Ltd. Thailand; Praj Projects (Tanzania) Limited; Praj Far East Phillipines Ltd Inc; Praj Far East Philippinnes Ltd., The Philippinnes

### ORCHID PHARMA LIMITED
CIN L24222TN1992PLC022994 | NSE ORCHPHARMA | SCOPE: FULL: AR FY26 + AOC-1 page range + all subs financials | KNOWN SUBS PAGE: https://www.orchidpharma.com/downloads/annualreports/
TARGET FOLDER: L24222TN1992PLC022994__ORCHID PHARMA LIMITED
Expected foreign subs (6): Diakron Pharmaceuticals Inc., USA; Bexel Pharmaceuticals Inc., USA; Orchid Pharmaceuticals Inc USA (including the 2 Step Down Subsidiaries); O r c h i d Pharmaceuticals Inc And Subsidiaries, USA (including the 2 Step Down Subsidiaries); Orchid Pharmaceuticals I n c . , a n d Subsidiaries, USA; Diakron Pharmaceuticals Inc, USA

### NUCLEUS SOFTWARE EXPORTS LIMITED
CIN L74899DL1989PLC034594 | NSE NUCLEUS | SCOPE: SUBS FINANCIALS ONLY (we hold the FY26 AR; record the AR url and AOC-1 page range, do not list the AR as a download) | KNOWN SUBS PAGE: https://investor.nucleussoftware.com/SubsidiaryFinancials.aspx
TARGET FOLDER: L74899DL1989PLC034594__NUCLEUS SOFTWARE EXPORTS LIMITED
Expected foreign subs (6): NUCLEUS SOFTWARE SOLUTIONS PTE LTD; NUCLEUS SOFTWARE JAPAN KABUSHIKI KAISHA; NUCLEUS SOFTWARE AUSTRALIA PTY LTD; NUCLEUS SOFTWARE SOUTH AFRICA PTY. LTD.; NUCLEUS SOFTWARE INC.; NUCLEUS SOFTWARE NETHERLANDS B.V.
