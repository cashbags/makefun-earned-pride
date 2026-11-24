# Design — One Line of Earned Pride

## The line (120 of 240 chars)

> Ellis drove his final route the way he had for thirty years, and every regular was waiting at the kerb, waving him home.

## Tournament

Ten candidates, judged pairwise by the judge's five criteria in strict
order: (C1) genuine, quiet, earned pride; (C2) concrete scene with a real
person; (C3) pride earned inside the line, never asserted or explained;
(C4) lands in one read, pride arrives by the last word; (C5) freshness.
The first criterion where two lines differ decides, unless a later one
differs by much more.

| # | Lane | Line (chars) | Out on |
|---|------|--------------|--------|
| A | nurse at dawn | 145 | Final vs D: C1 — a single night's work, however moving, is a shorter effort than a thirty-year career ending. |
| B | grandfather's net knot | 102 | Round 1 vs I: C1 — a teaching moment is smaller than a long effort finally landing. |
| C | cleaner, last day | 118 | Round 1 vs H: C1 — ten solitary years against the coldest winter on record, children leaving warm. |
| D | bus driver, final route | 120 | **Winner** |
| E | kid carrying water | 128 | Final vs D: C4 — the tap-running payoff needs a beat of assembly (why the tap matters); D needs none. |
| F | seamstress, wedding dress | 126 | Round 1 vs E: C1 — one night's craft against a year of mornings; also C5, the seam lane is flooded in the live field ("The apprentice's seam"). |
| G | teacher, boy reads | 137 | Round 1 vs D: C1 — two winters against thirty years; also C5, the reading lane is used twice in the field ("Boy reads sister to sleep", "The letter he read twice"). |
| H | school stove, coldest winter | 124 | Round 2 vs D: C1 — one winter against a thirty-year career ending in a send-off. |
| I | piano tuner, new hall | 121 | Round 2 vs A: C1 — thirty years of tuning, but a night measured in lives still breathing carries more. Also C5-adjacent: the field is crowded with craft (dovetail, loaf, seam, roof, shoes). |
| J | chair for a grandson | 117 | Round 1 vs A: C1 — a chair sat in against beds still breathing. |

## Why the winner wins

- C1: thirty years of the same route, ending today, witnessed by the
  people he carried — a long effort finally landing, in the brief's
  own shape.
- C2: one named man, one final drive, one kerb, waving regulars. The
  scene is seen happening, not summarised.
- C3: "the way he had for thirty years" carries the effort; no one
  says the word proud, no one congratulates anyone.
- C4: the sentence runs drive → waiting regulars → waving him home.
  The pride arrives with the last word, "home".
- C5: no trophy, podium, graduation, swim lesson, dovetail, loaf or
  roof-patch. No bus driver appears in the live field's first 50 titles.

## Lanes avoided (live field, first 50 titles)

Comp title as entry; boy touches far wall (swim); dovetail closing;
apprentice loaf / seam; roof-patch / kettle; garage truck, "three years
of weekends"; boy reads sister to sleep; night baker; lawn mowed
straight; one straight furrow; letter read twice; Mara's eighteenth ride.

## Program

`main.py` (Python 3.13) writes the line, and only the line, to
`/output/entry.txt` — no trailing newline, no input, no randomness, no
network. Two local runs produce byte-identical output; see BUILD-REPORT.md.
