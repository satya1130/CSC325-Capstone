# November 8 — Epic 1 and Epic 2 Evidence Tracker

> **Team scope decision (October 31, 2026):** Select Epic 1, Character Search and Discovery, and Epic 2, Character Profiles and Information, from [Project_Description.md](../Project_Description.md). These six user stories are the intended November 8 scope. This is a planning and evidence tracker, **not a claim that six stories have met the rubric**.

## Chosen stories, implementation, and acceptance criteria

| Epic / user story | GitHub issue | Currently working in Django | Remaining acceptance/test and process work |
| --- | --- | --- | --- |
| Epic 1 — US-01 Search for a character | [#4](https://github.com/satya1130/CSC325-Capstone/issues/4) | Name search on the roster; standalone search tests | Verify no-match message, matching cards, and image-if-available behavior in actual Django UI; record story-specific feature PR and teammate approval |
| Epic 1 — US-02 Browse characters | [#5](https://github.com/satya1130/CSC325-Capstone/issues/5) | 49 imported characters, list API, browse page | Acceptance test for multiple characters and browsing usability; link story-specific PR and approval |
| Epic 1 — US-03 Filter results | [#6](https://github.com/satya1130/CSC325-Capstone/issues/6) | Name search and clear-search behavior only | Build available filters, including combined filter behavior and clear/reset; automated acceptance test; feature branch, linked PR, approval |
| Epic 2 — US-04 View description | [#7](https://github.com/satya1130/CSC325-Capstone/issues/7) | Profile displays name and description | Test organized labels and missing-description fallback; story-specific PR and approval evidence |
| Epic 2 — US-05 View powers and abilities | [#8](https://github.com/satya1130/CSC325-Capstone/issues/8) | Profile displays powers | Test multiple powers are readable and missing powers show an honest fallback; story-specific PR and approval |
| Epic 2 — US-06 View character images | [#9](https://github.com/satya1130/CSC325-Capstone/issues/9) | Image field is nullable; actual character image assets **not yet integrated** | Obtain approved images, connect cards and profiles, test missing-image placeholder and responsive sizing; feature branch, linked PR, approval |

**Important:** Four stories have meaningful existing functionality, but the professor's new requirement says **each story** must be developed on a feature branch, linked to a Kanban issue, checked by at least one acceptance test, approved by a teammate, and merged with a green pipeline. Do not claim retrospective compliance unless the actual GitHub artifacts support it. New PRs should make meaningful fixes/tests for existing stories rather than empty paperwork commits.

## Suggested division (confirm with team)

- **Satya:** US-01 / US-04 tests and integration, help with backend work.
- **Aryan:** US-03 filtering and tests; review teammates' PRs.
- **Kyle:** US-06 image assets and integration once usable sources and usage rights are available; fallback placeholder and layout can be implemented first.
- **Sal:** US-02 / US-05 acceptance tests, documentation, Kanban linking and status.

**Image dependency:** Kyle previously collected 49 pictures in Google Slides, but the integration-ready assets were not yet supplied. US-06 is **not complete** until the approved images/placeholder behavior actually appear in the Django application and pass tests. If images cannot be prepared by November 8, escalate to the team/instructor rather than falsely marking Epic 2 done.

## Required evidence per story

1. Actual GitHub Project Kanban card with story, owner, priority, deadline, status, and issue link.
2. A feature branch from current `main` containing genuine functionality or meaningful acceptance-test improvements.
3. At least one test that explicitly checks the story's acceptance criteria.
4. PR referencing the issue (e.g. `Closes #9` only after acceptance criteria pass; `Refs #9` if partial).
5. Passing `Test` CI job and a formal **APPROVED** review by a teammate other than the PR author.
6. Merge into `main`, update Kanban status only after verification, and preserve PR/run links for the demo.

## Existing project and CI evidence

- [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60) supplied working backend, 49-character roster, profiles, tests and APIs. Earlier tests are useful, but do not prove a separate approved PR for each selected user story.
- [PR #63](https://github.com/satya1130/CSC325-Capstone/pull/63) merged the four-stage CI/CD workflow and documentation. Its review was COMMENTED, not APPROVED.
- [Four-stage main run](https://github.com/satya1130/CSC325-Capstone/actions/runs/41265092817) has Setup, Dependencies and Test green; Deploy was skipped, **not deployed**.
- [PR #62](https://github.com/satya1130/CSC325-Capstone/pull/62) is Kyle's already-merged responsive-design story (Epic 5), and **does not count toward selected Epic 1 + Epic 2**.
- The team still needs an active branch-protection ruleset, real hosting, secrets, a verified Deploy job, and the new-teammate sanity check before saying the November 8 assignment is complete.

## Recording and submission

Use a genuinely completed story PR showing the linked issue, branch, acceptance test, teammate approval, green `Test` status, merge, and real deployment. Record an **unlisted video of at most three minutes**. Submit repository/README, green run, qualifying merged PR, actual Kanban board URL, and the YouTube link. Do not invent unverified links or statuses.
