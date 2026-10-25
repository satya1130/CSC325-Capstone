# Marvel Clash — Proposed Character API Contract

**Issue:** #43  
**Author:** Aryan Grewal  
**Status:** Proposed for teammate review; not an implemented endpoint.

## Scope and dependencies

This document specifies the JSON interface between the planned Django backend (#28), future character data import (#29), and frontend integration (#30). It does **not** claim the Django backend, database, API, or image hosting currently works.

Source character descriptions and powers will come from the team's reviewed `Marvel.xlsx` dataset. Categories and image references must be reviewed during import; neither should be guessed or populated with unlicensed image URLs.

## Character object

| Field | JSON type | Meaning and source |
| --- | --- | --- |
| `id` | string | Stable, unique identifier assigned during normalized import |
| `name` | string | Character name from reviewed source data |
| `description` | string | Description from reviewed source data |
| `powers` | string or array of strings | Source-backed powers; agree on one representation during implementation |
| `image_ref` | string or null | Reviewed asset reference, or null when no cleared asset exists |
| `category` | string or null | Team-reviewed category; null if unclassified |

The two pending implementation decisions (`powers` format and category taxonomy) must be resolved before coding. Do not infer battle damage, health, weaknesses, or other canonical facts from this contract.

## Proposed REST routes

### GET /api/characters/

Returns HTTP **200** and a JSON object with `characters`, an array of character objects. An empty catalogue returns `{"characters": []}` with HTTP 200.

Illustrative response **shape only**, not a claim about a verified character row:

```json
{
  "characters": [
    {
      "id": "source-reviewed-id",
      "name": "Source-reviewed character name",
      "description": "Description from reviewed source data",
      "powers": ["Reviewed ability"],
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
- [ ] Satya/frontend integrator confirms response wrapper and property names.
- [ ] Team resolves `powers` representation and category vocabulary.
- [ ] Backend implements routes and automated tests in a separate PR.

**Suggested contract tests once implemented:** list returns HTTP 200 and `characters` array; known detail returns fields with expected types; unknown ID returns JSON 404; empty catalog returns an empty array; unreviewed image/category values remain null.

This proposal is ready for review, **not** a completed API implementation.
