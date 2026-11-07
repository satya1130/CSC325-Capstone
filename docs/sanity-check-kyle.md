# Teammate Sanity Check: Kyle

Date: 2026-11-07
Tester: Kyle Wilson
Branch: test/kyle-sanity-check
Base commit: 90e4dbd (main, Merge pull request #80)

## Environment

| Item | Value |
|---|---|
| Operating system | macOS, Terminal in VS Code |
| Git | 2.54.0 |
| Python | 3.14.7 |
| Dependencies | Installed from requirements.txt (Django 6.1.2) |

## Results

| Check | Result | Evidence |
|---|---|---|
| Clone latest main | Pass | HEAD at 90e4dbd, working tree clean |
| Install dependencies | Pass | All packages in requirements.txt installed |
| Run migrations | Pass | All migrations applied with OK |
| Import characters | Pass | Processed 49 Marvel characters |
| Automated tests | Pass | Ran 36 tests, OK |
| Launch local server | Pass | Home page returned 200 |
| Character images | Pass | All 49 images loaded |
| Descriptions and powers | Pass | Shown for all 49 characters |
| Search by name | Pass, with one issue | "spider" and "spider-man" found Spider-Man. "spiderman" returned no results |
| Clear search | Pass | Full list returned |
| Filters | Pass | Results changed as expected |
| API list endpoint | Pass | /api/characters/ returned 200 |
| API detail endpoint | Pass | /api/characters/1/ returned 200 |

## Known issues

1. Searching "spiderman" with no hyphen returns no results. Searching "spider-man" works. Suggested follow-up: make search ignore hyphens and spaces.
2. Running tests and the server prints "No directory at: backend/staticfiles/". Tests pass and local static files load. Confirm the deployment step collects static files before the site goes live.
3. /favicon.ico returns 404. This is cosmetic only.

## Notes

Tests and the local server used a SQLite database created with migrate. No database files were committed.