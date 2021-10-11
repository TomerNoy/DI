// exercise 1
// const x = 5,
//   y = 5;
// if (x === y) {
//   console.log("values are equal");
// } else {
//   if (x > y) {
//     console.log(`${x} is bigger than ${y}`);
//   } else {
//     console.log(`${y} is bigger than ${x}`);
//   }
// }
//----------------------------------------------------

// exercise 2
// const newDog = "Chihuahua";
// const length = newDog.length;
// console.log(`there're ${length} letters in newDog`);
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());
// if (newDog === "Chihuahua") {
//     console.log('I love Chihuahuas, it’s my favorite dog breed');
// } else {
//     console.log('I dont care, I prefer cats') ;
// }
//----------------------------------------------------

// exercise 3
// const val = Number(prompt("pleas enter a number"));
// if (val % 2 === 0){
//     console.log( "x is an even number");
// } else {
//     console.log( "x is an odd number");
// }
//----------------------------------------------------

// exercise 4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
const length = users.length;

switch (length) {
  case 0:
    console.log("no one is online");
    break;
  case 1:
    console.log(`user ${users[0]} is online`);
    break;
  case 2:
    console.log(`users ${users[0]} and ${users[1]} are online`);
    break;
  default:
    console.log(
      `${users[0]}, ${users[1]} and ${length - 2} more users are online`
    );
  
}
