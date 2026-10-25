"use strict";
/*
 * Marvel Clash character roster, frontend-only MVP.
 * These sample records are copied from the team's Marvel .xlsx spreadsheet.
 * No Django endpoint or database connection is claimed here.
 * Keep the data source replaceable when the team's Django API is available.
 */
const sampleCharacters = [
  {id:1,name:"Iron Man",description:"Smart inventor who battles in tough armor.",powers:"Smart mind. Powered suit. The ability to fly. Repulsor blasts. Missile volleys. Energy guns."},
  {id:2,name:"Captain America",description:"Super soldier and team leader.",powers:"Great power. Fast movement. Tough body. Quick recovery. Expert fighting skills. Skilled with shields."},
  {id:3,name:"Thor",description:"Thor, the Norse god of thunder.",powers:"Super strength. Lasts a long time. Lightning powers. Controls weather. Can fly. Warrior skills."},
  {id:4,name:"Hulk",description:"Extremely powerful gamma-powered superhero.",powers:"Massive strength, durability, regeneration, super jumps."},
  {id:5,name:"Black Widow",description:"Elite spy and Avenger.",powers:"Martial arts, acrobatics, espionage, weapons expertise."},
  {id:6,name:"Hawkeye",description:"Master archer and Avenger.",powers:"Expert archery, incredible accuracy, trick arrows, combat skills."},
  {id:7,name:"War Machine",description:"Military hero equipped with heavily armed armor.",powers:"Powered armor, flight, strength, guns, missiles, energy weapons."},
  {id:8,name:"Falcon",description:"Highly trained aerial hero using advanced wings.",powers:"Flight, aerial combat, martial arts, advanced wing technology."},
  {id:11,name:"Spider-Man",description:"A hero with spider powers. He can climb and move with ease.",powers:"Hard strength. Fast moves. A kind of spider awareness. He can climb walls. He fires web lines from his gear."},
  {id:12,name:"Doctor Strange",description:"Sorcerer who guards Earth against strange, dangerous forces.",powers:"Magic. Spellcasting. Portals. Teleportation. Shields. Dimensional abilities."},
  {id:16,name:"Black Panther",description:"A Wakandan hero who gets power from the Heart-Shaped Herb.",powers:"Stronger. Faster. Sharper senses. Faster healing too. Trained in martial arts. All while wearing a vibranium suit."},
  {id:35,name:"Jean Grey",description:"A mutant with serious power and a psychic edge.",powers:"She can read thoughts, move objects with its mind, and control energy. She also has Phoenix-type traits."}
];

function normalize(value) {
  return String(value ?? "").normalize("NFKC").trim().toLocaleLowerCase();
}
function filterCharacters(characters, query) {
  const q = normalize(query);
  return characters.filter(character => normalize(character.name).includes(q));
}
function renderRoster(doc, characters) {
  const roster = doc.getElementById("roster");
  const count = doc.getElementById("count");
  const empty = doc.getElementById("empty");
  const query = doc.getElementById("search").value;
  const matches = filterCharacters(characters, query);
  roster.replaceChildren();
  count.textContent = `${matches.length} of ${characters.length} characters shown (source-data preview)`;
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
    button.setAttribute("aria-label", `View ${character.name} profile`);
    button.addEventListener("click", () => openProfile(doc, character));
    article.append(avatar,title,description,button);
    roster.append(article);
  }
}
function openProfile(doc, character) {
  doc.getElementById("profile-name").textContent = character.name;
  doc.getElementById("profile-description").textContent = character.description;
  doc.getElementById("profile-powers").textContent = character.powers || "Not available in the source data.";
  doc.getElementById("profile").showModal();
}
function init(doc) {
  const search = doc.getElementById("search");
  search.addEventListener("input", () => renderRoster(doc, sampleCharacters));
  doc.getElementById("clear").addEventListener("click", () => {
    search.value = "";
    renderRoster(doc, sampleCharacters);
    search.focus();
  });
  doc.getElementById("close").addEventListener("click", () => doc.getElementById("profile").close());
  renderRoster(doc, sampleCharacters);
}
if (typeof document !== "undefined") init(document);
if (typeof module !== "undefined") module.exports = {normalize,filterCharacters,sampleCharacters};
