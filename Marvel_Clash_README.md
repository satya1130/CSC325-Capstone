> **Documentation note:** This file preserves an earlier group-created version of the Marvel Clash prototype documentation. For the current CSC 325 assignment submission, please refer to the main [README.md](README.md), which contains the current Product Goal, primary Figma design, architecture, test plan, and submission links.

---


# Marvel Clash

Marvel Clash is a fan-made Marvel character exploration and brawler prototype built in Figma (CSC 325). Users can explore 49 character profiles, learn abilities and powers, compare characters, choose two fighters, and view an explained simulated matchup.

**Product Goal:** Make Marvel characters easy to explore and turn character comparisons into entertaining, understandable Brawls. A future AI-powered Brawl feature is planned to use reviewed powers, moves, abilities and counters to generate varied fights, move-by-move explanations, health changes, and optional character animations. The current prototype is not a live AI service. Results are game simulations, not official Marvel canon.

## Architecture

Marvel Clash is organized as a single system with clearly separated layers. The current submission is a client-side prototype, and the planned production architecture is shown alongside it.

**Current prototype (implemented)**

- **Presentation layer (client):** Figma screens for desktop and mobile, in dark and light themes. The screens cover Discover/Home, Roster, character Profile, Compare, fighter selection, Brawl and battle details, and winner/result. Clicking through the primary journey is wired in the new file, on desktop and mobile.
- **Data layer:** A curated character dataset of 49 profiles containing powers, abilities, and related attributes. The data is static and reviewed by the team before use.
- **Session layer:** Browser/device session state tracks the current persona (Guest, Aryan, MarvelFan, or Admin), selected fighters, and the current step in the Brawl flow.
- **Simulation layer (illustrative):** Current Brawl fights are pre-authored example sequences. They show health changes, moves, and commentary, but they are not computed by an engine.

**Planned production architecture (not yet implemented)**

- **Client:** A web front end that renders the same screens and connects to the data and session layers.
- **Character service:** Serves verified character content from a persistent store.
- **Accounts:** Secure, real-user sign-in with persistent storage. The prototype uses a password-free MarvelFan login for demonstration only.
- **AI Brawl service:** A battle engine grounded in reviewed powers, moves, counters, and weaknesses. It would track health, damage, turns, and moves, then generate narration and optional animations, with safeguards for generated content.

External actors are Aryan, MarvelFan, the Admin (Salih), the curated character dataset, browser/device session state, and the planned AI Brawl service.

## Prototype

**Figma public link (project guide file):** https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15

**Figma file built for this submission:** https://www.figma.com/design/rjq4hv5d0kOMdmc7z41K5j

*Note: the project guide file is view-only for our account, so the screens were rebuilt in the new file above.*

**Context diagram:** https://www.figma.com/design/Ofvhw6kOEZxiq2Vz9ECJ15?node-id=324-2

### Personas

**Primary: Aryan and MarvelFan**

- **Aryan** is a user who is not a Marvel fan but still wants to log in and use the site. Aryan has the same access as a normal user or MarvelFan.
- **MarvelFan** is a fan persona who can log in without a password as a registered guest rather than an anonymous guest.
- Both roles can browse and learn about Marvel characters, inspect abilities, choose fighters, watch simulated fights, and understand the results.

**Secondary: Guest and Admin (Salih)**

- **Guest** is anyone who opens the site without an account or without signing in. Guests can access basic browsing, and advanced options unlock after signing up or logging in.
- **Admin (Salih)** has access to everything normal users can use, plus hidden menus and tabs for experimentation and testing.

### Context Diagram

Marvel Clash is a single system. The context diagram shows the external actors (Aryan, MarvelFan, the Admin, the curated character dataset, browser/device session state, and the planned AI Brawl service) and labels the data flowing between them. The planned AI connection is marked as future work.

### UI Screens

Key screens in the new Figma file:

- Personas and context diagram frames
- Desktop (dark theme): Discover/Home, Roster, Character Profile, Compare, Favorites, Fighter Selection, Brawl battle, Winner and explanation
- Light theme: Discover/Home, Roster, Character Profile, Compare, Favorites, Fighter Selection, Brawl battle, and Winner (desktop); Roster, Character Profile, and Brawl battle (mobile)
- Access demonstrations: Guest (signed out), Member (MarvelFan or Aryan), and Admin (Salih), showing which features each role can use
- Mobile (dark theme): Discover, Roster, Character Profile, Compare, Favorites, and Brawl battle
- UX flow: the primary MarvelFan journey as numbered steps

Clicking through the primary journey works in the new file: Discover → Roster → Character Profile → Compare → Fighter Selection → Brawl → Winner, with replay and new-fighter options on the result screen. The mobile flow Discover → Roster → Profile → Compare → Brawl is also linked.

### UX Flow (Primary User Journey)

1. Open the Figma design and log in as MarvelFan (no password required).
2. Click Discover and Roster.
3. Read character profiles and compare fighters.
4. Select and assign two fighters in Brawl.
5. Confirm and start the matchup.
6. Follow health bars, moves, and commentary.
7. Read the winner and explanation, then replay or choose new characters.
8. If a selection is missing, return to fighter selection.

### Limitations

The Figma prototype demonstrates the user experience. Live login, a persistent character database, and the AI Brawl engine are future development goals and are not working integrations in the current prototype.

## Test Plan Overview

The test plan covers four categories, each matched to a layer of the architecture.

**1. Unit testing (data layer)**

- Verify that each of the 49 character profiles contains the required fields (name, powers, abilities, and related attributes).
- Verify that comparison logic returns the correct attributes for any two characters.
- Verify that the fighter-selection rule accepts exactly two distinct characters.

**2. Integration testing (screen and session flow)**

- Verify that navigation links connect Discover, Roster, Profile, Compare, Favorites, and Brawl as designed.
- Verify that selecting a fighter from Roster or Profile carries the selection into Brawl.
- Verify that the session retains the current persona and selected fighters when moving between screens.
- Verify that a missing selection routes the user back to fighter selection.

**3. System testing (end-to-end user journeys)**

- Run the full primary user journey (steps 1 to 8 above) as MarvelFan on desktop and mobile.
- Run the Aryan journey to confirm it matches MarvelFan's access.
- Run the Guest journey to confirm that restricted options are locked and that signing up or logging in unlocks them.
- Run the Admin journey to confirm that hidden menus appear only for the admin persona.

**4. Usability testing (user-centered validation)**

- Observe a non-fan user (Aryan persona) completing the Brawl flow without guidance and record confusion points.
- Test clickable areas and touch targets on mobile screens to catch overlapping hitboxes and mis-taps.
- Confirm that results explain why a winner was chosen in language a non-fan can follow.

**Future testing (after deployment)**

- Automated browser tests for the deployed site.
- Validation that AI-generated Brawl narration stays consistent with the reviewed character data.
- Safety review of generated content.

## Project Notes

**AI use statement:** ChatGPT (OpenAI) was used for help with planning the context diagram, prototype interactions, UX journey, and written explanation. Figma was used for the clickable screens, UI design, and diagram. AI suggestions that overstated Figma's account capabilities or implied that the live AI Brawl already existed were rejected or corrected.

**Next steps for a deployed version:** secure real-user accounts, persistent storage, verified character content, a running battle engine with AI grounding and safeguards, animations, and full browser testing.

**Video guide:** https://youtu.be/8gb0xLyrx2o

## AI Tool Use

### (1) AI tools used and what each was used for

- **ChatGPT (OpenAI):** Planning the context diagram, prototype interactions, UX journey, and written explanation for the project guide.
- **Claude (Anthropic, Claude Haiku 5.5):** Drafting this README (Architecture, Prototype, and Test Plan Overview sections) and building the Figma file for the prototype through the Figma tools: persona cards, the context diagram, desktop and mobile screens, and the UX flow frame.
- **Figma:** Clickable screens, UI design, and diagram. No Figma AI image generation was used.

### (2) AI outputs accepted, edited, or rejected

**ChatGPT (from the project guide):**

- **Accepted:** Layout suggestions, the clear user journey, and the main persona structure.
- **Edited:** The context diagram, to make the information flows easier to follow and to add the project admin, character dataset, browser state, and future AI Brawl service.
- **Revised:** The login screens and clickable areas, after testing showed confusing interactions.
- **Rejected or corrected:** Outputs that overstated Figma's account capabilities or implied the live AI Brawl already existed. Final claims were kept separate from future development.
- **Missed by the tool:** Overlapping hitboxes and mobile interactions, which were caught in testing.

**Claude:**

- **Accepted:** The README structure and the four test categories (unit, integration, system, usability), based on the project guide's product goal and user journey.
- **Edited during the Figma build:** Removed stray placeholder layers left from an early build step, and centered the winner headline on the result screen after a visual check showed it was off-center.
- **Corrected:** The first draft of this README claimed Favorites screens, guest/member/admin screens, light theme, and working prototype links that the first Figma build did not contain. Those screens and links were added afterward, and the README now matches the file.
- **Not accepted:** Claude could not edit the project guide's Figma file (view-only access), so it built a new file instead. The new file is linked above.
