"use strict";

const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const script = fs.readFileSync(path.join(__dirname, "roster.js"), "utf8");
const context = vm.createContext({});
vm.runInContext(script, context);
const availablePowers = vm.runInContext("availablePowers", context);
const populatePowerOptions = vm.runInContext("populatePowerOptions", context);
const filterCharacters = vm.runInContext("filterCharacters", context);

const roster = [
  { name: "Iron Man", category: "Hero", powers: "Powered armor. Flight. Repulsor blasts." },
  { name: "Thor", category: "Hero", powers: "Flight. Lightning control. Superhuman strength." },
  { name: "Doctor Strange", category: "Hero", powers: "Magic. Teleportation." },
  { name: "Loki", category: "Villain", powers: "Magic. Illusions." },
  { name: "Unknown", category: "Antihero", powers: null },
];
const names = items => Array.from(items, item => item.name);

test("US-03: options derive from actual roster abilities, sorted alphabetically", () => {
  assert.deepEqual(Array.from(availablePowers(roster)), [
    "Flight", "Illusions", "Lightning control", "Magic", "Powered armor",
    "Repulsor blasts", "Superhuman strength", "Teleportation",
  ]);
});

test("US-03: duplicate abilities are listed only once", () => {
  const terms = Array.from(availablePowers(roster));
  assert.equal(terms.filter(x => x === "Flight").length, 1);
  assert.equal(terms.filter(x => x === "Magic").length, 1);
});

test("US-03: native select includes an All option and one option per ability", () => {
  const select = {
    children: [],
    replaceChildren(...items) { this.children = items; },
    append(item) { this.children.push(item); },
  };
  const doc = {
    getElementById(id) {
      assert.equal(id, "powers-filter");
      return select;
    },
    createElement(tag) {
      assert.equal(tag, "option");
      return { value: "", textContent: "" };
    },
  };
  populatePowerOptions(doc, roster);
  assert.equal(select.children[0].value, "");
  assert.equal(select.children[0].textContent, "All powers and abilities");
  assert.equal(select.children.length, 9);
  assert.equal(select.children[1].value, "Flight");
  assert.equal(select.children.at(-1).value, "Teleportation");
});

test("US-03: selection filters characters with that ability", () => {
  assert.deepEqual(names(filterCharacters(roster, "", "Flight")), ["Iron Man", "Thor"]);
  assert.deepEqual(names(filterCharacters(roster, "", "Magic")), ["Doctor Strange", "Loki"]);
});

test("US-03: power selection combines with name and character-type filters", () => {
  assert.deepEqual(names(filterCharacters(roster, "Lo", "Magic", "Villain")), ["Loki"]);
  assert.deepEqual(names(filterCharacters(roster, "", "Magic", "Hero")), ["Doctor Strange"]);
});

test("US-03: clearing power selection restores all matching characters", () => {
  assert.equal(filterCharacters(roster, "", "").length, roster.length);
  assert.deepEqual(names(filterCharacters(roster, "", "", "Hero")), [
    "Iron Man", "Thor", "Doctor Strange",
  ]);
});

test("US-03: missing powers do not generate blank dropdown items", () => {
  assert.ok(!Array.from(availablePowers(roster)).some(x => !x.trim()));
  assert.deepEqual(names(filterCharacters(roster, "", "Magic", "Antihero")), []);
});
