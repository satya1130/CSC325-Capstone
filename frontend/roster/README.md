# Marvel Clash: Working Character Roster Preview (Satya's Feature)

**User stories:** US-01 Search for a Marvel Character, US-02 Browse Marvel Characters, US-04 View Character Description, US-05 View Powers and Abilities.

This independent, working frontend preview demonstrates searchable character cards and an accessible profile dialog. It is **not a Django integration** and does **not** implement all 49 characters yet.

## Run locally
From the repository root in VS Code:

```powershell
cd frontend/roster
py -m http.server 5500
```

Visit **http://localhost:5500/** in your browser. No npm or Django install is required for this standalone frontend page.

## Tests
With Node.js installed, run:

```powershell
node --test roster.test.cjs
```

The tests cover case-insensitive searching, empty and unmatched searches, and source-data matching.

## Included functionality
- Responsive desktop/mobile roster page inspired by the project's dark Figma theme
- Search character names without reloading
- Clear search and no-results messages
- Profile dialog with descriptions and powers
- Semantic labels, keyboard-focus indicators, live result count and Esc-to-close native dialog
- 12 representative character records copied from the team's supplied **Marvel .xlsx** file

## Scope and next steps
This PR intentionally adds files only inside `frontend/roster/` so it does not conflict with Kyle's Django project setup or Salih's planned database/API work. The team can replace `sampleCharacters` with an API request returning the documented `{characters: [...]}` format once the Django endpoint exists. Character images are deliberately omitted until reviewed assets are available. The source workbook contains **49 characters**, while this proof-of-concept loads **12**. No AI battles, persistence, or authentication is claimed.

**Reviewer:** AryanGrewal05. Please inspect the source, try a valid name and a nonsense query, open/close a profile and verify responsive behavior before approving.
