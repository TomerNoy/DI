const sphereVolume = (r) => (4 / 3) * Math.PI * Math.pow(r, 3);
const form = document.forms[0];

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const radius = form.elements.radius.value;
    if (radius !== '') form.elements.volume.value = sphereVolume(radius);
});


