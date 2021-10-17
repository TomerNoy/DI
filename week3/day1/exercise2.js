
const uls = document.getElementsByClassName('list');
const n = uls[0].lastElementChild;
n.textContent = "Richard";

for (ul of uls) ul.firstElementChild.textContent = "Tom"

for (ul of uls) {
    const li = document.createElement("li");
    const text = document.createTextNode("Hey students");
    li.appendChild(text);
    ul.appendChild(li);
}

const parent = uls[1];
const child = uls[1].children[1];
parent.removeChild(child);

for (ul of uls) {
    ul.classList.add("student_list");
    console.log(ul);
}

uls[0].classList.add("university", "attendance");
