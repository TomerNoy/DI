// const genres = document.getElementById('genres');

// const classic = document.createElement('option');
// classic.textContent = 'classic';
// classic.value = 'classic';

// genres.appendChild(classic);

// const selection = document.createElement('h1');
// selection.id = 'selection';

// document.body.appendChild(selection);

// genres.addEventListener('change', select);

// function select(e) {
//     document.getElementById('selection').textContent = `you selected "${e.target.value}"`;
// }

// genres.selectedIndex = '2';
// --------------------------------------------------------------------------------------------

// const input = document.getElementsByTagName('input')[0];

// const removecolor = () => {
//     const colorSelect = document.getElementById('colorSelect');
//     const selectedIndex = colorSelect.selectedIndex;

//     colorSelect.remove(selectedIndex);
// }

// input.addEventListener('click', removecolor);
// --------------------------------------------------------------------------------------------

let shoppingList = [];

const root = document.getElementById('root');

/// form
const form = document.createElement('form');
root.appendChild(form);

/// input
const input = document.createElement('input');
input.id = 'input';
form.appendChild(input);

/// list
const list = document.createElement('ul');
root.appendChild(list);

/// button
const button = document.createElement('button');
form.appendChild(button);
button.textContent = 'AddItem';
button.addEventListener('click', addItem)
function addItem(e) {
    e.preventDefault();
    let item = input.value;
    if (item === '') return;
    shoppingList.push(item);
    input.value = '';
    const li = document.createElement('li');
    li.textContent = item;
    list.appendChild(li);
}

/// clear all button
const clear = document.createElement('button');
clear.textContent = 'clear';
root.appendChild(clear);
clear.addEventListener('click', clearAll);
function clearAll(e) {
    e.preventDefault();
    shoppingList = [];
    list.innerHTML = '';
}

