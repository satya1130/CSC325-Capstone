"use strict";

const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

// Load the actual website script without a browser so we can trigger
// onload/onerror deterministically. No network calls or external packages.
const script = fs.readFileSync(path.join(__dirname, "roster.js"), "utf8");
const context = vm.createContext({});
vm.runInContext(script, context);
const showCharacterImage = vm.runInContext("showCharacterImage", context);

function profileFixture() {
  const image = {
    hidden: true,
    alt: "",
    src: "",
    removeAttribute(name) {
      if (name === "src") this.src = "";
    },
  };
  const placeholder = { hidden: true, textContent: "" };
  const dialog = { dataset: { staticBase: "/static/" } };
  const doc = {
    getElementById(id) {
      const elements = {
        "profile": dialog,
        "profile-image": image,
        "profile-image-placeholder": placeholder,
      };
      assert.ok(id in elements, `Unexpected element: ${id}`);
      return elements[id];
    },
  };
  return { doc, image, placeholder };
}

test("US-06: a successfully loaded character image replaces the placeholder", () => {
  const { doc, image, placeholder } = profileFixture();
  showCharacterImage(doc, {
    name: "Iron Man",
    image_ref: "characters/images/iron-man.jpg",
  });

  assert.equal(image.src, "/static/characters/images/iron-man.jpg");
  assert.equal(image.alt, "Portrait of Iron Man");
  assert.equal(image.hidden, true); // hidden until the image finishes loading
  image.onload();
  assert.equal(image.hidden, false);
  assert.equal(placeholder.hidden, true);
});

test("US-06: missing image reference shows a readable placeholder, not a broken image", () => {
  const { doc, image, placeholder } = profileFixture();
  showCharacterImage(doc, { name: "Iron Man", image_ref: null });

  assert.equal(image.hidden, true);
  assert.equal(image.src, "");
  assert.equal(placeholder.hidden, false);
  assert.equal(placeholder.textContent, "No image available for Iron Man");
});

test("US-06: image network/load failure restores the visible placeholder", () => {
  const { doc, image, placeholder } = profileFixture();
  showCharacterImage(doc, {
    name: "Iron Man",
    image_ref: "characters/images/iron-man.jpg",
  });

  image.onerror(); // simulate a 404 or failed image download
  assert.equal(image.hidden, true);
  assert.equal(placeholder.hidden, false);
  assert.equal(placeholder.textContent, "No image available for Iron Man");
});

test("US-06: invalid external image reference is rejected safely", () => {
  const { doc, image, placeholder } = profileFixture();
  showCharacterImage(doc, {
    name: "Iron Man",
    image_ref: "https://example.com/unapproved.jpg",
  });

  assert.equal(image.hidden, true);
  assert.equal(image.src, "");
  assert.equal(placeholder.hidden, false);
});
