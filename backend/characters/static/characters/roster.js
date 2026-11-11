
"use strict";

// Marvel Clash character roster connected to the Django API.
let characters = [];

function normalize(value) {
  return String(value ?? "").normalize("NFKC").trim().toLocaleLowerCase();
}

function filterCharacters(characters, query, powers = "", category = "") {
  const q = normalize(query);
  const powerQuery = normalize(powers);
  const categoryQuery = normalize(category);
  const matches = characters.filter(character =>
    normalize(character.name).includes(q) &&
    normalize(character.powers).includes(powerQuery) &&
    (!categoryQuery || normalize(character.category) === categoryQuery)
  );

  // Prioritize names starting with the search while preserving other partial matches.
  // An empty query retains the original alphabetical roster order.
  if (!q) return matches;
  return matches.sort((a, b) =>
    Number(normalize(b.name).startsWith(q)) -
    Number(normalize(a.name).startsWith(q))
  );
}

// Build a single-select, alphabetical list from abilities actually in the roster.
// Powers are stored as period-separated phrases in the team's character data.
function availablePowers(roster) {
  const distinct = new Map();
  for (const character of roster) {
    for (const item of String(character.powers ?? "").split(/[.;\n]+/)) {
      const power = item.trim();
      if (power && !distinct.has(normalize(power))) {
        distinct.set(normalize(power), power);
      }
    }
  }
  return [...distinct.values()].sort((a, b) =>
    a.localeCompare(b, undefined, { sensitivity: "base" })
  );
}

function populatePowerOptions(doc, roster) {
  const select = doc.getElementById("powers-filter");
  const all = doc.createElement("option");
  all.value = "";
  all.textContent = "All powers and abilities";
  select.replaceChildren(all);
  for (const power of availablePowers(roster)) {
    const option = doc.createElement("option");
    option.value = power;
    option.textContent = power;
    select.append(option);
  }
}

function renderRoster(doc, characters) {
  const roster = doc.getElementById("roster");
  const count = doc.getElementById("count");
  const empty = doc.getElementById("empty");
  const query = doc.getElementById("search").value;
  const powers = doc.getElementById("powers-filter").value;
  const category = doc.getElementById("category-filter").value;

  const matches = filterCharacters(characters, query, powers, category);

  roster.replaceChildren();

  count.textContent = `${matches.length} of ${characters.length} characters shown`;
  empty.hidden = matches.length > 0;

  for (const character of matches) {
    const article = doc.createElement("article");
    article.className = "card";

    // Display each character's checked-in portrait on the roster instead of initials.
    const avatar = doc.createElement("div");
    avatar.className = "card-portrait";
    const imagePath = String(character.image_ref ?? "");
    const fallback = doc.createElement("span");
    fallback.className = "card-portrait-fallback";
    fallback.textContent = "Image unavailable";
    fallback.setAttribute("role", "img");
    fallback.setAttribute("aria-label", `Image unavailable for ${character.name}`);
    avatar.append(fallback);
    if (/^characters\/images\/[a-z0-9-]+\.jpg$/.test(imagePath)) {
      const picture = doc.createElement("img");
      picture.alt = `Portrait of ${character.name}`;
      picture.loading = "lazy";
      picture.decoding = "async";
      picture.onload = () => { fallback.hidden = true; };
      picture.onerror = () => { picture.remove(); fallback.hidden = false; };
      picture.src = `${doc.getElementById("profile").dataset.staticBase || "/static/"}${imagePath}`;
      avatar.append(picture);
    }

    const title = doc.createElement("h2");
    title.textContent = character.name;

    const description = doc.createElement("p");
    description.textContent = character.description;

    const button = doc.createElement("button");
    button.type = "button";
    button.textContent = "View profile";
    button.setAttribute(
      "aria-label",
      `View ${character.name} profile`
    );

    button.addEventListener("click", () => {
      openProfile(doc, character);
    });

    article.append(avatar, title, description, button);
    roster.append(article);
  }
}

function showCharacterImage(doc, character) {
  const dialog = doc.getElementById("profile");
  const image = doc.getElementById("profile-image");
  const placeholder = doc.getElementById("profile-image-placeholder");
  const path = String(character.image_ref ?? "");
  image.hidden = true;
  image.removeAttribute("src");
  placeholder.hidden = false;
  placeholder.textContent = character.name
    ? `No image available for ${character.name}`
    : "Character image unavailable";

  // Only images checked into our project may be loaded.
  if (!/^characters\/images\/[a-z0-9-]+\.jpg$/.test(path)) return;
  image.alt = `Portrait of ${character.name}`;
  image.onload = () => {
    image.hidden = false;
    placeholder.hidden = true;
  };
  image.onerror = () => {
    image.hidden = true;
    placeholder.hidden = false;
  };
  image.src = `${dialog.dataset.staticBase || "/static/"}${path}`;
}

function openProfile(doc, character) {
  doc.getElementById("profile-name").textContent = character.name;
  showCharacterImage(doc, character);

  doc.getElementById("profile-description").textContent =
    character.description;

  // Preserve each power as its own readable, accessible list item.
  const powersList = doc.getElementById("profile-powers");
  powersList.replaceChildren();
  const powers = String(character.powers ?? "")
    .split(/[.;\n]+/)
    .map(power => power.trim())
    .filter(Boolean);
  for (const power of (powers.length ? powers : ["Not available in the source data."])) {
    const item = doc.createElement("li");
    item.textContent = power;
    powersList.append(item);
  }

  doc.getElementById("profile").showModal();
}

async function init(doc) {
  const search = doc.getElementById("search");
  const count = doc.getElementById("count");

  const powersFilter = doc.getElementById("powers-filter");
  const categoryFilter = doc.getElementById("category-filter");
  powersFilter.addEventListener("change", () => renderRoster(doc, characters));
  categoryFilter.addEventListener("change", () => renderRoster(doc, characters));

  search.addEventListener("input", () => {
    renderRoster(doc, characters);
  });

  doc.getElementById("clear").addEventListener("click", () => {
    search.value = "";
    powersFilter.value = "";
    categoryFilter.value = "";
    renderRoster(doc, characters);
    search.focus();
  });

  doc.getElementById("close").addEventListener("click", () => {
    doc.getElementById("profile").close();
  });

  count.textContent = "Loading Marvel characters...";

  try {
    const response = await fetch("/api/characters/");

    if (!response.ok) {
      throw new Error("Failed to load Marvel characters");
    }

    const data = await response.json();

    characters = data.characters;
    populatePowerOptions(doc, characters);
    // Fixed character types are defined in the HTML dropdown.
    // The selected value is applied by renderRoster through filterCharacters.
    renderRoster(doc, characters);

  } catch (error) {
    console.error("Marvel Clash API error:", error);

    count.textContent =
      "Unable to load characters. Please try refreshing.";
  }
}

if (typeof document !== "undefined") {
  init(document);
}
