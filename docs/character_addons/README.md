# Marvel Clash — Optional Character Detail Add-on

This folder holds **extra reference data only**. It complements (but does not replace) the team's working Django character records.

## Files

- `character_extra_details.csv` — 49 rows, one for every character in the existing `backend/characters/data/marvel_characters.csv` on `main`.
- Every row uses the **existing roster's exact `name` string** as its lookup key.

## What's new here

The existing Django import already stores `name`, `description`, and `powers`. The optional file does **not** repeat `description` or `powers`. It contains Figma-derived **alignment, origin/home, weapons/equipment, power acquisition, intelligence/strategy, opponent counterplay guidance, portrait slide reference, and profile link**.

These fields are **reference-only**. No existing model field, importer, API, frontend, database migration, test, existing CSV, or working feature is modified. The current site will **not** automatically show this data. Team members can use it for planning or selectively import it in a separate, reviewed future change.

## Source and accuracy

Source: the team's earlier Figma profile data captured in the proposed character master on branch `data/figma-character-master-nov5`. Figma design: https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15

- `counterplay_strategy` and `counterplay_detail` are **game-design ideas/inferences**, not established Marvel canon, guaranteed battle results, or balanced game mechanics.
- Other character-background details also come from that team's source and should be reviewed before being treated as canonical.
- `portrait_source` identifies group presentation slides; it is **not** an image file or a working URL.
- Existing Django records currently support a `category` column but the standard CSV importer does not populate it. This optional `alignment` column **does not** change that backend category.
- The existing import spells **Valkryie**, whereas Figma spells **Valkyrie**. This add-on deliberately uses `Valkryie` as the join key to match the current import. **No rename was made.**
- In the old Figma master, `strengths` repeated `powers_and_abilities` on all 49 rows, and `weakness_opponent_approach` repeated `counterplay_title` on all 49 rows, so those redundant fields were not carried over.

## Team safety / review

This is a **non-invasive supplement**. Merging these two new static files would not change Django runtime behavior, but **nothing is merged automatically**. Review this add-on independently. It is intended as a simpler, safer alternative to the expanded character master in PR #68; **do not merge both PRs by accident**.

**No original project files were edited.**
