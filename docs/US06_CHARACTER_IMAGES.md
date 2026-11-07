# US-06 — Character portrait assets

The team provided a 50-page PDF exported from Kyle's slide deck. Pages 2–50 each correspond to one of the 49 characters in `backend/characters/data/marvel_characters.csv`. A primary embedded image from each character page was extracted and resized to a JPEG. Where a page contains multiple images, the first embedded picture was selected.

**Asset upload required before merging:** Put the 49 JPEGs into:

`backend/characters/static/characters/images/`

Names follow the character names in the CSV with hyphens, for example `iron-man.jpg`, `spider-man.jpg`, `ant-man.jpg`, `the-mighty-thor.jpg`, `valkryie.jpg` (matching the current CSV spelling), and `dark-phoenix.jpg`.

The Django importer sets `image_ref` to `characters/images/<filename>.jpg` when a corresponding image exists. The API includes that value; profile JavaScript resolves it beneath the Django static prefix. If the reference is absent or the image cannot be loaded, a readable image placeholder appears. Portraits resize responsively without covering character descriptions.

After uploading assets on the US-06 feature branch:
1. Confirm all **49 JPG** files are visible in the GitHub branch at the path above.
2. Verify GitHub Actions **Test** is green on the latest commit.
3. Open the site and verify several profiles (Iron Man, Ant-Man, Hela, Dark Phoenix) plus the fallback behavior in a test environment.
4. Obtain a formal teammate approval and merge this PR.
5. Verify the Render deployment rebuilt static assets and re-imported character records.

The slide images appear to be Marvel film stills. They were supplied by the team for this unofficial student prototype; do not imply that Marvel licenses the images for commercial use.
