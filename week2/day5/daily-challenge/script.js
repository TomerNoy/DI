let v = prompt('Welcome to the "99 Bottles of Beer" song!\nEnter a number:');

const isValidNum = (n) =>
  n !== undefined && n !== null && n.length > 0 && !isNaN(n);

while (!isValidNum(v)) v = prompt("Invalid try again?!\nEnter a number:");

const sing = (v) => {
  let total = v;

  for (let i = 1; i <= total; i++) {
    console.log(
      `${total} ${total > 1 ? "bottles" : "bottle"} of beer on the wall`
    );
    console.log(`${total} ${total > 1 ? "bottles" : "bottle"} of beer`);
    console.log(`Take ${i} down, pass ${i > 1 ? "them" : "it"} around`);
    total -= i;
    console.log(
      `${
        total - i < 1 ? "Not enough" : total > 1 ? "bottles" : "bottle"
      } bottles of beer on the wall`
    );
  }
  console.log(`Not enough bottles of beer on the wall`);
  console.log(`Not enough bottles of beer`);
  console.log(`Go to the store and buy some more`);
  console.log(`${v} bottles of beer on the wall`);
};

sing(Number(v));
