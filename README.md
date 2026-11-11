# Marvel Clash — CSC 325 Capstone

**Team:** Satya, Kyle, Aryan, and Salih  
**Repository:** https://github.com/satya1130/CSC325-Capstone

Marvel Clash is a fan-made **Django character-exploration web app** backed by MongoDB Atlas, alongside an interactive **Figma Brawl prototype**. The deployed app lets visitors browse 49 Marvel characters, view their images and profiles, and search or filter their powers and categories. The Figma design explores future fighter comparisons, selections, and illustrative Brawls; a live Brawl engine is not implemented.

**Product Goal:** Make Marvel characters easy to explore and turn character comparisons into entertaining, understandable Brawls.


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

## Database migration and deployment journal — November 10, 2026

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

**Satya's documented migration/deployment work:** synchronized the local team repository, configured and tested the Django/Atlas integration, ran the one-time 49-character transfer and image-reference repair, validated character profiles and images, committed the integration branch, coordinated the PR/CI troubleshooting, added Render environment configuration and outbound IP ranges to Atlas, and verified the deployed application. ChatGPT was used for step-by-step assistance, code changes, troubleshooting, GitHub PR creation/updates, and README documentation. Teammate review and the prior team's original frontend/API/Figma contributions remain separate contributions.

**Evidence and source files:** [MongoDB integration PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88) · [Django settings](backend/marvelclash/settings.py) · [Mongo migrations](backend/mongo_migrations/) · [Character model](backend/characters/models.py) · [CSV import command](backend/characters/management/commands/import_characters.py) · [Character API views](backend/characters/views.py) · [Django test suite](backend/characters/tests.py) · [GitHub Actions runs](https://github.com/satya1130/CSC325-Capstone/actions).

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
> **🧪 CI / Evidence:** [Four-stage CI/CD](.github/workflows/marvel-clash-cicd.yml) · [Django tests workflow](.github/workflows/django-tests.yml) · [Feature Status](docs/M7_FEATURE_STATUS.md) · [Kanban/PR Evidence](docs/M7_TEAM_KANBAN_EVIDENCE.md) · [Nov. 8 Story Evidence](docs/NOV8_STORY_EVIDENCE.md)

### Historical implementation snapshot — November 7, 2026

- **Working Django roster:** 49 imported Marvel characters with name search, power search, Hero/Villain/Antihero filtering, profile descriptions, organized powers, and 49 uploaded local JPG portraits in the profile and roster cards. The original Figma Brawl remains a design prototype; an executable AI Brawl engine and real member sign-in have not been implemented.
- **Six selected user stories, two epics:** US-01 through US-06 all have dedicated branches, acceptance tests, successful CI, formal teammate approval, and merged PRs #70, #71, #73, #74, #75 and #76. Additional visual improvements: #77 (profile layout) and #78 (roster images), both merged.
- **Four-stage CI/CD:** Setup → Dependencies → Test → Deploy triggers on pull requests and pushes to `main`; only successful `main` pushes with the deployment variable enabled trigger the Render deployment hook.
- **Protected branch:** Active **Protect Main Branch** ruleset requires pull requests, one teammate approval, and a passing `Test` check. No bypass actors.
- **Production configuration:** Render service and GitHub deployment secret/variable were configured and deployment was previously demonstrated. A green Deploy job proves the hook request succeeded, **not by itself that Render finished serving the new version**; verify live functionality after changes.
- **November 8 submission:** Kyle's independent clean-clone sanity check is complete in [PR #81](https://github.com/satya1130/CSC325-Capstone/pull/81), with 36 passing Django tests and documented minor findings. The **new** unlisted video under three minutes remains to be recorded and linked.

**Module 7 midpoint navigation:** [Presentation guide and 10-item rubric](docs/M7_MIDPOINT_PRESENTATION.md) · [Truthful feature matrix and architecture](docs/M7_FEATURE_STATUS.md) · [Team roles / Kanban / PR evidence](docs/M7_TEAM_KANBAN_EVIDENCE.md). **Recorded group video and real Projects board verification are still required.**


## Current Django MVP — roster and profile implementation

The Django roster first appeared in PR #58, was temporarily reverted by PR #59, and was **restored to `main` by merged PR #60**. PR #65 later added combined name, powers and optional category filtering with acceptance tests. The current Django app supports a 49-character roster, profiles and filtered read-only APIs backed by MongoDB Atlas following PR #88. The CSV source is committed; the legacy generated SQLite database is intentionally not committed. Brawl simulation, secure accounts, and persistent favorites remain future work. Character image mapping, profile portraits, and roster thumbnails were implemented in PRs #76 and #78.

### Earlier local setup (SQLite-era; superseded by the MongoDB instructions above)

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

Open `http://127.0.0.1:8000/` for the roster or `/api/characters/` for the JSON list. Current character detail URLs require MongoDB ObjectIds, not `/api/characters/1/`. The import command uses `update_or_create` so it can be rerun without duplicating names. The original `frontend/roster` preview is retained; Django uses its own copied template/static assets.

**Tests:** The Django test suite (expanded after the original midpoint) covers the character list/detail API, missing characters, unsupported POST requests, homepage, empty roster, nullable unreviewed fields, repeatable imports, Django admin registration, and US-03 name/powers/category filtering behavior. The November 8 feature PRs each have successful `Marvel Clash CI/CD` runs; see the verified per-story matrix below. The earlier verified main run for the restored MVP is preserved here: https://github.com/satya1130/CSC325-Capstone/actions/runs/40442492711 .

**Development safety:** `DEBUG` defaults to true for local work. For any deployment, set `DJANGO_DEBUG=false`, configure `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS`, and follow Django's deployment checklist. Do not deploy with the development defaults or the built-in server.

## Architecture

### Current architecture: Interactive prototype

This section documents the original Figma prototype. The working Django roster originated in PR #58, was restored in PR #60, and has since been deployed to Render. The prototype uses these conceptual layers:

- **Presentation:** Figma desktop/mobile and dark/light screens for Discover, Roster, character profiles, Compare, Favorites, Brawl and results, with Guest, member and admin demonstrations.
- **Character content:** A curated set of 49 character profiles and illustrations based on the team's spreadsheet and presentation, represented as static prototype content. The original Figma prototype does not call the API; the new local Django roster does.
- **Prototype interaction/state:** Figma navigation and variables demonstrate the selected persona, fighter choices and screen transitions. These are not secure, persistent accounts or a browser database.
- **Illustrative simulation:** Pre-authored battle actions, commentary, health changes and results. Fights are **not** computed by a running AI or combat engine.

### Planned architecture: Web application

A possible future deployment would use a web client, a character-data service and database, authenticated account services with server-side authorization, and a battle engine that uses reviewed powers, moves, strengths, weaknesses and counters.

The planned AI-assisted battle service would generate varied explanations and battle sequences grounded in that data. Animation and replay capabilities could be added later.

**The roster and read-only API are implemented on `main`; PR #88 subsequently replaced the SQLite data layer with MongoDB Atlas.** Accounts and battle simulation are still planned.

## Prototype

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


---

## CSC 325 — November 8, 2026 final delivery evidence (current)

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
- Render's ephemeral filesystem and SQLite startup import are **not durable user-data storage**; adding accounts or persistent favorites requires a persistent production database. The current roster is source-CSV backed.

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
