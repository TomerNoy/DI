const Mercury = { name: "Mercury", moons: 0 };
const Venus = { name: "Venus", moons: 0 };
const Earth = { name: "Earth", moons: 1 };
const Mars = { name: "Mars", moons: 2 };
const Jupiter = { name: "Jupiter", moons: 62 };
const Saturn = { name: "Saturn", moons: 33 };
const Uranus = { name: "Uranus", moons: 27 };
const Neptune = { name: "Neptune", moons: 13 };

const planets = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune];

const listPlanets = document.getElementsByClassName("listPlanets")[0];

planets.forEach((e) => {
  const planet = document.createElement("div");

  planet.classList.add("planet", `${e.name}`);
  planet.textContent = e.name;
  planet.style.color = "white";

  listPlanets.appendChild(planet);

  const moons = document.createElement("div");
  moons.classList.add("moons");

  for (let i = 0; i < e.moons; i++) {
    const moon = document.createElement("div");
    moon.classList.add("moon");
    moon.style.left = `${140 + 50 * i}px`;
    moon.style.top = "40px";
    planet.appendChild(moon);
  }
});

document.getElementsByClassName("Mercury")[0].style.backgroundColor = "gray";
document.getElementsByClassName("Venus")[0].style.backgroundColor = "red";
document.getElementsByClassName("Earth")[0].style.backgroundColor = "lightblue";
document.getElementsByClassName("Mars")[0].style.backgroundColor = "brown";
document.getElementsByClassName("Jupiter")[0].style.backgroundColor = "white";
document.getElementsByClassName("Saturn")[0].style.backgroundColor = "yellow";
document.getElementsByClassName("Uranus")[0].style.backgroundColor = "blue";
document.getElementsByClassName("Neptune")[0].style.backgroundColor =
  "darkblue";
