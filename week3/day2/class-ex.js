// Exercise

// let colors = ["blue", "yellow", "green", "pink"];
// const container = document.body.getElementsByClassName("container")[0];

// colors.forEach((e) => {
//   const col = document.createElement("button");
//   col.textContent = e;
//   col.style.padding = "8px 16px";
//   col.addEventListener("click", () => (col.style.backgroundColor = e));
//   container.appendChild(col);
// });

// let pics = [
//   "https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
//   "https://images.pexels.com/photos/2253275/pexels-photo-2253275.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
//   "https://images.pexels.com/photos/3439576/pexels-photo-3439576.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
// ];

// 1. Using this array, create a button on the page that when clicked on
//      display one animal randomly
// 2. Set a class to the image, so each image will be 200px height,
//      and width, and in the middle of the page
// 3. Add a button next to each image
// 4. When we click on one image, it should disapear(ie. be deleted),
//      When we hover on the image, it should display the "alt".

// const container = document.body.getElementsByClassName("container")[0];

// container.style.display = "flex";

// const btn = document.createElement("button");
// const img = document.createElement("img");
// img.style.width = "200px";
// img.style.height = "200px";
// img.style.borderRadius = "8px";
// img.style.border = "1px solid gray";
// img.style.marginLeft = '3px';

// btn.textContent = "random";
// btn.style.padding = "8px 16px";
// btn.addEventListener("click", () => {
//   const random = Math.floor(Math.random() * 3);

//   img.src = pics[random];
// });

// container.appendChild(btn);
// container.appendChild(img);
