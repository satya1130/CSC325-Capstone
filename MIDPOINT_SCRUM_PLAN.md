# Marvel Clash — Midpoint Scrum and Kanban Plan

> **Planning document, not evidence of completed implementation.** Based on the actual current README, original 15 GitHub user stories, `BRAWL_BACKLOG.md`, the team's Figma prototype, 49-character source materials and the CSC 325 midpoint instructions. No live Django server or pull-request evidence was verified on 2026-10-22.

## Product goal
Make Marvel characters easy to explore and turn character comparisons into entertaining, understandable Brawls.

## Current evidence versus proposed work
- **Existing artifacts:** Figma prototype, revised context diagram, personas, 49-character source materials, illustrated/scripted Brawl flow, README and original GitHub user stories.
- **Not yet verified as built:** Django backend, production database, REST API, persistent accounts/favorites, real simulation engine, automated tests, feature pull requests.
- **Scope guardrail:** Deliver basic character browsing/profiles plus a simple Brawl demonstration before stretching into AI-generated fights. AI summary, Q&A and recommendations remain low priority.

## Kanban columns and entry/exit rules
| Column | Meaning |
| --- | --- |
| Product Backlog | Validated idea/story, not committed to imminent sprint |
| Ready | Requirements and acceptance criteria known, available to start |
| In Progress | Actual implementation or review work has begun; link evidence |
| In Review | Artifact / PR exists and teammate verification pending |
| Done | Acceptance criteria met, evidence attached, review completed |

**These are suggested target columns, not edits to GitHub Projects cards.** Change the actual board only after verifying status. Never move unimplemented user stories to Done solely because their Figma screens exist.

## Proposed ownership and target dates
Names below are *proposed task owners*, not historical credit. Team must confirm capacity, GitHub handles and member roster. Kyle is proposed for two stories (US-06 and US-13), per the latest team request. His GitHub username is not confirmed, so these are not GitHub account assignments.

| Issues | Work area | Proposed owner | Priority | Target | Target column |
| --- | --- | --- | --- | --- | --- |
| #4 US-01, #7 US-04 | Search and character descriptions | Satya / Salih | High | Nov 5 | Ready |
| #5 US-02, #8 US-05 | Browse and powers | Salih / Aryan | High | Nov 5–12 | Ready |
| #6 US-03, #9 US-06 | Filter and images | Aryan / Kyle | Medium | Nov 12 | Product Backlog |
| #10 US-07, #11 US-08 | Selection and comparison | Salih / Aryan | High | Nov 12–19 | Ready |
| #12 US-09 | Persistent favorites | Satya | Medium | Nov 19 | Product Backlog |
| #13–15 US-10–12 | AI summaries, recommendations, Q&A | Salih / Aryan / Satya | Low | Dec 3 | Product Backlog |
| #16 US-13, #17 US-14, #18 US-15 | Responsive UI, navigation, errors | Kyle / Aryan / Satya | Medium / High | Nov 19–26 | Backlog / Ready |
| #19–21 US-16–18 | Fighter selection, scripted Brawl, results | Aryan / Salih / Satya | High | Nov 19–26 | Ready |
| #22–23 US-19–20 | AI battle engine and explanations (stretch) | Salih / Aryan | Low | Dec 10 | Product Backlog |
| #24–25 | Final Figma and context/persona review | Satya / Aryan | High / Medium | Oct 29 | In Review (verify) |
| #26–27 | Proposal, architecture and test plan | Salih / Satya | High | Oct 30 | Ready / In Review (verify) |
| #28 | Initialize Django REST backend | Aryan | High | Nov 5 | Ready |
| #29 | Import curated 49-character data | Salih | High | Nov 12 | Ready |
| #30 | Connect browser UI to actual API | Satya | High | Nov 19 | Ready |
| #31 | Validate Kanban properties/cards | Aryan | High | Oct 28 | Ready |
| #32 | Collect real GitHub branch/PR/review/merge evidence | Salih | High | Nov 20 | Ready |
| #33 | Record 8–10 minute midpoint demo | Satya | High | Nov 20 | Ready |

## Sprint milestones (proposals; adjust to actual course deadline)
1. **Oct 28–30:** Confirm member responsibilities, working Figma navigation, Kanban owner/priority/due-date fields; reconcile proposal and architecture.
2. **Nov 5:** Local Django application and tested JSON endpoint, initial roster/profile implementation.
3. **Nov 12:** Load validated character dataset, show real API-backed detail and basic tests.
4. **Nov 19:** Implement or integrate character browsing/selection; connect simple Brawl flow to app, as feasible.
5. **Nov 20–26:** Each member supplies own branch/PR; teammates review and merge actual work. Prepare working demo, risks and 8–10 minute group video.
6. **Dec 3–10:** Optional finishing, QA, accessibility, AI stretch only after MVP is reliable.

## Pull request workflow
1. Contributor creates a meaningful feature branch, e.g. `feature/character-api`.
2. Contributor implements and tests their change, commits, pushes and opens a PR with linked issue.
3. A different teammate reviews the code and comments/approves as appropriate.
4. Merge the reviewed PR into `main`; move the linked card to Done **only** when acceptance criteria pass.
5. Presentation shows the *real* PR URLs, review author and merge status. Do not create placeholder PRs or award fictional contribution credit.

## Recommended midpoint recording sequence (9 minutes target)
1. Problem, target users, product goal (0:50).
2. Final scope and honest implementation/prototype statuses (0:55).
3. Figma full navigation and user journey (1:30).
4. Actual current architecture and planned Django/REST/database (0:55).
5. Working Django code demo, if implemented (1:10).
6. Kanban columns, assignees, priority and dates (0:55).
7. Branches, PRs, reviews and merges (0:55).
8. Confirmed team responsibilities and upcoming milestones (0:50).
9. Challenges, risks, mitigation and next steps (1:00).

## Risks and mitigation
- **Prototype versus code confusion:** Explicitly label Figma as illustrated rather than deployed functionality.
- **Scope creep:** Prioritize Django catalog, profile and Brawl demonstration before optional AI.
- **Inconsistent original proposal:** Update summary to revised Brawl-focused goal without erasing the existing discovery feature backlog.
- **Missing evidence:** Keep actual task links, demo recordings and PR reviews attached to board cards.
- **Deadline pressure:** Split small issues across confirmed members, review weekly and defer optional features.

## Submission evidence
- [Primary Figma prototype](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15)
- [Context diagram](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=324-2)
- [Existing prototype walkthrough](https://youtu.be/8gb0xLyrx2o) — this is **not** the required 8–10 minute midpoint video
- [README](README.md), [Original proposal](Project_Description.md), [Brawl extension](BRAWL_BACKLOG.md)
- [GitHub Issues](https://github.com/satya1130/CSC325-Capstone/issues)
- Kanban Project URL and actual PR links: add once confirmed.

## Workflow update (2026-10-22)
- Archived duplicate Kanban setup issues #1 and #3 as Done; #2 remains open because the update was unavailable.
- Design-verification tasks #24, #25 and #27 are **In Review**, not Done; the referenced materials exist, but formal team approval is not verified.
- Process/presentation preparation tasks #31 and #33 are marked **In Progress** at the issue-label level. The prototype video is not the midpoint recording.
- Planned backend implementation and Brawl coding tasks remain **Ready** or **Product Backlog**, not Done.
- Salih's GitHub username is **Justemre12** and existing repository permission was confirmed as **write**. GitHub write access does not automatically grant access to another person's ChatGPT connector.
- Issue-label statuses are not the same thing as moving cards into GitHub Projects board columns. Confirm board status independently.
