
const drums = { A: 'boom', S: 'clap', D: 'hihat', F: 'kick', G: 'openhat', H: 'ride', J: 'snare', K: 'tink', L: 'tom' }
const boxes = document.getElementsByClassName('boxes')[0];

Object.keys(drums).forEach(e => {
    const audio = new Audio(`drumset_setup/sounds/${drums[e]}.wav`);
    box = document.createElement('div');
    box.className = drums[e];
    box.addEventListener('click', (e) => audio.play());
    boxes.append(box);

    title = document.createElement('h1');
    title.textContent = e
    box.append(title)

    p = document.createElement('p');
    p.textContent = drums[e]
    box.append(p)
})


document.addEventListener('keydown', (e) => {
    boxes.children[0].className
    const key = e.key.toLocaleUpperCase();
    for (box of boxes.children) {
        if (Object.keys(drums).includes(key)) {
            console.log(drums[key]);
            const audio = new Audio(`drumset_setup/sounds/${drums[key]}.wav`);
            audio.play()
        }
    }
})
