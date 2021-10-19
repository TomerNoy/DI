const item = document.getElementById('item');
console.log(item);

item.addEventListener('dragstart', ondragstart);

function ondragstart(e) {
    console.log(e.target);
};

item.addEventListener('dragend', ondragend);

function ondragend(e) {
    console.log(e.target);
};