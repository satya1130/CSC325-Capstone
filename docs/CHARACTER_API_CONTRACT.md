# Marvel Clash — Character API Contract

**Original author:** Aryan Grewal · **Issue:** #43 · **Updated:** November 10, 2026

> This document reflects the **MongoDB Atlas-backed Django application** on `main` after [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88). The first version described the earlier SQLite prototype restored in PR #60. The roster is now deployed on Render; the Figma Brawl is still a prototype.

## Architecture and source data

The Django `characters` model stores 49 Marvel characters in **MongoDB Atlas**, configured with `django_mongodb_backend`. The repeatable [CSV importer](../backend/characters/management/commands/import_characters.py) reads the checked-in [49-character CSV](../backend/characters/data/marvel_characters.csv) and uses `update_or_create(name=...)` to avoid duplicates. JPG portraits are checked into [static assets](../backend/characters/static/characters/images/). The data and use of third-party artwork still need editorial/licensing review.

The backend uses Django's **`JsonResponse`**, not Django REST Framework viewsets. The API is read-only, unauthenticated character browsing; it is **not** an account or Brawl service.

## Character representation

| Field | JSON type | Current meaning |
| --- | --- | --- |
| `id` | string | MongoDB ObjectId, serialized as a **24-character hexadecimal string** |
| `name` | string | Unique Marvel character name |
| `description` | string | Character description |
| `powers` | string | Period-separated or otherwise textual abilities |
| `image_ref` | string or null | Relative local static JPG reference, when available |
| `category` | string or null | Team-assigned Hero, Villain, or Antihero category |

ObjectIds remain stable for existing documents, including repeat imports by name, but clients should not assume the same ID survives deleting and recreating the database. An independently sourced permanent identifier could be added later with team agreement.

## HTTP endpoints

### `GET /api/characters/`

Returns HTTP **200** and an alphabetically sorted `{"characters":[...]}` object. Optional case-insensitive query parameters can be combined:

- `q`: partial match within the character name
- `powers`: partial match within the powers text
- `category`: exact category match, ignoring case

No matches returns `{"characters":[]}`. Example **illustrative structure** (not a claim about an actual database record):

```json
{
  "characters": [
    {
      "id": "507f1f77bcf86cd799439011",
      "name": "Iron Man",
      "description": "Example character description.",
      "powers": "Powered suit. Flight.",
      "image_ref": "characters/images/iron-man.jpg",
      "category": "Hero"
    }
  ]
}
```

### `GET /api/characters/{objectid}/`

Returns one character object with the same six fields. The URL parameter must represent a MongoDB ObjectId, **not** the old numeric SQLite ID. Both a malformed ID and an unknown valid ObjectId return HTTP **404**:

```json
{"error":{"code":"character_not_found","message":"Character not found."}}
```

The list and detail views reject unsupported methods, including POST, with HTTP **405** and `{"error":"Method not allowed"}`.

## Tests and implementation evidence

The [Django tests](../backend/characters/tests.py) cover the list/detail JSON API, missing and malformed IDs, method restrictions, search/category/power filtering, importer idempotency, profile/roster rendering, and character imagery. The [Django tests workflow](../.github/workflows/django-tests.yml) and [four-stage CI/CD workflow](../.github/workflows/marvel-clash-cicd.yml) run against a temporary **MongoDB 7** service, not production Atlas. The November 10 `main` CI runs passed, and the deployed site was manually reported working.

## Outstanding decisions

- [ ] Confirm editorial accuracy and use rights for all character artwork and descriptions.
- [ ] Determine whether a source-backed permanent character identifier is needed beyond MongoDB ObjectIds.
- [ ] Add automated browser end-to-end tests; current unit/API/Node tests are not complete browser E2E coverage.

**History:** [PR #58](https://github.com/satya1130/CSC325-Capstone/pull/58) first implemented Django; [PR #60](https://github.com/satya1130/CSC325-Capstone/pull/60) restored the MVP; [PR #88](https://github.com/satya1130/CSC325-Capstone/pull/88) migrated it to MongoDB. The October SQLite contract and eight-test snapshots are historical.
