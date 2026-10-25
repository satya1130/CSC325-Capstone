const {test} = require("node:test");
const assert = require("node:assert/strict");
const {normalize,filterCharacters,sampleCharacters} = require("./roster.js");
test("normalization trims and ignores case", () => assert.equal(normalize("  THOR  "), "thor"));
test("empty search shows the whole preview", () => assert.equal(filterCharacters(sampleCharacters,"").length,sampleCharacters.length));
test("partial case-insensitive names work", () => assert.deepEqual(filterCharacters(sampleCharacters,"spIDer").map(x=>x.name),["Spider-Man"]));
test("unknown character returns no matches", () => assert.deepEqual(filterCharacters(sampleCharacters,"not-a-character"),[]));
test("results preserve actual character source data", () => assert.equal(filterCharacters(sampleCharacters,"thor")[0].id,3));
