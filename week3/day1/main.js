// For each of the questions, find 2 WAYS of accessing :
// 1. The div DOM node?
// 2. The ul DOM node?
// 3. The second li (with Pete)?

// const div = document.body.firstElementChild;
// const ul = document.body.firstElementChild.nextElementSibling;
// const li = document.body.firstElementChild.nextElementSibling.firstElementChild;

// const div2 = document.body.children[0];
// const ul2 = document.body.children[1];
// const li2 = document.body.children[1].children[0];

// For each of the questions, find 2 WAYS to access :
// 1. The div node
// 2. The ul nodes, and render all of it's children one by one
// 3. The first li of each ul

// const d1 = document.getElementById("container");
// d1.style.backgroundColor = "cyan";
// const d11 = document.getElementsByTagName("div");

// // console.log(d1);

// const d2 = d1.children;
// const d21 = document.querySelectorAll(".list li");

// const d3 = d1.children.array.forEach((e) => e.children[0]);

// const d3 = document.querySelectorAll(".list > :first-child");
// console.log(d3);

// 1. Create a function that adds the name of each students to
// a paragraph

// 2. each paragraph needs to be background yellow, font-size 25px
// 3. Add the 3 paragraph to the div already on the page

const names = ["John", "Lola", "Tom"];
const div = document.getElementById("container");

for (n of names) add(n);

function add(name) {
  let para = document.createElement("p");
  let node = document.createTextNode(`${name} ...some text`);
  para.appendChild(node);

  para.style.backgroundColor = "yellow";
  para.style.fontSize = "25px";

  div.appendChild(para);
}
