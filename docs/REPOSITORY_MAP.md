# Marvel Clash — Repository Map

> **Purpose:** one place to find the project’s current code, data, design, documentation, workflow, and assignment evidence.
>
> **Current snapshot:** November 5, 2026. Historical planning documents are preserved for course evidence; use `README.md` and this map for current navigation.

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
| Character model / database schema | [`models.py`](../backend/characters/models.py) | SQLite-backed `Character` model |
| Character API views | [`views.py`](../backend/characters/views.py) | List/detail JSON endpoints and filters |
| API contract | [`CHARACTER_API_CONTRACT.md`](CHARACTER_API_CONTRACT.md) | Fields, endpoints, limitations, and expected behavior |
| Automated Django tests | [`tests.py`](../backend/characters/tests.py) | API, importer/admin, and US-03 filter coverage |

### Database and source data

The current Django importer continues to use [`backend/characters/data/marvel_characters.csv`](../backend/characters/data/marvel_characters.csv). The expanded 49-character reference data is stored separately in [`marvel_character_master.csv`](../backend/characters/data/marvel_character_master.csv), with a battle-oriented view in [`marvel_combat_index.csv`](../backend/characters/data/marvel_combat_index.csv). See [`CHARACTER_DATA_GUIDE.md`](CHARACTER_DATA_GUIDE.md) for compatibility notes.

The local SQLite file is **generated**, not committed: `backend/db.sqlite3` is intentionally ignored by `.gitignore`. Create it with migrations, then populate it using the importer:

- Database model: [`backend/characters/models.py`](../backend/characters/models.py)
- Django import CSV: [`backend/characters/data/marvel_characters.csv`](../backend/characters/data/marvel_characters.csv)
- Full character master: [`backend/characters/data/marvel_character_master.csv`](../backend/characters/data/marvel_character_master.csv)
- Combat/Brawl index: [`backend/characters/data/marvel_combat_index.csv`](../backend/characters/data/marvel_combat_index.csv)
- Data guide: [`docs/CHARACTER_DATA_GUIDE.md`](CHARACTER_DATA_GUIDE.md)
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

## Current Organizational Status — Nov. 5, 2026

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
6. Keep secrets, local SQLite databases, virtual environments, and `.env` files out of Git.
7. Do not claim Figma-only features (accounts, dynamic Brawl/AI, favorites) are working Django features until they are actually implemented and tested.

---

Maintained as the repository navigation/index for the CSC325 Marvel Clash capstone.