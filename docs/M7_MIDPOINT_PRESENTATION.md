# CSC325 Marvel Clash — Module 7 Midpoint Presentation Package

> **Status:** READY TO RECORD, NOT SUBMITTED. Current code and records verified on October 27, 2026 UTC. This is preparation material, not proof of a submitted video or of teammates' individual participation.

## Deliverables and authoritative links
- Repository: https://github.com/satya1130/CSC325-Capstone
- Primary Figma: https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15
- Updated system context: https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=324-2
- Personas: https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=42-20
- Primary UX journey: https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=42-66
- Proposal: ../Project_Description.md
- Technical/API contract: CHARACTER_API_CONTRACT.md
- Feature-by-feature status: M7_FEATURE_STATUS.md
- Kanban/team and evidence: M7_TEAM_KANBAN_EVIDENCE.md
- CI proof: https://github.com/satya1130/CSC325-Capstone/actions/runs/40442492711

## Run of show: 9 minutes, 20 seconds (practice with a timer)
**All four members must actually participate. Assignments below are a speaking plan—not proof of agreement or participation.**

| Time | Presenter (proposed) | Content and what to display | Rubric items |
| --- | --- | --- | --- |
| 0:00–1:30 | Satya | Problem, audience, product goal, completed vs planned feature scope. Show this repo and updated proposal. | 1, 2 |
| 1:30–3:35 | Salih | Figma: personas, context diagram, home, roster, profile, compare, two-fighter Brawl setup, scripted result and correction path. Show primary journey. | 3 |
| 3:35–5:40 | Aryan | Architecture diagram: Django, SQLite, character data, REST JSON endpoints, JavaScript. Show real API or local site and GitHub Actions passing; distinguish Figma-only features. | 4, 5 |
| 5:40–7:25 | Kyle | Shared Kanban project: backlog, assignees, priority, due dates, stages; show issue and PR evidence for each member. Explain what still needs a Kyle-authored PR if missing. | 6, 7, 8 |
| 7:25–9:20 | Each member briefly / Satya leads | Roles, target dates, Brawl roadmap, risks, testing, next steps. Every speaker confirms own role and one deliverable. | 8, 9, 10 |

**Timing:** target 9:20; stay within 8:00–10:00. Use real screen recordings, not invented team participation. Rehearse and adjust if a demo takes longer.

## Simple narration outline

### Opening — project overview (Satya)
“Marvel Clash is a fan-made character discovery and Brawl project. Marvel fans often have to check different sites to compare abilities and imagine a matchup. Our goal is to give users one place to learn about 49 characters and, eventually, watch explainable fights. At midpoint, the Django roster is implemented, while the full Brawl experience is represented by our Figma prototype.”

### UI and UX demo (Salih)
“Our primary user selects a character from Discover or Roster, reads the powers, compares possible opponents, chooses two fighters, and opens a scripted Brawl result. We designed both desktop and mobile versions. The context diagram shows the user, admin, curated data source, browser state and a future AI Brawl component. AI is a planned feature, not something currently running in Django.”

### Technical architecture and live progress (Aryan)
“The backend uses Python and Django with an SQLite Character model. The CSV importer seeds 49 characters. The API offers GET /api/characters/ and GET /api/characters/{id}/. JavaScript loads that API into the roster UI. We have a successful GitHub Actions run that applies migrations, imports 49 records and executes Django tests. We still need secure accounts, categories/images, favorites, comparisons and actual Brawl computation.”

### Scrum / GitHub workflow (Kyle)
“We track stories through Product Backlog, Ready, In Progress, In Review, and Done. The issue labels are a snapshot, not proof that our separate Projects board is synchronized. Our actual merged contributions include Salih’s project hub and templates (#55), Aryan’s API specification (#56), Satya’s roster (#57), Django (#58), revert (#59), and restoration (#60). We are checking each person's own meaningful feature PR and teammate approval before claiming full compliance.”

### Roadmap and risks (group)
“Next we’ll finish and verify the data/image mapping, add stable character IDs and importer tests, implement fighter selection and a rules-based Brawl, test mobile/keyboard usability, and then explore grounded AI move variation. Our main risks are scope, review discipline, unsupported character claims, artwork rights and unfinished account/security features. We will prioritize a reliable, playable MVP over claiming an AI system we have not built.”

## Live demo checklist
1. Before recording, get the latest `main` branch, create Python virtual environment, install `requirements.txt`, run migrations and `python manage.py import_characters`, then `python manage.py runserver` from `backend/`.
2. Open localhost:8000 and visibly search for two recognizable characters; clear the search, try a misspelled name, open/close a profile.
3. Open localhost:8000/api/characters/ to show live JSON list; show /api/characters/1/ and a missing ID returning 404. Avoid claiming images and categories are complete.
4. Show the real green CI run on GitHub, not a slide that merely says “8 tests passed.”
5. Present Figma persona/context/home/roster/profile/Brawl and journey screens. Test Figma Present mode before recording. Note that login/roles and battles are simulated.
6. Open the *actual GitHub Projects Kanban board* and show priorities, due dates and accountable members. If it is not configured, set it up first; labels alone are not sufficient.
7. Open each member's *own* real feature branch/PR and review history. As of this snapshot Kyle has no authored PR in this repo; he must create a genuine meaningful one. PR #60 has no recorded teammate review before merge.
8. Show finalized plan with milestones, risks and ownership—get teammates to confirm the proposed rows in M7_TEAM_KANBAN_EVIDENCE.md.
9. Each actual team member must speak. Do not create simulated voices or imply participation that did not occur.
10. Upload the actual group recording to YouTube **Unlisted**, verify viewers with the URL, paste URL into Brightspace, and submit repo, Figma, proposal and Kanban links.

## Rubric completion tracker

| # | Requirement | Evidence | Completion |
|---|---|---|---|
| 1 | Project overview | README and intro script | Prepared |
| 2 | Final proposal + feature list/status | Project_Description and M7_FEATURE_STATUS | Prepared; team sign-off needed |
| 3 | Finalized Figma screen/navigation/UX | Figma links above | Designed; live end-to-end check needed |
| 4 | Django/frontend/DB/API architecture | README and contract | Documented |
| 5 | Working progress | Local Django roster + green CI run | Backend evidenced; presenter live demo needed |
| 6 | Shared Kanban w/ owners, priorities, deadlines, statuses | M7_TEAM_KANBAN_EVIDENCE | Plan prepared; **live Projects card verification outstanding** |
| 7 | Each member's branch, PR, reviews, merges | PR list in evidence doc | **Kyle PR missing; PR review process needs evidence** |
| 8 | Team member roles | Team planning matrix | Proposed; each member must confirm |
| 9 | Remaining plan with milestones | Milestone matrix | Proposed; approve dates |
| 10 | Challenges and mitigation | Risks list below | Prepared |
| Submission | 8–10 min, all speak, unlisted YouTube, Brightspace and all links | Recording/upload | **NOT DONE** |

## Risks and mitigations
- **Scope:** Prioritize a deterministic rules-based Brawl before AI animation and dynamic narration.
- **Character facts:** Cross-check 49 imported rows with the workbook; incorrect source names/typos require a reviewed change.
- **Data identity:** SQLite IDs are database-local. Plan a reviewed stable source slug before favorites and persistent history.
- **Security:** Prototype PINs are *not* production authentication. Use Django auth/permissions before public accounts.
- **GitHub workflow:** Require review before merge and CI pass; repository owner/admin must set branch protection.
- **Accessibility:** Test coded site with keyboard and small screens, not just screenshots.
- **Copyright:** Review every Marvel artwork asset and usage/attribution before public deployment.
- **Presentation:** Reserve time for team rehearsal and a backup screen recording; do not present incomplete AI features as live.

## Final sign-off items requiring real teammates
- [ ] Satya confirms technical explanation, demo branch and code status.
- [ ] Aryan confirms backend/API contract and risk language.
- [ ] Kyle confirms assigned frontend/accessibility task and submits own meaningful branch + PR.
- [ ] Salih confirms personas/context diagram and accurate task documentation.
- [ ] The team jointly signs off on roles and proposed dates.
- [ ] Project owner updates GitHub Projects board, protects `main` and verifies checks.
- [ ] Each member speaks; actual 8–10-minute unlisted YouTube link is submitted alongside all required artifacts.
