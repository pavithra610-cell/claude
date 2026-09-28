# Emami Cluster Research — Fastgrow Crops / Supergrow / Superfast LLP Network

## 1. What is Fastgrow Crops Private Limited?

Fastgrow Crops Private Limited (CIN U01403WB2011PTC160585) is itself listed, by name,
as item 16 in Emami Realty Limited's SEBI Regulation 23(9) Related Party Transaction
(RPT) disclosures, in the category **"Entities wherein the Company's promoters have
significant influence."** It sits in the same list as other Emami-promoter-linked
entities such as Emami Limited, Emami Agrotech Limited, Emami Estates Private Limited,
Emami Home Private Limited, Emami Vriddhi Commercial Private Limited, and — critically
— the entire "Fastgrow", "Superfast", "Supergrow", "Everline", "Prime", "Snowline",
"Viewline", "Fast Home" and "Supervalue" families of LLPs.

Its listing under the "promoters have significant influence" heading (rather than
under "Subsidiaries", "Associates", or "Joint Ventures") is consistent with Fastgrow
Crops being a company **controlled or significantly influenced by the Emami promoter
group** (the Goenka family / Emami Group), not an independent third party. This matches
the working hypothesis that Fastgrow Crops functions as a promoter-group holding/
investment vehicle used to hold minority (in the source MGT-7 data, 50%) stakes in the
very large family of "Supergrow ___ LLP" / "Superfast ___ LLP" / "Fastgrow ___ LLP"
single-asset real-estate LLPs.

**Caveat:** none of the documents actually read for this task state Fastgrow Crops'
own shareholding percentage in any specific LLP, nor its own list of directors or
paid-up capital — direct attempts to reach MCA/Zaubacorp/Tofler company-detail pages
for Fastgrow Crops were blocked (bot-detection / 403) and could not be read. The
50%-associate figure comes from the internal MGT-7 dataset referenced in the task
brief, not from anything independently confirmed in this research pass.

## 2. What the RPT disclosures show about the LLP cluster

Across the documents actually read, Emami Realty Ltd. discloses **hundreds of LLPs**
(and a smaller number of private limited companies) under the single heading "Entities
wherein the Company's promoters have significant influence." These fall into clear
naming families, each family sharing a common first word and a project-style second
word, e.g.:

- **Fastgrow** ___ LLP (Amenities, Avas, Avenues, Bricks, Buildcon, Buildings,
  Citylights, Concrete, Connect, Constech, Designs, Developers, Dream Home, Dwelling,
  Elite Property, Empire, Galaxy, Greenview, Heritage, Home Constructions, Iconic,
  Landmark, Legacy, Lighthouse, Living, Lodging, Luxe Living, Majestic, Modern Realty,
  Nest, Niketan, Northwood, Residency, Residential, Skytowers, Smart Homes, Sweet
  Living, Township, Ultima, Urban, Voyage Realty …)
- **Supergrow** ___ LLP (Abasan, Amenities, Apartment, Ashiyana, Avas, Avenues, Brick,
  Buildcon, Buildings, Citylights, Commodeal, Conclave, Concrete, Connect, Constech,
  Creative, Designs, Developers, Dream Home, Dwelling, Elite Properties, Empire,
  Enclave, Estate, Galaxy, Heritage, Highrise, Home Construction, Horizon, Housing,
  Iconic, Infocom, Landmark, Legacy, Lifestyle, Lighthouse, Lodging, Luxe Living,
  Majestic, Modern Realty, Nest, Niketan, Nirman, Nivas, Northwood, Paradise, Planner,
  Promoters, Residency, Resort, Shelter, Skytowers, Township, Ultima, Villa …)
- **Superfast** ___ LLP — a very large family (100 distinct names extracted in full;
  see CSV) that appears newly added between the March-2021 and September-2021/2022
  disclosures (it is **absent** from the year-ended-31-March-2021 filing and present
  in the half-year-ended-30-September-2021 and half-year-ended-30-September-2022
  filings).
- Sibling families with the same design pattern but different lead words: **Everline**,
  **Prime** / **Prime Fast**, **Snowline**, **Viewline**, **Fast Home**, **Supervalue**.

All of these sit alongside the smaller number of directly-named Emami/Fastgrow/
Supervalue private limited companies (Fastgrow Beverages Pvt Ltd, Fastgrow Nirman Pvt
Ltd, Fastgrow Crops Pvt Ltd, Fastgrow Projects Pvt Ltd, Supervalue Buildcon/
Constructions/Projects Pvt Ltd, Emami Agrotech, Emami Estates, Emami Home, Emami
Vriddhi Commercial, etc.) under the very same "significant influence" heading — i.e.
the disclosure treats the private companies and the hundreds of LLPs as one
undifferentiated promoter-influence bucket, it does not separately flag Fastgrow Crops
as the specific holder of the LLP interests.

No document read stated an explicit linking sentence such as "Fastgrow Crops Private
Limited holds 50% in each of the following LLPs" — that specific mechanical link (the
50%-associate relationship) is asserted only in the internal MGT-7 dataset described
in the task brief, and was not independently corroborated in the public disclosures
read here. The public disclosures corroborate only that (a) Fastgrow Crops and (b) the
whole Supergrow/Superfast/Fastgrow LLP cluster are named together, in the same
promoter-influence category, across multiple half-yearly filings.

## 3. Documents read (fetched) and used as evidence

All four were scanned/OCR'd PDFs; standard PDF text extraction returned only
compressed image-stream garbage, so they were read via a text-rendering fetch proxy
(`r.jina.ai/<original PDF url>`) over the same published PDF URLs — the content is
the same underlying public filing, just extracted through a working text pipeline.

| # | Document | Period | URL |
|---|----------|--------|-----|
| 1 | Emami Realty Ltd. RPT Disclosure (Reg. 23(9) SEBI LODR) | Year ended 31 March 2021 | https://emamirealty.com/wp-content/uploads/2022/07/ERL-RPT-Disclosure-March-2021.pdf |
| 2 | Emami Realty Ltd. RPT Disclosure (Reg. 23(9) SEBI LODR) | Half-year ended 30 September 2021 | https://emamirealty.com/wp-content/uploads/2023/01/ERL-RPT-Disclosure-Sep-2021.pdf |
| 3 | Emami Realty Ltd. RPT Disclosure (Reg. 23(9) SEBI LODR) | Half-year ended 30 September 2022 | https://emamirealty.com/wp-content/uploads/2022/12/ERL_RPT-Disclosure_30.09.2022.pdf |
| 4 | Emami Realty Ltd. RPT Disclosure (Reg. 23(9) SEBI LODR) | Half-year ended 31 March 2022 | https://emamirealty.com/wp-content/uploads/2022/07/ERL-RPT-Disclosure_31.03.2022.pdf |

Document 1 was extracted in **full** (226 entities, serials 1–226).
Document 2 was extracted in **full** for serials 1–20 and 100–323 (303 entities); the
middle range (21–99) was not separately re-verified and is not asserted here beyond
what overlaps with Document 1's confirmed entries.
Document 3 was only **partially** extracted: a representative sample of the private
limited companies (including confirmed presence of "Fastgrow Crops Private Limited")
plus a **complete, separately re-extracted list of 100 distinct "Superfast ___ LLP"
names**. The bulk of its ~410 total rows (Everline/Prime/Snowline/Viewline/Fastgrow/
Supergrow blocks) was only summarised by the fetch tool, not transcribed verbatim, and
is therefore **not** included as individual CSV rows.
Document 4 was only minimally extracted: the tool confirmed "Fastgrow Crops Private
Limited" appears at serial 99 with loan/security-deposit transactions, but did not
return other individual entity names verbatim.

## 4. Documents/sources sought but NOT usable (do not treat as evidence)

- `https://www.bseindia.com/bseplus/AnnualReport/533218/72121533218.pdf` — HTTP 403,
  not read.
- `https://nsearchives.nseindia.com/corporate/EMAMILTD_23062021190755_Emami_RPT_H2Mar21.pdf`
  (Emami Ltd., not Emami Realty, RPT half-year Mar-2021) — HTTP 503, not read.
- Emami Realty Annual Report 2020–21
  (`https://emamirealty.com/wp-content/uploads/2022/07/Emami-Realty-Limited_Annual-Report-2020-21-1.pdf`)
  — fetched, but the extracted excerpt only pointed to "Note 41" of the standalone
  financial statements for the related-party detail; that note's content itself was
  not present in the extracted text and so is not used as evidence here.
- Zaubacorp and Tofler company pages for Fastgrow Crops Private Limited — both blocked
  by bot-detection/403; no company-registry detail (directors, capital, shareholding)
  for Fastgrow Crops was obtainable in this pass.
- No RPT disclosure PDFs specifically dated 2023, 2024, 2025 or 2026 were found on
  emamirealty.com via search; the site's most recent located filings in this pass were
  the AGM/annual-report intimations for FY2023-24/2024-25, not standalone RPT-format
  disclosure PDFs. If later-period RPT disclosures exist, their URLs were not
  discoverable via the search queries used here — do not assume they don't exist, only
  that they weren't found.
- No Emami Paper Mills related-party disclosure was located.

## 5. How to use EMAMI_CLUSTER_EVIDENCE.csv

Row agents should match their assigned "Supergrow ___ LLP" / "Superfast ___ LLP" /
"Fastgrow ___ LLP" (etc.) entity name against the `ENTITY_NAME` column (case-
insensitive, allowing for minor punctuation/spacing variants such as "Appartments" vs
"Apartments" or "Everrise" vs "Ever Rise" as actually printed in the source PDFs). A
match confirms the entity is named in a specific Emami Realty Ltd. Reg. 23(9) RPT
disclosure, under "Entities wherein the Company's promoters have significant
influence," alongside Fastgrow Crops Private Limited and the wider Emami-promoter
entity list — supporting (but not, on its own, proving the exact 50% figure for) the
house-24349 Emami Group association. `FETCHED_OR_SNIPPET` is always `FETCHED` in this
file (no snippet-only rows were included; entities not independently confirmed by
extracted text were left out rather than guessed).
