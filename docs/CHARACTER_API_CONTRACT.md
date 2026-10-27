# Marvel Clash — Proposed Character API Contract

**Issue:** #43  
**Author:** Aryan Grewal  
**Status:** Character list/detail endpoints and 49-character roster **merged into `main` in PR #60**. First `main` GitHub Actions run passed. This is a local Django MVP, not a deployed API.

## Scope and dependencies

This document specifies the current JSON interface on `main` for the Django character backend, CSV importer and roster frontend. PR #60 restored the code after PR #59 reverted the original PR #58. [GitHub CI passed](https://github.com/satya1130/CSC325-Capstone/actions/runs/40442492711); the application is not publicly deployed.

Source character descriptions and powers will come from the team's reviewed `Marvel.xlsx` dataset. Categories and image references must be reviewed during import; neither should be guessed or populated with unlicensed image URLs.

## Character object

| Field | JSON type | Meaning and source |
| --- | --- | --- |
| `id` | string | SQLite auto-increment primary key, exposed as a string; stable within one database only |
| `name` | string | Character name from reviewed source data |
| `description` | string | Description from reviewed source data |
| `powers` | string | Source-backed powers; agree on one representation during implementation |
| `image_ref` | string or null | Reviewed asset reference, or null when no cleared asset exists |
| `category` | string or null | Team-reviewed category; null if unclassified |

**ID stability limitation:** The existing API uses SQLite-generated primary keys. An ID remains fixed while its record stays in the same database, but may change if a database is recreated or records are imported in a different order. Clients must not treat these IDs as globally permanent. A source-backed unique slug/ID and migration are possible follow-up work, requiring team API-contract agreement (Aryan's review of PR #58).

The current implementation stores `powers` as a string. The category taxonomy and licensed image assets are still pending team review. Do not infer battle damage, health, weaknesses, or other canonical facts from this contract.

## Proposed REST routes

### GET /api/characters/

Returns HTTP **200** and a JSON object with `characters`, an array of character objects. An empty catalogue returns `{"characters": []}` with HTTP 200.

Illustrative response **shape only**, not a claim about a verified character row:

```json
{
  "characters": [
    {
      "id": "1",
      "name": "Iron Man",
      "description": "Smart inventor who battles in tough armor.",
      "powers": "Smart mind. Powered suit. The ability to fly. Repulsor blasts. Missile volleys. Energy guns.",
      "image_ref": null,
      "category": null
    }
  ]
}
```

### GET /api/characters/{id}/

Returns HTTP **200** and one character object for a known ID. Unknown IDs return HTTP **404**:

```json
{
  "error": {
    "code": "character_not_found",
    "message": "Character not found."
  }
}
```

Invalid route/method behavior follows Django's routing conventions; unsupported methods should return HTTP **405** if the route matches. No authentication requirement is proposed for read-only character browsing.

## Acceptance and review checklist

- [x] Drafted required fields, list/detail routes, and example JSON.
- [x] Specified empty-list and missing-character behavior.
- [x] Distinguished sourced roster data from invented simulation attributes.
- [ ] Salih/assigned importer confirms mapping to reviewed workbook and image manifest.
- [x] Django roster frontend uses the `characters` response wrapper and agreed property names.
- [x] Implementation uses a string for `powers`; category taxonomy remains unreviewed.
- [x] Backend routes and original eight tests are on `main` following merged PR #60.
- [ ] Decide with the team whether to introduce source-backed persistent character IDs.

**Implemented contract tests:** list returns HTTP 200 and `characters` array; known detail returns fields with expected types; unknown ID returns JSON 404; empty catalog returns an empty array; unreviewed image/category values remain null.

**Implementation status:** List and detail endpoints, CSV importer and full 49-character roster are on `main` following PR #60. The [successful CI run](https://github.com/satya1130/CSC325-Capstone/actions/runs/40442492711) completed migrations, verified 49 imported records and passed the eight existing tests. This does not prove stable cross-database IDs, image/category completeness, public deployment or battle simulation.
