# Marvel Clash — CSC 325 Capstone

**Team:** Satya, Kyle, Aryan, and Salih  
**Repository:** https://github.com/satya1130/CSC325-Capstone

Marvel Clash is a fan-made **Django character-exploration web app** backed by MongoDB Atlas, alongside an interactive **Figma Brawl prototype**. The deployed app lets visitors browse 49 Marvel characters, view their images and profiles, and search or filter their powers and categories. The Figma design explores future fighter comparisons, selections, and illustrative Brawls; a live Brawl engine is not implemented.

**Product Goal:** Make Marvel characters easy to explore and turn character comparisons into entertaining, understandable Brawls.

## 📋 Current Sprint 3 backlog — 5 epics / 15 active user stories (November 13, 2026)

> **Authoritative current planning scope.** All 24 previously numbered user stories were classified: **15 active stories** in five epics (three each) and **9 preserved deferred features** renamed FUT-01–FUT-09. The older October epic tables and "Epic 6" extensions farther down this README and the related documents are **historical evidence**, not extra current requirements. No working code or database was changed during the backlog restructure.

| Epic | Active user stories (GitHub issue numbers stay unchanged) | Current website status |
| --- | --- | --- |
| **1 — Character Search and Discovery** | [US-01 Search (#4)](https://github.com/satya1130/CSC325-Capstone/issues/4), [US-02 Browse (#5)](https://github.com/satya1130/CSC325-Capstone/issues/5), [US-03 Filter (#6)](https://github.com/satya1130/CSC325-Capstone/issues/6) | **3 Done** |
| **2 — Character Profiles** | [US-04 Description (#7)](https://github.com/satya1130/CSC325-Capstone/issues/7), [US-05 Powers (#8)](https://github.com/satya1130/CSC325-Capstone/issues/8), [US-06 Images (#9)](https://github.com/satya1130/CSC325-Capstone/issues/9) | **3 Done** |
| **3 — User Accounts and Character Selection** | [US-07 Member Login (#45)](https://github.com/satya1130/CSC325-Capstone/issues/45), [US-08 User Permissions (#46)](https://github.com/satya1130/CSC325-Capstone/issues/46), [US-09 Select Character (#10)](https://github.com/satya1130/CSC325-Capstone/issues/10) | **2 Ready, 1 Backlog** |
| **4 — OpenAI Features** | [US-10 AI Summary (#13)](https://github.com/satya1130/CSC325-Capstone/issues/13), [US-11 AI Recommendations (#14)](https://github.com/satya1130/CSC325-Capstone/issues/14), [US-12 AI Questions (#15)](https://github.com/satya1130/CSC325-Capstone/issues/15) | **3 Backlog** (not implemented) |
| **5 — Brawl Engine** | [US-13 Two Fighters (#19)](https://github.com/satya1130/CSC325-Capstone/issues/19), [US-14 Display Brawl (#20)](https://github.com/satya1130/CSC325-Capstone/issues/20), [US-15 Working Engine (#49)](https://github.com/satya1130/CSC325-Capstone/issues/49) | **1 Ready, 2 Backlog** |

**Delivery baseline:** Figma prototypes and journeys are complete, and the 49-character Django roster with MongoDB Atlas is deployed through Render. **Real** signup/login, sessions and role enforcement, playable Brawls, and OpenAI character features still need implementation. UI-only Figma examples cannot count as deployed backend functionality. The active login story includes signup and logout, and the active Brawl features require a verifiable winner/result. Original Given/When/Then criteria and GitHub issue/PR history were preserved.

### Future Scope (nine deferred stories)

- **FUT-01** Compare characters [#11](https://github.com/satya1130/CSC325-Capstone/issues/11); **FUT-02** Save favorites [#12](https://github.com/satya1130/CSC325-Capstone/issues/12); **FUT-03** Responsive improvements [#16](https://github.com/satya1130/CSC325-Capstone/issues/16)
- **FUT-04** Navigation improvements [#17](https://github.com/satya1130/CSC325-Capstone/issues/17); **FUT-05** Error handling improvements [#18](https://github.com/satya1130/CSC325-Capstone/issues/18); **FUT-06** Extended Brawl results/retry [#21](https://github.com/satya1130/CSC325-Capstone/issues/21)
- **FUT-07** AI-generated Brawl actions [#22](https://github.com/satya1130/CSC325-Capstone/issues/22); **FUT-08** AI Brawl explanations [#23](https://github.com/satya1130/CSC325-Capstone/issues/23); **FUT-09** Match history/replay [#51](https://github.com/satya1130/CSC325-Capstone/issues/51)

A related Favorites persistence task [#47](https://github.com/satya1130/CSC325-Capstone/issues/47) is deferred too. All these issues keep their original histories and acceptance criteria. Future Scope is a **GitHub Projects tab**, not a new epic. Issue labels `scope:future` and `kanban:future-scope` identify deferred items; the Projects view filter/Status must also be configured or verified separately. The remaining technical/design/process tasks have `scope:supporting` and do **not** count toward the fifteen active user stories.

**Review links:** [All 54 issue labels and recommended Projects card positions](docs/KANBAN_BOARD_PLACEMENT.md) · [Current 5-epic story definitions and acceptance guidance](Project_Description.md#current-requirements--sprint-3-active-product-scope-november-13-2026) · [Brawl backlog (active Epic 5 and historical extension)](BRAWL_BACKLOG.md) · [GitHub Issues](https://github.com/satya1130/CSC325-Capstone/issues) · [GitHub Projects board](https://github.com/satya1130/CSC325-Capstone/projects).




## 🚀 Current status — November 10, 2026

**Marvel Clash is deployed on Render and uses MongoDB Atlas.** The team verified the live roster, character images, profiles, name search, Hero/Villain/Antihero filtering, and power/ability filtering after deployment.

| Area | Current implementation |
| --- | --- |
| Frontend | Django templates, HTML, CSS, JavaScript and 49 local JPG portraits |
| Backend | Python 3.14, Django 6.1, read-only character API |
| Database | MongoDB Atlas via the official `django-mongodb-backend` |
| Hosting | Render web service with Gunicorn and WhiteNoise |
| Automation | GitHub Actions Django tests and four-stage CI/CD |
| Design | Figma interactive prototype for future fighter comparison/Brawl |
| Not yet implemented | Live AI Brawl engine, secure member accounts, persistent favorites |

**MongoDB migration:** [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88) migrated Django to MongoDB Atlas, introduced MongoDB-specific migrations and ObjectId character IDs, and updated CI to test against a separate temporary MongoDB service. The 49 character records were imported into Atlas, not committed to Git. The original SQLite database is legacy local development data, **not** the current application database.

### Local development (Windows PowerShell)

Install Python 3.14 and have access to a MongoDB Atlas deployment or another compatible MongoDB server. From the repository root:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:MONGODB_URI = Read-Host "MongoDB connection URI"
cd backend
..\.venv\Scripts\python.exe manage.py check
..\.venv\Scripts\python.exe manage.py migrate --noinput
..\.venv\Scripts\python.exe manage.py import_characters
..\.venv\Scripts\python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/` for the roster and `http://127.0.0.1:8000/api/characters/` for the API. A character detail endpoint uses a **MongoDB ObjectId**, for example `/api/characters/<24-character-objectid>/`; numeric paths such as `/api/characters/1/` are no longer valid. The import command is repeatable and updates characters by name.

**Security:** Never commit or share `MONGODB_URI`, `DJANGO_SECRET_KEY` or deployment secrets. For production, set `DJANGO_DEBUG=false`, `DJANGO_ALLOWED_HOSTS` to the actual Render hostname, and `DJANGO_SECRET_KEY` to a secure secret. Atlas Network Access must include the Render service's outbound IP ranges. Keep production data separate from CI test data.

### Production deployment on Render

The Render service needs these environment variables: `MONGODB_URI`, `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=false`, `DJANGO_ALLOWED_HOSTS`, and a suitable `PYTHON_VERSION`. The deployment runs Django migrations and the repeatable 49-character import before starting Gunicorn. Static images, CSS and JavaScript are served using Django staticfiles and WhiteNoise.

The verified live functionality is the **character roster**, not a playable Brawl or production authentication system. This section supersedes older SQLite/deployment descriptions kept below as project history.

---

## 🧭 Project Hub — Important Links

> **Use this section first.** It is the front-door index for the current Marvel Clash project.
>
> **🎨 Design:** [Primary Figma](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15) · [Personas](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=42-20) · [Context Diagram](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=324-2) · [Primary UX Journey](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=42-66)
>
> **🐍 Django / Backend:** [Backend folder](backend/) · [Django project](backend/marvelclash/) · [Character app](backend/characters/) · [API contract](docs/CHARACTER_API_CONTRACT.md)
>
> **🗄️ Data / Database:** [49-character CSV](backend/characters/data/marvel_characters.csv) · [Character model](backend/characters/models.py) · [Import command](backend/characters/management/commands/import_characters.py) · **MongoDB Atlas is the active database; the legacy SQLite DB is not committed**
>
> **📋 Project Management:** [Repository Map](docs/REPOSITORY_MAP.md) · [Project Description](Project_Description.md) · [Brawl Backlog](BRAWL_BACKLOG.md) · [Scrum/Kanban Plan](MIDPOINT_SCRUM_PLAN.md) · [Issues](https://github.com/satya1130/CSC325-Capstone/issues) · [Projects/Kanban](https://github.com/satya1130/CSC325-Capstone/projects) · [Pull Requests](https://github.com/satya1130/CSC325-Capstone/pulls)
>
> **🧪 CI / Evidence:** [Four-stage CI/CD](.github/workflows/marvel-clash-cicd.yml) · [Django tests workflow](.github/workflows/django-tests.yml) · [Current feature status](docs/M7_FEATURE_STATUS.md) · [Historical M7 Kanban planning](docs/M7_TEAM_KANBAN_EVIDENCE.md) · [Historical Nov. 8 planning tracker](docs/NOV8_STORY_EVIDENCE.md). For completed six-story acceptance evidence, see the [November 8 delivery section](#november-8-2026--six-story-delivery-and-cicd-evidence) below.

---

## Development timeline — oldest to newest

The sections below follow the order in which the project evolved. The **current production status and important links remain above** for quick reference; older sections are explicitly historical and do not override the current MongoDB configuration.

| Period | Milestone | What changed |
| --- | --- | --- |
| **October 2026** | Figma concept and planning | Defined the product goal, personas, UI screens, prototype Brawl journey, Scrum/Kanban process and initial architecture |
| **October 26** | Early Django MVP and recovery | Built/restored character APIs and the 49-character CSV-backed roster; the original implementation used SQLite |
| **November 7** | Feature completion and collaboration | Expanded search, category/power filters, profiles, 49 portraits, automated tests and reviewed story pull requests |
| **November 8** | Six-story delivery evidence | Recorded the two selected epics, four-stage GitHub Actions pipeline, protected-branch review and team sanity checks |
| **November 10** | MongoDB migration and deployment | Transferred the roster from SQLite to MongoDB Atlas, repaired images and ObjectId APIs, fixed CI/Render errors, and verified the deployed roster |
| **After the migration** | Documentation and follow-up | Updated README, API contract, repository map, feature status and AI-use disclosures; further Brawl/account features remain planned |

**Reading guide:** Start with the October prototype, then follow the dated implementation sections through November 10. Finish with the **Implementation reference**, **Project-wide AI-Use Statement**, and **Next Steps**. Each phase below references the central disclosure rather than presenting separate, inconsistent claims about AI usage. Historic submission requirements are retained for coursework and may no longer describe the latest assignment.

---

## October 2026 — Figma prototype and user journeys

**AI disclosure:** AI-assisted planning and prototype-writing support is described in the [project-wide AI-use statement](#project-wide-ai-use-statement). The Figma files are team design artifacts, not evidence that AI authored every screen or that the prototype implements live AI battles.

**Primary Marvel Clash Figma design:** https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15

**Updated context diagram:** https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=324-2

**Additional group-created Figma design (supplementary):** https://www.figma.com/design/rjq4hv5d0kOMdmc7z41K5j

**YouTube walkthrough:** https://youtu.be/8gb0xLyrx2o

**Before submission:** The group must confirm the primary design is publicly viewable and the video is unlisted, accessible, **under two minutes**, and demonstrates the same Figma design and user journey.

### Personas

- **Jordan — primary user / Marvel fan and matchup strategist:** Uses the full discovery-to-result journey. Jordan wants to find characters, inspect powers, compare opponents, choose two fighters, and understand the displayed Brawl result.
- **Alex — secondary user / casual new visitor:** Uses a phone, recognizes familiar Marvel characters, and needs simple descriptions, clear portraits, readable controls, and easy discovery before attempting a matchup.

### Prototype access roles

The Figma prototype also demonstrates **Guest**, normal-member examples such as **MarvelFan/Aryan**, and **Salih (Admin)**. These are access states used to show UI permissions; they are not a replacement for the Jordan/Alex user-centered personas, and they are not secure production accounts.

### Context Diagram

The single Marvel Clash system exchanges information with Aryan, MarvelFan, Guest and Admin Salih.

Its external prototype inputs include curated team character content and temporary Figma interaction state.

Planned connections to a grounded AI Brawl service and secure persistent accounts are explicitly marked **future**, not live.

### Key UI Screens

Discover/Home, categorized Roster, individual profiles, powers and abilities, Compare, Favorites, two-fighter selection, Brawl setup, scripted battle/health indicators, winner/result explanations and replay or correction routes.

Account and project-support screens include light/dark and desktop/mobile versions.

### UX Flow — Primary Jordan Persona

1. Open Discover and move to the Roster.
2. Search or filter characters and open a character profile.
3. Read powers/abilities and compare possible opponents.
4. Choose two different fighters for Brawl.
5. Confirm the matchup and begin the simulated fight.
6. Follow the example moves, health bars and commentary.
7. Review the winner and explanation, then replay or choose different fighters.
8. If a selection is missing or invalid, return to fighter selection and correct it.

### Sanity Check

The personas reflect who uses Marvel Clash, including a primary member who completes character discovery and Brawl.

The context diagram shows the same system and actors; the key UI screens support its character-to-Brawl Product Goal; and the UX flow follows MarvelFan from browsing to an explained result.

The prototype is illustrative: it does not implement permanent login sessions, persistent favorites or dynamic AI fights.

---

## October 2026 — Original architecture and planned web application

### October snapshot: Interactive Figma prototype architecture

This section documents the original Figma prototype. The working Django roster originated in PR #58, was restored in PR #60, and has since been deployed to Render. The prototype uses these conceptual layers:

- **Presentation:** Figma desktop/mobile and dark/light screens for Discover, Roster, character profiles, Compare, Favorites, Brawl and results, with Guest, member and admin demonstrations.
- **Character content:** A curated set of 49 character profiles and illustrations based on the team's spreadsheet and presentation, represented as static prototype content. The original Figma prototype does not call the API; the new local Django roster does.
- **Prototype interaction/state:** Figma navigation and variables demonstrate the selected persona, fighter choices and screen transitions. These are not secure, persistent accounts or a browser database.
- **Illustrative simulation:** Pre-authored battle actions, commentary, health changes and results. Fights are **not** computed by a running AI or combat engine.

### Original proposal: Web application architecture

A possible future deployment would use a web client, a character-data service and database, authenticated account services with server-side authorization, and a battle engine that uses reviewed powers, moves, strengths, weaknesses and counters.

The planned AI-assisted battle service would generate varied explanations and battle sequences grounded in that data. Animation and replay capabilities could be added later.

**The roster and read-only API are implemented on `main`; PR #88 subsequently replaced the SQLite data layer with MongoDB Atlas.** Accounts and battle simulation are still planned.

---

## October 2026 — Original test plan and quality goals

The following are **original October test-plan ideas**, not a claim that all tests were implemented. The later November 8 and November 10 sections document the actual Django/JavaScript tests and deployment checks.

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

---

## October 2026 — Planned Brawl AI features (not implemented)

The main planned AI feature is a grounded **Brawl engine**.

The engine would receive selected fighters and reviewed character moves, abilities, strengths, weaknesses and counter relationships.

It would generate varied battle actions, damage and health changes, turn events and understandable explanations.

Older project-backlog ideas—AI character summaries, recommendations and character Q&A—can remain as **additional future features**, but are not the current priority or a working integration.

Results would represent fan-made game simulations rather than official Marvel canon.

---

## October 2026 — Midpoint Scrum and Kanban planning

The [midpoint Scrum and Kanban plan](MIDPOINT_SCRUM_PLAN.md) maps the existing 15 issues and five new Brawl user stories to the current product goal, with proposed owners, priority, dates, workflow rules, architecture milestones and presentation evidence requirements.

**Important:** Proposed owners are planning assignments to be confirmed by the actual team; they are not proof of prior contributions. The interactive Figma prototype is not the same as a working Python/Django application. GitHub Project card statuses, individual feature branches, reviews and merges must be verified from real artifacts before reporting them as complete.

The previous prototype walkthrough's under-two-minute limit applies to that earlier deliverable. The **new midpoint assignment requires an 8–10-minute group presentation video**, with every actual group member participating.


---

## October 26, 2026 — Initial Django MVP and recovery history

> **Archive notice (November 10):** The following October notes describe the earlier SQLite-based implementation and review history. They are not current setup, deployment, or database instructions. See [Current status](#-current-status--november-10-2026) at the top and the [November 10 migration journal](#november-10-2026--sqlite-to-mongodb-migration-and-render-deployment) further below for the active MongoDB Atlas system.

The earlier sections preserve the project's original Figma planning and development roadmap. This **October recovery snapshot** records the working local Django MVP originally delivered in [PR #58](https://github.com/satya1130/CSC325-Capstone/pull/58), reverted by [PR #59](https://github.com/satya1130/CSC325-Capstone/pull/59), and restored in [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60). The current application uses MongoDB Atlas, not this original SQLite configuration.

### Completed implementation

- **Backend and data (October snapshot):** Django project in `backend/marvelclash/`, character app in `backend/characters/`, then-SQLite-backed `Character` model, 49-row CSV dataset and repeatable `import_characters` management command. **As of PR #88, MongoDB Atlas is the active database.**
- **API contract:** `GET /api/characters/` and `GET /api/characters/{id}/` implemented using JSON with stable string IDs; missing characters return a structured HTTP 404, and unsupported methods return HTTP 405. See [API contract](docs/CHARACTER_API_CONTRACT.md).
- **Frontend integration:** The Django-served roster uses the character API rather than the original 12 hard-coded sample entries. Users can view the 49-character roster, search by name, clear filters, see no-match feedback, and open/close a character profile with description and powers. The earlier standalone preview in `frontend/roster/` is retained.
- **Testing (October snapshot):** Eight Django tests passed locally (`python manage.py test`, result `OK`), and the local site was checked for roster count, search, and profiles. Later GitHub Actions runs and expanded tests are described in the current migration and CI sections.
- **Local setup (historical):** The earlier SQLite database and virtual environment were ignored by Git. **Do not use the old SQLite setup:** follow **Local development (Windows PowerShell)** at the top of this README and set `MONGODB_URI`.

### GitHub collaboration evidence

| Pull request | Contribution | Recorded status |
| --- | --- | --- |
| [#55](https://github.com/satya1130/CSC325-Capstone/pull/55) | Salih: project hub, issue templates, PR template | Merged |
| [#56](https://github.com/satya1130/CSC325-Capstone/pull/56) | Aryan: character API contract | Merged |
| [#57](https://github.com/satya1130/CSC325-Capstone/pull/57) | Satya: initial 12-character searchable frontend preview | Merged |
| [#58](https://github.com/satya1130/CSC325-Capstone/pull/58) | Satya: Django backend, SQLite, full 49-character import, API, frontend integration and Django tests | Merged then reversed from `main` by [#59](https://github.com/satya1130/CSC325-Capstone/pull/59); Aryan commented on ID stability post-merge |

**October snapshot only:** Contributor credit in this table is limited to the PRs that existed at that point. Kyle's later responsive work is recorded in [PR #62](https://github.com/satya1130/CSC325-Capstone/pull/62) and his independent sanity check in [PR #81](https://github.com/satya1130/CSC325-Capstone/pull/81). The GitHub Projects board should still be checked separately from issue labels.

### Figma prototype versus coded application

The [Figma design](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15) contains prototype screens illustrating comparison, favorites, two-fighter selection, scripted Brawls, results, and persona/account flows; these are not live Django Brawl or account functionality. **Since this October snapshot, the roster has been deployed to Render using MongoDB Atlas**. The live website supports character browsing, name search, category/power filtering, profiles, images, and read-only API access. Real authentication, persistent favorites, a working comparison/Brawl engine, AI-generated battle outcomes and more comprehensive accessibility testing remain future work.

### AI assistance on implementation

**Disclosure for this October phase:** [Project-wide AI-Use Statement](#project-wide-ai-use-statement), especially the ChatGPT/Django MVP entry. This phase used AI-assisted drafting and debugging; code correctness was checked by the team using the actual application and tests.

The [project-wide AI-Use Statement](#project-wide-ai-use-statement) **below** discloses ChatGPT's substantive assistance with the Django model, views/API routes, CSV importer, JavaScript integration, tests, setup, and Git workflow. Supporting implementation history is visible in [PR #58](https://github.com/satya1130/CSC325-Capstone/pull/58) and [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60). Satya ran and manually verified the local website, then ran the eight automated tests successfully. AI-assisted code is still subject to teammate review; no functional AI Brawl engine has been implemented.

For the formal 8–10 minute midpoint group presentation, demonstrate the live local Django roster separately from the interactive Figma Brawl prototype. **Current status:** [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60) restored Django on `main`; [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88) migrated the running roster to MongoDB Atlas. The October descriptions above are historical.

### Historical restoration review notes — SQLite-era implementation superseded by PR #88

- **Character IDs (before MongoDB):** The October implementation returned string-encoded SQLite integer keys. **Current API IDs are string-encoded MongoDB ObjectIds** after PR #88; see the live API route documentation above.
- **Automated CI (current):** `.github/workflows/django-tests.yml` starts a temporary **MongoDB 7** service, runs Django checks and migrations, imports and checks 49 records, and executes the automated tests. The four-stage workflow also uses MongoDB for its Test job. Confirm green results on GitHub before merging.
- **Review workflow:** PR #58 was merged before a submitted teammate review and subsequently reverted by PR #59. Request teammate review on the replacement PR *before* merging. A COMMENTED review is not the same as an APPROVED review.
- **Document scope (historical):** Existing Figma and Brawl plans were unchanged at that stage. **Images and Render deployment have since been implemented**, but executable Brawl and production authentication have not.


---

## November 7, 2026 — Implemented roster, team stories and delivery checks

- **Working Django roster:** 49 imported Marvel characters with name search, power search, Hero/Villain/Antihero filtering, profile descriptions, organized powers, and 49 uploaded local JPG portraits in the profile and roster cards. The original Figma Brawl remains a design prototype; an executable AI Brawl engine and real member sign-in have not been implemented.
- **Six selected user stories, two epics:** US-01 through US-06 all have dedicated branches, acceptance tests, successful CI, formal teammate approval, and merged PRs #70, #71, #73, #74, #75 and #76. Additional visual improvements: #77 (profile layout) and #78 (roster images), both merged.
- **Four-stage CI/CD:** Setup → Dependencies → Test → Deploy triggers on pull requests and pushes to `main`; only successful `main` pushes with the deployment variable enabled trigger the Render deployment hook.
- **Protected branch:** Active **Protect Main Branch** ruleset requires pull requests, one teammate approval, and a passing `Test` check. No bypass actors.
- **Production configuration:** Render service and GitHub deployment secret/variable were configured and deployment was previously demonstrated. A green Deploy job proves the hook request succeeded, **not by itself that Render finished serving the new version**; verify live functionality after changes.
- **November 8 submission:** Kyle's independent clean-clone sanity check is complete in [PR #81](https://github.com/satya1130/CSC325-Capstone/pull/81), with 36 passing Django tests and documented minor findings. The **new** unlisted video under three minutes remains to be recorded and linked.

**Module 7 midpoint navigation (historical presentation package):** [October presentation guide](docs/M7_MIDPOINT_PRESENTATION.md) · [Updated feature matrix and architecture](docs/M7_FEATURE_STATUS.md) · [Historical team roles / Kanban planning](docs/M7_TEAM_KANBAN_EVIDENCE.md). The October presentation guide includes superseded SQLite-era technical context.. **Recorded group video and real Projects board verification are still required.**

---

## November 8, 2026 — Six-story delivery and CI/CD evidence

This section supersedes older pre-deployment and planning-status statements elsewhere in this historical README. The selected scope is **Epic 1: Character Search & Discovery** and **Epic 2: Character Profiles & Information**, with six stories total. **Login / US-21 is not part of this six-story submission.**

### A. Four-stage CI/CD

Workflow: [`.github/workflows/marvel-clash-cicd.yml`](.github/workflows/marvel-clash-cicd.yml). It runs on pull requests targeting `main` and pushes to `main`.

| Job | Responsibility |
| --- | --- |
| **Setup** | Checkout, Python 3.14, validate required files |
| **Dependencies** | Install Python requirements and verify Django |
| **Test** | Django system checks, migrations, import/count of 49 characters, Django acceptance/API tests, Node roster tests |
| **Deploy** | After Test, call Render deploy hook for eligible pushes to `main` |

**Why Deploy shows skipped on PRs:** the deploy job condition explicitly requires a `push` to `refs/heads/main` and repository Actions variable `RENDER_DEPLOY_ENABLED == 'true'`. It is intentionally skipped during PR validation, while the required **Test** check runs.

- [Verified successful four-stage main workflow run (Nov. 7)](https://github.com/satya1130/CSC325-Capstone/actions/runs/42400002283).
- [Four-stage workflow file](.github/workflows/marvel-clash-cicd.yml).
- [Original standalone Django tests workflow](.github/workflows/django-tests.yml).
- Deployment is via Render using encrypted **GitHub Actions secret** `RENDER_DEPLOY_HOOK` and repository variable `RENDER_DEPLOY_ENABLED=true`. Never copy their values into commits, screenshots, README or logs.
- CI's Deploy success shows the hook returned successfully. Render's final deploy health and the current live images/filters should be manually checked at the hosted site; the hook alone is not a health check.
- **Current persistence:** Render's filesystem is ephemeral, but the active application uses **MongoDB Atlas for durable database storage**, with a repeatable source-CSV roster import. Future accounts and persistent favorites require additional models, authorization, and implementation; they are not live features.

### B. Protected `main` branch

The repository's [**Protect Main Branch** ruleset](https://github.com/satya1130/CSC325-Capstone/rules/26650396) is **active**. It targets the default branch (`main`) and has **no bypass actors**. Verified configured rules:

- Pull request required before merging.
- **One submitted teammate APPROVED review** required; COMMENTED does not qualify.
- Previously submitted approval is dismissed on a subsequent push.
- GitHub Actions **Test** status check must pass.
- Force pushes and branch deletions blocked.

A real instance is [US-01 PR #70](https://github.com/satya1130/CSC325-Capstone/pull/70): Kyle (`wilska1-stack`) submitted **APPROVED** before the PR was merged.

### C. Six-story evidence: two selected epics

Each linked PR is a distinct branch contribution, has recorded teammate APPROVED review, was merged into `main`, and ran the `Marvel Clash CI/CD` workflow successfully. Feature implementations sometimes predated these acceptance-test PRs; the story PRs add or improve implementation and regression coverage rather than claiming each feature was first invented in its listed PR.

| Epic / story | Issue and acceptance focus | Feature branch | Approved merged PR | Passing workflow |
| --- | --- | --- | --- | --- |
| **Epic 1 / US-01 Search** | [#4](https://github.com/satya1130/CSC325-Capstone/issues/4): partial, case-insensitive, multi-result and no-match search | `feature/us01-search-acceptance` | [#70](https://github.com/satya1130/CSC325-Capstone/pull/70) — Kyle | [CI](https://github.com/satya1130/CSC325-Capstone/actions/runs/42111610364) |
| **Epic 1 / US-02 Browse** | [#5](https://github.com/satya1130/CSC325-Capstone/issues/5): all 49 character records, ordering and optional image references | `feature/us02-browse-acceptance` | [#71](https://github.com/satya1130/CSC325-Capstone/pull/71) — Aryan | [CI](https://github.com/satya1130/CSC325-Capstone/actions/runs/42264142738) |
| **Epic 1 / US-03 Filter** | [#6](https://github.com/satya1130/CSC325-Capstone/issues/6): Hero/Villain/Antihero, 49 imported categories, combined filters | `feature/aryan-us03-character-filters` | [#73](https://github.com/satya1130/CSC325-Capstone/pull/73) — Aryan; earlier [#65](https://github.com/satya1130/CSC325-Capstone/pull/65) | [CI](https://github.com/satya1130/CSC325-Capstone/actions/runs/42390325040) |
| **Epic 2 / US-04 Description** | [#7](https://github.com/satya1130/CSC325-Capstone/issues/7): labeled character name and description | `feature/us04-profile-description-label` | [#74](https://github.com/satya1130/CSC325-Capstone/pull/74) — Aryan | [CI](https://github.com/satya1130/CSC325-Capstone/actions/runs/42392662214) |
| **Epic 2 / US-05 Powers** | [#8](https://github.com/satya1130/CSC325-Capstone/issues/8): readable powers, API data and missing-information fallback | `feature/us05-readable-powers` | [#75](https://github.com/satya1130/CSC325-Capstone/pull/75) — Aryan | [CI](https://github.com/satya1130/CSC325-Capstone/actions/runs/42395973186) |
| **Epic 2 / US-06 Images** | [#9](https://github.com/satya1130/CSC325-Capstone/issues/9): 49 character JPGs, responsive profile portrait, unavailable-image fallback | `feature/us06-character-profile-images` | [#76](https://github.com/satya1130/CSC325-Capstone/pull/76) — Aryan | [CI](https://github.com/satya1130/CSC325-Capstone/actions/runs/42397587339) |

**Additional enhancements (not additional required stories):** [PR #77](https://github.com/satya1130/CSC325-Capstone/pull/77) makes profile details more consistent; [PR #78](https://github.com/satya1130/CSC325-Capstone/pull/78) replaces roster initials with the 49 images. Both are merged. The 49 static JPGs are at [`backend/characters/static/characters/images/`](backend/characters/static/characters/images/) and sourced from a team-supplied slides PDF. Note: Hero/Villain/Antihero classifications are team-proposed editorial choices where fictional character alignment is ambiguous.

### D. Local onboarding and review-to-deploy walkthrough

On **Windows PowerShell**, install Python 3.14, Node.js 22 and Git, then:

```powershell
git clone https://github.com/satya1130/CSC325-Capstone.git
cd CSC325-Capstone
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:MONGODB_URI = Read-Host "MongoDB connection URI"
cd backend
..\.venv\Scripts\python.exe manage.py migrate --noinput
..\.venv\Scripts\python.exe manage.py import_characters
..\.venv\Scripts\python.exe manage.py test
..\.venv\Scripts\python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/` for the roster and `http://127.0.0.1:8000/api/characters/` for the API. In a new terminal from repo root, run the original frontend tests with `cd frontend/roster; node --test roster.test.cjs`. The importer uses `update_or_create` and can run repeatedly without duplicate character names.

For a new story or fix, branch from updated `main` with `git checkout -b feature/<issue-name>`, implement code and an acceptance test, then push `git push -u origin <branch-name>`. Open a PR into `main`, reference its issue, request a real teammate **Approve**, wait for green **Test**, and merge. The new `main` workflow starts Deploy only under its conditional hook configuration. Check the host's actual deployment and the live UI after merging. Protected `main` intentionally disallows bypassing approval/CI.

Do **not** commit local SQLite files, `.env`, secret tokens, deployment hook URLs or API keys. The repo's standard Django read-only character endpoints do not require external AI keys.

### E. AI-use disclosure and actual corrections

**Disclosure for the November 8 phase:** See the [project-wide AI-Use Statement](#project-wide-ai-use-statement) for tools, roles, verification and accepted/edited/rejected suggestions. The [historical story-planning tracker](docs/NOV8_STORY_EVIDENCE.md), [four-stage workflow](.github/workflows/marvel-clash-cicd.yml) and [PR #63](https://github.com/satya1130/CSC325-Capstone/pull/63) show project artifacts; they do not independently prove which prompts a person used.

ChatGPT was used to assist with the four-stage GitHub Actions workflow, Django/JS changes and acceptance tests for the selected user stories, CSS/profile/roster presentation, 49-image integration instructions, branch and PR creation, and README/evidence writing. The team's own character data, images and Figma design were used as inputs. Every change was submitted to GitHub with a visible diff and required a real teammate review and successful CI before merge. AI-generated outputs were **not treated as independently verified facts**.

Recorded issues and corrections from actual work (not invented examples):

1. **Render static assets:** Initial production CSS/JS did not load. PR [#66](https://github.com/satya1130/CSC325-Capstone/pull/66) added WhiteNoise/static file and startup support; a production-storage/test-mode issue was then corrected before tests passed. The site was visually checked after deployment.
2. **US-03 wrong branch / conflicts:** The category dropdown changes were initially submitted on a newly created branch as PR [#72](https://github.com/satya1130/CSC325-Capstone/pull/72). After a request to use the original filtering branch, the changes were transferred, the old branch/main divergence was reconciled, the duplicate PR closed, and [#73](https://github.com/satya1130/CSC325-Capstone/pull/73) reviewed and merged.
3. **US-04 wording and failing test:** The first version used 'Description'; it was changed to the requested **'Character Description'** label and its acceptance test updated on the same PR [#74](https://github.com/satya1130/CSC325-Capstone/pull/74). An earlier test run failed; a later run passed before review and merge.
4. **US-06 image delivery:** The team provided a PDF slide deck with one character image per page. A ZIP was first committed in the image folder, but the application required individual JPEG static assets; all 49 JPGs were then uploaded and verified. [#76](https://github.com/satya1130/CSC325-Capstone/pull/76) merged with those files, and [#78](https://github.com/satya1130/CSC325-Capstone/pull/78) added roster-card portraits.

Limitations: the images are third-party Marvel film visuals supplied for an **unofficial student fan prototype**; no commercial rights are claimed. The Figma Brawl engine and true login remain conceptual, and Render's hook success is not an automatic end-to-end live health assertion.

### F. Final teammate sanity check

**Teammate sanity check: COMPLETE (November 7, 2026).** Kyle independently cloned the latest `main` repository on macOS, installed dependencies, applied migrations, imported 49 Marvel characters, and launched the local Django website. He reported **36 Django tests passing**, confirmed 49 character images and descriptions, and checked search, filters, and the character API. See his written findings in [`docs/sanity-check-kyle.md`](docs/sanity-check-kyle.md) and his [merged PR #81](https://github.com/satya1130/CSC325-Capstone/pull/81), which Satya formally approved.

Kyle also documented three honest follow-ups: searching `spiderman` without a hyphen returns no results, a local missing `staticfiles` directory warning appears, and `/favicon.ico` returns 404. None prevented the tests from passing. After PR #81 merged, the [main-branch four-stage workflow](https://github.com/satya1130/CSC325-Capstone/actions/runs/42417364258) completed successfully, including the Render deployment-hook step. **The successful hook does not independently prove the live site is healthy; live deployment verification remains a separate check.**

The older 8–10 minute midpoint presentation and its separate video are **not** substitutes for the November 8 submission's ≤3-minute recorded story walkthrough.

---

## November 10, 2026 — SQLite-to-MongoDB migration and Render deployment

This section records the work performed to move the **working 49-character Marvel Clash Django roster from local SQLite to MongoDB Atlas**, repair the character imagery, update GitHub Actions, and deploy the result on Render. It documents completed actions, errors encountered, and the fixes used. The Django roster was already part of the team repository; the playable Brawl engine shown in the Figma prototype is **not** part of the live Django implementation.

### 1. Start with the latest team code

The local project was originally behind `origin/main` by 61 commits. The latest team changes were pulled into the Windows/VS Code working copy before database work began. This preserved the current character models, API routes, templates, JavaScript, images, and tests rather than rebuilding them separately. Work was then isolated on the `feature/mongodb-integration` branch and later reviewed in [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88).

The character model includes the name, description, powers, image reference, and Hero/Villain/Antihero category. The existing local SQLite database contained **49 characters**, and the checked-in project also contains a [49-character source CSV](backend/characters/data/marvel_characters.csv).

### 2. Configure MongoDB Atlas and Django

A MongoDB Atlas cluster and database user were configured. The Atlas connection string was stored in the `MONGODB_URI` environment variable, rather than written into GitHub source files. After an initial MongoDB authentication failure, the database user password and URI formatting were corrected and the Atlas connection succeeded.

The Django backend changed from `django.db.backends.sqlite3` to the official `django_mongodb_backend` engine. Current configuration is in [`backend/marvelclash/settings.py`](backend/marvelclash/settings.py):

```python
DATABASES = {
    "default": {
        "ENGINE": "django_mongodb_backend",
        "HOST": os.environ.get("MONGODB_URI"),
        "NAME": "marvelclash",
    }
}
DEFAULT_AUTO_FIELD = "django_mongodb_backend.fields.ObjectIdAutoField"
```

The project uses Django 6.1.2 with `django-mongodb-backend==6.1.0`, PyMongo and dnspython. The [root requirements file](requirements.txt) is used by GitHub Actions; the [backend requirements file](backend/requirements.txt) also lists the MongoDB dependencies.

MongoDB uses BSON **ObjectIds** for primary keys, unlike the integer primary keys originally generated by SQLite. The project now includes custom admin, auth, and content-type app configurations in [`backend/marvelclash/apps.py`](backend/marvelclash/apps.py), together with MongoDB-specific migration packages under [`backend/mongo_migrations/`](backend/mongo_migrations/). The Django system check and migrations were run successfully against Atlas.

### 3. Transfer all 49 character records and repair images

A temporary, **local-only** `import_characters.py` helper read the old `db.sqlite3` character rows using Python's `sqlite3` module and inserted the relevant fields through the Django `Character` model into MongoDB Atlas. The transfer was verified with a Django ORM count of **49**.

An image check then showed missing `image_ref` values even though all portrait JPG files already existed in `backend/characters/static/characters/images/`. A second temporary, **local-only** `fix_images.py` helper matched slugs of character names to those JPG filenames and filled each MongoDB record's `image_ref`. Verification reported **49 updated, zero unmatched images**, and the roster images and character profiles were checked visually.

Those two one-time helper scripts were **not included in PR #88**; they are not required for ordinary deployment. The maintained and committed [`python manage.py import_characters` command](backend/characters/management/commands/import_characters.py) instead reads the checked-in CSV, assigns images only when the corresponding file exists, and uses `update_or_create(name=...)`. It is **idempotent**, so rerunning it does not duplicate the 49 characters. Render and GitHub Actions use that maintained command.

### 4. Make character API routes compatible with MongoDB IDs

The old character detail URL accepted only integer IDs (for example, `/api/characters/1/`). Under MongoDB, IDs are 24-character hexadecimal ObjectIds. The detail route was updated to use a string parameter, the view validates the value using `ObjectId.is_valid()`, and valid IDs are converted to `ObjectId` for database lookups.

The read-only endpoints remain:

- `GET /api/characters/`: an alphabetical list of characters; supports optional `q`, `powers`, and `category` query parameters.
- `GET /api/characters/<objectid>/`: a character's ID, name, description, powers, image reference, and category.
- Invalid or unknown character IDs return JSON with `character_not_found` and HTTP **404**; unsupported methods return HTTP **405**.

The corresponding [views](backend/characters/views.py) and [routes](backend/characters/urls.py) are checked into the repository. API IDs are serialized to strings for JavaScript clients.

### 5. GitHub workflow and pull-request troubleshooting

The MongoDB migration was proposed through [PR #88: Integrate MongoDB Atlas with Marvel Clash](https://github.com/satya1130/CSC325-Capstone/pull/88). Because the repository protects `main`, the PR needed passing automated tests and a teammate review before merging. Aryan participated in the code review.

The CI integration needed several fixes, in this order:

| Observed failure | Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'django_mongodb_backend'` | GitHub Actions installed the root `requirements.txt`, which initially lacked the MongoDB backend | Added the MongoDB backend dependency to the **root** requirements |
| `localhost:27017: Connection refused` during `migrate` | No MongoDB server was available in the GitHub runner | Added a temporary MongoDB service container and `MONGODB_URI=mongodb://127.0.0.1:27017/` to both test jobs |
| MongoDB container failed to initialize on the GitHub runner | The `mongo:8` image reported a Linux kernel compatibility error on the runner | Pinned test jobs to Ubuntu 24.04 and used the `mongo:7.0` test image |
| Seven Django API test problems (six failures and one error) | Detail routes still used an integer URL converter; a missing numeric ID also caused ObjectId validation errors | Updated the URL converter, ObjectId lookup, and invalid-ID handling described above |

The updated workflows are [Django tests](.github/workflows/django-tests.yml) and [Marvel Clash CI/CD](.github/workflows/marvel-clash-cicd.yml). Automated checks use a **temporary MongoDB test database**, not the Atlas data containing the production roster. The 36-test Django suite includes API, roster, search, filters, import, images, and profile checks. PR #88 was reviewed and merged into `main` after the fixes. This journal records the issues without claiming that all interim runs succeeded.

### 6. Connect Render to MongoDB Atlas

The existing Render web service was updated with environment variables rather than hard-coded credentials:

| Render environment variable | Purpose |
| --- | --- |
| `MONGODB_URI` | MongoDB Atlas connection URI; keep secret |
| `DJANGO_SECRET_KEY` | Django signing secret; keep secret |
| `DJANGO_DEBUG` | Set to `false` for production |
| `DJANGO_ALLOWED_HOSTS` | Render hostname, without the `https://` prefix |
| `PYTHON_VERSION` | Select an appropriate supported Python runtime |

The observed Render start command was:

```bash
cd backend && python manage.py migrate --noinput && python manage.py import_characters && gunicorn marvelclash.wsgi:application --bind 0.0.0.0:$PORT
```

The first deployment failed with a PyMongo `ServerSelectionTimeoutError`, showing `SSL handshake failed` against Atlas replica-set members. Two Render **outbound IP ranges ending in `/24`** were found in the Render dashboard and added, including their `/24` CIDR suffixes, to **Atlas Security → Network Access**. Once both entries showed **Active**, the deployment was retried. The user then confirmed that the live site worked. Only the IP ranges provided by Render were approved; no MongoDB URI, password, or database user credential is included here.

If a future Render deployment fails, inspect **Events / Logs**, confirm the exact Atlas Network Access entries, verify the secret environment variables, and check the Render startup/build commands. Do **not** disable TLS certificate verification or publish the URI in logs, issues, or commits.

### 7. Live acceptance checks and current scope

After the successful deployment, the following were manually confirmed on the deployed site:

- All **49** characters load from the MongoDB-backed roster, with character portraits.
- Opening character profiles displays their descriptions and powers.
- Name search and the **Hero, Villain, Antihero** filter work.
- The **powers and abilities** filter works.

This is a **working, hosted character exploration application**, not merely a Figma mock-up. The team's Figma Compare/Brawl journey, AI-driven fighting, real member sign-in, and persistent user favorites should still be described as **prototype or future work**, unless separately implemented and verified.

### 8. Contribution and evidence

**Disclosure for the migration phase:** See the [project-wide AI-Use Statement](#project-wide-ai-use-statement), which distinguishes ChatGPT-assisted planning, code suggestions, troubleshooting and documentation from the configuration, test runs and live verification performed by people.

**Satya's documented migration/deployment work:** synchronized the local team repository, configured and tested the Django/Atlas integration, ran the one-time 49-character transfer and image-reference repair, validated character profiles and images, committed the integration branch, coordinated the PR/CI troubleshooting, added Render environment configuration and outbound IP ranges to Atlas, and verified the deployed application. ChatGPT was used for step-by-step assistance, code changes, troubleshooting, GitHub PR creation/updates, and README documentation. Teammate review and the prior team's original frontend/API/Figma contributions remain separate contributions.

**Evidence and source files:** [MongoDB integration PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88) · [Django settings](backend/marvelclash/settings.py) · [Mongo migrations](backend/mongo_migrations/) · [Character model](backend/characters/models.py) · [CSV import command](backend/characters/management/commands/import_characters.py) · [Character API views](backend/characters/views.py) · [Django test suite](backend/characters/tests.py) · [GitHub Actions runs](https://github.com/satya1130/CSC325-Capstone/actions).

---

## Implementation reference — Django roster, API and local setup history

The Django roster first appeared in [PR #58](https://github.com/satya1130/CSC325-Capstone/pull/58), was temporarily reverted by [PR #59](https://github.com/satya1130/CSC325-Capstone/pull/59), and was **restored to `main` by merged [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60)**. [PR #65](https://github.com/satya1130/CSC325-Capstone/pull/65) later added combined name, powers and optional category filtering with acceptance tests. The current Django app supports a 49-character roster, profiles and filtered read-only APIs backed by MongoDB Atlas following PR #88. The CSV source is committed; the legacy generated SQLite database is intentionally not committed. Brawl simulation, secure accounts, and persistent favorites remain future work. Character image mapping, profile portraits, and roster thumbnails were implemented in [PR #76](https://github.com/satya1130/CSC325-Capstone/pull/76) and [PR #78](https://github.com/satya1130/CSC325-Capstone/pull/78).

### Historical local setup (SQLite era, not current instructions)

Before [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88), the team used a local SQLite database for the Django MVP. **Do not reuse those old commands without MongoDB configuration.** For the current application, follow [Local development (Windows PowerShell)](#local-development-windows-powershell) near the top of this README, including the required `MONGODB_URI` environment variable, then run Django checks, migrations, the importer, and tests against the configured MongoDB instance.

Current character detail URLs require MongoDB ObjectIds, not `/api/characters/1/`. The import command uses `update_or_create` so it can be rerun without duplicating names. The original `frontend/roster` preview is retained; Django uses its own template/static assets.

**Tests:** The Django test suite (expanded after the original midpoint) covers the character list/detail API, missing characters, unsupported POST requests, homepage, empty roster, nullable unreviewed fields, repeatable imports, Django admin registration, and US-03 name/powers/category filtering behavior. The November 8 feature PRs each have successful `Marvel Clash CI/CD` runs; see the verified per-story matrix in the [November 8 section](#november-8-2026--six-story-delivery-and-cicd-evidence) above. The earlier verified main run for the restored MVP is preserved here: https://github.com/satya1130/CSC325-Capstone/actions/runs/40442492711 .

**Development safety:** `DEBUG` defaults to true for local work. For any deployment, set `DJANGO_DEBUG=false`, configure `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS`, and follow Django's deployment checklist. Do not deploy with the development defaults or the built-in server.

---

## Project-wide AI-Use Statement

This disclosure covers **the whole Marvel Clash project**, from Figma planning and the original Django MVP through the November user stories, MongoDB migration, GitHub Actions, deployment, and documentation. It distinguishes **AI-assisted suggestions and drafts** from changes that team members applied, tested, reviewed, and deployed. AI output was not treated as automatically correct. Individual AI usage is attributed only where reported or documented; unverified use by other teammates is not assumed.

**Evidence and attribution:** Relevant GitHub PRs, workflows, and code files are linked throughout this section. These citations support **what was built, reviewed and merged**. A GitHub PR alone does **not prove which exact AI prompts were used**, so descriptions of personal AI-tool use are explicitly reported disclosures, not independently verified prompt transcripts.

### AI Tools Used

**ChatGPT (OpenAI), planning and Django MVP (October):** Satya reports using ChatGPT to help plan and revise prototype user flows, the context diagram, written explanations and some Figma interactions. Project planning artifacts are linked in the [Figma prototype section](#october-2026--figma-prototype-and-user-journeys); this does not mean AI independently created or reviewed the team's entire Figma file. For the initial Django MVP in [PR #58](https://github.com/satya1130/CSC325-Capstone/pull/58), Satya used ChatGPT to help draft and revise Python/Django code, character models and API views, the CSV import command, HTML templates, JavaScript API integration, automated tests, local setup instructions, and Git/GitHub steps. Satya applied the proposed code in VS Code and checked the working 49-character roster, search, profiles, and Django tests.

**ChatGPT, November user stories, testing and CI/CD:** Satya reports ChatGPT assistance with Django/JavaScript acceptance tests, roster/profile CSS and layout, the 49 portrait integration workflow, GitHub Actions configuration, Git troubleshooting, and README/evidence drafting. Code and review evidence: [PR #63](https://github.com/satya1130/CSC325-Capstone/pull/63) (CI/CD), [PR #65](https://github.com/satya1130/CSC325-Capstone/pull/65) (filters), [PR #76](https://github.com/satya1130/CSC325-Capstone/pull/76) and [PR #78](https://github.com/satya1130/CSC325-Capstone/pull/78) (images), and [November 8 story evidence](docs/NOV8_STORY_EVIDENCE.md). These links establish the project changes, not the exact text of AI interactions.

**ChatGPT, SQLite-to-MongoDB migration and Render deployment ([PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88), November 2026):** Satya used ChatGPT for guided migration planning and troubleshooting. Assistance included MongoDB Atlas connection setup, configuring `django-mongodb-backend` and migrations, transferring the existing 49 character records, correcting image references, updating character API routes for MongoDB ObjectIds, diagnosing CI dependency/service/test failures, revising GitHub Actions, and troubleshooting the Render-to-Atlas TLS connection failure. ChatGPT also helped draft GitHub PR changes and update this README. These were **AI-assisted development and documentation tasks**, not a claim that AI independently verified the software.

**Claude (Anthropic):** A group contributor was previously reported to have used Claude to assist with README drafting and a separate Figma prototype. This is a **team-reported contribution, not independently confirmed for a named teammate**. The contributor should confirm the specific assistance and review before submission; no additional Claude usage is assumed.

**Non-AI development tools:** [Figma](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15) was used for interface design, interactive prototypes, personas, context diagram, and user journey. [GitHub](https://github.com/satya1130/CSC325-Capstone) and [GitHub Actions](.github/workflows/marvel-clash-cicd.yml) supported source control, pull requests, peer review, and automated checks. These tools are **not themselves cited as generative AI models**. MongoDB Atlas and Render are database/hosting infrastructure, also not generative AI.

### How AI-Assisted Work Was Reviewed

**Accepted and implemented:** Useful interface concepts and documentation outlines, along with reviewed suggestions for Django models, API endpoints, import scripts, frontend integration, tests, MongoDB configuration, GitHub Actions, and Render deployment instructions.

**Edited and adapted:** Persona details, access-state descriptions, design flows, wording about existing versus planned features, MongoDB/ObjectId route handling, image references, workflow configuration, test environments, and deployment setup. Proposed instructions and code were changed when they did not match the actual environment or tests.

**Rejected or corrected:** Confusing prototype navigation and account claims; suggestions implying secure production accounts or a live AI battle engine existed; and technical approaches that failed real checks, such as incomplete CI requirements, a missing MongoDB test service, incompatible MongoDB runner setup, and integer-only character detail routes after adopting ObjectIds. The migration fixes are described in the [November 10 troubleshooting journal](#5-github-workflow-and-pull-request-troubleshooting) and represented in [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88).

### Human Implementation, Verification, and Accountability

Satya worked in VS Code, configured MongoDB Atlas and Render settings, ran the migrations/imports, checked the transferred 49 character records and corresponding images, examined GitHub Actions/Render failures, and verified the deployed roster, character profiles, name search, and category/power filters. The MongoDB integration went through the team's GitHub pull-request and code-review process; the detailed sequence and source links are in the [November 10 migration and deployment journal](#november-10-2026--sqlite-to-mongodb-migration-and-render-deployment) above.

AI assistance also helped write and revise the README and documentation (see merged [PR #89](https://github.com/satya1130/CSC325-Capstone/pull/89) and [PR #90](https://github.com/satya1130/CSC325-Capstone/pull/90)). Screens, integration behavior, automated check outcomes, and deployment results are described as verified **only where they were actually tested or reported as working**. 

The Figma prototype's Brawl flow is separate from the deployed Django roster: **a live AI combat engine, production member login, and persistent favorites have not been implemented**. Team members should confirm their individual AI-tool use and contributions before submission.

---

## Project Backlog and Next Steps

**As of November 10, 2026:** The current implemented scope is the MongoDB-backed 49-character roster, read-only APIs, portraits, search, and filters. PR #86's prefix-first smart-search change remains a separate proposal until merged; do not describe it as live functionality based solely on an open PR.

The original backlog and project details are in [Project_Description.md](Project_Description.md) and the GitHub Issues tab.

The additional Brawl-focused user stories are documented in [BRAWL_BACKLOG.md](BRAWL_BACKLOG.md).

Remaining implementation work includes secure authenticated accounts, team review of character data, persistent favorites and match history, combat logic, AI grounding and safeguards, accessibility testing and optional animations. The Django roster and APIs were restored by PR #60 and migrated to MongoDB Atlas in PR #88; the full fighter-selection/AI Brawl experience is still planned.

---

## Submission Checklist

- [ ] Confirm that the root README and primary Figma link can be viewed by the professor.
- [ ] Confirm the Figma screens, personas, context diagram and UX journey follow the Product Goal.
- [ ] For the **earlier** prototype assignment, confirm the short video is unlisted and under two minutes. For **Module 7**, separately record an 8–10-minute video with **all group members participating**.
- [ ] Demonstrate MarvelFan's complete Figma workflow, from sign-in to the Brawl result.
- [ ] Have every team member confirm their actual AI tool usage and contributions. Review the [project-wide AI-use disclosure](#project-wide-ai-use-statement) and its linked implementation evidence before submission.
