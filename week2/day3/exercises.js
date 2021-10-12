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
let val = Number(prompt("please enter a number"));
// console.log (typeof val === number);

while (val < 10) {
  let newVal = Number(prompt("please enter a number"));
  val = newVal;
}
