# Marvel Clash — GitHub Projects Kanban Placement Guide

**Scope baseline: November 13, 2026.** This is a **verified mapping of the GitHub issue titles and labels**, not proof of actual GitHub Projects card/status placement. User story numbers are preserved as GitHub issue numbers; the new user-facing identifiers are US-01–US-15 and FUT-01–FUT-09.

## How to sync the GitHub Projects board

1. Open the existing [Marvel Clash GitHub Projects board](https://github.com/satya1130/CSC325-Capstone/projects). **Future Scope is an existing tab/view**, not a sixth epic. If its saved filter is empty, edit the view filter to include `label:scope:future` and save it. If the tab uses an explicit Projects **Status** value, the issue label alone will not set that Status; move those ten item cards to the Future Scope value using Projects controls.
2. On the active Kanban view, filter out `scope:future` items (for example, `-label:scope:future`); optionally filter on `label:scope:active` to show **only the 15 professor-required stories**. Use `scope:supporting` for team implementation/process tasks, which do **not** count as additional user stories.
3. Compare every card's Projects **Status field** with the expected `kanban:*` label below. A label update does **not** automatically change Projects Status or move a card between board columns without an automation configured for that purpose.
4. Retain all issue numbers, old discussions, PR references, acceptance criteria, priority labels, and completed evidence. Future ideas are **deferred**, not deleted. Do not mark an open issue Done simply because a Figma prototype shows it.
5. Ensure the professor can access the board and see the active 5 epics/15 stories, assignees, priorities, dates, and authentic branches/PR reviews. Add or verify Projects fields where missing; the GitHub issue API does not set custom Projects dates or columns.

## Verified issue-by-issue placement

### Active user stories — 15 issue(s)

| Expected Kanban label | GitHub issue | Issue title | Priority | GitHub state |
| --- | --- | --- | --- | --- |
| `kanban:done` | [#4](https://github.com/satya1130/CSC325-Capstone/issues/4) | US-01: Search Characters | high | closed |
| `kanban:done` | [#5](https://github.com/satya1130/CSC325-Capstone/issues/5) | US-02: Browse Characters | high | closed |
| `kanban:done` | [#6](https://github.com/satya1130/CSC325-Capstone/issues/6) | US-03: Filter Characters | medium | closed |
| `kanban:done` | [#7](https://github.com/satya1130/CSC325-Capstone/issues/7) | US-04: Character Description | high | closed |
| `kanban:done` | [#8](https://github.com/satya1130/CSC325-Capstone/issues/8) | US-05: Powers and Abilities | high | closed |
| `kanban:done` | [#9](https://github.com/satya1130/CSC325-Capstone/issues/9) | US-06: Character Images | medium | closed |
| `kanban:ready` | [#45](https://github.com/satya1130/CSC325-Capstone/issues/45) | US-07: Member Login | high | open |
| `kanban:ready` | [#46](https://github.com/satya1130/CSC325-Capstone/issues/46) | US-08: User Permissions | high | open |
| `kanban:ready` | [#49](https://github.com/satya1130/CSC325-Capstone/issues/49) | US-15: Working Brawl Engine | high | open |
| `kanban:backlog` | [#10](https://github.com/satya1130/CSC325-Capstone/issues/10) | US-09: Select a Character | high | open |
| `kanban:backlog` | [#13](https://github.com/satya1130/CSC325-Capstone/issues/13) | US-10: AI Character Summary | low | open |
| `kanban:backlog` | [#14](https://github.com/satya1130/CSC325-Capstone/issues/14) | US-11: AI Character Recommendations | low | open |
| `kanban:backlog` | [#15](https://github.com/satya1130/CSC325-Capstone/issues/15) | US-12: Ask AI About a Character | low | open |
| `kanban:backlog` | [#19](https://github.com/satya1130/CSC325-Capstone/issues/19) | US-13: Choose Two Fighters | high | open |
| `kanban:backlog` | [#20](https://github.com/satya1130/CSC325-Capstone/issues/20) | US-14: Display Brawl | high | open |

### Future Scope — 10 issue(s)

| Expected Kanban label | GitHub issue | Issue title | Priority | GitHub state |
| --- | --- | --- | --- | --- |
| `kanban:future-scope` | [#11](https://github.com/satya1130/CSC325-Capstone/issues/11) | FUT-01: Compare Marvel Characters | low | open |
| `kanban:future-scope` | [#12](https://github.com/satya1130/CSC325-Capstone/issues/12) | FUT-02: Save Favorite Characters | low | open |
| `kanban:future-scope` | [#16](https://github.com/satya1130/CSC325-Capstone/issues/16) | FUT-03: Responsive Website Design Improvements | low | open |
| `kanban:future-scope` | [#17](https://github.com/satya1130/CSC325-Capstone/issues/17) | FUT-04: Easy Website Navigation Improvements | low | open |
| `kanban:future-scope` | [#18](https://github.com/satya1130/CSC325-Capstone/issues/18) | FUT-05: Handle Errors Clearly | low | open |
| `kanban:future-scope` | [#21](https://github.com/satya1130/CSC325-Capstone/issues/21) | FUT-06: Understand and Retry Brawl Results | low | open |
| `kanban:future-scope` | [#22](https://github.com/satya1130/CSC325-Capstone/issues/22) | FUT-07: Generate Grounded AI Battle Actions | low | open |
| `kanban:future-scope` | [#23](https://github.com/satya1130/CSC325-Capstone/issues/23) | FUT-08: Explain AI-Generated Results Transparently | low | open |
| `kanban:future-scope` | [#47](https://github.com/satya1130/CSC325-Capstone/issues/47) | FUT-TASK: Persist Favorite Characters for Registered Accounts | low | open |
| `kanban:future-scope` | [#51](https://github.com/satya1130/CSC325-Capstone/issues/51) | FUT-09: Review Previous Brawl Results and Replay Them | low | open |

### Supporting development/design/process work — 29 issue(s)

| Expected Kanban label | GitHub issue | Issue title | Priority | GitHub state |
| --- | --- | --- | --- | --- |
| `kanban:done` | [#1](https://github.com/satya1130/CSC325-Capstone/issues/1) | Need to edit KanBan Board | not labeled | closed |
| `kanban:done` | [#2](https://github.com/satya1130/CSC325-Capstone/issues/2) | KanBan board needs to be created. | not labeled | closed |
| `kanban:done` | [#3](https://github.com/satya1130/CSC325-Capstone/issues/3) | KanBan board needs to be created. | not labeled | closed |
| `kanban:done` | [#28](https://github.com/satya1130/CSC325-Capstone/issues/28) | DEV: Initialize Django REST Backend | high | closed |
| `kanban:done` | [#29](https://github.com/satya1130/CSC325-Capstone/issues/29) | DEV: Load 49 Character Profiles Into Database | high | closed |
| `kanban:done` | [#30](https://github.com/satya1130/CSC325-Capstone/issues/30) | DEV: Connect Character Browse UI to API | high | closed |
| `kanban:done` | [#34](https://github.com/satya1130/CSC325-Capstone/issues/34) | ARTIFACT: Original 49-character source collection prepared | not labeled | closed |
| `kanban:done` | [#35](https://github.com/satya1130/CSC325-Capstone/issues/35) | ARTIFACT: Prototype guide and UX journey documented | not labeled | closed |
| `kanban:done` | [#36](https://github.com/satya1130/CSC325-Capstone/issues/36) | ARTIFACT: Four themed/responsive login prototypes are prepared | medium | closed |
| `kanban:done` | [#37](https://github.com/satya1130/CSC325-Capstone/issues/37) | ARTIFACT: Four-persona design and primary user-journey boards prepared | medium | closed |
| `kanban:done` | [#43](https://github.com/satya1130/CSC325-Capstone/issues/43) | API: Specify Django character list/detail response contract | high | closed |
| `kanban:done` | [#48](https://github.com/satya1130/CSC325-Capstone/issues/48) | DEV: Add basic search/filter API for roster and categories | medium | closed |
| `kanban:in-review` | [#24](https://github.com/satya1130/CSC325-Capstone/issues/24) | DESIGN: Verify Final Figma Prototype | high | open |
| `kanban:in-review` | [#25](https://github.com/satya1130/CSC325-Capstone/issues/25) | DESIGN: Review Personas and System Context Diagram | high | open |
| `kanban:in-review` | [#27](https://github.com/satya1130/CSC325-Capstone/issues/27) | DOCS: Verify Architecture and Test Plan | high | open |
| `kanban:in-review` | [#38](https://github.com/satya1130/CSC325-Capstone/issues/38) | DATA: Peer-review 49-character roster, spreadsheet names, and slideshow images | high | open |
| `kanban:in-review` | [#39](https://github.com/satya1130/CSC325-Capstone/issues/39) | DESIGN: Peer-review Figma login interactions and hotspot usability | medium | open |
| `kanban:in-progress` | [#26](https://github.com/satya1130/CSC325-Capstone/issues/26) | DOCS: Finalize Updated Proposal and Feature Scope | high | open |
| `kanban:in-progress` | [#31](https://github.com/satya1130/CSC325-Capstone/issues/31) | PROCESS: Configure and Review GitHub Kanban Board | high | open |
| `kanban:in-progress` | [#32](https://github.com/satya1130/CSC325-Capstone/issues/32) | PROCESS: Record Individual Branch and PR Evidence | high | open |
| `kanban:in-progress` | [#33](https://github.com/satya1130/CSC325-Capstone/issues/33) | PRESENTATION: Prepare 8–10 Minute Midpoint Demo | high | open |
| `kanban:in-progress` | [#40](https://github.com/satya1130/CSC325-Capstone/issues/40) | PROCESS: Align GitHub issue statuses with verified artifacts and real implementation | high | open |
| `kanban:in-progress` | [#52](https://github.com/satya1130/CSC325-Capstone/issues/52) | TEST: Add Django unit, API integration and Brawl invariant tests | medium | open |
| `kanban:ready` | [#41](https://github.com/satya1130/CSC325-Capstone/issues/41) | DESIGN: Prepare Figma-to-code screen and component handoff | high | open |
| `kanban:ready` | [#42](https://github.com/satya1130/CSC325-Capstone/issues/42) | DATA: Produce normalized character and image import manifest | high | open |
| `kanban:ready` | [#44](https://github.com/satya1130/CSC325-Capstone/issues/44) | PROCESS: Confirm each team member's GitHub account, task ownership and dates | high | open |
| `kanban:backlog` | [#50](https://github.com/satya1130/CSC325-Capstone/issues/50) | DATA: Define reviewed move, weakness and counter fields for future Brawls | high | open |
| `kanban:backlog` | [#53](https://github.com/satya1130/CSC325-Capstone/issues/53) | UX: Audit coded desktop/mobile flows and accessibility | medium | open |
| `kanban:backlog` | [#54](https://github.com/satya1130/CSC325-Capstone/issues/54) | CONTENT: Review usage and attribution of Marvel character artwork | low | open |

## Completion notes

- 15 active issues = 6 Done, 3 Ready, 6 Backlog, 0 In Progress, 0 In Review (a status must be earned by actual feature work).
- Future Scope = 9 deferred feature stories + 1 supporting Favorites persistence task (#47).
- Supporting work = 29 issues, including verified completed infrastructure and still-needed review/testing/project-management tasks.
- The live Django app uses MongoDB Atlas and is hosted on Render. Figma prototype functionality does not imply deployed authentication, AI features, or a working Brawl engine.
- Source of active requirements: [Project_Description.md](../Project_Description.md). Brawl Epic 5 and archived older ideas: [BRAWL_BACKLOG.md](../BRAWL_BACKLOG.md).
