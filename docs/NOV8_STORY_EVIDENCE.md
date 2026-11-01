# November 8 — Two-Epic User Story Evidence Tracker

This document is a **work plan**, not a certification that six stories satisfy the rubric. Only mark a row complete after checking the *actual* PR, teammate approval, green Test job, linked Kanban card and an acceptance-criteria test. Updated following the successful four-stage PR run (Deploy was skipped).

## Chosen epics from Project_Description.md

**Epic 1 — Character Search and Discovery:** US-01, US-02, US-03.

**Epic 5 — User Experience, Accessibility, and Reliability:** US-13, US-14, US-15.

This is six stories in exactly two original epics. Implementing them may require small improvements to features that already partially work. Historical merges alone do not satisfy a new requirement for an individual approved feature PR and test for every story.

| Story / issue | Current executable evidence | Acceptance-test gap | Branch and PR / review evidence |
|---|---|---|---|
| US-01 [#4](https://github.com/satya1130/CSC325-Capstone/issues/4) Search | Django roster JS filters by name; standalone Node case-insensitive name test | Add test against actual Django-served roster or clarify standalone coverage; test no-match message | Existing [PR #57](https://github.com/satya1130/CSC325-Capstone/pull/57) and [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60); check formal approval and Kanban linking |
| US-02 [#5](https://github.com/satya1130/CSC325-Capstone/issues/5) Browse | API list and homepage tests plus 49 import assertion | Browser acceptance test for multiple displayed profiles and browsing | Existing [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60); verify review/link |
| US-03 [#6](https://github.com/satya1130/CSC325-Capstone/issues/6) Filter | Clear name search works | Multiple filters (category etc.) not implemented; implement and test clearing and intersections | **New branch and reviewed PR required** |
| US-13 [#16](https://github.com/satya1130/CSC325-Capstone/issues/16) Responsive UI | Kyle's merged [PR #62](https://github.com/satya1130/CSC325-Capstone/pull/62) has formal Satya approval | Add automated responsive acceptance check (e.g., Playwright viewport/no-overflow) and manual device test | PR #62 review verified; confirm Kanban issue linkage |
| US-14 [#17](https://github.com/satya1130/CSC325-Capstone/issues/17) Navigation | Basic roster/profile navigation exists | Test keyboard focus, returning to roster, clear path among main screens | **New branch and reviewed PR required** |
| US-15 [#18](https://github.com/satya1130/CSC325-Capstone/issues/18) Error handling | API 404/405 tests and no-match filter test | Implement/test failed fetch feedback and recovery, accessibility | **New branch and reviewed PR required** |

## Rules for every future story

1. Confirm a team member owns the story; add Kanban priority, deadline, status, and issue link.
2. Create a branch from current main: `feature/us-XX-short-name`.
3. Implement visible behavior and at least one automated test tied to **that story's** acceptance criteria.
4. Open a PR referencing `Closes #issue-number` (if all criteria satisfied) or `Refs #issue-number` otherwise.
5. Wait for green **Test** job and a formal **APPROVED** review by another teammate.
6. Merge via PR. Confirm issue and actual Kanban card agree with reality.
7. Capture one full workflow for the 3-minute unlisted video.

**Do not count the six stories as finished** solely because this tracking document exists. Epic 1 / Epic 5 and task ownership should be approved by the team, especially if the professor expects all 6–10 stories to be *newly developed during this assignment*.

## Workflow and ruleset evidence

- [Four-stage successful PR check](https://github.com/satya1130/CSC325-Capstone/actions/runs/41263298970): Setup, Dependencies, Test **success**; Deploy **skipped** by design on PRs.
- [PR #63](https://github.com/satya1130/CSC325-Capstone/pull/63): proposed workflow and README, reviews requested.
- [PR #62](https://github.com/satya1130/CSC325-Capstone/pull/62): Kyle's responsive feature, merged with Satya's submitted approval.
- Repository ruleset must be set by a repository admin; none was found at time of audit.
- Deployment and hosted health verification are still missing.
