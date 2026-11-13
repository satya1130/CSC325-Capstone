"use strict";

const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

// Verify the same search function the production website uses.
const source = fs.readFileSync(path.join(__dirname, "roster.js"), "utf8");
const context = vm.createContext({});
vm.runInContext(source, context);
const filterCharacters = vm.runInContext("filterCharacters", context);

const characters = [
  { name: "Doctor Strange", powers: "Magic", category: "Hero" },
  { name: "Thanos", powers: "Strength", category: "Villain" },
  { name: "Spider-Man", powers: "Web-slinging", category: "Hero" },
  { name: "Scarlet Witch", powers: "Magic", category: "Hero" },
  { name: "Iron Man", powers: "Technology", category: "Hero" },
];
const names = results => Array.from(results, item => item.name);

test("US-01: first-letter matches appear before other contains matches", () => {
  assert.deepEqual(names(filterCharacters(characters, "s")), [
    "Spider-Man", "Scarlet Witch", "Doctor Strange", "Thanos"
  ]);
});

test("US-01: partial names still match anywhere, ignoring case and spaces", () => {
  assert.deepEqual(names(filterCharacters(characters, "  pIDer ")), ["Spider-Man"]);
  assert.deepEqual(names(filterCharacters(characters, "MAN")), ["Spider-Man", "Iron Man"]);
});

test("US-01: empty name search preserves original order", () => {
  assert.deepEqual(names(filterCharacters(characters, "")), names(characters));
});

test("US-01: no matching characters gives empty result list", () => {
  assert.deepEqual(names(filterCharacters(characters, "xyz-not-found")), []);
});

test("US-03: powers and character type filters still work", () => {
  assert.deepEqual(names(filterCharacters(characters, "s", "magic", "hero")), [
    "Scarlet Witch", "Doctor Strange"
  ]);
  assert.deepEqual(names(filterCharacters(characters, "", "", "villain")), ["Thanos"]);
});

test("US-01: search never reorders or mutates the original character list", () => {
  const before = names(characters);
  filterCharacters(characters, "s");
  assert.deepEqual(names(characters), before);
});
