# CLOUD SWEEP — RUNBOOK FOR A NEW CLAUDE ACCOUNT (27-Sep-2026)

Goal: fetch FY26 subsidiary financials (and annual reports where we lack them) for listed Indian parents,
using the account's Claude Code on the web credit. The cloud agent FINDS and VERIFIES links and commits
manifests to GitHub; the Mac downloads the files to /Volumes/One Touch/SAGE_CLOUD_SWEEP/<CIN>__<PARENT NAME>/.
Nothing on the drive is ever deleted.

## A. One-time setup in the new account (about 5 minutes)
1. Open https://claude.ai/code signed in as the new account.
2. Connect GitHub: click New session -> it asks to connect GitHub -> sign in to GitHub as chocka123 ->
   when GitHub asks which repositories, choose "Only select repositories" -> hello-world -> Install & Authorize.
   (The repository holds the prompt files and receives the results. One repo for every account.)
3. Environment: above the composer click the chip that says "Default" -> Cloud -> Add cloud environment.
   Name: SWEEP  |  Network access: FULL (not Trusted; Trusted blocks company websites)  -> Add environment.
   Make sure the chip now shows SWEEP and the repo chip shows hello-world.
4. Model: click the model name near the composer -> Sonnet 5. If an effort setting shows, choose Medium.

## B. Launch one session per slice
Paste ONE line into a new session (SWEEP + hello-world selected) and press Enter. Replace R01 by the slice name.

    CLOUD SWEEP SLICE R01. Pull the latest master of this repo, then read the file CLOUD_SWEEP_PROMPTS/R01_PROMPT.md and follow it exactly as your standing instruction for this whole session. Commit results per parent on branch sweep/R01 as the file says. Company websites are reachable in this environment. Start now.

Slices for the FOCUS-64 (subs financials only; we already hold their FY26 annual reports):
    R01 (11 parents, 125 targets)  R02 (11, 125)  R03 (11, 107)  R04 (11, 95)  R05 (10, 89)  R06 (10, 77)
Zero-coverage slices S01..S26 also exist in the same folder; use them only for parents still open (ask the Mac session for the current gap list).

Notes while it runs
- The first session asks "Allow Claude to use add repo (Claude Code Remote)?" -> Allow once. It is the push permission for hello-world.
- If a session says NETWORK BLOCKED, the environment is not FULL -> fix step A3 and start again.
- A session finishes its slice on its own and stops. Several sessions run at once.
- Do not launch a slice twice; a second session would redo the same parents.
- Cost seen on 27-Sep: about USD 1.5 per parent at High effort with 25 parallel sessions. Medium effort and 6 sessions should be cheaper.

## C. Hand-back and downloads (already running on the Mac, nothing to do)
- Each session commits, per parent: MANIFEST_OUTPUT.csv (one row per file found: url, entity, period, verified),
  AOC1_PAGES_OUTPUT.csv (Part A / Part B page range of the annual report), NOT_FOUND_OUTPUT.csv, CASE.md,
  under SAGE_CLOUD_SWEEP/<CIN>__<PARENT NAME>/ on branch sweep/<slice>.
- The Mac loop ~/CLOUD_SWEEP_PROMPTS/pull_forever.sh (every 5 min) pulls every branch and downloads each URL
  to /Volumes/One Touch/SAGE_CLOUD_SWEEP/<CIN>__<PARENT NAME>/{AR,AOC1,subs_FY26,subs_CY2025,subs_FY25_fallback}/,
  checks each file is a real PDF, extracts zips, never overwrites, logs to PULL_LOG_OUTPUT.csv per parent.
  If the Mac was restarted:  nohup ~/CLOUD_SWEEP_PROMPTS/pull_forever.sh >/dev/null 2>&1 &
- Progress check on the Mac (read-only): python3 gap script -> ~/CLOUD_SWEEP_PROMPTS/CLOUD_SWEEP_GAP_<ts>_OUTPUT.xlsx
  and the union of all manifests ~/CLOUD_SWEEP_PROMPTS/ALL_CLOUD_MANIFESTS_UNION_OUTPUT.csv.

## D. Known cautions
- Agents cannot click; they use fetch/curl. Sites that need a real browser come back as SITE_BLOCKED -> local Chrome lane.
- Early manifests (S01-S07) sometimes padded rows to the expected list; from S08 on the prompt forbids it
  (one row per file actually opened). Downloads are safe either way: the puller keeps only real PDFs / real zip members.
- AOC-1 is NOT carved by the cloud; only its page range is recorded. Carving and reading stay local (V20 / Fable).
- FY25 files are fallbacks only; the goal is FY26 (31-Mar-2026) or CY2025 full-year.

## E. Files
- Prompts: ~/CLOUD_SWEEP_PROMPTS/S01..S26_PROMPT.md, R01..R06_PROMPT.md (also in hello-world master, folder CLOUD_SWEEP_PROMPTS/)
- Session log: ~/CLOUD_SWEEP_PROMPTS/SESSIONS_LOG.csv
- Focus lists: MG_WORK/MASTERGROUP/HOUSE_LEI/NEXT_FOCUS_HIGHLIGHTED_PARENTS_BY_BALANCE_20260927_INPUT.csv (64 parents),
  ~/CLOUD_SWEEP_PROMPTS/FOCUS90_PENDING_GE3SUBS_20260927_INPUT.csv (zero-coverage parents with >=3 subs)
- Coverage books: HOUSE_LEI/LISTED_PARTIAL_COVERAGE_BALANCE_20260927_OUTPUT.xlsx, NEXT_FOCUS64_ALREADY_HELD_CHECK / _VS_6465 books.
