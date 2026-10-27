
"use strict";

// Marvel Clash character roster connected to the Django API.
let characters = [];

function normalize(value) {
  return String(value ?? "").normalize("NFKC").trim().toLocaleLowerCase();
}

function filterCharacters(characters, query) {
  const q = normalize(query);

  return characters.filter(character =>
    normalize(character.name).includes(q)
  );
}

function renderRoster(doc, characters) {
  const roster = doc.getElementById("roster");
  const count = doc.getElementById("count");
  const empty = doc.getElementById("empty");
  const query = doc.getElementById("search").value;

  const matches = filterCharacters(characters, query);

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

  doc.getElementById("profile-powers").textContent =
    character.powers || "Not available in the source data.";

  doc.getElementById("profile").showModal();
}

async function init(doc) {
  const search = doc.getElementById("search");
  const count = doc.getElementById("count");

  search.addEventListener("input", () => {
    renderRoster(doc, characters);
  });

  doc.getElementById("clear").addEventListener("click", () => {
    search.value = "";
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
