# Marvel Clash — Brawl-Focused Backlog Extension

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
