console.log('ok');

const colorsArray = ['red', 'orangered', 'orange', 'yellow', 'yellowgreen',
    'lightgreen', 'green', 'turquoise', 'cyan', 'lightskyblue', 'dodgerblue',
    'blue', 'darkblue', 'indigo', 'darkmagenta', 'violet', 'lightpink',
    'lightgray', 'gray', 'black', 'white',
]
let myColor = 'white';
let isPressed = false;

const colors = document.getElementsByClassName('colors')[0];

colorsArray.forEach(e => {
    const col = document.createElement('div');
    col.classList.add('color');
    col.style.backgroundColor = e;
    col.addEventListener('click', getColor)
    colors.append(col);
})

function getColor(e) {
    myColor = e.target.style.backgroundColor;
}

const board = document.getElementsByClassName('board')[0];

for (let i = 0; i < 1440; i++) {
    const box = document.createElement('div');
    box.classList.add('box');
    box.style.backgroundColor = 'white';
    box.addEventListener('mousedown', mousedown);
    box.addEventListener('mouseover', mouseover);
    box.addEventListener('mouseup', mouseup);
    board.append(box);
}

function mousedown(e) {
    isPressed = true;
    e.target.style.backgroundColor = myColor;
}

function mouseover(e) {
    if (isPressed) e.target.style.backgroundColor = myColor;
}

function mouseup() {
    isPressed = false;
}

const btn = document.getElementById('btn');
btn.addEventListener('click', clear);

function clear() {
    for (box of board.children) {
        box.style.backgroundColor = 'white';
    }
    isPressed = false;
}