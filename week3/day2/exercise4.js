const title = document.getElementsByTagName('h1')[0];

title.addEventListener('click', (e) => {
    title.style.color = 'red';
});

title.addEventListener('dblclick', (e) => {
    title.style.fontSize = '20px';
});

title.addEventListener('drag', (e) => {
    title.style.position = 'absolute';
    title.style.top = '0px';
});

title.addEventListener('mousedown', (e) => {
    title.textContent = 'dont touch me'
});

title.addEventListener('mouseover', (e) => {
    title.style.opacity = '0.2'

});

title.addEventListener('mouseout', (e) => {
    title.style.opacity = '1';
    title.style.wordSpacing = '1em';
});

title.addEventListener('select', (e) => {
    title.textContent = 'dont touch me'
});

title.addEventListener('wheel', (e) => {
    title.style.border = '10px solid purple'
});

title.addEventListener('copy', (e) => {
    title.style.borderRadius = '45px';
});