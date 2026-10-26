# Marvel Clash — CSC 325 Capstone

**Team:** Satya, Kyle, Aryan, and Salih  
**Repository:** https://github.com/satya1130/CSC325-Capstone

Marvel Clash is a fan-made character-exploration and Brawl **Figma prototype**. Users can browse 49 Marvel character profiles, learn their powers and abilities, compare fighters, select two opponents, and follow an explained example Brawl.

**Product Goal:** Make Marvel characters easy to explore and turn character comparisons into entertaining, understandable Brawls.

## Current Django MVP (PR #58, pending team review)

The repository now includes a working **local Django character-roster MVP** on the `feature/satya-django-backend` branch. This supersedes the earlier Figma-only implementation-status descriptions below once PR #58 is merged. The Django app supports a searchable roster, profiles and read-only APIs backed by SQLite. The CSV source contains 49 characters; the local database is intentionally not committed. Brawl simulation, accounts, favorites, images and public deployment remain future work.

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

**Tests:** Six tests passed locally before PR #58. Two more API edge-case tests have been added to the PR and should be run locally before merge. No GitHub CI check is currently reported for this PR.

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

**The character roster, SQLite data layer and read-only API are implemented locally in PR #58.** Accounts and battle simulation are still planned.

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

Remaining implementation work includes secure authenticated accounts, team review of character data, persistent favorites and match history, combat logic, AI grounding and safeguards, accessibility testing and optional animations. The local Django roster frontend and character APIs are included in PR #58.

## Submission Checklist

- [ ] Confirm that the root README and primary Figma link can be viewed by the professor.
- [ ] Confirm the Figma screens, personas, context diagram and UX journey follow the Product Goal.
- [ ] Confirm that the YouTube link is unlisted and the video runs for **less than two minutes**.
- [ ] Demonstrate MarvelFan's complete Figma workflow, from sign-in to the Brawl result.
- [ ] Confirm that the AI-use statement and team contribution information are accurate.

## CSC 325 Midpoint Scrum / Kanban Plan

The [midpoint Scrum and Kanban plan](MIDPOINT_SCRUM_PLAN.md) maps the existing 15 issues and five new Brawl user stories to the current product goal, with proposed owners, priority, dates, workflow rules, architecture milestones and presentation evidence requirements.

**Important:** Proposed owners are planning assignments to be confirmed by the actual team; they are not proof of prior contributions. The interactive Figma prototype is not the same as a working Python/Django application. GitHub Project card statuses, individual feature branches, reviews and merges must be verified from real artifacts before reporting them as complete.

The previous prototype walkthrough's under-two-minute limit applies to that earlier deliverable. The **new midpoint assignment requires an 8–10-minute group presentation video**, with every actual group member participating.
