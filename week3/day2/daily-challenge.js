
// Get the value of each of the inputs in the HTML file when the button is clicked.

// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.


// Bonus: Add a “shuffle” button to the HTML file, 
//      when clicked the button should change the story currently displayed 
//      (but keep the values entered by the user). The user could click the 
//      button at least three times and get a new story. Display the stories randomly.

let button = document.getElementById('lib-button');
button.addEventListener('click', genStory);

let shuffle = document.createElement('button');
shuffle.textContent = 'shuffle';
shuffle.addEventListener('click', genStory);
shuffle.id = 'shuffle';
document.body.appendChild(shuffle);

function genStory(e) {

    let noun = document.getElementById('noun').value;
    let adjective = document.getElementById('adjective').value;
    let person = document.getElementById('person').value;
    let verb = document.getElementById('verb').value;
    let place = document.getElementById('place').value;

    const stories = [
        `warning ! ${person} likes to ${verb} everyday in ${place} while touching his ${adjective} ${noun} !!!`,
        `every time ${person} ${verb} at ${place}, he is so ${adjective} he forgets his ${noun}`,
        `everyone knows that ${noun} at ${place} are very ${adjective} but don't ask ${person} about it while he ${verb}`,
        `at the year 1919 at ${place}, ${person} first encountered he's first ${noun}, he thought it was extremely ${adjective} so much so he decided to ${verb}`
    ];

    switch (e.target.id) {
        case 'lib-button':
            if (noun === '' || adjective === '' || person === '' || verb === '' || place === '')
                return alert('hey ! type in something');
            return document.getElementById('story').textContent = stories[0];
        case 'shuffle':
            const random = Math.floor(Math.random() * 4);
            return document.getElementById('story').textContent = stories[random];

    }



}