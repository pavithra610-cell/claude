# HOLDS LANE - second-source web check (cloud session, WebSearch/WebFetch only)

You are verifying ownership facts for Indian companies. Input: HOLDS_LANE/HOLDS_WORKLIST_20260928_INPUT.csv (88 rows). Each row has a MEMBER (CIN), a COUNTERPARTY (CIN), the register claim (STATEMENT / CP_REL) and VERIFIED_NOTE explaining what is already known and what is missing.

For EVERY row, in order, find up to THREE independent current (2025-2026) web pages that state who owns / controls the MEMBER company today (or the specific fact named in VERIFIED_NOTE: sale date, merger, strike-off, JV split, parent name). Preferred sources, in this order: the company's or parent's own website or annual report; stock-exchange filing (BSE/NSE); MCA-derived registries (thecompanycheck.com, zaubacorp.com, falconebiz.com, tofler.in); rating rationale (ICRA/CRISIL/CARE/India Ratings); reputable business press. Open each page (WebFetch) and copy the exact sentence that supports the fact. Do NOT rely on search snippets. Do NOT infer from names.

HARD RULES: one output row per page actually opened; if a page does not load or does not state the fact, do not list it. Never invent a URL. If nothing is found after 5 searches, write one row with URL=NONE and QUOTE=what you searched.

Output: append to HOLDS_LANE/HOLDS_EVIDENCE_OUTPUT.csv after EVERY hold (checkpoint), columns:
HOLD_ID,MEMBER_CIN,URL,PAGE_DATE_OR_ASOF,QUOTE,FACT_TYPE(OWNER|SALE|MERGER|STRIKEOFF|JV|RENAME|NONE),OWNER_NAME_AS_STATED,PCT_IF_STATED,YOUR_READING(one line)
Commit and push to branch holds/<your-session-name> after every 10 holds: git add HOLDS_LANE && git commit -m "holds evidence <n>" && git push.
Start with HOLD_ID H001. Report at the end: holds done, pages opened, holds with NONE.

IDENTITY RULE (no token matching): identify every company by its exact CIN, never by partial or similar name tokens. A page counts as evidence only if it shows the exact MEMBER_CIN, or the exact full registered MEMBER name (every word, same order; ignore only case, punctuation, PVT/PRIVATE and LTD/LIMITED). Shared words, a common group surname or a look-alike name (e.g. "Jankalyan Vinimay" for "Jaltarang Vinimay") do not count. Press or rating pages without a CIN need the exact full name; a short or brand name is not enough. Start YOUR_READING with "ID: CIN on page" or "ID: exact name on page"; rows without it are rejected.
