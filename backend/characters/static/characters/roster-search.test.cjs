"use strict";

const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

// Exercise the same character-search function used by the live Django roster.
const source = fs.readFileSync(path.join(__dirname, "roster.js"), "utf8");
const context = vm.createContext({});
vm.runInContext(source, context);
const filterCharacters = vm.runInContext("filterCharacters", context);

const sample = [
  { name: "Doctor Strange", powers: "Magic", category: "Hero" },
  { name: "Thanos", powers: "Strength", category: "Villain" },
  { name: "Spider-Man", powers: "Web-slinging", category: "Hero" },
  { name: "Scarlet Witch", powers: "Magic", category: "Hero" },
  { name: "Iron Man", powers: "Technology", category: "Hero" },
];
const names = (results) => Array.from(results, character => character.name);

test("US-01: first letters match only names that start with the query", () => {
  assert.deepEqual(names(filterCharacters(sample, "s")), ["Spider-Man", "Scarlet Witch"]);
  assert.deepEqual(names(filterCharacters(sample, "Th")), ["Thanos"]);
});

test("US-01: name prefixes work regardless of case or surrounding spaces", () => {
  assert.deepEqual(names(filterCharacters(sample, "  spID  ")), ["Spider-Man"]);
  assert.deepEqual(names(filterCharacters(sample, "IRON")), ["Iron Man"]);
  assert.deepEqual(names(filterCharacters(sample, "man")), []);
});

test("US-01: empty search preserves original roster order", () => {
  assert.deepEqual(names(filterCharacters(sample, "")), names(sample));
});

test("US-01: unmatched search returns no characters", () => {
  assert.deepEqual(names(filterCharacters(sample, "not-a-character")), []);
});

test("US-03: power and category filters continue to work with prefix search", () => {
  assert.deepEqual(names(filterCharacters(sample, "s", "magic", "hero")), [
    "Scarlet Witch",
  ]);
  assert.deepEqual(names(filterCharacters(sample, "", "", "villain")), ["Thanos"]);
});
