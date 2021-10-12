// exercise 1
// const colors = ["red", "cyan", "orange"];
// for (let i = 0; i < colors.length; i++) {
//   console.log(`My ${i + 1} choice is ${colors[i]}`);
//     const _suffix = i < 1 ? "st" : "nd";
//   // --------------------------------------------------------------
//   // bonus option 1
//     console.log(`My ${i + 1}${_suffix} choice is ${colors[i]}`);
//   // --------------------------------------------------------------
//   // bonus option 2 with hint
//     const _ending = ["st", "rd", "rd"];
//     console.log(`My ${i + 1}${_ending[i]} choice is ${colors[i]}`);
// }
// --------------------------------------------------------------

// exercise 2
// let people = ["Greg", "Mary", "Devon", "James"];
// people.shift();
// --------------------------------------------------------------
// people[3] = "Jason";
// --------------------------------------------------------------
// people.push("Tomer");
// --------------------------------------------------------------
// for (let i = 0; i < people.length; i++) {
//     console.log (people[i]);
// }
// --------------------------------------------------------------
// for (let i = 0; i < people.length; i++) {
//   console.log(people[i]);
//   if (people[i] == "Jason") {
//     break;
//   }
// }
// --------------------------------------------------------------
// const rmNames = ["Mary", "Tomer"];
// let newList = people;

// for (let rmName of rmNames) {
//   let rmIndex = newList.indexOf(rmName);
//   newList = [...newList.slice(0, rmIndex), ...newList.slice(rmIndex + 1)];
// }
// --------------------------------------------------------------
// console.log(people.indexOf("Mary"));
// --------------------------------------------------------------
// console.log(people.indexOf("Foo"));
// --------------------------------------------------------------
// console.log(people.indexOf("James") === people.length - 1);
// console.log(people);

// exercise 3
// let num = prompt("enter a number");
// while (typeof num === "string" && num !== null && num !== "" && !isNaN(Number(num))) {
//   num = prompt("enter a new number");
// }
// --------------------------------------------------------------

// exercise 4
// const guestList = {
//   randy: "Germany",
//   karla: "France",
//   wendy: "Japan",
//   norman: "England",
//   sam: "Argentina"
// }

// const student = prompt('please enter your name:').toLowerCase();
// const keys = Object.keys(guestList), index = keys.indexOf(student);
// console.log(index === -1 ? `Hi! I'm a guest.` :
//   `Hi! I'm ${keys[index]}, and I'm from ${guestList[student]}.`);
// --------------------------------------------------------------

// exercise 5
// const family = { key1: "val1", key2: "val2", key3: "val3" };
// for (let x in family) console.log(x);
// for (let x in family) console.log(family[x]);
// --------------------------------------------------------------

// exercise 6
// let details = { my: 'name', is: 'Rudolf', the: 'raindeer' };
// let val = '';
// Object.keys(details).forEach((k) => val += `${k} ${details[k]} `);
// console.log(val);
// --------------------------------------------------------------

// exercise 7
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// let secret = names.map(e => e[0]).sort().join('');
// console.log(secret);