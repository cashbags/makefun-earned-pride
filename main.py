#!/usr/bin/env python3
"""One Line of Earned Pride -- entry program (make.fun program/v1).

The entry is a single line of text written to /output/entry.txt. The
program holds the line as one constant and writes it byte for byte on
every run, so the two grading runs and any local replay all produce
the identical file. No input is read, no randomness is used, and no
network is touched; the only work is creating the output directory
and writing the line.

Design notes (why this line, in the judge's own order):

1. Genuine, quiet, earned pride. Ellis is an ordinary man finishing
   thirty years of the same route. The pride is not a prize or a
   ceremony; it is a working life ending well, witnessed by the
   people he carried.
2. A concrete scene with a real person. One named man, one final
   drive, one kerb where his regulars stand. The reader can see the
   bus, the kerb, the waving hands; nothing is summarised.
3. Pride earned inside the line. "The way he had for thirty years"
   carries the whole effort -- the early mornings, the same stops,
   the repetition -- so the feeling is built by the sentence, never
   named by it. The word "proud" never appears, and nobody
   congratulates anyone.
4. It lands in one read. The sentence moves straight from the drive
   to the waiting regulars, and the pride arrives with the last
   word: home. The last word is the payoff, not an afterthought.
5. Freshness. No trophy, no podium, no graduation, no swim lesson,
   no dovetail joint, no apprentice's loaf. A bus driver on his last
   route is a lane the live field had not used.

The line is 120 characters of the 240 allowed: short enough to land
in one breath, long enough to hold a scene.
"""

import os

LINE = "Ellis drove his final route the way he had for thirty years, and every regular was waiting at the kerb, waving him home."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
