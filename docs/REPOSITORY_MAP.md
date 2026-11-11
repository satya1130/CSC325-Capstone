# Marvel Clash — Repository Map

> **Purpose:** one place to find the project’s current code, data, design, documentation, workflow, and assignment evidence.
>
> **Current snapshot:** November 10, 2026. The running character roster uses **MongoDB Atlas** and is deployed on **Render** following [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88). Historical planning documents are preserved for course evidence; use [README.md](../README.md) for setup and the full migration log.

## Start Here

| Area | Link | What it is |
| --- | --- | --- |
| Main project overview | [README.md](../README.md) | Current product goal, setup, architecture, prototype, testing, AI-use statement, and status |
| Project description / backlog | [Project_Description.md](../Project_Description.md) | Original proposal, epics, user stories, and acceptance criteria |
| Brawl backlog | [BRAWL_BACKLOG.md](../BRAWL_BACKLOG.md) | Brawl-focused user stories and future AI battle stories |
| Project dashboard | [PROJECT_HUB.md](../PROJECT_HUB.md) | Visual/history dashboard and workflow reference |
| Scrum / Kanban plan | [MIDPOINT_SCRUM_PLAN.md](../MIDPOINT_SCRUM_PLAN.md) | Scrum workflow, planned ownership, stages, milestones, and presentation planning |
| GitHub Issues | [Issues](https://github.com/satya1130/CSC325-Capstone/issues) | User stories, bugs, process tasks, priority and `kanban:*` status labels |
| GitHub Projects / Kanban | [Projects](https://github.com/satya1130/CSC325-Capstone/projects) | Live board that should mirror real issue/PR evidence |
| Pull requests | [Pull Requests](https://github.com/satya1130/CSC325-Capstone/pulls) | Review, CI, approval, and merge evidence |

## Figma / UX Design

| Artifact | Link |
| --- | --- |
| Primary Marvel Clash Figma | [Open Figma](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15) |
| Personas board | [Jordan + Alex personas](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=42-20) |
| Updated context diagram | [System context](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=324-2) |
| Primary user journey | [Discover → Roster → Profile → Brawl → Result](https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=42-66) |
| Earlier short prototype video | [YouTube](https://youtu.be/8gb0xLyrx2o) |

## Django / Backend

| Area | Link | Notes |
| --- | --- | --- |
| Django backend root | [`backend/`](../backend/) | Django project and `characters` app |
| Django entry point | [`backend/manage.py`](../backend/manage.py) | Local commands, migrations, tests, runserver |
| Project configuration | [`backend/marvelclash/`](../backend/marvelclash/) | Settings, root URLs, WSGI/ASGI |
| Character app | [`backend/characters/`](../backend/characters/) | Model, API views, templates, static files, tests, importer |
| Character model / database schema | [`models.py`](../backend/characters/models.py) | MongoDB Atlas-backed `Character` model with ObjectId IDs |
| Character API views | [`views.py`](../backend/characters/views.py) | List/detail JSON endpoints and filters |
| API contract | [`CHARACTER_API_CONTRACT.md`](CHARACTER_API_CONTRACT.md) | Fields, endpoints, limitations, and expected behavior |
| Automated Django tests | [`tests.py`](../backend/characters/tests.py) | API, importer/admin, and US-03 filter coverage |

### Database and source data

The committed source of truth for the current 49-character import is [`backend/characters/data/marvel_characters.csv`](../backend/characters/data/marvel_characters.csv).

**Active database:** MongoDB Atlas, configured with the `MONGODB_URI` environment variable in [Django settings](../backend/marvelclash/settings.py). The old generated `backend/db.sqlite3` is ignored and **not used by the current app**. Apply MongoDB migrations and populate with the repeatable importer as documented in [README.md](../README.md):

- Database model: [`backend/characters/models.py`](../backend/characters/models.py)
- CSV source: [`backend/characters/data/marvel_characters.csv`](../backend/characters/data/marvel_characters.csv)
- Import command: [`backend/characters/management/commands/import_characters.py`](../backend/characters/management/commands/import_characters.py)

## Frontend / Roster

| Area | Link |
| --- | --- |
| Django roster template | [`index.html`](../backend/characters/templates/characters/index.html) |
| Django roster JavaScript | [`roster.js`](../backend/characters/static/characters/roster.js) |
| Django roster CSS | [`style.css`](../backend/characters/static/characters/style.css) |
| Earlier standalone roster | [`frontend/roster/`](../frontend/roster/) |

## CI/CD and GitHub Workflow

| Artifact | Link |
| --- | --- |
| Four-stage CI/CD | [`marvel-clash-cicd.yml`](../.github/workflows/marvel-clash-cicd.yml) |
| Django test workflow | [`django-tests.yml`](../.github/workflows/django-tests.yml) |
| Issue templates | [`.github/ISSUE_TEMPLATE/`](../.github/ISSUE_TEMPLATE/) |
| Pull request template | [`.github/PULL_REQUEST_TEMPLATE.md`](../.github/PULL_REQUEST_TEMPLATE.md) |

## Assignment / Evidence Documents

| Document | Link |
| --- | --- |
| Feature / architecture status | [`M7_FEATURE_STATUS.md`](M7_FEATURE_STATUS.md) |
| Midpoint presentation package | [`M7_MIDPOINT_PRESENTATION.md`](M7_MIDPOINT_PRESENTATION.md) |
| Team / Kanban / PR evidence | [`M7_TEAM_KANBAN_EVIDENCE.md`](M7_TEAM_KANBAN_EVIDENCE.md) |
| November 8 story evidence | [`NOV8_STORY_EVIDENCE.md`](NOV8_STORY_EVIDENCE.md) |

## Historical Organizational Status — Nov. 5, 2026

> This section is an archived November 5 status snapshot, not the latest PR or issue status. As of November 10, the MongoDB migration [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88) is merged and the README documentation is being reviewed in [PR #89](https://github.com/satya1130/CSC325-Capstone/pull/89). Check [open pull requests](https://github.com/satya1130/CSC325-Capstone/pulls) and [issues](https://github.com/satya1130/CSC325-Capstone/issues) for live status.

- All **46 currently open issues** have both a `kanban:*` status and a `priority:*` label.
- Current open-issue status spread: **24 Backlog, 8 Ready, 5 In Progress, 9 In Review**.
- US-03 issue #6 was closed by merged PR #65 and its Kanban label was corrected from Backlog to **Done**.
- PR #65 (Aryan) merged combined name/powers/category roster filtering and acceptance tests.
- PR #62 (Kyle) is merged responsive-layout evidence.
- PR #63 (Satya) is merged four-stage CI/CD work.
- PR #64 is still open and proposes changing the November 8 tracked scope to Epic 1 + Epic 2. Do not treat that scope as final until the team reviews/merges it.
- PR #66 is merged with green CI for Render static-file/production fixes. It has no submitted teammate review recorded, and a live deployment URL is not documented here as verified yet.

## Organization Rules

1. Treat `README.md` + this repository map as the current navigation layer.
2. Keep historical assignment files instead of deleting them, but label snapshots/dates clearly.
3. Every active issue should keep one `kanban:*` label and one `priority:*` label.
4. Move an issue to Done only after its acceptance criteria are supported by a reviewed/merged artifact or code change.
5. Use a feature/docs branch and pull request for meaningful repository changes; do not silently overwrite teammate work on `main`.
6. Keep MongoDB Atlas credentials, deployment secrets, local SQLite archives, virtual environments, and `.env` files out of Git.
7. Do not claim Figma-only features (accounts, dynamic Brawl/AI, favorites) are working Django features until they are actually implemented and tested.

---

Maintained as the repository navigation/index for the CSC325 Marvel Clash capstone.