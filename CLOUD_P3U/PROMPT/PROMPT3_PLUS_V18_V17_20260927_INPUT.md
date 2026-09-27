You are extracting MAXIMUM financial and corporate intelligence from a subsidiary company's audited annual report PDF. Extract EVERY data point available. Return ONLY valid JSON.

{
  "DENOMINATION_EVIDENCE": {
    "MANDATORY_NOTE": "You MUST populate all 5 evidence fields below. Read the P&L header, Balance Sheet header, notes header, auditor report, and any footnote. Quote EXACTLY as printed.",
    "E1_PL_HEADER": "MANDATORY — exact verbatim quote of denomination statement from P&L / Income Statement header or footer e.g. 'All amounts in INR lakhs unless otherwise stated' or 'USD thousands'",
    "E2_BS_HEADER": "MANDATORY — exact verbatim quote of denomination statement from Balance Sheet header or footer",
    "E3_NOTES_HEADER": "exact verbatim quote from Notes to Accounts header, if denomination stated there",
    "E4_AUDITOR_OR_OTHER": "exact verbatim quote from auditor report or any other section confirming denomination e.g. 'materiality threshold of Rs. 2.5 lakhs' or 'balance sheet total EUR 10,243 thousand'",
    "E5_CROSS_CHECK": "arithmetic cross-check: pick ONE number from the document (e.g. share capital, total assets, or EPS) and verify it is consistent with the stated denomination. Format: 'Share capital = 5.00 in statement. Authorized capital note says Rs 50,00,000 = Rs 50 lakhs → consistent with lakhs denomination'",
    "currency_confirmed": "3-letter ISO code confirmed from E1/E2",
    "denomination_confirmed": "units/thousands/millions/lakhs/crores confirmed from E1/E2",
    "digit_grouping_on_page": "(V5) WESTERN 1,234,567 / INDIAN 12,34,567 / EUROPEAN_DOT 1.234.567 / MIXED — as printed on the statements. Regroup every number to plain western digits; removing separators is the only transformation allowed, never divide or multiply",
    "statement_scope": "(V5) standalone / consolidated / both printed — say which column every number below is taken from",
    "column_labels": "(V5) exact year headers of the cy and py columns as printed, e.g. '31 March 2025' / '31 March 2024'",
    "statement_pages": {"balance_sheet": null, "profit_and_loss": null, "cash_flow": null, "notes_from_to": null, "cash_and_bank_note": null, "borrowings_note": null, "related_party_note": null, "contingent_liabilities_note": null, "fx_risk_note": null, "page_numbering": "(V5) PRINTED or PDF_INDEX — which numbering every page field in this JSON uses"}
  },

  "IDENTITY": {
    "company_name": null,
    "company_registration_number": "Companies House # / CIN / registration ID",
    "tax_id": "VAT number / GST number / TIN / EIN / PAN",
    "lei": "Legal Entity Identifier if mentioned",
    "sic_code": "SIC / NIC / NAICS code if stated",
    "principal_activity": "what the company does — one line",
    "date_of_incorporation": "YYYY-MM-DD",
    "country_of_incorporation": null,
    "registered_address": "full address as printed",
    "business_address": "operating address if different from registered",
    "currency": "3-letter ISO (GBP/USD/INR/EUR etc) — MUST match DENOMINATION_EVIDENCE.currency_confirmed",
    "denomination": "units/thousands/millions/lakhs/crores — MUST match DENOMINATION_EVIDENCE.denomination_confirmed",
    "financial_year_end": "YYYY-MM-DD",
    "dormant_flag": "true if company is dormant/inactive/shell, false if active",
    "has_employees": "true/false",
    "status": "active/dormant/under_liquidation/struck_off"
  },

  "OWNERSHIP": {
    "immediate_parent": "name of direct parent company",
    "immediate_parent_country": null,
    "ultimate_parent": "name of ultimate holding company",
    "ultimate_parent_country": null,
    "parent_holding_pct": "% held by immediate parent",
    "shares_issued": "number of shares in issue",
    "par_value_per_share": null,
    "share_capital_currency": null,
    "ownership_chain": "(V5) immediate parent -> intermediate holdcos -> ultimate parent, each with country, exactly as printed",
    "indian_parent_link": "(V5) how the Indian parent holds this company (direct / via which holdco), as printed",
    "changes_in_year": "(V5) acquisitions, disposals, renames, mergers, capital injections or reductions in the year, as printed, with page",
    "branches": [ {"country": null, "page": null} ]
  },

  "SUB_SUBSIDIARIES": [
    {
      "name": "name of entity owned by THIS company",
      "country": null,
      "holding_pct": null,
      "nature": "subsidiary/associate/JV"
    }
  ],

  "GOVERNANCE": {
    "directors": [
      {"name": null, "designation": "director/managing director/chairman", "remuneration_cy": null}
    ],
    "company_secretary": null,
    "auditor": null,
    "audit_opinion": "unqualified/qualified/adverse/disclaimer/emphasis_of_matter",
    "audit_fee_cy": null,
    "audit_fee_py": null,
    "non_audit_fee_cy": null,
    "going_concern_flag": "true if going concern doubt mentioned, false otherwise",
    "kmp_total_remuneration_cy": null,
    "highest_paid_director_cy": null,
    "average_employee_remuneration_cy": null
  },

  "PROFIT_AND_LOSS": {
    "revenue": {"cy": null, "py": null},
    "cost_of_sales": {"cy": null, "py": null},
    "gross_profit": {"cy": null, "py": null},
    "employee_costs": {"cy": null, "py": null},
    "employee_count": {"cy": null, "py": null},
    "depreciation_and_amortisation": {"cy": null, "py": null},
    "research_and_development": {"cy": null, "py": null},
    "other_expenses": {"cy": null, "py": null},
    "total_expenses": {"cy": null, "py": null},
    "operating_profit": {"cy": null, "py": null},
    "other_income": {"cy": null, "py": null},
    "interest_income": {"cy": null, "py": null},
    "dividend_income": {"cy": null, "py": null},
    "finance_costs": {"cy": null, "py": null},
    "foreign_exchange_gain_loss": {"cy": null, "py": null},
    "exceptional_items": {"cy": null, "py": null, "detail": null},
    "profit_before_tax": {"cy": null, "py": null},
    "current_tax": {"cy": null, "py": null},
    "deferred_tax": {"cy": null, "py": null},
    "profit_after_tax": {"cy": null, "py": null},
    "other_comprehensive_income": {"cy": null, "py": null},
    "total_comprehensive_income": {"cy": null, "py": null}
  },

  "SEGMENT": {
    "has_segments": "true/false",
    "segments": [
      {"name": null, "revenue_cy": null, "profit_cy": null, "assets_cy": null}
    ],
    "geographic_revenue": [
      {"geography": null, "revenue_cy": null, "revenue_py": null}
    ],
    "major_customer_flag": "true if any single customer >10% revenue"
  },

  "BALANCE_SHEET": {
    "fixed_assets_tangible": {"cy": null, "py": null},
    "fixed_assets_intangible": {"cy": null, "py": null},
    "right_of_use_assets": {"cy": null, "py": null},
    "capital_work_in_progress": {"cy": null, "py": null},
    "goodwill": {"cy": null, "py": null},
    "investments_in_subsidiaries": {"cy": null, "py": null},
    "investments_other_non_current": {"cy": null, "py": null},
    "loans_and_advances_non_current": {"cy": null, "py": null},
    "deferred_tax_asset": {"cy": null, "py": null},
    "other_non_current_assets": {"cy": null, "py": null},
    "total_non_current_assets": {"cy": null, "py": null},

    "inventories": {"cy": null, "py": null},
    "trade_receivables": {"cy": null, "py": null},
    "unbilled_receivables": {"cy": null, "py": null},
    "cash_and_cash_equivalents": {"cy": null, "py": null, "banks_named": "list every bank where cash/current account is held e.g. HDFC Bank, Barclays, Citibank"},
    "fixed_deposits": {"cy": null, "py": null, "detail": "maturity/rate if stated", "banks_named": "list every bank where FD/deposit is placed"},
    "bank_balances_other": {"cy": null, "py": null, "banks_named": "list every bank for earmarked/escrow/margin money accounts"},
    "loans_and_advances_current": {"cy": null, "py": null},
    "other_current_assets": {"cy": null, "py": null},
    "investments_current": {"cy": null, "py": null},
    "contract_assets": {"cy": null, "py": null},
    "total_current_assets": {"cy": null, "py": null},

    "total_assets": {"cy": null, "py": null},

    "share_capital": {"cy": null, "py": null},
    "reserves_and_surplus": {"cy": null, "py": null},
    "total_equity": {"cy": null, "py": null},

    "borrowings_non_current": {"cy": null, "py": null},
    "lease_liabilities_non_current": {"cy": null, "py": null},
    "pension_obligation": {"cy": null, "py": null, "plan_assets_cy": null, "deficit_cy": null},
    "deferred_tax_liability": {"cy": null, "py": null},
    "provisions_non_current": {"cy": null, "py": null},
    "other_non_current_liabilities": {"cy": null, "py": null},
    "total_non_current_liabilities": {"cy": null, "py": null},

    "borrowings_current": {"cy": null, "py": null},
    "current_maturities_of_long_term_debt": {"cy": null, "py": null},
    "trade_payables": {"cy": null, "py": null},
    "lease_liabilities_current": {"cy": null, "py": null},
    "provisions_current": {"cy": null, "py": null},
    "current_tax_liability": {"cy": null, "py": null},
    "contract_liabilities": {"cy": null, "py": null},
    "other_current_liabilities": {"cy": null, "py": null},
    "total_current_liabilities": {"cy": null, "py": null},

    "total_liabilities": {"cy": null, "py": null},
    "total_equity_and_liabilities": {"cy": null, "py": null}
  },

  "CASH_FLOW": {
    "operating_cash_flow": {"cy": null, "py": null},
    "investing_cash_flow": {"cy": null, "py": null},
    "financing_cash_flow": {"cy": null, "py": null},
    "capex": {"cy": null, "py": null},
    "net_change_in_cash": {"cy": null, "py": null},
    "opening_cash": {"cy": null, "py": null},
    "closing_cash": {"cy": null, "py": null}
  },

  "DIVIDEND": {
    "dividend_paid": {"cy": null, "py": null},
    "dividend_per_share": {"cy": null, "py": null},
    "dividend_proposed": {"cy": null, "py": null}
  },

  "INTERCOMPANY": {
    "royalty_paid_to_parent": {"cy": null, "py": null},
    "royalty_received": {"cy": null, "py": null},
    "management_fee_paid": {"cy": null, "py": null},
    "management_fee_received": {"cy": null, "py": null},
    "brand_fee_paid": {"cy": null, "py": null},
    "shared_service_charge_paid": {"cy": null, "py": null},
    "cost_recharge_paid": {"cy": null, "py": null},
    "cost_recharge_received": {"cy": null, "py": null},
    "intercompany_sales": {"cy": null, "py": null},
    "intercompany_purchases": {"cy": null, "py": null},
    "intercompany_loans_given": {"cy": null, "py": null},
    "intercompany_loans_taken": {"cy": null, "py": null},
    "intercompany_interest_paid": {"cy": null, "py": null},
    "intercompany_interest_received": {"cy": null, "py": null},
    "intercompany_receivables": {"cy": null, "py": null},
    "intercompany_payables": {"cy": null, "py": null},
    "transfer_pricing_method": "TNMM / CUP / cost plus / resale minus / if mentioned",
    "loans_detail": [
      {"counterparty": "(V5) exact group entity name as printed", "direction": "from group / to group", "currency": null, "amount_cy": null, "amount_py": null, "interest_rate": "as printed", "repayment_or_maturity": "as printed", "security": "as printed", "subordination": "subordinated to bank debt? as printed", "page": null}
    ],
    "capital_received_in_year": {"amount_cy": null, "instrument": "(V5) equity / preference / quasi-equity / shareholder loan converted", "from_entity": null, "page": null},
    "group_treasury_deposits": {"counterparty": "(V5) group treasury / cash-pool entity holding this company's cash, if printed", "amount_cy": null, "currency": null, "page": null}
  },

  "BORROWINGS": {
    "total_borrowings_cy": null,
    "total_borrowings_py": null,
    "credit_facilities_available": "total sanctioned/committed facility amount",
    "credit_facilities_drawn": "total utilized amount",
    "undrawn_headroom": "available but undrawn amount",
    "all_lender_banks": "MANDATORY — comma-separated list of EVERY bank/NBFC/lender named anywhere in borrowing notes",
    "facilities": [
      {
        "bank_name": "MANDATORY — exact name AS PRINTED in the borrowing footnote. Read the note word by word. e.g. 'HDFC Bank Limited', 'State Bank of India', 'ING Bank N.V.'. NEVER shorten or guess. Use 'Not disclosed' ONLY if truly absent after reading every line of the note.",
        "bank_country": "country of the lending bank",
        "facility_type": "term loan/overdraft/revolving credit/bond/NCD/working capital/commercial paper/other",
        "currency": "MANDATORY — facility currency as stated in footnote e.g. INR, USD, EUR, GBP",
        "amount_cy": null,
        "amount_py": null,
        "sanctioned_limit": null,
        "interest_rate": "exact rate as printed e.g. SONIA+1.5%, 8.75% p.a., SOFR+2%, MCLR+0.25%",
        "interest_rate_benchmark": "SONIA/SOFR/LIBOR/MCLR/T-Bill/fixed/other",
        "maturity_date": "exact date or tenor as printed e.g. March 2028, 5 years from drawdown",
        "secured_unsecured": "Secured / Unsecured",
        "security_detail": "MANDATORY if secured — exact collateral/charge as printed e.g. 'first pari passu charge on all fixed assets', 'pledge of shares of subsidiary', 'mortgage on land at [address]'",
        "covenant_compliance": "compliant/breached/waived if stated",
        "purpose": "purpose of facility if stated",
        "footnote_verification": "MANDATORY — copy the exact sentence(s) from the borrowing footnote that names this bank and confirms this facility. Quote verbatim. e.g. 'Term loan from HDFC Bank Limited: INR 500 lakhs @ 8.75% p.a. repayable in 20 quarterly instalments, secured by first charge on fixed assets'",
        "drawn_cy": "(V5) amount drawn at year end, as printed",
        "undrawn_cy": "(V5) sanctioned minus drawn only if the note prints both; else null",
        "page": "(V5) integer page of the footnote line"
      }
    ]
  },

  "GUARANTEES": {
    "total_cy": null,
    "total_py": null,
    "has_corporate_guarantee": "true/false",
    "has_bank_guarantee": "true/false",
    "has_sblc": "true/false",
    "has_sbdc": "true/false",
    "has_parent_guarantee": "MANDATORY true/false — did the parent company give ANY guarantee on behalf of this entity? Check: contingent liabilities note, related party note, directors report, any mention of 'guarantee by holding company' or 'corporate guarantee from parent'",
    "has_comfort_letter": "true/false",
    "all_guarantee_banks": "MANDATORY — comma-separated list of EVERY bank named in any guarantee/SBLC/BG",
    "details": [
      {
        "type": "MANDATORY — Corporate Guarantee / Bank Guarantee / SBLC / SBDC / Parent Guarantee / Letter of Comfort / Performance Guarantee / Financial Guarantee / Indemnity / Other",
        "given_by": "MANDATORY — exact name of entity that gave the guarantee",
        "given_by_relationship": "parent/fellow subsidiary/bank/third party",
        "given_to": "MANDATORY — beneficiary: who receives the guarantee e.g. bank name, lender",
        "on_behalf_of": "entity whose obligation is being guaranteed",
        "purpose": "reason for guarantee",
        "amount_cy": null,
        "amount_py": null,
        "currency": "ISO 3-letter",
        "denomination": "units/thousands/millions/lakhs/crores",
        "issuing_bank": "name of bank that issued BG/SBLC",
        "issuing_bank_country": null,
        "expiry_date": null,
        "outstanding_balance_cy": null,
        "counter_guarantee": null,
        "footnote_exact_text": "MANDATORY — copy the exact sentence(s) from the document that describes this guarantee. Quote verbatim."
      }
    ],
    "guarantees_received": [
      {
        "type": "Corporate Guarantee / Bank Guarantee / SBLC / Parent Guarantee / Letter of Comfort / Other",
        "received_from": "MANDATORY — exact name of guarantor",
        "received_from_relationship": "parent/fellow subsidiary/bank/associate/third party",
        "in_favour_of": "lender/bank/counterparty",
        "purpose": null,
        "amount_cy": null,
        "amount_py": null,
        "currency": null,
        "denomination": "units/thousands/millions/lakhs/crores",
        "issuing_bank": null,
        "expiry_date": null,
        "footnote_exact_text": "MANDATORY — copy the exact sentence(s) from the document that describes this guarantee received. Quote verbatim."
      }
    ]
  },

  "PARENT_GUARANTEE": {
    "MANDATORY_NOTE": "This section is ALWAYS mandatory. If no parent guarantee exists, explicitly state that with evidence. Do NOT leave null.",
    "exists": "true/false — MANDATORY",
    "guarantor_name": "exact name of parent/holding company that gave the guarantee",
    "guarantor_relationship": "immediate parent / ultimate parent / fellow subsidiary / holding company",
    "beneficiary_banks": "MANDATORY — exact names of ALL banks/lenders covered by parent guarantee. Quote from document.",
    "total_amount_cy": "total amount covered by parent guarantee",
    "currency": null,
    "denomination": null,
    "purpose": "what the guarantee secures e.g. working capital facilities, term loans, deferred payment",
    "footnote_exact_text": "MANDATORY — copy the EXACT verbatim sentence(s) from the document. If none exists, write: 'No parent guarantee mentioned. Searched: contingent liabilities note p[X], related party note p[X], directors report p[X]'",
    "search_pages_checked": "list of page numbers / sections where you looked for parent guarantee"
  },

  "BANK_RELATIONSHIPS": [
    {
      "bank_name": "MANDATORY — exact name as printed",
      "bank_country": null,
      "facility_types": "all product types with this bank",
      "total_loan_exposure_cy": null,
      "bg_outstanding_cy": null,
      "sblc_outstanding_cy": null,
      "lc_outstanding_cy": null,
      "cash_held_cy": null,
      "fd_held_cy": null,
      "total_relationship_value_cy": null,
      "relationship_type": "domestic bank / foreign bank / multilateral / NBFC",
      "role": "(V5) every role seen for this bank: general banker / current account / deposit / lender / overdraft / guarantee issuer / LC bank / hedge counterparty / escrow or trustee",
      "bank_std": "(V5) standard group name e.g. 'Standard Chartered', 'FirstRand / FNB', 'Emirates NBD'",
      "where_named": "(V5) company-information page / note number / audit report / security clause — with page"
    }
  ],

  "BANKING_SUMMARY": {
    "total_banks_named": null,
    "all_banks_list": "MANDATORY — complete list of EVERY bank name found ANYWHERE in document",
    "primary_banker": null,
    "domestic_banks": null,
    "foreign_banks": null,
    "debenture_trustee": null,
    "escrow_bank": null,
    "banks_named_only_in_text_no_amount": "(V5) banks named on the company-information page or in text with no amount attributed — list each with page; they still get a BANK_RELATIONSHIPS row",
    "not_disclosed": "(V5) MANDATORY — list which of these the filing does NOT print, each with the pages you checked: cash by bank / cash by currency / deposits by bank / deposit tenor and rate / overdraft by bank / lending by bank / facility limit-drawn-undrawn / facility rate-maturity-security / lending by currency / FX exposure by currency / hedges by instrument and counterparty / any bank name at all. Write 'all printed' only if every one is present"
  },

  "FACTORING": {
    "receivables_factored_cy": null,
    "receivables_factored_py": null,
    "bank_or_provider_name": "MANDATORY — name of factoring bank or provider",
    "recourse_type": "with recourse/without recourse",
    "supply_chain_finance_cy": null,
    "supply_chain_finance_bank": null,
    "bills_discounted_cy": null,
    "bills_discounted_bank": null,
    "reverse_factoring_cy": null,
    "forfaiting_cy": null,
    "forfaiting_bank": null
  },

  "PARENT_SUPPORT": {
    "has_parent_guarantee": "true/false",
    "has_parent_loan": "true/false",
    "has_comfort_letter": "true/false",
    "has_keepwell_agreement": "true/false",
    "has_subordination_agreement": "true/false",
    "parent_name": null,
    "parent_guarantee_total_cy": null,
    "parent_loan_outstanding_cy": null,
    "parent_guarantee_given_to": "comma-separated list of lenders covered",
    "parent_support_description": null
  },

  "DOWNSTREAM_SUPPORT": {
    "has_given_guarantee_to_stepdown": "true/false",
    "has_given_loan_to_stepdown": "true/false",
    "has_given_comfort_letter_to_stepdown": "true/false",
    "total_guarantees_given_cy": null,
    "total_loans_given_cy": null,
    "downstream_details": [
      {
        "beneficiary_name": null,
        "support_type": "Corporate Guarantee / SBLC / Loan / Comfort Letter / Equity Infusion / Other",
        "amount_cy": null,
        "currency": null,
        "denomination": null,
        "given_to_bank": null,
        "purpose": null
      }
    ]
  },

  "TRADE": {
    "exports_cy": null,
    "exports_py": null,
    "exports_by_geography": {},
    "imports_cy": null,
    "imports_py": null,
    "imports_by_category": {},
    "earnings_in_foreign_currency_cy": null,
    "expenditure_in_foreign_currency_cy": null,
    "cif_value_of_imports_cy": null,
    "fob_value_of_exports_cy": null
  },

  "FX_EXPOSURE": {
    "total_unhedged_cy": null,
    "total_hedged_cy": null,
    "currencies_exposed": [],
    "forward_contracts_outstanding_cy": null,
    "options_outstanding_cy": null,
    "sensitivity_1pct_impact": null,
    "natural_hedge_description": null,
    "exposure_by_currency": [
      {"currency": "(V5) ISO3", "gross_exposure_cy": null, "hedged_cy": null, "unhedged_cy": null, "receivable_or_payable": "as printed", "page": null}
    ],
    "hedges": [
      {"instrument": "(V5) forward / option / swap / other", "counterparty_bank": "exact bank name as printed, or 'Not disclosed'", "currency": null, "notional_cy": null, "maturity": null, "hedged_item": "as printed", "page": null}
    ],
    "functional_vs_presentation_currency": "(V5) state both if they differ, with page"
  },

  "LEASE": {
    "total_lease_liability_cy": null,
    "total_lease_liability_py": null,
    "lease_payments_cy": null,
    "weighted_avg_lease_term": null,
    "major_lease_type": "property/vehicles/equipment/other"
  },

  "RELATED_PARTY_TRANSACTIONS": [
    {
      "party_name": null,
      "relationship": "parent/fellow subsidiary/associate/JV/KMP/key shareholder",
      "transaction_type": "sales/purchases/services/interest/dividend/royalty/guarantee/loan/reimbursement/rent/IP license",
      "amount_cy": null,
      "amount_py": null,
      "balance_outstanding_cy": null
    }
  ],

  "CONTINGENT_LIABILITIES": {
    "total_cy": null,
    "total_py": null,
    "items": [
      {"type": "tax/legal/regulatory/guarantee/other", "amount_cy": null, "detail": null}
    ]
  },

  "CAPITAL_COMMITMENTS": {"cy": null, "py": null},

  "POST_BALANCE_SHEET_EVENTS": "describe any material events after year-end",

  "ACCOUNTING_POLICIES": {
    "revenue_recognition": "point in time / over time / percentage of completion",
    "depreciation_method": "straight line / WDV / other",
    "inventory_valuation": "FIFO / weighted average / other",
    "functional_currency": null,
    "first_year_of_current_accounting_standard": null
  },

  "RATIOS": {
    "gross_margin_pct": null,
    "operating_margin_pct": null,
    "net_margin_pct": null,
    "current_ratio": null,
    "debt_equity_ratio": null,
    "return_on_equity_pct": null,
    "revenue_per_employee": null
  },

  "SIGNIFICANT_NOTES": "any other material items: litigation, regulatory actions, impairment, write-offs, restructuring, brand IP held, patents, environmental liabilities, insurance claims, cyber incidents, fraud",

  "KEY_QUOTES": [
    {"topic": "(V5) one entry per topic, in this order: BUSINESS, BANKS, FACILITIES, SECURITY, INTERCOMPANY, GUARANTEES, PARENT_SUPPORT, FX_HEDGING, GOING_CONCERN, AUDIT, OWNERSHIP, DIVIDEND, RISK, EXPANSION, SUBSEQUENT_EVENTS", "verbatim": "at most 600 characters exactly as printed, or NOT_PRINTED", "page": "integer; null only when verbatim is NOT_PRINTED"}
  ],

  "INTELLIGENCE_SUMMARY": {
    "MANDATORY_NOTE": "(V5) Written LAST. The banker's brief for this company, derived ONLY from the fields above (same numbers, same pages). Every sentence carrying a number or a name ends with its page as (p.N). Currency and denomination stated once per paragraph. No facts that are not in the fields above. Write NOT_PRINTED where the filing is silent; never omit a key.",
    "headline": "2-3 sentences: who it is, what it does, year, scope, size (revenue / PAT / equity / cash as printed), state (profit or loss, going concern, audit opinion)",
    "banking_relationships": "every bank named, its role, amounts attributable with limit vs drawn, security given, and what is NOT disclosed",
    "liquidity_and_cash": "cash total, split by bank / currency / restricted where printed, deposits with tenor and rate, overdraft usage",
    "debt_and_facilities": "every external facility by product with limit / drawn / undrawn, rate, maturity, security; lease liabilities; finance cost",
    "group_funding": "loans from and to group by counterparty with terms, capital injected, investments in group entities, trade balances, net position, parent support wording",
    "guarantees_and_contingents": "guarantees given and received (by whom, to whom, amount, purpose), bank instruments, contingent liabilities, charges registered",
    "fx_and_hedging": "exposure by currency, hedges by instrument and counterparty bank, sensitivity, functional vs presentation currency",
    "ownership_and_structure": "immediate parent (country), chain to ultimate, Indian parent link, step-downs and branches with countries, changes in the year",
    "dividends_royalties_fees": "dividends declared or paid; royalty / management / technical fees to group with counterparties",
    "risks_and_watchpoints": "going concern wording, audit qualification or emphasis, covenant breaches, negative equity, material uncertainties, subsequent events, litigation, internal inconsistencies on the page",
    "what_is_not_in_this_filing": "the splits and sections the filing does not print (filleted / abridged accounts, exemptions taken) so the reader knows the limits"
  }
}

RULES:
1. Use numbers AS PRINTED. Do NOT convert denomination.
2. (123) means -123. "—" or "-" means null.
3. If a field is NOT in the document → null. NEVER fabricate or guess.
4. IDENTIFIERS: Company registration number is CRITICAL. Look on cover page, directors' report, footer.
5. DENOMINATION_EVIDENCE — MANDATORY: Before extracting any number, read the P&L header and Balance Sheet header. Quote them verbatim in E1 and E2. Then find 3 more confirmations. The denomination in IDENTITY MUST match E1/E2. If headers say "USD thousands" then currency=USD denomination=thousands — no exceptions.
6. BORROWINGS — BANK VERIFICATION MANDATORY: For EVERY facility row, go to the borrowing note/footnote in the PDF. Read each line. Extract the EXACT bank name as printed — never shorten, never guess. Copy the verbatim sentence into footnote_verification. Facility currency is also MANDATORY from the footnote. If a note says "Working capital facility from HDFC Bank Limited: INR 200 lakhs" then bank_name="HDFC Bank Limited" currency="INR" amount_cy=200. Do a second pass of the entire borrowing note to check you missed no bank.
7. GUARANTEES — PARENT GUARANTEE MANDATORY: Search the ENTIRE document for parent/holding company guarantees. Check: (a) Contingent Liabilities note, (b) Related Party Transactions note, (c) Directors' Report / Board's Report, (d) Borrowing note security description, (e) any mention of "corporate guarantee", "guarantee given by holding", "guarantee from parent". Fill PARENT_GUARANTEE section completely. If none found, explicitly write what pages you searched.
8. BANK NAMES — MANDATORY: Scan the ENTIRE document for every bank name. NEVER leave bank_name null if a bank is named anywhere.
9. PARENT vs HOLDING NUANCE: Fill both PARENT_SUPPORT and DOWNSTREAM_SUPPORT as applicable.
10. TRADE: Look for "earnings in foreign currency", "expenditure in foreign currency", CIF/FOB.
11. FACTORING: "receivables sold/assigned", "factoring", "bill discounting", "supply chain finance". Always name the bank.
12. RELATED PARTY: Extract TOP 15 largest. ALWAYS include parent company transactions.
13. INTERCOMPANY: Management fees, royalties, brand fees, cost recharges, shared services, IP licenses.
14. SUB-SUBSIDIARIES: If this entity owns other entities, list them all with holding %.
15. PENSION: Extract defined benefit obligation, plan assets, net deficit/surplus.
16. SEGMENT: Revenue/profit by business segment AND by geography if available.
17. RATIOS: Calculate from the extracted numbers.
18. Return ONLY the JSON. No markdown fences. No text outside JSON. No truncation — output the complete JSON to the last closing brace.

=====================================================================
V3 ADDENDUM — ADDITIONAL MANDATORY SECTIONS (append these keys to the SAME JSON object; all existing sections and rules above remain unchanged and mandatory)
=====================================================================

  "IDENTITY_EVIDENCE": {
    "MANDATORY_NOTE": "Read the subsidiary's FULL LEGAL NAME from AT LEAST 5 DIFFERENT PLACES in the document. Quote each verbatim with its location. The 5+ places to check: (1) cover page / title page, (2) independent auditor's report addressee line ('To the members/shareholders of ...'), (3) directors' report / strategic report heading, (4) balance sheet or P&L statement heading / signature block, (5) notes to accounts general-information note ('The Company ... was incorporated in ...'), (6) page footer / registration footer if present.",
    "name_readings": [
      {"location": "cover page / auditor report / directors report / statement heading / general info note / footer", "page": null, "verbatim_quote": "exact sentence or heading containing the company name, copied verbatim"}
    ],
    "name_readings_count": "MUST be >= 5 (fewer only if the document genuinely has fewer occurrences — then state so)",
    "name_variants_found": "list every spelling/form variant seen across the readings",
    "FULL_LEGAL_NAME_FINAL": "the complete legal name with suffix, as most consistently printed",
    "country_of_incorporation_final": null,
    "country_evidence_quote": "verbatim sentence proving the country e.g. 'incorporated in the Netherlands', 'registered in England and Wales'",
    "registry_id_final": "company registration number / KvK / UEN / CH number / CIN etc.",
    "registry_id_evidence_quote": "verbatim text where the registration number is printed",
    "registry_authority": "which register the ID belongs to e.g. Companies House, ACRA, KvK, Mauritius Registrar",
    "document_is_this_company": "(V5) YES / PARTIAL (combined or booklet document — the company's own statements are a section; give sub_section_pages) / NO (a different company — fill DENOMINATION_EVIDENCE, IDENTITY, IDENTITY_EVIDENCE only and stop)",
    "sub_section_pages": null,
    "pages_total": null,
    "pages_read": "(V5) e.g. '1-42 (all)'",
    "unreadable_pages": []
  },

  "CASH_AND_BANK_SCHEDULE": {
    "MANDATORY_NOTE": "Go to the cash & cash equivalents note AND the other bank balances note. Read the schedule line by line. Break up BY BANK.",
    "rows": [
      {
        "bank_name": "exact name as printed; 'Cash on hand' for physical cash; 'Not named' only if the note truly does not name banks",
        "account_type": "current account / call deposit / fixed deposit / escrow / margin money / earmarked / cash on hand",
        "amount_cy": null,
        "amount_py": null,
        "currency": "ISO 3-letter as printed for this line",
        "denomination": "units/thousands/millions/lakhs/crores as applicable to this schedule",
        "verbatim_quote": "the schedule line as printed",
        "tenor_or_maturity": "(V5) for deposits: tenor or maturity date as printed",
        "interest_rate": "(V5) as printed",
        "under_lien_or_restricted": "(V5) true/false and purpose (margin money, escrow, DSRA, guarantee cover) as printed",
        "page": "(V5) integer page of the schedule line"
      }
    ],
    "total_reconciles_to_balance_sheet": "true/false — sum of rows vs BS cash + other bank balances",
    "reconciliation_note": "state the totals compared",
    "cash_by_currency": [
      {"currency": "(V5) ISO3", "amount_cy": null, "amount_py": null, "page": null}
    ]
  },

  "LIABILITIES_BANKWISE_SPLIT": {
    "MANDATORY_NOTE": "Read the borrowings/loans notes AND the current + non-current liabilities schedules. For EVERY lender/bank: amount, facility, denomination, and whether CURRENT or NON-CURRENT (long-term). This complements the BORROWINGS section above — fill BOTH.",
    "rows": [
      {
        "lender_name": "exact bank/NBFC/group-entity name as printed",
        "facility_type": "term loan / overdraft / RCF / WC / NCD / shareholder loan / lease / other",
        "amount_cy": null,
        "amount_py": null,
        "currency": null,
        "denomination": "units/thousands/millions/lakhs/crores",
        "current_or_noncurrent": "CURRENT / NON_CURRENT / split (state both amounts)",
        "verbatim_quote": "the note line as printed",
        "sanctioned_limit": "(V5) as printed",
        "drawn_cy": "(V5) as printed",
        "undrawn_cy": "(V5) only if the note prints both limit and drawn; else null",
        "interest_rate": "(V5) as printed",
        "maturity": "(V5) as printed",
        "security": "(V5) as printed",
        "page": "(V5) integer page of the note line"
      }
    ],
    "total_current_liabilities_check": "sum of current rows vs BS total",
    "total_noncurrent_liabilities_check": "sum of non-current rows vs BS total",
    "by_currency_totals": [ {"currency": "(V5) ISO3", "borrowings_cy": null, "page": null} ],
    "by_product_totals": [ {"product": "(V5) term loan / overdraft / RCF / WC / NCD / shareholder loan / lease / other", "borrowings_cy": null, "page": null} ]
  },

  "STEPDOWN_SUBSIDIARIES_CHECK": {
    "MANDATORY_NOTE": "ALWAYS check whether THIS entity itself holds subsidiaries/participations/step-downs. Read: investments-in-subsidiaries note, 'participations in group companies' note, 'financial fixed assets' note, consolidation-exemption note, and the general-information note. This complements SUB_SUBSIDIARIES above — fill BOTH.",
    "has_stepdowns": "true/false — MANDATORY",
    "stepdowns": [
      {
        "FULL_NAME": "complete legal name of the step-down entity as printed",
        "country": null,
        "holding_pct": null,
        "nature": "subsidiary/associate/JV",
        "carrying_value_cy": null,
        "verbatim_quote": "the note line naming this entity"
      }
    ],
    "if_none_evidence": "if has_stepdowns=false, quote the note or state 'no participations note found; searched pages [X]'"
  }

ADDITIONAL RULES (18-21, extending rules 1-17 above):
18. IDENTITY_EVIDENCE is MANDATORY on every document: minimum 5 name readings with verbatim quotes and page/location; final name, country and registry id must each carry an evidence quote.
19. CASH_AND_BANK_SCHEDULE is MANDATORY: per-bank breakup with amount + currency + denomination per line, reconciled to the balance sheet.
20. LIABILITIES_BANKWISE_SPLIT is MANDATORY: every lender with amount, facility, denomination and CURRENT vs NON-CURRENT classification.
21. STEPDOWN_SUBSIDIARIES_CHECK is MANDATORY: explicit true/false with full names + countries + verbatim quotes, or evidence of absence.

ADDITIONAL RULES (22-27, extending rules 1-21 above — the (V5) fields):
22. PAGES: every (V5) field named page carries an INTEGER printed page number; if the filing has no printed numbers use the PDF page index and say so in DENOMINATION_EVIDENCE.statement_pages.page_numbering. Fill statement_pages for every filing.
23. BANK NAMING IS COMPLETE: every bank named anywhere in the document (company-information page, notes, security clauses, audit report, signature blocks) gets a BANK_RELATIONSHIPS row with role and page even when no amount is attributed to it; BANKING_SUMMARY.all_banks_list must equal the union of bank names across every section. Use the exact printed name in bank_name and the standard group name in bank_std. Never shorten, never guess.
24. SPLITS ARE ROWS: cash by bank and by currency, deposits with tenor and rate, lending by facility with limit / drawn / undrawn and rate / maturity / security, borrowings by currency and by product, FX exposure by currency, hedges by instrument with counterparty bank, intercompany loans by counterparty with terms, step-downs by entity. Where the filing prints a total but no split, leave the rows empty and name that split in BANKING_SUMMARY.not_disclosed with the pages you checked. Never invent a split, a bank, a rate or a counterparty; 'Not disclosed' with pages checked is always a valid answer.
25. DIGIT GROUPING: statements prepared for an Indian parent often print foreign-currency figures as 3,52,52,948 (lakh/crore grouping); European statements print 25.026.456 with dot separators. In both cases the number is the plain digits (35252948 / 25026456) in the header denomination. Removing separators is the only transformation allowed — never divide or multiply — and DENOMINATION_EVIDENCE.digit_grouping_on_page must say which grouping the page uses. Bracketed figures are negative.
26. KEY_QUOTES: one entry per topic in the listed order, verbatim from the page, at most 600 characters, with an integer page; NOT_PRINTED with page null when the filing is silent on that topic. No paraphrase.
27. INTELLIGENCE_SUMMARY is written LAST from the fields above only, every number or name followed by (p.N); NOT_PRINTED where silent. Rule 18 stands: the whole answer is ONE JSON object — the sections above in their order, then IDENTITY_EVIDENCE, CASH_AND_BANK_SCHEDULE, LIABILITIES_BANKWISE_SPLIT, STEPDOWN_SUBSIDIARIES_CHECK, KEY_QUOTES, INTELLIGENCE_SUMMARY — no markdown fences, no text outside it, complete to the last closing brace.

===== SUBSIDIARY-FILINGS ADDENDUM (read this BEFORE the schema above; it overrides nothing, it adds) =====

CONTEXT. This document is one filing from the FY2025-26 subsidiary-financial-statements set published by the Indian listed parent named in THIS ITEM (on its investor site, or carved from its "Annual Report of Subsidiary Companies"). Your output feeds the same overseas-subsidiary book as the schema above, so fill THAT schema exactly. In addition, fill the DOC_CONTROL block below.

THE DOCUMENT IS NOT ALWAYS WHAT THE LIST SAYS. The website groups everything under one heading. In this set a
document may be any of: full audited statutory financial statements; unaudited or management accounts; a
DRAFT; a directors'/management report with no statements; a consolidated pack; a tax or local-GAAP filing; or
a period that is NOT the year to 31 March 2026. Determine what you are actually holding by reading it. Do not
assume, and do not upgrade a draft or a management report into audited statements.

LANGUAGE. Many of these filings are not in English (Spanish, Portuguese, French, Dutch, German, Italian,
Hungarian, Romanian, Polish, Czech, Slovak, Turkish, Greek, Russian, Ukrainian, Vietnamese, Thai, Japanese,
Chinese, Korean, Bahasa, Arabic). Read the document in its own language. Report every field in English, but
keep every verbatim_quote in the ORIGINAL language exactly as printed, and add an English rendering after it
in square brackets. Never translate a number, a currency code or a proper name.

IDENTITY. The Indian parent of the group is the one named in THIS ITEM. The IMMEDIATE parent is often an intermediate overseas holding company. Record the ownership chain EXACTLY as the document prints it (immediate parent, intermediate holdcos, ultimate parent, each with country and % where printed). Do not infer a chain from the company's name. An Indian CIN printed in an overseas company's accounts is usually the PARENT's number - it does not make this entity Indian.

DOC_CONTROL — add this block to your JSON output, at the top level:

  "DOC_CONTROL": {
    "document_type": "AUDITED_FS / UNAUDITED_FS / MANAGEMENT_ACCOUNTS / DRAFT_FS / DIRECTORS_OR_MANAGEMENT_REPORT_ONLY / TAX_FILING / CONSOLIDATED_PACK / OTHER",
    "document_type_evidence": "the exact words on the page that decide it, with page",
    "is_draft": "YES / NO — say YES if the word Draft/Borrador/Entwurf/Concept or a watermark appears, quote it",
    "audited": "YES / NO / CANNOT_TELL",
    "auditor_name": "the audit firm, or null - the AUDIT FIRM IS NEVER A BANK",
    "audit_opinion": "unqualified / qualified / adverse / disclaimer / none present",
    "audit_report_date": null,
    "period_covered": "as printed, e.g. '1 April 2025 to 31 March 2026' or 'year ended 31 December 2025'",
    "period_end_date": "YYYY-MM-DD",
    "is_FY2026_31MARCH": "YES / NO — NO if the period end is anything other than 31 March 2026",
    "statement_basis": "STANDALONE / CONSOLIDATED / BOTH_PRESENT",
    "reporting_framework": "IFRS / local GAAP (name it) / IND AS / other, as printed",
    "language_of_document": "English / Spanish / ... ",
    "entity_legal_name_as_printed": "exact, in the original script",
    "entity_registry_id_as_printed": "registration / CNPJ / RUT / KvK / SIREN / UEN / tax id - say WHICH kind it is, or 'not disclosed in document'",
    "country_of_incorporation": null,
    "immediate_parent_as_printed": null,
    "ultimate_parent_as_printed": null,
    "pages_in_document": null,
    "pages_you_read": "e.g. '1-38 (all)'",
    "document_is_this_company": "YES / NO - NO if the filing inside is for a different entity than the file title"
  }

BANK NAMING — the same rules that govern the rest of this schema, restated because they decide the value of
this whole exercise:
  - A bank counts as NAMED only when the document names a specific financial institution as a counterparty of
    THIS company (e.g. "Rabobank", "BNP Paribas Fortis", "Banco Santander", "Standard Bank").
  - The AUDIT FIRM is never a bank. Identifiers printed on an auditor's letterhead belong to the auditor.
  - The parent, fellow subsidiaries, related parties, lessors and factoring counterparties that are group
    companies are never banks.
  - "Cash at bank", "loan from bank", "borrowings" with no institution named = bank NOT named. That is a
    legitimate answer - say so plainly rather than guessing an institution.

WHAT MATTERS MOST IN THIS RUN, in order:
  1. THE BREAKUPS. Cash split by bank and by account type; deposits by bank with tenor and rate; borrowings by
     lender with limit, drawn, undrawn, rate, maturity and security; guarantees by issuer and beneficiary.
     A total with no breakup is a weak result. If the breakup is genuinely absent from the document, say
     exactly that in the not_disclosed field and name the pages you checked.
  2. THE BANKS. Every institution named anywhere, with the page and the verbatim line.
  3. CURRENCY-WISE SPLITS. Cash by currency, borrowings by currency, FX exposure by currency, hedges by
     currency and instrument. These are group-wide treasury facts and they matter even when small.
  4. INTERCOMPANY. Loans and balances with the parent and with fellow subsidiaries, each counterparty named,
     with rate, repayment terms and whether subordinated - this is how Indian groups fund their overseas arms.
  5. PARENT SUPPORT. Guarantees, comfort letters, keep-well or going-concern support from the Indian parent or any
     intermediate holdco, quoted verbatim.

HONESTY RULES. Report only what is on the page. Never carry a number from one statement into another. If a
figure is illegible or the page is a poor scan, say so in the relevant field rather than guessing. If the
document contradicts itself, report both and flag it. An empty, well-evidenced answer is worth more to us
than a filled-in guess.

===== LESSONS ADDENDUM (added 18-Sep-2026 after earlier outputs of this same prompt were audited page by page; it overrides nothing, it adds) =====

These are the mistakes that were actually found in earlier outputs. Avoid each one.

L1. FUNDING SPLIT IS MANDATORY. "Borrowings" on the balance sheet is NOT bank debt. Fill FUNDING_SPLIT_CHECK (below) so that
    total_borrowings = from_banks_and_financial_institutions + from_group_and_related_parties + preference_shares_or_hybrids_classed_as_debt
    + bonds_or_notes_to_market + lender_not_disclosed. Group loans, shareholder loans, cash-pool payables and redeemable preference shares never go into the bank figure.
    If the document does not say who the lender is, the amount goes to lender_not_disclosed - do not assume a bank.
L2. ONE FACILITY, ONE ROW. The same loan must not appear twice (once in BORROWINGS and again in LIABILITIES_BANKWISE_SPLIT with different wording).
    Give every facility a facility_ref and reuse it; totals across the two blocks must not double.
L3. NOT BORROWINGS: accrued expenses, trade and other payables, provisions, lease liabilities, derivative liabilities, and amounts owed to a factor or
    under a receivables programme. Report leases and factoring in their own blocks. If you see bank interest expense but no bank loan at year end, do not invent a loan -
    state it in FUNDING_SPLIT_CHECK.intra_year_bank_line_signal with the interest amount and page.
L4. BALANCE vs FLOW. A closing balance is what is owed or held at the period end. Loans granted, drawn or repaid DURING the year, dividends paid, and
    cash-flow lines are flows. Never put a flow into a balance field; label each figure BALANCE or FLOW where the schema allows.
L5. HEDGING: notional amount and fair value are different numbers - report both, separately, with currency pair, instrument and counterparty bank.
    Group-level risk notes printed in a consolidated pack belong to the consolidated entity, not to each subsidiary.
L6. FACTORING / RECEIVABLES PROGRAMMES / SECURITISATION / SUPPLY-CHAIN FINANCE: name the programme bank or arranger, with-recourse or without, limit, amount
    outstanding or derecognised at period end, and the discount or fee cost for the year, each with page. Absence is a valid answer.
L7. GUARANTEES: separate GIVEN by this company from RECEIVED for its benefit. For each: guarantor, beneficiary (name the bank), amount, currency, what it secures.
    Cross-guarantees and parent guarantees of bank facilities are the single most useful fact for a lender - quote the sentence.
L8. CASH POOLING / TREASURY CENTRE: if the company takes part in a cash pool or sweeping arrangement, name the pool bank, the pool header entity and the balance.
L9. UNIT AND CURRENCY ARE READ FROM THE STATEMENT HEADER ON EACH PAGE YOU TAKE NUMBERS FROM (units, thousands, lakhs, millions). Do not carry one page's unit to another.
    Earlier outputs were wrong by x1,000 and x100,000 for exactly this reason. Never convert currency; never rescale.
L10. PRIOR YEAR IS REQUIRED wherever the statement prints it: revenue, profit after tax, total assets, borrowings, cash, receivables, inventory, payables.
L11. WORKING-CAPITAL INPUTS (WORKING_CAPITAL_INPUTS below): trade receivables, inventories, trade payables, revenue and cost of sales (or cost of materials + changes in
    inventory where cost of sales is not printed - say which), current and prior year, and the number of months in the period if it is not 12.
L12. DIVIDEND AND ROYALTY: dividends declared and paid (to whom), royalty / technical / management / brand fees paid or received (counterparty, amount, page).
L13. WHAT THE FILE REALLY IS. Besides the DOC_CONTROL types, this set also contains: (i) a one- or two-page NOTE saying the company's accounts are included in another
    company's consolidated statements (document_type = NOTE_ONLY - report which company consolidates it and stop; do not invent figures); (ii) a file holding TWO sets for the
    same company (e.g. IFRS + local GAAP, or local language + English) - use ONE set, say which and why, and do not add them; (iii) CONSOLIDATED sets of an intermediate
    holdco "and subsidiaries" - set statement_basis = CONSOLIDATED and list the entities consolidated so the figures are not added to those subsidiaries' own filings;
    (iv) MANAGEMENT ACCOUNTS / unaudited / balance-sheet-only printouts; (v) a file that ends abruptly - say at which page and which note is cut.
L14. HOLDING STRUCTURE: list every subsidiary, associate and joint venture THIS company holds (name, country, % held, page). Say whether this company has operations of its own
    (revenue, employees) or is a pure holding / finance / dormant vehicle, quoting the principal-activity sentence.
L15. BANK ROLES: for every bank named, give the exact legal entity name as printed (not the brand alone), its role (account bank, lender, guarantor bank, hedge counterparty, security agent, programme arranger) and the page. Treat every bank the same way.
L16. PERIOD: state the exact period start and end. Many filings in this set end 31 December 2025, some are stub periods or first-year periods, and some sites still serve
    last year's accounts. Do not assume 31 March 2026.

Add these two blocks to your JSON output at the top level (same single JSON object, same rules: integers for pages, NOT_PRINTED where silent):

  "FUNDING_SPLIT_CHECK": {
    "currency": null, "unit_as_printed": null, "as_at": "YYYY-MM-DD",
    "total_borrowings_cy": null, "total_borrowings_py": null,
    "from_banks_and_financial_institutions_cy": null, "from_group_and_related_parties_cy": null,
    "preference_shares_or_hybrids_classed_as_debt_cy": null, "bonds_or_notes_to_market_cy": null, "lender_not_disclosed_cy": null,
    "split_adds_to_total": "YES / NO - if NO explain", "lease_liabilities_cy": null, "factoring_or_receivables_programme_outstanding_cy": null,
    "group_lenders_named": [{"name": null, "country": null, "amount": null, "rate": null, "maturity": null, "page": null}],
    "banks_lending_named": [{"bank_name_as_printed": null, "facility_ref": null, "amount_drawn": null, "limit": null, "page": null}],
    "intra_year_bank_line_signal": null, "cash_pool": {"participates": "YES / NO / NOT_PRINTED", "pool_bank": null, "pool_header_entity": null, "balance": null, "page": null},
    "pages_checked": null
  },
  "WORKING_CAPITAL_INPUTS": {
    "currency": null, "unit_as_printed": null, "months_in_period": 12,
    "revenue_cy": null, "revenue_py": null, "cost_of_sales_cy": null, "cost_of_sales_py": null, "cost_of_sales_basis": "cost of sales as printed / cost of materials + change in inventory / not printed",
    "trade_receivables_cy": null, "trade_receivables_py": null, "inventories_cy": null, "inventories_py": null, "trade_payables_cy": null, "trade_payables_py": null,
    "of_which_receivables_from_group_cy": null, "of_which_payables_to_group_cy": null, "pages": null
  }

L17. INTERCOMPANY LOANS GET THEIR OWN BLOCK (INTERCOMPANY_LOANS below) - one row per loan or funding balance, in BOTH directions:
    loans, advances, cash-pool balances, shareholder loans, "other current liabilities / receivables" owed to or by the parent, holders of participations,
    fellow subsidiaries or entities in which this company holds a participation (Swiss and German formats print them under those captions and do not call them loans).
    For each row give the LENDER and the BORROWER by exact legal name as printed, the relationship, the amount exactly as printed, the DENOMINATION of that figure
    (units / thousands / lakhs / millions - read from that page's header) and the CURRENCY, plus rate, maturity, security, subordination where printed.
    Trade payables and receivables with group companies are NOT loans: report them in the trade rows of the same block with kind = TRADE so nothing is lost and nothing is mixed.
    If the counterparty is described only by category ("entities in which the entity holds a participation") and not named, put that category in lender/borrower and set named = "NO".

  "INTERCOMPANY_LOANS": {
    "rows": [{"direction": "TAKEN_BY_THIS_COMPANY / GIVEN_BY_THIS_COMPANY", "kind": "LOAN / CASH_POOL / SHAREHOLDER_LOAN / OTHER_FUNDING_BALANCE / TRADE",
              "lender_name_as_printed": null, "lender_country": null, "borrower_name_as_printed": null, "relationship_of_counterparty": "parent / intermediate holdco / fellow subsidiary / subsidiary / associate / other related party",
              "named": "YES / NO", "amount_cy_as_printed": null, "amount_py_as_printed": null, "denomination": "units / thousands / lakhs / millions", "currency": null,
              "balance_or_flow": "BALANCE / FLOW", "interest_rate": null, "maturity_or_repayment_terms": null, "secured": null, "subordinated": null, "interest_for_year": null, "page": null, "verbatim_line": null}],
    "total_loans_taken_from_group_cy": null, "total_loans_given_to_group_cy": null, "currency": null, "denomination": null,
    "not_disclosed": "say exactly what the document does not give (e.g. counterparties not named) and the pages checked"
  }


===== ADDENDUM 21-SEP-2026 (user order) - applies on top of everything above; add these blocks to the SAME single JSON object =====
L18. LENDING SPLIT - THREE BUCKETS, EVERY PERIOD PRINTED. Besides FUNDING_SPLIT_CHECK, BORROWINGS and LIABILITIES_BANKWISE_SPLIT, fill LENDING_SPLIT3. Every borrowing / funding line goes into exactly ONE bucket:
    INTERCOMPANY  = lent by the parent, an intermediate holding company, a fellow subsidiary, a shareholder, a director or any related party (incl. cash-pool payables and shareholder loans). Name the lender exactly as printed and the relationship. These rows must agree with INTERCOMPANY_LOANS direction TAKEN_BY_THIS_COMPANY, kind not TRADE.
    BANK          = a bank / financial institution is NAMED on the page. lender_name_as_printed verbatim + page.
    UNDISCLOSED   = a borrowing exists and NO lender name is printed. This bucket takes EVERY no-name variant: "Not disclosed", "Undisclosed", "Not named", "Not available", "Not", "N/A", "NA", "-", "None named", "various", "others", "bank", "banks", "a bank", "bank loan", "credit institution(s)", "financial institution(s)", "lender(s)", blank. Keep the printed words in lender_description_as_printed; lender_name_as_printed stays null. NEVER invent, infer or carry over a name into this bucket, and never write such a placeholder as a bank name anywhere in the JSON.
    OTHER_NAMED   = bonds / notes to market, a named leasing or finance company, government or development institution, supplier or factor finance with a named provider, preference shares classed as debt.
    Lease liabilities, trade payables, accruals, provisions and derivative liabilities are NOT lending (L3).
  "LENDING_SPLIT3": {
    "rows": [{"bucket": "INTERCOMPANY / BANK / UNDISCLOSED / OTHER_NAMED", "lender_name_as_printed": null, "lender_description_as_printed": null, "relationship_if_intercompany": null,
              "facility_type": null, "current_or_non_current": null, "amount_cy_as_printed": null, "amount_py_as_printed": null, "denomination": null, "currency": null,
              "rate": null, "maturity": null, "security": null, "guarantor": null, "page": null, "verbatim_line": null}],
    "totals_by_period": [{"period_end": null, "currency": null, "denomination": null, "intercompany": null, "bank": null, "undisclosed": null, "other_named": null, "total": null,
                          "balance_sheet_borrowings_total": null, "ties": "YES / NO", "difference_explained": null}],
    "no_borrowings_statement": "if the page positively shows no borrowings: the verbatim sentence or 'no borrowings line on the balance sheet', with page; all buckets 0"
  }
L19. NO WEB SEARCH IN THIS RUN. Do not search the web. Bank names, the company name and its country come ONLY from the attached PDF, exactly as printed.
    Financial numbers NEVER come from the web - only from the attached PDF.
L20. TRAPS SEEN IN THESE TWO PARENTS' FY2025-26 SETS: (a) INDIAN DIGIT GROUPING on foreign-currency statements (1,80,25,204 = 18,025,204) - report the true number and say grouping = INDIAN; (b) group-reporting packs audited by an Indian firm "solely to enable the parent to prepare its consolidated financial statements" - framework = group accounting policies (Ind AS), special purpose, no local registry id printed; (c) a CNPJ / NIT / RCS / firm-registration number printed beside the AUDITOR is the auditor's, never the company's; an Indian CIN on a foreign subsidiary's page is the parent's unless the page says otherwise; (d) if the statement headers name a different company from the list title or from the auditor's opinion text, report both with pages; (e) consolidated sets: basis = CONSOLIDATED, list the consolidated members named in the PDF under "consolidated_members_do_not_sum_with" - no separate records for members; (f) all-nil statements: report zeros, say DORMANT with page; (g) give the PDF page of THIS file (first page = 1) and the booklet page printed at the foot where there is one.

===== ADDENDUM 24-SEP-2026 — INDIAN SUBSIDIARIES + V18 BANKING + V17 TREASURY (user order). Applies on top of everything above; add the blocks below to the SAME single JSON object. It overrides nothing above except where it says so. =====

D0. INDIAN COMPANIES. Many files in this run are Indian companies or Indian partnership firms, not overseas subsidiaries. Where the document is an Indian entity:
    - The CIN / LLPIN / firm registration printed as the company's own IS this entity's identifier (rule L20(c) about "parent's CIN" does NOT apply to the entity's own CIN on its own cover, audit report or statement heading).
    - Figures are in Indian Rupees as printed: "Rs in lakhs", "₹ in lakhs", "₹ in crores", "₹ in millions" or absolute rupees. Report as printed; never rescale. Indian digit grouping (12,34,567) is removed only (rule 25).
    - TWO SETS IN ONE FILE: some files print the same statements twice (e.g. once "in lakhs" and again "in absolute rupees", or quarterly results tables before the annual statements). Use ONE set — the audited annual statements, the first complete set — say which pages you used and why, and never add the two sets together.
    - PARTNERSHIP FIRMS: there is no share capital. Report partners' capital accounts per partner (name, opening, share of profit, drawings, closing) in a PARTNERS block and each partner's profit-sharing ratio as printed. The Indian listed partner (e.g. Uno Minda Limited) is the immediate parent for OWNERSHIP.
    - Section 8 (not-for-profit) companies: report as printed; revenue = income from grants/donations/CSR as printed; flag SECTION_8 in DOC_CONTROL.document_type_evidence.
    - The Board's Report / Directors' Report, CARO annexure and internal-financial-controls annexure are part of the filing: read them for bank names, credit ratings, FX earnings/outgo, working-capital limits and quarterly returns filed with banks.

D1. BORROWINGS — V18 FOUR-LAYER READ (overrides nothing; deepens BORROWINGS / LIABILITIES_BANKWISE_SPLIT / LENDING_SPLIT3).
    Before writing borrowings, locate and cite: non-current borrowings note (page, note no.), current borrowings note (page, note no.), text below every borrowing table, every sub-note referenced ("Refer Note x"), the "Bankers:" list on the corporate information page, and — for Indian companies — the CARO clause (ii)(b) table of QUARTERLY RETURNS / STATEMENTS FILED WITH BANKS for working-capital limits > Rs 5 crore (bank names and sanctioned limits are often ONLY there).
    Read four layers: (1) the table, (2) the TEXT BELOW the table — where bank names, rates, security and tenor live, (3) sub-notes, (4) corporate information "Bankers:" — used only when the note says "from banks" without naming them.
    For EVERY facility one row in V18_FACILITIES with the 10 dimensions: bank name exact (consortium = one row per member bank), rate verbatim decomposed into benchmark + benchmark_tenor + margin_bps + effective rate + rate_type (FLOATING / FIXED / INTEREST_FREE), facility type (Term Loan-Rupee / Term Loan-ECB / Cash Credit / Overdraft / WCDL / Packing Credit-PCFC / Buyers Credit / FCNR / NCD / CP / Vehicle Loan / Equipment Loan / ECLGS / WCTL / Bill Discounting / other), amount_cy + amount_py + sanctioned_limit + current_maturity, currency, secured/unsecured, security clause VERBATIM, cg_backed + cg_issuer (actual name) when the security mentions a corporate guarantee / SBLC, tenor / maturity / repayment terms, page + verbatim quote, bank_name_source (table row / text below table / security clause / sub-note / corporate info / CARO quarterly-return table).
    Benchmarks: MCLR (1Y/6M/3M/ON), EBLR, Repo, T-Bill (1M/3M; always INR), MIBOR, MIFOR, SOFR (ON/1M/3M/6M/Term), EURIBOR, SONIA, SORA, TONA, SIBOR, HIBOR, Fixed. A facility quoting two benchmarks = one row per option, noted "alternative pricing".
    NOT borrowings: loans from directors / promoters / partners, ICDs and loans from group companies (these go to INTERCOMPANY_LOANS and LENDING_SPLIT3 bucket INTERCOMPANY), security deposits, lease liabilities, government grants. INCLUDE: current maturities of long-term debt, buyers credit, CP, WCTL, ECLGS.
    Never write "banks", "various banks", "consortium", "parent", "subsidiary" as a name. If not found after all four layers: "NOT_IDENTIFIED_IN_PDF".

D2. GUARANTEES — V17/V18 CHAIN. Every guarantee (given or received) as WHO gave -> VIA which bank (issuing bank for BG/SBLC/LC) -> TO whom (beneficiary) -> FOR what obligation / whose borrowing -> AMOUNT (with currency and denomination) -> page + verbatim. Read all five locations: contingent liabilities note, related party note, borrowings security clauses, Board's Report / Directors' Report, commitments / other notes. Keep GUARANTEES and PARENT_GUARANTEE filled as above.

D3. TREASURY — V17 SECTIONS 3-7, extended to name the bank when the page does (fill TREASURY_V17 block):
    a) EEFC ACCOUNT: the "Balances with banks in EEFC accounts" line (cash & cash equivalents note, or other bank balances note). eefc_balance_cy, eefc_balance_py, currency if printed, bank if printed, page, verbatim. null = no EEFC line in the document (say pages checked).
    b) TMD — TREASURY / MONEY-MARKET / TERM / FIXED DEPOSITS: total deposits cy/py; split <3 months (inside cash equivalents) / 3-12 months (other bank balances) / >12 months (other non-current financial assets); margin money / under lien, with what it secures (BG, LC, DSRA, borrowing); by bank if printed; currency; interest rate if printed; tenor/maturity if printed; liquid mutual-fund / money-market investments held as treasury (current investments) with scheme or issuer as printed. Each line: page + verbatim. NOT_PRINTED where absent.
    c) TMD INTEREST: interest income on bank deposits / fixed deposits for the year (other income note) cy and py, and any other treasury income (gain on mutual funds, interest on ICDs given) as separate lines, page + verbatim. If only a total "interest income" is printed, give it and say the split is not printed.
    d) HEDGING OUTSTANDING at the balance sheet date, one row per instrument: instrument_type (Forward Contract / Interest Rate Swap / Cross-Currency Swap / Option / NDF / Cap-Floor / Commodity), currency pair, buy/sell or export/import, notional in foreign currency, notional in INR (as printed), maturity bucket or date, counterparty bank as printed (or NOT_PRINTED), MTM / fair value cy (separate from notional), designated in hedge accounting yes/no, page + verbatim. If the document says no derivative contracts are outstanding, quote it.
    e) FX EXPOSURE per currency: receivables/assets, payables/liabilities, hedged, unhedged, net, and sensitivity % and impact, as printed — each currency its own row.
    f) FX EARNINGS AND OUTGO (Board's Report "Conservation of energy, technology absorption, foreign exchange earnings and outgo", or notes "earnings / expenditure in foreign currency", "CIF value of imports"): earnings total, outgo total, and any breakup printed (raw material CIF, capital goods CIF, royalty, interest, travel, dividend). If deferred to an annexure not in the file, say so.
    g) CREDIT RATINGS: agency, instrument, rating, outlook, amount — from the Board's Report or notes. NOT_PRINTED if none.

Add these blocks at the top level of the SAME JSON object:
  "V18_FACILITIES": [{"facility_ref": null, "bank_name": null, "bank_name_source": null, "facility_type": null, "amount_cy": null, "amount_py": null, "sanctioned_limit": null, "current_maturity": null, "rate_text": null, "benchmark": null, "benchmark_tenor": null, "margin_bps": null, "effective_rate": null, "rate_type": null, "currency": null, "secured_unsecured": null, "security_detail": null, "cg_backed": null, "cg_issuer": null, "tenor_text": null, "maturity_date": null, "denomination": null, "page": null, "verbatim_quote": null}],
  "CARO_QUARTERLY_RETURNS": [{"bank_name": null, "sanctioned_limit": null, "quarter": null, "amount_per_books": null, "amount_per_return": null, "difference": null, "page": null, "verbatim_quote": null}],
  "PARTNERS": [{"partner_name": null, "profit_sharing_ratio": null, "opening_capital": null, "share_of_profit": null, "drawings": null, "closing_capital": null, "page": null}],
  "TREASURY_V17": {
    "eefc": {"balance_cy": null, "balance_py": null, "currency": null, "bank": null, "page": null, "verbatim": null, "pages_checked": null},
    "deposits": {"total_cy": null, "total_py": null, "lt3m_cy": null, "m3to12_cy": null, "gt12m_cy": null, "under_lien_cy": null, "lien_purpose": null,
                 "rows": [{"bank": null, "amount_cy": null, "amount_py": null, "currency": null, "rate": null, "tenor_or_maturity": null, "under_lien": null, "page": null, "verbatim": null}],
                 "treasury_investments": [{"instrument_or_scheme": null, "issuer": null, "amount_cy": null, "amount_py": null, "page": null}]},
    "deposit_interest": {"fd_interest_income_cy": null, "fd_interest_income_py": null, "other_treasury_income": [{"line": null, "amount_cy": null, "amount_py": null, "page": null}], "split_printed": "YES / NO", "page": null, "verbatim": null},
    "hedges_outstanding": [{"instrument_type": null, "currency_pair": null, "direction": null, "notional_fcy": null, "notional_inr": null, "maturity": null, "counterparty_bank": null, "fair_value_cy": null, "designated": null, "page": null, "verbatim": null}],
    "no_hedges_statement": null,
    "fx_exposure": [{"currency": null, "assets_cy": null, "liabilities_cy": null, "hedged_cy": null, "unhedged_cy": null, "net_cy": null, "sensitivity_pct": null, "sensitivity_impact_cy": null, "page": null}],
    "fx_earnings_outgo": {"earnings_cy": null, "outgo_cy": null, "earnings_py": null, "outgo_py": null, "breakup": [{"line": null, "amount_cy": null}], "page": null, "verbatim": null},
    "credit_ratings": [{"agency": null, "instrument": null, "rating": null, "outlook": null, "amount": null, "page": null}],
    "denomination": null, "currency": null
  }
