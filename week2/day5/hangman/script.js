const err = () => alert('Error: invalid input, try again...');
const duplicate = () => alert('You already guest this character, try again...');

const promptPlayer1 = () => {
    let p1 = prompt("Player 1, please enter a minimum 8 letter word:");
    while (p1 === null || p1.length < 8) {
        err();
        p1 = prompt("please enter again a minimum 8 letter word:")
    }
    return p1;
}

const promptPlayer2 = (guesses) => {
    let p2 = prompt("Player 2, please enter a character:");
    while (p2 === null || p2.length != 1) {
        err();
        p2 = prompt("please enter again a character:")
    }
    if (guesses.includes(p2)) {
        duplicate();
        p2 = prompt("please enter another a character:")
    }
    return p2;
}

const reveal = (str, chr) => {
    let result = '';
    for (let i = 0; i < str.length; i++)
        result += (str[i] === chr) ? chr : lastGuess[i];
    return result;
}

const word = promptPlayer1(), guesses = [];
let lastGuess = '*'.repeat(word.length);

console.log(lastGuess);

const loopAsk = () => {
    while (guesses.length < 10) {
        const guess = promptPlayer2(guesses);
        guesses.push(guess);
        lastGuess = reveal(word, guess);
        console.log(lastGuess);
        if (lastGuess === word) return true;
    }
    return false;
}
console.log(loopAsk() ? 'CONGRATS YOU WIN.' : 'YOU LOSE.');
