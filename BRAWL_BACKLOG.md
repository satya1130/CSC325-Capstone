# Marvel Clash — Active Brawl Backlog and Future Scope

> **Current Sprint 3 requirement (November 13, 2026):** The overall product has **5 epics with 3 stories each (15 active stories total)**. The Brawl is **Epic 5** with **US-13, US-14, US-15**. Earlier "Epic 6" and "US-16+" identifiers are **historical only**, preserved below for context. The current official story IDs are the GitHub issue titles linked here.

## Epic 5 — Brawl Engine (3 active stories)

### US-13 — Choose Two Fighters (original US-16; issue #19)

**As a** member, **I want** to choose two different characters, **so that** I can start a valid Brawl matchup.

- **Given** I picked one fighter, **when** I choose a different second fighter, **then** I can see both choices before starting.
- **Given** I select the same character twice, **when** I confirm, **then** the website asks me to choose distinct fighters.
- **Given** a fighter is missing, **when** I press Start, **then** I stay on selection and no false match is created.

**Delivery:** [Issue #19](https://github.com/satya1130/CSC325-Capstone/issues/19) · Backlog · High priority · Figma mock-up exists; website implementation not yet complete.

### US-14 — Display Brawl (original US-17; issue #20)

**As a** member, **I want** to watch the fight's turns, moves, and health, **so that** I can understand the match.

- **Given** two valid fighters, **when** I start the Brawl, **then** the match display shows the fighters and live/simulated turns.
- **Given** a turn or attack happens, **when** the view updates, **then** move descriptions and health indicators remain readable.
- **Given** the match ends, **when** the result appears, **then** the website identifies the winner and shows an understandable outcome.

**Delivery:** [Issue #20](https://github.com/satya1130/CSC325-Capstone/issues/20) · Backlog · High priority · Figma scripted sequence exists, not live Django gameplay.

### US-15 — Working Brawl Engine (original US-23; issue #49)

**As a** member, **I want** a repeatable battle calculation using defined rules, **so that** results are consistent, checkable, and functional without an AI model.

- **Given** two distinct fighters and valid moves, **when** the match begins, **then** the server produces a legal turn sequence under reviewed combat rules.
- **Given** an attack, **when** health changes, **then** damage, health, and victory conditions remain within allowed bounds.
- **Given** a finished match, **when** the engine determines a winner, **then** the result is repeatable for the same starting conditions and made available to US-14.

**Delivery:** [Issue #49](https://github.com/satya1130/CSC325-Capstone/issues/49) · Ready · High priority · Not implemented in the deployed backend.

### Supporting work (not additional user stories)

- [#50 Define reviewed moves, weaknesses, and counters](https://github.com/satya1130/CSC325-Capstone/issues/50) — prerequisite/reference data; `scope:supporting`.
- [#52 Django/API/Brawl tests](https://github.com/satya1130/CSC325-Capstone/issues/52) — technical quality task; `scope:supporting`.
- Source character data and image details should come from the team's accepted files. Do not merge deprecated alternative character masters or replace the MongoDB data model without team review.

## Future Scope — deferred Brawl ideas

| Deferred ID | Issue | Future functionality |
| --- | --- | --- |
| FUT-06 | [#21](https://github.com/satya1130/CSC325-Capstone/issues/21) | Extended result explanations, retry journeys |
| FUT-07 | [#22](https://github.com/satya1130/CSC325-Capstone/issues/22) | Grounded AI-generated battle actions |
| FUT-08 | [#23](https://github.com/satya1130/CSC325-Capstone/issues/23) | Transparent AI-generated result explanations |
| FUT-09 | [#51](https://github.com/satya1130/CSC325-Capstone/issues/51) | Saved battle history and replay library |

The complete nine-story deferred list, including non-Brawl features, is in [Project_Description.md](Project_Description.md). These features are **not required to claim the current 15 active stories**. Real login, permissions, and OpenAI character summary/recommendation/Q&A belong to separate **active** Epics 3 and 4; they are not part of Epic 5.

**Important:** The Figma prototype demonstrates a scripted Brawl, but the Django/MongoDB site does **not yet** run a live battle engine. Do not mark the three active Brawl stories Done without code, tests, and team acceptance.

---

## Historical Brawl extension — archived for traceability

> The original text below is left intact except for its top-level heading. Its **Epic 6 and US-16 through US-20 IDs are no longer active** and should not be counted as additional current stories.


These are **proposed** stories to align the existing character-search/discovery backlog with the revised Product Goal. They supplement, rather than replace, the team's earlier five epics and 15 stories. Figma examples are not working AI or server implementations.

## Epic 6: Brawl Matchups and Explanation

### US-16 — Choose two fighters

**As a** registered member, **I want** to choose two distinct characters, **so that** I can set up a Brawl matchup.

- **Given** I have selected one fighter, **when** I choose a different second fighter, **then** both choices are visible before starting.
- **Given** I select the same fighter twice, **when** I try to confirm, **then** the prototype shows a meaningful correction path.
- **Given** a fighter is missing, **when** I press Start, **then** the interface returns me to fighter selection without a false result.

### US-17 — See a narrated example Brawl

**As a** member, **I want** to see turns, moves and health indicators, **so that** I can understand how the matchup develops.

- **Given** two fighters are confirmed, **when** I start the Brawl, **then** the prototype displays an example battle sequence.
- **Given** a turn or hit occurs, **when** the example updates, **then** its move description and health indicator are readable.
- **Given** the example finishes, **when** the result appears, **then** the winner is clearly identified.

### US-18 — Understand and retry results

**As a** member, **I want** an explanation of the winner and a replay/change option, **so that** I can understand and explore alternatives.

- **Given** a Brawl has ended, **when** I open the result, **then** I see a concise reason for the displayed outcome.
- **Given** I want different fighters, **when** I select New Matchup, **then** I return to an editable selection state.
- **Given** the Brawl is scripted, **when** I review its explanation, **then** it is not represented as official Marvel canon or live AI output.

## Epic 7: Future AI Battle Engine (Not Implemented)

### US-19 — Generate varied, grounded battle actions

**As a** member, **I want** fights based on verified character abilities and counters, **so that** the result varies and is meaningful.

- **Given** reviewed character data is available, **when** a future Brawl begins, **then** only permitted moves are considered.
- **Given** a move is selected, **when** the engine resolves it, **then** health and turn state update consistently.
- **Given** the information is insufficient, **when** an action needs unverified powers, **then** the system explains the limitation rather than inventing canon.

### US-20 — Explain AI results transparently

**As a** member, **I want** the engine to explain major battle decisions, **so that** I can understand the simulated outcome.

- **Given** a generated turn, **when** an explanation appears, **then** it references the permitted powers, weaknesses or counters.
- **Given** a generated result, **when** it is shown, **then** the UI labels it as a fan-game simulation.
- **Given** a future generated sequence fails validation, **when** the system detects the issue, **then** it rejects or corrects the event before showing it.

## Suggested Test Categories

- **Unit:** Valid move sets, two-distinct-fighter rules, bounded health/damage transitions.
- **Integration:** Fighter selection passed into match setup; engine action into view and explanation.
- **System:** Complete member, guest and admin journeys across devices.
- **Usability:** A non-fan user can follow the meaning of turns and results.
