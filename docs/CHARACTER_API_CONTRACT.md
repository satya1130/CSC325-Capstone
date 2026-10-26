# Marvel Clash — Proposed Character API Contract

**Issue:** #43  
**Author:** Aryan Grewal  
**Status:** Implemented in PR #58 (pending review and merge into `main`).

## Scope and dependencies

This document specifies the JSON interface for the Django character backend, CSV import, and roster frontend implemented on `feature/satya-django-backend` in PR #58. It is running and locally tested, but the PR remains unmerged and the application is not publicly deployed.

Source character descriptions and powers will come from the team's reviewed `Marvel.xlsx` dataset. Categories and image references must be reviewed during import; neither should be guessed or populated with unlicensed image URLs.

## Character object

| Field | JSON type | Meaning and source |
| --- | --- | --- |
| `id` | string | Stable, unique identifier assigned during normalized import |
| `name` | string | Character name from reviewed source data |
| `description` | string | Description from reviewed source data |
| `powers` | string | Source-backed powers; agree on one representation during implementation |
| `image_ref` | string or null | Reviewed asset reference, or null when no cleared asset exists |
| `category` | string or null | Team-reviewed category; null if unclassified |

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
- [x] Backend routes and automated tests implemented in PR #58 (not yet merged).

**Implemented contract tests:** list returns HTTP 200 and `characters` array; known detail returns fields with expected types; unknown ID returns JSON 404; empty catalog returns an empty array; unreviewed image/category values remain null.

**Implementation status:** Character list and detail endpoints, CSV import, and the Django roster are implemented in PR #58. Eight Django tests are defined, including empty-list and null-field checks. These two added tests need to be rerun locally after updating the branch. Deployment, images, and battle simulation are outside this API implementation.
