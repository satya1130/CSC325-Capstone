# CSC325 Midpoint — Scrum/Kanban, ownership and GitHub evidence

> **Accuracy rule:** Actual GitHub issues, pull requests and CI are evidence. Proposed assignments below must be confirmed by teammates. GitHub `kanban:*` issue labels are not the same as a live GitHub Projects board. This document is a board-setup checklist and presentation reference, not proof that Projects cards have been updated.

## Team identity and PR evidence

| Actual GitHub identity | Recorded contribution(s) | PR and verification | Midpoint requirement |
| --- | --- | --- | --- |
| Satya `@satya1130` | Django backend, 49-row importer/API/frontend/CI; standalone roster | [#57](../pull/57), [#58](../pull/58), [#60](../pull/60) | Meaningful authored branch/PR evidenced |
| Aryan `@AryanGrewal05` | Character API contract; PR #58 post-merge feedback; several merges | [#56](../pull/56), [#58](../pull/58) | Meaningful authored branch/PR evidenced |
| Salih `@JustEmre12` | Project Hub, issue/PR templates; this M7 readiness branch | [#55](../pull/55), M7 readiness PR pending review | Meaningful authored branch/PR evidenced |
| Kyle `@wilska1-stack` | README contribution and earlier repository commits | [commit evidence](https://github.com/satya1130/CSC325-Capstone/commits?author=wilska1-stack) | **No Kyle-authored PR verified as of snapshot — requires genuine branch + PR** |

**Review warning:** #55 and #56 have submitted Satya approvals. #57 and #59 had no submitted review; #58 received an Aryan COMMENTED review *after* merge; #60 merged without a recorded submitted peer review. This M7 PR must be reviewed **before** merge. Do not forge approvals or claim reviewers were present.

## Suggested current sprint board (confirm individual owners and due dates)

| Issue / objective | Proposed accountable owner | Priority | Proposed due date | Evidence-based current stage |
| --- | --- | --- | --- | --- |
| [#28](../issues/28) Django setup | Satya (author of actual MVP) | High | Oct 29, 2026 | In Review: code merged in #60, close after team acceptance |
| [#29](../issues/29) Import 49 rows | Salih review + Satya importer | High | Oct 30, 2026 | In Review: importer + 49-row CI verified; editorial review pending |
| [#30](../issues/30) Roster UI wired to API | Satya | High | Oct 29, 2026 | In Review: integrated; browser QA pending |
| [#43](../issues/43) Character API contract | Aryan | High | Oct 29, 2026 | In Review: authored spec in #56; final contract signoff |
| [#31](../issues/31) Configure real Projects board | Satya and Aryan | High | Oct 28, 2026 | In Progress: **live board setup not verified** |
| [#32](../issues/32) Each member's branch and PR proof | Salih | High | Oct 29, 2026 | In Progress: Kyle PR missing |
| [#33](../issues/33) 8–10 minute midpoint group video | Whole group | High | **Professor's actual deadline TBD** | In Progress: recording/upload not done |
| [#38](../issues/38) Audit character names/image usage | Kyle + Salih (proposed) | High | Nov 5, 2026 | In Review: source corrections needed |
| [#41](../issues/41) Figma-to-code handoff | Salih + Kyle (proposed) | High | Nov 5, 2026 | Ready |
| [#52](../issues/52) Extend automated tests | Salih + Aryan (proposed) | Medium | Nov 5, 2026 | In Progress: importer/admin/Node tests on M7 PR |
| [#53](../issues/53) Mobile/accessibility QA | Kyle (proposed) | Medium | Nov 12, 2026 | Backlog (candidate for Kyle's authentic PR) |
| [#49](../issues/49) Deterministic Brawl engine | Aryan + Satya (proposed) | High for product goal | Nov 19, 2026 | Backlog |
| [#50](../issues/50) Source-approved powers/moves/counters | Salih + Kyle (proposed) | Medium | Nov 12, 2026 | Backlog |
| [#46](../issues/46) Real role permissions | Aryan + Satya (proposed) | Medium | Nov 26, 2026 | Backlog |
| [#51](../issues/51) Replay/history | Satya (proposed) | Low | Dec 3, 2026 | Backlog |

**Note:** Dates are *planning targets*, not verified course due dates or agreements. Update live issues/Projects fields only after confirming with actual owners. The formal midpoint deadline must be copied from Brightspace.

## Five Kanban columns and acceptance gates
1. **Product Backlog:** requested, acceptance criteria documented, no current commitment.
2. **Ready:** requirements and owner confirmed, estimated, deadline assigned.
3. **In Progress:** author working on an actual branch with issue reference.
4. **In Review:** PR open, checks green, different teammate reviewing, test evidence available.
5. **Done:** acceptance criteria verified, PR reviewed/merged, issue updated, board card moved.

Recommended Projects fields: `Status`, `Assignee`, `Priority` (High/Medium/Low), `Target date`, `Epic/Area`, `PR evidence`. Add all active relevant issues as project items. Show the **real Projects URL** and live columns on video. As of this audit, GitHub connector exposes issue labels but not a tool to modify Projects v2 cards.

## Next milestones and dependencies
- **Oct 28–30 (proposed):** green CI, board synchronization, final technical/doc review and source data proof; every member demonstrates PR evidence; record midpoint video by actual course deadline.
- **Nov 5 (proposed):** reviewed 49-row source data, image manifest and permanent ID decision; mobile/browser QA.
- **Nov 12 (proposed):** fighter selectors, category/favorites/compare MVP progress and reviewed move/counter schema.
- **Nov 19 (proposed):** deterministic rules-based combat, nonnegative health, unique fighter validation and replay explanation.
- **Nov 26 (proposed):** permission handling, integration tests and error paths.
- **Dec 3–10 (proposed):** AI narrator/animations only if the playable rules engine works; final polish and regression checks.

## Group roles (proposed, must be confirmed verbally)
- **Satya — technical integration:** Django API/data/frontend, merge conflict and deployment planning, working demo.
- **Aryan — API and combat rules:** contract, ID strategy, algorithm/rules tests, backend review.
- **Salih — product, UX and project evidence:** Figma handoff, character-source QA, issue/PR traceability, midpoint narration and docs.
- **Kyle — frontend/accessibility/assets:** device/browser QA, art mapping/attribution, UI improvements and a meaningful branch/PR.

These are prospective roles. They are not claims that each proposed task has already been performed.

## Remaining controls outside this pull request
- [ ] Repository admin enables required pull-request reviews and required passing CI on protected `main`. A write-level collaborator cannot necessarily do this.
- [ ] Actual Projects board is created/configured, assigned tasks show priority/due date/status and a public/shareable link.
- [ ] Kyle authors and submits a meaningful PR, gets a real teammate review and merges after approval.
- [ ] Group verifies other members' ownership and date acceptance.
- [ ] Working browser/Figma/CI demo performed, group video recorded with all voices, uploaded unlisted, Brightspace link submitted.
