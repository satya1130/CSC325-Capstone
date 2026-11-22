"use strict";
const byId = id => document.getElementById(id);
let roster = [];
let match = null;
let nextIndex = 0;
let animating = false;
const imagePattern = /^characters\/images\/[a-z0-9-]+\.jpg$/;
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
function errorMessage(message) {
  byId("brawl-error").textContent = message;
  byId("brawl-error").hidden = !message;
}
function choice(id) { return roster.find(c => c.id === byId(id).value); }
function portrait(fighter) {
  if (!fighter || !imagePattern.test(fighter.image_ref || "")) return null;
  const img = document.createElement("img");
  img.src = "/static/" + fighter.image_ref;
  img.alt = "Portrait of " + fighter.name;
  return img;
}
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
    const img = portrait(fighter);
    if (img) article.append(img);
    panel.append(article);
  }
  errorMessage("");
}
function setupStage() {
  [1, 2].forEach((number, index) => {
    const fighter = roster.find(c => c.id === match.fighters[index].id);
    byId("stage-name-" + number).textContent = match.fighters[index].name;
    const sprite = byId("sprite-" + number);
    sprite.replaceChildren();
    const img = portrait(fighter);
    if (img) sprite.append(img);
    else sprite.textContent = match.fighters[index].name;
  });
  byId("stage-impact").textContent = "";
  byId("stage-announcement").textContent = "READY? FIGHT!";
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
function showTurn(turn) {
  renderHealth(turn.health);
  const line = document.createElement("li");
  line.textContent = "Turn " + turn.turn + ": " + turn.attacker_name +
    " uses " + turn.move + " on " + turn.defender_name +
    " for " + turn.damage + " damage (" + turn.health_after + " HP left).";
  byId("turn-log").append(line);
  byId("turn-status").textContent = "Turn " + nextIndex + " of " + match.turns.length;
  if (nextIndex === match.turns.length) {
    byId("winner").textContent = "Winner: " + match.winner.name;
    byId("stage-announcement").textContent = match.winner.name + " WINS!";
    byId("next-turn").hidden = true;
    byId("new-match").hidden = false;
    byId("turn-status").textContent = "Battle complete. " + match.disclaimer;
  }
}
function animateTurn(turn) {
  const attackerNumber = match.fighters[0].id === turn.attacker_id ? 1 : 2;
  const defenderNumber = attackerNumber === 1 ? 2 : 1;
  const attacker = byId("stage-fighter-" + attackerNumber);
  const defender = byId("stage-fighter-" + defenderNumber);
  const impact = byId("stage-impact");
  const stage = byId("arcade-stage");
  const next = byId("next-turn");
  animating = true;
  next.disabled = true;
  byId("stage-announcement").textContent = turn.attacker_name + " attacks!";
  attacker.classList.remove("attacking");
  defender.classList.remove("hit");
  impact.classList.remove("pop");
  void attacker.offsetWidth;
  attacker.classList.add("attacking");
  const duration = reduceMotion.matches ? 0 : 450;
  window.setTimeout(() => {
    defender.classList.add("hit");
    stage.classList.add("impact-flash");
    impact.textContent = "-" + turn.damage;
    impact.classList.add("pop");
    showTurn(turn);
    window.setTimeout(() => {
      attacker.classList.remove("attacking");
      defender.classList.remove("hit");
      impact.classList.remove("pop");
      stage.classList.remove("impact-flash");
      impact.textContent = "";
      animating = false;
      next.disabled = false;
      if (nextIndex !== match.turns.length) byId("stage-announcement").textContent = "NEXT ROUND";
    }, reduceMotion.matches ? 0 : 700);
  }, duration);
}
function advanceTurn() {
  if (!match || animating || nextIndex >= match.turns.length) return;
  const turn = match.turns[nextIndex++];
  animateTurn(turn);
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
    if (!Array.isArray(data.turns) || !data.winner || !Array.isArray(data.fighters) || data.fighters.length !== 2) {
      throw new Error("Invalid Brawl response.");
    }
    match = data;
    nextIndex = 0;
    byId("battle").hidden = false;
    byId("turn-log").replaceChildren();
    byId("winner").textContent = "";
    byId("next-turn").hidden = false;
    byId("next-turn").disabled = false;
    byId("new-match").hidden = true;
    byId("turn-status").textContent = "Ready. Advance turns to watch the battle.";
    renderHealth([100, 100]);
    setupStage();
    byId("battle").scrollIntoView({behavior: reduceMotion.matches ? "auto" : "smooth"});
  } catch (error) { errorMessage(error.message); }
  finally { button.disabled = false; }
});
byId("next-turn").addEventListener("click", advanceTurn);
byId("new-match").addEventListener("click", () => {
  if (animating) return;
  match = null;
  byId("battle").hidden = true;
  byId("fighter1").value = "";
  byId("fighter2").value = "";
  preview();
  byId("fighter1").focus();
});
loadRoster().catch(error => errorMessage(error.message));
