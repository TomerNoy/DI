// var audio = new Audio('audio_file.mp3');
// audio.play();

const boxes = document.getElementsByClassName('boxes')[0];
// console.log(boxes.children[0].children[1]);

for (box of boxes.children) {
    box.addEventListener('click', (e) => {
        console.log(e.target)
        // const audio = new Audio(`drumset_setup/sounds/${e.target.children[1].textContent}.wav`);
        // audio.play();
    });
}
