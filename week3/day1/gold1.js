const book1 = {
    title: 'QED: The Strange Theory of Light and Matter',
    author: 'Richard Feynman',
    image: 'https://m.media-amazon.com/images/P/B00BR40XJ6.01._SCLZZZZZZZ_SX500_.jpg',
    alreadyRead: false,
}

const book2 = {
    title: 'Wild Swans: Three Daughters of China',
    author: 'Jung Chang',
    image: 'https://images-na.ssl-images-amazon.com/images/I/511p8drRKDL._SX324_BO1,204,203,200_.jpg',
    alreadyRead: true,
}

const allBooks = [book1, book2];

const listBooks = document.getElementsByClassName('listBooks')[0];

// add table
const table = document.createElement('table');

const tr = document.createElement('tr');

const thTitle = document.createElement('th');
thTitle.style.padding = '16px';
thTitle.textContent = 'title';
thTitle.style.textAlign = 'start';

const thDetails = document.createElement('th');
thDetails.style.padding = '16px';
thDetails.textContent = 'author';
thDetails.style.textAlign = 'start';

const thImg = document.createElement('th');
thImg.style.padding = '16px';
thImg.textContent = 'preview';
thImg.style.textAlign = 'start';

tr.appendChild(thTitle);
tr.appendChild(thDetails);
tr.appendChild(thImg);

table.appendChild(tr);
listBooks.appendChild(table);

// add books
allBooks.forEach(e => {
    const tr = document.createElement('tr');

    const tdTitle = document.createElement('td');
    tdTitle.style.padding = '16px';
    tdTitle.textContent = e.title;

    const tdDetails = document.createElement('td');
    tdDetails.style.padding = '16px';
    tdDetails.textContent = `written by ${e.author}`;
    if (e.alreadyRead) tdDetails.style.color = 'red';

    const tdImg = document.createElement('td');
    tdImg.style.padding = '16px';
    const img = document.createElement('img');
    img.src = e.image;
    img.style.width = '100px';
    tdImg.appendChild(img);

    tr.appendChild(tdTitle);
    tr.appendChild(tdDetails);
    tr.appendChild(tdImg);
    table.appendChild(tr);
    listBooks.appendChild(table);

});
