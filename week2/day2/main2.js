let userCart = {
  username: "John",
  password: 1234,
  isUserSignedIn: true,
  cart: {
    apple: 2,
    banana: 1,
    pear: 5,
  },
  prices: {
    apple: 0.5,
    banana: 0.8646466363,
    pear: 0.2,
  },
};

userCart["lastName"] = "Smith";

userCart["cart"]["banana"] *= Number(userCart["prices"]["banana"]);

const fruits = prompt("please add fruits between Apple, Banana and Pear");
const listFruits = fruits.split(" ");

for (let i = 0; i < listFruits.length; i++) {
    // console.log((userCart["cart"][listFruits[i].toLowerCase()]));
  const price = console.log(
    `${listFruits[i]} costs ${(userCart["cart"][listFruits[i].toLowerCase()] *=
      Number(userCart["prices"][listFruits[i].toLocaleLowerCase()]))}`
  );
}
