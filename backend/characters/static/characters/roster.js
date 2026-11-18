
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


// US-10: Request an AI summary for the character currently in the profile.
let activeCharacterId = null;
let summaryRequest = null;
let recommendRequest = null;
let askRequest = null;

function resetSummary(doc, character) {
  if (summaryRequest) {
    summaryRequest.abort();
    summaryRequest = null;
  }
  if (recommendRequest) { recommendRequest.abort(); recommendRequest = null; }
  if (askRequest) { askRequest.abort(); askRequest = null; }
  doc.getElementById("ask-ai-question").value = "";
  doc.getElementById("ask-ai-answer").textContent = "Ask a question based on this character’s profile.";
  doc.getElementById("ask-ai-source").hidden = true;
  doc.getElementById("ask-ai-submit").disabled = !character;
  activeCharacterId = character ? String(character.id ?? "") : null;
  doc.getElementById("generate-recommendations").disabled = !activeCharacterId;
  doc.getElementById("recommend-list").replaceChildren();
  doc.getElementById("recommend-reason").textContent = "Find characters with related abilities.";
  doc.getElementById("recommend-source").hidden = true;
  const button = doc.getElementById("generate-summary");
  const text = doc.getElementById("ai-summary-text");
  const source = doc.getElementById("ai-summary-source");
  button.disabled = !activeCharacterId;
  button.textContent = "Generate AI Summary";
  text.textContent = activeCharacterId
    ? "Select Generate AI Summary to see a short character overview."
    : "Summary unavailable for this character.";
  source.hidden = true;
  source.textContent = "";
}

async function loadCharacterSummary(doc) {
  const characterId = activeCharacterId;
  if (!characterId || summaryRequest) return;

  const button = doc.getElementById("generate-summary");
  const text = doc.getElementById("ai-summary-text");
  const source = doc.getElementById("ai-summary-source");
  const controller = new AbortController();
  summaryRequest = controller;
  button.disabled = true;
  button.textContent = "Generating...";
  text.textContent = "Generating character summary...";
  source.hidden = true;
  source.textContent = "";

  try {
    const response = await fetch(
      `/api/characters/${encodeURIComponent(characterId)}/summary/`,
      { signal: controller.signal }
    );
    if (!response.ok) throw new Error(`Summary request failed: ${response.status}`);
    const result = await response.json();
    if (controller.signal.aborted || activeCharacterId !== characterId) return;
    if (result.character_id !== characterId ||
        typeof result.summary !== "string" || !result.summary.trim()) {
      throw new Error("Invalid summary response");
    }
    text.textContent = result.summary;
    source.textContent = result.source === "openai"
      ? "AI-generated summary. Check character details for accuracy."
      : "Fallback summary based on the character's stored information.";
    source.hidden = false;
  } catch (error) {
    if (controller.signal.aborted || activeCharacterId !== characterId) return;
    console.error("Marvel Clash summary error:", error);
    text.textContent = "Unable to generate a summary right now. Please try again.";
  } finally {
    if (summaryRequest === controller) {
      summaryRequest = null;
      button.disabled = false;
      button.textContent = "Generate AI Summary";
    }
  }
}

async function loadRecommendations(doc) {
  const id = activeCharacterId;
  if (!id || recommendRequest) return;
  const controller = new AbortController();
  recommendRequest = controller;
  const button = doc.getElementById("generate-recommendations");
  const list = doc.getElementById("recommend-list");
  const reason = doc.getElementById("recommend-reason");
  const source = doc.getElementById("recommend-source");
  button.disabled = true;
  reason.textContent = "Finding recommendations...";
  list.replaceChildren();
  source.hidden = true;
  try {
    const response = await fetch(`/api/characters/${encodeURIComponent(id)}/recommendations/`, {signal: controller.signal});
    if (!response.ok) throw new Error("Recommendation request failed");
    const result = await response.json();
    if (controller.signal.aborted || activeCharacterId !== id) return;
    if (result.character_id !== id || !Array.isArray(result.recommendations)) throw new Error("Invalid response");
    reason.textContent = result.reason || "Suggested characters:";
    for (const item of result.recommendations) {
      const li = doc.createElement("li");
      const link = doc.createElement("button");
      link.type = "button";
      link.textContent = item.name;
      link.addEventListener("click", () => {
        const match = characters.find(c => String(c.id) === String(item.id));
        if (match) openProfile(doc, match);
      });
      li.append(link);
      list.append(li);
    }
    source.textContent = result.source === "openai" ? "AI-assisted suggestions based on stored character data." : "Offline recommendations based on stored character data.";
    source.hidden = false;
  } catch (error) {
    if (!controller.signal.aborted && activeCharacterId === id) reason.textContent = "Recommendations unavailable. Please try again.";
  } finally {
    if (recommendRequest === controller) {
      recommendRequest = null;
      button.disabled = false;
    }
  }
}

async function askCharacterQuestion(doc) {
  const id = activeCharacterId;
  const question = doc.getElementById("ask-ai-question").value.trim();
  if (!id || !question || question.length > 300 || askRequest) return;
  const controller = new AbortController();
  askRequest = controller;
  const button = doc.getElementById("ask-ai-submit");
  const answer = doc.getElementById("ask-ai-answer");
  const source = doc.getElementById("ask-ai-source");
  button.disabled = true;
  answer.textContent = "Thinking...";
  source.hidden = true;
  try {
    const token = doc.querySelector("#ask-ai-form input[name=csrfmiddlewaretoken]").value;
    const response = await fetch(`/api/characters/${encodeURIComponent(id)}/ask/`, {
      method: "POST",
      headers: {"Content-Type": "application/json", "X-CSRFToken": token},
      body: JSON.stringify({question}),
      signal: controller.signal,
    });
    if (!response.ok) throw new Error("Question request failed");
    const result = await response.json();
    if (controller.signal.aborted || activeCharacterId !== id) return;
    if (result.character_id !== id || typeof result.answer !== "string" || !result.answer.trim()) {
      throw new Error("Invalid answer");
    }
    answer.textContent = result.answer;
    source.textContent = result.source === "openai"
      ? "AI answer based on stored character information. Verify important details."
      : "Safe offline answer based on stored character information.";
    source.hidden = false;
  } catch (error) {
    if (!controller.signal.aborted && activeCharacterId === id) {
      answer.textContent = "Unable to answer right now. Please try again.";
    }
  } finally {
    if (askRequest === controller) {
      askRequest = null;
      button.disabled = false;
    }
  }
}

function openProfile(doc, character) {
  resetSummary(doc, character);
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
  doc.getElementById("profile").addEventListener("close", () => {
    resetSummary(doc, null);
  });
  doc.getElementById("ask-ai-form").addEventListener("submit", event => {
    event.preventDefault();
    askCharacterQuestion(doc);
  });
  doc.getElementById("generate-recommendations").addEventListener("click", () => loadRecommendations(doc));
  doc.getElementById("generate-summary").addEventListener("click", () => {
    loadCharacterSummary(doc);
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
