"use strict";
const byId = id => document.getElementById(id);
let roster = [];
let match = null;
let nextIndex = 0;
const imagePattern = /^characters\/images\/[a-z0-9-]+\.jpg$/;

function errorMessage(message) {
  byId("brawl-error").textContent = message;
  byId("brawl-error").hidden = !message;
}
function choice(id) { return roster.find(c => c.id === byId(id).value); }
function preview() {
  const panel = byId("selection-preview");
  panel.replaceChildren();
  for (const id of ["fighter1", "fighter2"]) {
    const fighter = choice(id);
    if (!fighter) continue;
    const article = document.createElement("article");
    const title = document.createElement("strong");
    title.textContent = fighter.name;
    article.append(title);
    if (imagePattern.test(fighter.image_ref || "")) {
      const img = document.createElement("img");
      img.src = "/static/" + fighter.image_ref;
      img.alt = "Portrait of " + fighter.name;
      article.append(img);
    }
    panel.append(article);
  }
  errorMessage("");
}
function renderHealth(health) {
  const panel = byId("health-bars");
  panel.replaceChildren();
  match.fighters.forEach((fighter, i) => {
    const wrap = document.createElement("div");
    const label = document.createElement("label");
    label.textContent = fighter.name + ": " + health[i] + "/100 HP";
    const progress = document.createElement("progress");
    progress.max = 100;
    progress.value = health[i];
    progress.setAttribute("aria-label", fighter.name + " health");
    wrap.append(label, progress);
    panel.append(wrap);
  });
}
function advanceTurn() {
  if (!match || nextIndex >= match.turns.length) return;
  const turn = match.turns[nextIndex++];
  renderHealth(turn.health);
  const line = document.createElement("li");
  line.textContent = "Turn " + turn.turn + ": " + turn.attacker_name +
    " uses " + turn.move + " on " + turn.defender_name +
    " for " + turn.damage + " damage (" + turn.health_after + " HP left).";
  byId("turn-log").append(line);
  byId("turn-status").textContent = "Turn " + nextIndex + " of " + match.turns.length;
  if (nextIndex === match.turns.length) {
    byId("winner").textContent = "Winner: " + match.winner.name;
    byId("next-turn").hidden = true;
    byId("new-match").hidden = false;
    byId("turn-status").textContent = "Battle complete. " + match.disclaimer;
  }
}
async function loadRoster() {
  const response = await fetch("/api/characters/");
  if (!response.ok) throw new Error("Unable to load characters.");
  const data = await response.json();
  if (!Array.isArray(data.characters)) throw new Error("Invalid roster response.");
  roster = data.characters;
  for (const id of ["fighter1", "fighter2"]) {
    const select = byId(id);
    roster.forEach(fighter => {
      const option = document.createElement("option");
      option.value = fighter.id;
      option.textContent = fighter.name;
      select.append(option);
    });
    select.addEventListener("change", preview);
  }
}
byId("brawl-form").addEventListener("submit", async event => {
  event.preventDefault();
  const first = choice("fighter1"), second = choice("fighter2");
  if (!first || !second) { errorMessage("Choose both fighters."); return; }
  if (first.id === second.id) { errorMessage("Choose two different fighters."); return; }
  const button = byId("start-brawl");
  button.disabled = true;
  errorMessage("");
  try {
    const response = await fetch("/api/brawl/start/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": byId("brawl-form").querySelector("[name=csrfmiddlewaretoken]").value
      },
      body: JSON.stringify({fighter1: first.id, fighter2: second.id})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Unable to start Brawl.");
    if (!Array.isArray(data.turns) || !data.winner || !Array.isArray(data.fighters)) {
      throw new Error("Invalid Brawl response.");
    }
    match = data;
    nextIndex = 0;
    byId("battle").hidden = false;
    byId("turn-log").replaceChildren();
    byId("winner").textContent = "";
    byId("next-turn").hidden = false;
    byId("new-match").hidden = true;
    byId("turn-status").textContent = "Ready. Advance turns to watch the battle.";
    renderHealth([100, 100]);
    byId("battle").scrollIntoView({behavior:"smooth"});
  } catch (error) { errorMessage(error.message); }
  finally { button.disabled = false; }
});
byId("next-turn").addEventListener("click", advanceTurn);
byId("new-match").addEventListener("click", () => {
  match = null;
  byId("battle").hidden = true;
  byId("fighter1").value = "";
  byId("fighter2").value = "";
  preview();
  byId("fighter1").focus();
});
loadRoster().catch(error => errorMessage(error.message));
