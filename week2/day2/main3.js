/// challenge not bad

let sentence = "the movie is not that bad, I like it!";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordBad > wordNot) {
  sentence = sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad + 3);
}

console.log(sentence);
