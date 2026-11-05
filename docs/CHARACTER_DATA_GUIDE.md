# Marvel Clash Character Data

The repository keeps the working Django import and the expanded Figma character database separate so the current app is not broken by a schema change.

## Working Django import

`backend/characters/data/marvel_characters.csv`

This is the CSV currently read by `backend/characters/management/commands/import_characters.py`. The importer expects only `name`, `description`, and `powers`.

Do not replace this file with the expanded master until the Django model/importer is intentionally upgraded and migrated.

## Full 49-character master

`backend/characters/data/marvel_character_master.csv`

This is the expanded repository reference dataset copied from the current Marvel Clash Figma source-profile frames. It includes alignment, descriptions, powers/abilities, origin/home, weapons/equipment, how powers were acquired, intelligence/strategy, strengths, opponent counterplay, weakness/opponent approach, portrait source, and direct Figma profile links.

The Figma counterplay section is explicitly labeled as game-design strategy/inference rather than definitive Marvel canon.

## Combat/Brawl index

`backend/characters/data/marvel_combat_index.csv`

This is a smaller battle-focused view of the same data for future Brawl logic, comparisons, grounded AI prompts, health/damage rules, and move-selection work.

## Primary source

Figma: https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15

Current expanded master row count: **49 characters**.

This data update does not claim that the Django database already stores every expanded field. The current Django model remains the smaller MVP schema until a reviewed backend migration adds those fields.
