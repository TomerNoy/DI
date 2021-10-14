const playTheGame = () => {
    const v = confirm("Wanna Play?");
    if (!v) alert('No problem, Goodbye');
    else {
        countFail = 0;
        return game();
    }
};

let countFail = 0;

const game = () => {
    if (countFail > 2) {
        alert('out of chances');
        return null;
    }

    let n
    while (!isValidNum(n)) {
        n = prompt('enter a number 0-10');
    }

    n = Number(n);
    if (n > 10 || 0 > n) {
        alert('Sorry it’s not a good number,  try again');
        return game();
    }

    const computerNumber = Math.floor(Math.random() * 10);
    return test(n, computerNumber);
}

const isValidNum = (n) => n !== undefined && n !== null && n.length > 0 && !isNaN(n);


const test = (userNumber, computerNumber) => {
    if (userNumber === computerNumber) {
        alert("WINNER");
    } else if (userNumber > computerNumber) {
        alert("Your number is bigger then the computer’s, guess again");
        countFail++;
        return game();
    } else {
        alert("Your number is smaller then the computer’s, guess again");
        countFail++;
        return game();
    }
}
