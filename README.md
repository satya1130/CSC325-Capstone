# Marvel Clash — CSC 325 Capstone

**Team:** Satya, Kyle, Aryan, and Salih  
**Repository:** https://github.com/satya1130/CSC325-Capstone

Marvel Clash is a fan-made character-exploration and Brawl **Figma prototype**. Users can browse 49 Marvel character profiles, learn their powers and abilities, compare fighters, select two opponents, and follow an explained example Brawl.

**Product Goal:** Make Marvel characters easy to explore and turn character comparisons into entertaining, understandable Brawls.

**Module 7 midpoint navigation:** [Presentation guide and 10-item rubric](docs/M7_MIDPOINT_PRESENTATION.md) · [Truthful feature matrix and architecture](docs/M7_FEATURE_STATUS.md) · [Team roles / Kanban / PR evidence](docs/M7_TEAM_KANBAN_EVIDENCE.md). **Recorded group video and real Projects board verification are still required.**


## Current local Django MVP — merged in PR #60

The Django roster first appeared in PR #58, was temporarily reverted by PR #59, and was **restored to `main` by merged PR #60**. The current `main` branch contains this tested Django MVP and a passing GitHub Actions workflow. The Django app supports a searchable roster, profiles and read-only APIs backed by SQLite. The CSV source contains 49 characters; the local database is intentionally not committed. Brawl simulation, accounts, favorites, images and public deployment remain future work.

### Run locally (Windows PowerShell)

From the repository root, with Python 3.14 available:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
cd backend
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py import_characters
..\.venv\Scripts\python.exe manage.py test
..\.venv\Scripts\python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/` for the roster, `/api/characters/` for the JSON list, or `/api/characters/1/` for one character. The import command uses `update_or_create` so it can be rerun without duplicating names. The original `frontend/roster` preview is retained; Django uses its own copied template/static assets.

**Tests:** All eight Django tests passed locally after the two additional API edge-case tests were added (reported result: `Ran 8 tests` and `OK`). These cover the character list, details, missing characters, unsupported POST requests, homepage, empty roster, and null fields for unreviewed image/category data. GitHub Actions on `main` passed the 49-record import and eight Django tests: https://github.com/satya1130/CSC325-Capstone/actions/runs/40442492711 .

**Development safety:** `DEBUG` defaults to true for local work. For any deployment, set `DJANGO_DEBUG=false`, configure `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS`, and follow Django's deployment checklist. Do not deploy with the development defaults or the built-in server.

## Architecture

### Current architecture: Interactive prototype

This section documents the original Figma prototype. A working local Django roster is now included in PR #58, as described above; the app is not deployed. The prototype uses these conceptual layers:

- **Presentation:** Figma desktop/mobile and dark/light screens for Discover, Roster, character profiles, Compare, Favorites, Brawl and results, with Guest, member and admin demonstrations.
- **Character content:** A curated set of 49 character profiles and illustrations based on the team's spreadsheet and presentation, represented as static prototype content. The original Figma prototype does not call the API; the new local Django roster does.
- **Prototype interaction/state:** Figma navigation and variables demonstrate the selected persona, fighter choices and screen transitions. These are not secure, persistent accounts or a browser database.
- **Illustrative simulation:** Pre-authored battle actions, commentary, health changes and results. Fights are **not** computed by a running AI or combat engine.

### Planned architecture: Web application

A possible future deployment would use a web client, a character-data service and database, authenticated account services with server-side authorization, and a battle engine that uses reviewed powers, moves, strengths, weaknesses and counters.

The planned AI-assisted battle service would generate varied explanations and battle sequences grounded in that data. Animation and replay capabilities could be added later.

**The character roster, SQLite data layer and read-only API are implemented on `main` following PR #60.** Accounts and battle simulation are still planned.

## Prototype

**Primary Marvel Clash Figma design:** https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15

**Updated context diagram:** https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=324-2

**Additional group-created Figma design (supplementary):** https://www.figma.com/design/rjq4hv5d0kOMdmc7z41K5j

**YouTube walkthrough:** https://youtu.be/8gb0xLyrx2o

**Before submission:** The group must confirm the primary design is publicly viewable and the video is unlisted, accessible, **under two minutes**, and demonstrates the same Figma design and user journey.

### Personas

- **Aryan — primary:** A normal member who is not necessarily a Marvel fan, but wants to log in, discover characters and use the main features.
- **MarvelFan — primary:** A registered fan persona with a no-password demonstration sign-in. This differs from an anonymous Guest and can explore profiles, comparisons and Brawls.
- **Guest — secondary:** An unsigned visitor who can explore some content, with advanced features requiring login or registration in the prototype.
- **Salih (Admin) — secondary:** A member with additional restricted Control Room, project-review, legacy-screen and testing options.

These are personas and simulated prototype roles, not verified production account permissions.

### Context Diagram

The single Marvel Clash system exchanges information with Aryan, MarvelFan, Guest and Admin Salih.

Its external prototype inputs include curated team character content and temporary Figma interaction state.

Planned connections to a grounded AI Brawl service and secure persistent accounts are explicitly marked **future**, not live.

### Key UI Screens

Discover/Home, categorized Roster, individual profiles, powers and abilities, Compare, Favorites, two-fighter selection, Brawl setup, scripted battle/health indicators, winner/result explanations and replay or correction routes.

Account and project-support screens include light/dark and desktop/mobile versions.

### UX Flow — Primary MarvelFan Persona

1. Open the prototype and sign in as **MarvelFan** without a password.
2. Browse Discover and Roster.
3. Read profiles and compare character powers.
4. Select two fighters for Brawl.
5. Confirm and begin the simulated matchup.
6. Follow the scripted moves, health bars and commentary.
7. Review the winner and explanation; replay or select different fighters.
8. If a fighter is missing, return to selection and correct it.

### Sanity Check

The personas reflect who uses Marvel Clash, including a primary member who completes character discovery and Brawl.

The context diagram shows the same system and actors; the key UI screens support its character-to-Brawl Product Goal; and the UX flow follows MarvelFan from browsing to an explained result.

The prototype is illustrative: it does not implement permanent login sessions, persistent favorites or dynamic AI fights.

## Test Plan Overview

The following are **test plans**, not a claim that tests have been implemented or executed in a working application.

### 1. Unit Testing (Future Implementation)

- Check required fields in the 49-character dataset.
- Verify comparison rules use the correct character attributes.
- Verify that fighter selection requires two distinct characters.
- Test health and damage calculations when a working battle engine exists.

### 2. Integration Testing

- Manually verify Figma transitions between Discover, Roster, Profile, Compare, Brawl and Result.
- Verify that the selected fighters carry through the intended prototype workflow.
- Verify the correction path when a fighter is missing.
- Later, test connections between the client, character service, account service and battle engine.

### 3. System / End-to-End Testing

- Walk through MarvelFan's full eight-step user journey.
- Verify Aryan's normal-member experience.
- Verify that Guest has limited access.
- Verify Salih's admin-only navigation in the prototype.
- Check both desktop/mobile and light/dark screen variants.

### 4. Usability Testing

- Observe Marvel fans and non-fans using the prototype without instructions.
- Check text contrast, mobile tap targets, navigation and readability.
- Look for overlapping clickable areas or confusing interactions.
- Confirm that a non-fan can understand the Brawl result and explanation.

After implementation, add automated browser tests, persistence and authorization tests, and checks that generated battle events stay consistent with reviewed character powers.

## Planned AI Features

The main planned AI feature is a grounded **Brawl engine**.

The engine would receive selected fighters and reviewed character moves, abilities, strengths, weaknesses and counter relationships.

It would generate varied battle actions, damage and health changes, turn events and understandable explanations.

Older project-backlog ideas—AI character summaries, recommendations and character Q&A—can remain as **additional future features**, but are not the current priority or a working integration.

Results would represent fan-made game simulations rather than official Marvel canon.

## AI-Use Statement

### AI Tools Used

**ChatGPT (OpenAI):** Used to help plan and revise prototype flows, the context diagram, written explanations and some Figma interactions. For the Django MVP in PR #58, Satya also used ChatGPT to generate and revise Python/Django backend code, the character model and API views, the CSV import command, HTML template and JavaScript API integration, Django automated tests, setup documentation, and Git/GitHub instructions. Satya copied the code into VS Code, ran the application locally, verified the 49-character roster and search/profile features, and ran the Django tests (8 passed). The AI-assisted code remains subject to team code review.

**Claude (Anthropic):** A group contributor reported using Claude to assist with README drafting and a separate Figma prototype.

**Figma:** Used for user interface design, interactive screens, personas, context diagrams and the user journey.

**GitHub:** Used by the group for documentation, user stories and project organization.

### AI Outputs Accepted, Edited or Rejected

**Accepted:** Useful interface ideas, navigation layouts, a structured primary user journey, and a README architecture and testing outline. The Django MVP also incorporated AI-generated starter code for the model, APIs, import, frontend integration, and tests, which was checked by running the application and local tests.

**Edited:** Persona identities, account-access differences, context flows, navigation hit areas, mobile layouts and wording about current versus planned functionality.

**Rejected or corrected:** Incorrect personas, statements suggesting secure persistent accounts or live AI fights already exist, and confusing or overlapping interactions.

The Figma design, documentation and GitHub updates were worked on by different group members at different times. Members should confirm individual tool use and contributions before submission.

## Project Backlog and Next Steps

The original backlog and project details are in [Project_Description.md](Project_Description.md) and the GitHub Issues tab.

The additional Brawl-focused user stories are documented in [BRAWL_BACKLOG.md](BRAWL_BACKLOG.md).

Remaining implementation work includes secure authenticated accounts, team review of character data, persistent favorites and match history, combat logic, AI grounding and safeguards, accessibility testing and optional animations. The local Django roster frontend and character APIs are merged in PR #60; the full fighter-selection/AI Brawl experience is still planned.

## Submission Checklist

- [ ] Confirm that the root README and primary Figma link can be viewed by the professor.
- [ ] Confirm the Figma screens, personas, context diagram and UX journey follow the Product Goal.
- [ ] For the **earlier** prototype assignment, confirm the short video is unlisted and under two minutes. For **Module 7**, separately record an 8–10-minute video with **all group members participating**.
- [ ] Demonstrate MarvelFan's complete Figma workflow, from sign-in to the Brawl result.
- [ ] Confirm that the AI-use statement and team contribution information are accurate.

## CSC 325 Midpoint Scrum / Kanban Plan

The [midpoint Scrum and Kanban plan](MIDPOINT_SCRUM_PLAN.md) maps the existing 15 issues and five new Brawl user stories to the current product goal, with proposed owners, priority, dates, workflow rules, architecture milestones and presentation evidence requirements.

**Important:** Proposed owners are planning assignments to be confirmed by the actual team; they are not proof of prior contributions. The interactive Figma prototype is not the same as a working Python/Django application. GitHub Project card statuses, individual feature branches, reviews and merges must be verified from real artifacts before reporting them as complete.

The previous prototype walkthrough's under-two-minute limit applies to that earlier deliverable. The **new midpoint assignment requires an 8–10-minute group presentation video**, with every actual group member participating.


---

## Historical midpoint recovery notes (October 26, 2026 — superseded by PR #60)

The sections above preserve the project's original Figma planning and development roadmap. This update records the **working local Django MVP** originally delivered in [PR #58](https://github.com/satya1130/CSC325-Capstone/pull/58), subsequently reverted by [PR #59](https://github.com/satya1130/CSC325-Capstone/pull/59), and included on this recovery branch for renewed review.

### Completed implementation

- **Backend and data:** Django project in `backend/marvelclash/`, character app in `backend/characters/`, SQLite `Character` model, 49-row CSV dataset and repeatable `import_characters` management command.
- **API contract:** `GET /api/characters/` and `GET /api/characters/{id}/` implemented using JSON with stable string IDs; missing characters return a structured HTTP 404, and unsupported methods return HTTP 405. See [API contract](docs/CHARACTER_API_CONTRACT.md).
- **Frontend integration:** The Django-served roster uses the character API rather than the original 12 hard-coded sample entries. Users can view the 49-character roster, search by name, clear filters, see no-match feedback, and open/close a character profile with description and powers. The earlier standalone preview in `frontend/roster/` is retained.
- **Testing:** Eight Django tests passed locally (`python manage.py test`, result `OK`), and the running local site was checked for roster count, search, and profiles. A passing GitHub Actions run has **not** been verified.
- **Local setup:** Follow the Windows PowerShell setup steps in the **Current Django MVP** section above; the SQLite database and Python virtual environment are intentionally ignored by Git.

### GitHub collaboration evidence

| Pull request | Contribution | Recorded status |
| --- | --- | --- |
| [#55](https://github.com/satya1130/CSC325-Capstone/pull/55) | Salih: project hub, issue templates, PR template | Merged |
| [#56](https://github.com/satya1130/CSC325-Capstone/pull/56) | Aryan: character API contract | Merged |
| [#57](https://github.com/satya1130/CSC325-Capstone/pull/57) | Satya: initial 12-character searchable frontend preview | Merged |
| [#58](https://github.com/satya1130/CSC325-Capstone/pull/58) | Satya: Django backend, SQLite, full 49-character import, API, frontend integration and Django tests | Merged then reversed from `main` by [#59](https://github.com/satya1130/CSC325-Capstone/pull/59); Aryan commented on ID stability post-merge |

Contributor credit above is limited to the evidence in these pull requests. Proposed assignments elsewhere in the repo, including Kyle's responsive design/image tasks, are not completion evidence. The actual GitHub Projects Kanban board should be checked separately from issue labels.

### Figma prototype versus coded application

The [Figma design](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15) contains screens illustrating comparison, favorites, two-fighter selection, scripted Brawls, results, and persona/account flows. **These are currently prototype demonstrations, not coded Django functionality.** The implemented website covers character browsing, name search, profiles, and read-only API access. Real authentication, favorites, comparison/Brawl engines, AI-generated battle outcomes, licensed images, deployment, and more comprehensive accessibility testing remain future work.

### AI assistance on implementation

The AI-use statement above discloses ChatGPT's substantive assistance with the Django model, views/API routes, CSV importer, JavaScript integration, tests, setup, and Git workflow. Satya ran and manually verified the local website, then ran the eight automated tests successfully. AI-assisted code is still subject to teammate review; no functional AI Brawl engine has been implemented.

For the formal 8–10 minute midpoint group presentation, demonstrate the live local Django roster separately from the interactive Figma Brawl prototype. **Current status:** PR #60 restored Django on `main` with passing CI; historical recovery-branch descriptions above are superseded.

### Historical restoration review notes — current implementation is in PR #60

- **Character IDs:** API `id` values are string-encoded SQLite primary keys; they are stable only within a single database. Recreating/importing a database may change IDs. This limitation addresses Aryan's PR #58 review and is recorded in the API contract; source-backed permanent IDs remain a future compatibility decision.
- **Automated CI:** `.github/workflows/django-tests.yml` creates a clean SQLite test database and runs `python manage.py check`, migrations, the 49-character CSV importer and all Django tests for PRs and pushes to `main`. Confirm green results on GitHub before merging.
- **Review workflow:** PR #58 was merged before a submitted teammate review and subsequently reverted by PR #59. Request teammate review on the replacement PR *before* merging. A COMMENTED review is not the same as an APPROVED review.
- **Document scope:** Existing Figma, proposals, epics and Brawl plans remain unchanged; executable Brawl, production authentication, images and deployment are not claimed.
