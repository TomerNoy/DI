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

//###
//### Exercises XP Gold
//###

// let building = {
//   numberLevels: 4,
//   numberOfAptByLevel: {
//     "1": 3,
//     "2": 4,
//     "3": 9,
//     "4": 2,
//   },
//   nameOfTenants: ["Sarah", "Dan", "David"],
//   numberOfRoomsAndRent: {
//     "Sarah": [3, 990],
//     "Dan": [4, 1000],
//     "David": [1, 500],
//   },
// }
// console.log(building['numberLevels']);
// console.log(building['numberOfAptByLevel'][1], building['numberOfAptByLevel'][3]);
// console.log(building['nameOfTenants'][2], building['numberOfRoomsAndRent']['Dan'][0]);
// const saraRent = building['numberOfRoomsAndRent']['Sarah'][1];
// const davidRent = building['numberOfRoomsAndRent']['David'][1];
// console.log(saraRent + davidRent, "vs", building['numberOfRoomsAndRent']['Dan'][1]);
// while (saraRent + davidRent >= building['numberOfRoomsAndRent']['Dan'][1]) {
//   building['numberOfRoomsAndRent']['Dan'][1]++;
// }
// console.log('Dan\'s rent now', building['numberOfRoomsAndRent']['Dan'][1]);
// --------------------------------------------------------------

// const numbers = [123, 8409, 100053, 333333333, 7];
// for (let i = 0; i < numbers.length; i++) {
//   console.log(numbers[i] % 3 === 0);
// }
// --------------------------------------------------------------

// let age = [20, 5, 12, 43, 98, 55];
// let sum = 0;
// for (let i = 0; i < age.length; i++) {
//   sum += age[i];
// }
// console.log(sum);

// let largest = age[0];
// for (let i = 1; i < age.length; i++) {
//   if (age[i] > largest) largest = age[i]
// }
// console.log(largest);
// --------------------------------------------------------------

//###
//### Exercises XP Ninja
//###
// const obj1 = {
//   FullName: 'jack lake', Mass: 75, Height: 170,
//   bmi: function () {
//     return (this.Mass / (this, this.Height * this, this.Height)) * 703
//   }
// };

// const obj2 = {
//   FullName: 'johnny', Mass: 75, Height: 169,
//   bmi: function () {
//     return (this.Mass / (this, this.Height * this, this.Height)) * 703
//   }
// };

// function highestBMI(x, y) {
//   const bmi1 = x.bmi(), bmi2 = y.bmi();
//   if (bmi1 === bmi2) console.log('equal');
//   else console.log(`${bmi1 > bmi2 ? x.FullName : y.FullName} has the highest BMI`);
// }

// highestBMI(obj1, obj2);
// --------------------------------------------------------------

// const gradesList = [49, 100, 55, 67];
// function findAvg(gradesList) {
//     let total = 0;
//     for (n of gradesList) total += n;
//     const avg = total / gradesList.length;
//     console.log(avg);
//     return avg;
// }

// didPass = avg => gradesList.forEach(
//     v => console.log(v >= avg ? 'passed' : 'failed must repeat the course')
// );

// didPass(findAvg(gradesList));
