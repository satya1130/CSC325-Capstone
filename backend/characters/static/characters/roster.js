
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
  return characters.filter(character =>
    normalize(character.name).includes(q) &&
    normalize(character.powers).includes(powerQuery) &&
    (!categoryQuery || normalize(character.category) === categoryQuery)
  );
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

    const avatar = doc.createElement("div");
    avatar.className = "initial";
    avatar.setAttribute("aria-hidden", "true");
    avatar.textContent = character.name.slice(0, 1);

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

function openProfile(doc, character) {
  doc.getElementById("profile-name").textContent = character.name;

  doc.getElementById("profile-description").textContent =
    character.description;

  // Preserve each power as its own readable, accessible list item.
  const powersList = doc.getElementById("profile-powers");
  powersList.replaceChildren();
  const powers = String(character.powers ?? "")
    .split(/[.;\\n]+/)
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
  powersFilter.addEventListener("input", () => renderRoster(doc, characters));
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
