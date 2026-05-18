---
description: Run the daily market-close breakout screen, summarise new names, commit results
---

Run the daily SPY+QQQ breakout screen and produce the brief.

Steps:

1. Run the screen for the latest trading day:
   `python daily_screen.py`
   (defaults to today; pass a date `python daily_screen.py YYYY-MM-DD` to
   backfill a specific session.)

2. The script writes:
   - `results/screen_history/<date>.csv` — full ranked list that day
   - `results/daily_screen_latest.md` — the brief (full list + NEW/DROPPED
     diff vs. the previous run + per-new-name earnings recap & rise drivers)
   - `results/transcripts/*.txt` — raw call transcripts for NEW names,
     **only if** a transcript API key is set and the provider domain is
     allowlisted (see breakout/transcripts.py).

3. If any files exist under `results/transcripts/`, READ them and, for each
   new name, replace the placeholder note in `results/daily_screen_latest.md`
   with a 4-quarter call-transcript summary: per quarter, 2–3 bullet
   highlights (guidance, demand commentary, margins, capital return) and
   any issues/risks management flagged. Keep each name to ~8 bullets total.

4. Report the full list to the user, explicitly call out the NEW additions
   (and DROPPED), and for each new name give the earnings recap + the
   reasons driving the stock's rise.

5. Commit and push the new snapshot + brief to the working branch:
   `git add results/ && git commit -m "Daily breakout screen <date>" && git push`

Notes:
- Network policy permitting, transcripts come from Financial Modeling Prep
  (`FMP_API_KEY`) or Finnhub (`FINNHUB_API_KEY`). Without those, step 3 is
  skipped and the quantitative recap stands.
- This is an educational screen, not investment advice.
