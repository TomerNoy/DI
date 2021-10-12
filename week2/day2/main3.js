// /// challenge not bad

// let sentence = "the movie is not that bad, I like it!";
// const wordNot = sentence.indexOf("not");
// const wordBad = sentence.indexOf("bad");

// // const wordNot = sentence.search(/not/);
// // const wordBad = sentence.search(/bad/);

// if (wordBad > wordNot) {
//   sentence =
//     sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad + 3);
// }

// console.log(sentence);

var myObj = { k1: "test1", k2: "test2" };

const keyss = Object.keys(myObj),valuess = Object.values(myObj);

console.log(
  keyss.toString().replace(",", "\t") +
    "\n" +
    valuess.toString().replace(",", "\t")
);

// for (let i = 0; i < keyss.length; i++) {
//   console.log(keyss[i] + `\t`);
// }

// for (let i = 0; i < valuess.length; i++) {
//   console.log(valuess[i] + `\t`);
// }
