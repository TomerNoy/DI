const div = document.getElementsByTagName('div')[0];

div.style.backgroundColor = 'lightblue';
div.style.padding = '16px';

const ul = document.getElementsByTagName('ul')[0];
ul.firstElementChild.style.display = 'none';

ul.lastElementChild.style.border = '3px solid gray'

document.body.style.fontSize = '1.1em';

const names = [ul.children[0].textContent, ul.children[1].textContent];

if (div.style.backgroundColor == 'lightblue') alert(`Hello ${names[0]} and ${names[1]}`);

console.log(names);