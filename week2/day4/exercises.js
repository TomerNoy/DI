// exercise 1
// const infoAboutMe = () => console.log(`tom, 41, i like popping bubble wraps`);
// infoAboutMe();
// ----------------------------------------------------------------------
// const infoAboutPerson = (personName, personAge, personFavoriteColor) =>
//     console.log(`“You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}”`);
// infoAboutPerson("David", 45, "blue");
// infoAboutPerson("Josh", 12, "yellow");
// ----------------------------------------------------------------------
// const infoAboutPerson = (personName, personAge, personFavoriteColor, personHobbies) => {
//     console.log(`“You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}”`);
//     console.log(`your hobbies are:`);
//     personHobbies.forEach(e => console.log(e))
// }
// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])
// ----------------------------------------------------------------------

// exercise 2
// const age = Number(prompt(`whats your age?`));
// const checkDriverAge = (age) => {
//     console.log(age === 18 ? `“Congratulations on your first year of driving. Enjoy the ride!”` :
//         age > 18 ? `You are old enough to drive, Powering On. Enjoy the ride!`
//             : `Sorry, you are too young to drive this car. Powering off`);
// };
// checkDriverAge(age);
// ----------------------------------------------------------------------

// exercise 3
// const checkNumber = () => {
//     for (let i = 0; i < 100; i++) {
//         console.log(`the number ${i} is ${i % 2 == 0 ? 'even' : 'odd'}`);
//     }
// };
// checkNumber();
// ----------------------------------------------------------------------

// exercise 4
// const isDivisible = divisor => {
//     let outcome = '';
//     let sum = 0;
//     for (let i = 0; i < 500; i++) {
//         if (i % divisor == 0) {
//             sum += i;
//             outcome += `${i} `;
//         }
//     }
//     console.log(`Outcome: ${outcome}\nSum: ${sum}`);
// }
// isDivisible(3);
// ----------------------------------------------------------------------

// exercise 5
// let amazonBasket = { glasses: 1, books: 2, floss: 100 }
// const checkBasket = () => {
//     const item = prompt(`please enter item name:`).toLowerCase();
//     console.log(`item ${item in amazonBasket ? '' : 'not '}found`);
// };
// checkBasket();
// ----------------------------------------------------------------------

// exercise 6
// const changeEnough = (list, price) => {
//     const cList = [0.25, 0.10, 0.05, 0.01];
//     let inUsd = 0;
//     for (let i = 0; i < cList.length; i++) {
//         inUsd += list[i] * cList[i];
//     }

//     return inUsd > price;

// };

// changeEnough([25, 20, 5, 0], 4.25);
// changeEnough([2, 100, 0, 0], 14.11);
// changeEnough([0, 0, 20, 5], 0.75);
// ----------------------------------------------------------------------

// exercise 7
// const stock = { "banana": 6, "apple": 0, "pear": 12, "orange": 32, "blueberry": 1 }
// const prices = { "banana": 4, "apple": 2, "pear": 1, "orange": 1.5, "blueberry": 10 }
// const shoppingList = ['banana', 'orange', 'apple'];
// const myBill = () => {
//     let total = 0;
//     for (i of shoppingList) {
//         if (i in stock && stock[i] > 0) {
//             stock[i]--;
//             total += prices[i]
//         } else {
//             console.log(`we are out of ${i}`);
//         };

//     }
//     console.log(`total is ${total}`);
// }

// myBill();
// ----------------------------------------------------------------------

// exercise 8
// const val = Number(prompt('how much was the bill?'));
// const calcTip = val => {
//     let tip = 0;
//     if (val < 50) tip = val * 0.2;
//     else if (val >= 50 < 200) tip = val * 0.15;
//     else if (val > 200) tip = val * 0.1;
//     alert(`Tip amount:${tip}, Final bill:${val + tip}`);
// };

// calcTip(val);
// ----------------------------------------------------------------------
// exercise 9
// const hotelCost = () => {
//     let nights = 0;
//     while (nights < 1 || isNaN(nights)) {
//         nights = Number(prompt('please enter number of nights:'));
//     }
//     return nights * 140;
// };

// console.log(hotelCost())
// ----------------------------------------------------------------------
// const planeRideCost = () => {
//     let destination = '';
//     while (destination === '' || destination === null || typeof destination !== 'string') {
//         destination = prompt('please enter destination:');
//     }
//     switch (destination.toLowerCase()) {
//         case 'london':
//             return 183;
//         case 'paris':
//             return 220;
//         default:
//             return 300;
//     }
// };
// console.log(planeRideCost());
// ----------------------------------------------------------------------
// const rentalCarCost = () => {
//     let days = 0;
//     while (days < 1 || isNaN(days)) {
//         days = Number(prompt('please enter number of days to rent a car:'));
//     }
//     const val = days * 40;
//     return days > 10 ? val * 0.95 : val;
// };
// console.log(rentalCarCost());
// ----------------------------------------------------------------------
// const totalVacationCost = () => {
//     const hotel = hotelCost(), plane = planeRideCost(), car = rentalCarCost(), total = hotel + plane + car;
//     alert(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}, total of $${total}`);
// }
// totalVacationCost();