// exercise 1
// const me = ["my", "favorite", "color", "is", "blue"];
// const a = me.join(" ");
// console.log(a);
//----------------------------------------------------------------------------

// exercise 2
// const str1 = "first";
// const str2 = "second";
// const newWord = str2.slice(0, 2) + str1.slice(2) + " " + str1.slice(0, 2) + str2.slice(2);
// console.log(newWord);
//----------------------------------------------------------------------------

// exercise 3
// const num1 = prompt('Please Enter first number');
// const num2 = prompt('Please Enter second number');
// const sum = Number(num1) + Number(num2);
// alert(`sum is ${sum}`);

// const num1 = prompt('Please Enter first number');
// const num2 = prompt('Please Enter second number');
// const sum = Number(num1) - Number(num2);
// alert(`${num1} - ${num2} is ${sum}`);

// const num1 = prompt('Please Enter first number');
// const num2 = prompt('Please Enter second number');
// const sum = Number(num1) * Number(num2);
// alert(`${num1} * ${num2} is ${sum}`);

// const num1 = prompt('Please Enter first number');
// const num2 = prompt('Please Enter second number');
// const sum = Number(num1) / Number(num2);
// alert(`${num1} / ${num2} is ${sum}`);
//----------------------------------------------------------------------------

/// ninja exercise 1
// const word = prompt("add a word containing \"Nemo\"");
// const list =  word.split (" ");
// const index = list.indexOf("Nemo");

// if (index != -1) {
//     console.log(`found nemo at ${index}`);
// } else { console.log("I can’t find Nemo"); }
//----------------------------------------------------------------------------

/// exercise 1
// 5 >= 1                  true
// 0 === 1                 false
// 4 <= 1                  false
// 1 != 1                  false
// "A" > "B"               false
// "B" < "C"               true
// "a" > "A"               true
// "b" < "A"               false
// true === false          false
// true != true            false
//----------------------------------------------------------------------------

/// exercise 2
// let c;
// let a = 34;
// let b = 21;
// a = 2;
// console.log(3 + 4 + '5'); //75
//----------------------------------------------------------------------------

// exercise 3
// const string = prompt("enter list of numbers seperated by comma");
// const list = string.split(",");
// let result = 0;
// for (let i = 0; i < list.length; i ++){
//     result +=  Number(list[i]);
// }
// console.log(result);
//----------------------------------------------------------------------------

// exercise 4
// const userNum = Number(prompt("enter a number"));

// if (userNum < 2) {
//     alert("boom");
// } else if (userNum > 2) {
//     let result = "";
//     const middle = Array(userNum + 1).join("o");
//     result = `b${middle}m`;
//     if (userNum % 2 === 0) {
//         result += "!";
//     }
//     if (userNum % 5 === 0) {
//         result = result.toUpperCase();
//     }
//     alert(result);
// } else {
//     alert("2 wasn't included in the exercise )-:");
// }
//----------------------------------------------------------------------------

//########################
/// daily challenge
//########################

/// exercise 1
// let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// fruits.shift();
// fruits.sort();
// fruits.push("Kiwi");
// fruits.splice(0,1);
// fruits.reverse();
// console.log(fruits);
//----------------------------------------------------------------------------

/// exercise 2
// let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// const result = moreFruits[1][1][0];
// console.log(result);
//########################################################################