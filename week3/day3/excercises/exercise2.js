const element = document.getElementById('element');
const boxes = document.getElementsByClassName('box');

element.addEventListener('dragstart', dragStart);
function dragStart() {
    this.className += ' hold';
    setTimeout(() => (this.className = 'invisible'), 0);
}

element.addEventListener('dragend', () => element.className = 'element');

for (box of boxes) {
    box.addEventListener('dragover', (e)=> e.preventDefault());
    box.addEventListener('dragenter', dragEnter);
    box.addEventListener('dragleave', dragLeave);
    box.addEventListener('drop', dragDrop);
}

function dragEnter(e) {
    e.preventDefault();
    this.className += ' hovered';
}

function dragLeave() {
    this.className = 'box';
}

function dragDrop() {
    this.className = 'box';
    this.append(element);
}