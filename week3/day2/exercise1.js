
const article = document.getElementsByTagName('article')[0];

article.removeChild(article.lastElementChild);

const h2 = document.body.querySelector('article h2');
document.body.addEventListener('click', () => h2.style.backgroundColor = 'yellow');

const h1 = document.body.querySelector('article h1');
const random = Math.floor(Math.random() * 101);
h1.style.fontSize = `${random}px`;

const h3 = document.body.querySelector('article h3');
h3.addEventListener('click', () => h3.style.display = 'none');

const button = document.createElement('button');
button.textContent = 'make bold';
document.body.appendChild(button);

const allP = document.body.querySelectorAll('article p');
button.addEventListener('click', () => allP.forEach(e => e.style.fontWeight = 'bold'));

const form = document.forms[0];

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const fname = e.target.elements.fname.value;
    const lname = e.target.elements.lname.value;
    if (fname !== '' && lname !== '') {
        const table = document.createElement('table');
        const row = document.createElement('tr');
        const fnameTd = document.createElement('td');
        fnameTd.textContent = fname;

        const lnameTd = document.createElement('td');
        lnameTd.textContent = lname;

        row.appendChild(fnameTd);
        row.appendChild(lnameTd);

        table.appendChild(row);

        document.getElementsByClassName('usersAnswer')[0].appendChild(table);
    }
});

const secondP = document.querySelectorAll('article p')[1];
// secondP.style.transition = '1s ease-out';
secondP.addEventListener('mouseover', ()=>{
    console.log('kjhsakd');
    secondP.style.opacity = '0';
    secondP.style.transition = 'opacity 250ms ease-out'
})

    // When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

    // console.log(article.lastElementChild);