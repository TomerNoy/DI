

const createCalendar = (year, month) => {
  const daysList = getDaysInMonth(month, year);

  const monthGrid = { MO: [], TU: [], WE: [], TH: [], FR: [], SA: [], SU: [] };

  daysList.forEach(e => {
    const day = e.getDay();
    const date = e.getDate();
    const days = Object.keys(monthGrid);

    console.log(day);



    // monthGrid[days[day]].push(date);
  });

  console.log(monthGrid['MO']);

  const calendar = document.createElement("div");
  calendar.classList.add("calendar");

  const table = document.createElement("table");
  table.style.border = "1px solid gray";
  table.style.borderRadius = "8px";
  table.style.backgroundColor = "lightgray";
  const panelRow = document.createElement("tr");

  Object.keys(monthGrid).forEach((e) => {
    const day = document.createElement("th");
    day.textContent = e;
    day.style.padding = "16px";
    day.style.border = "1px solid gray";
    day.style.borderRadius = "8px";
    day.style.backgroundColor = "white";
    panelRow.appendChild(day);
  });

  table.appendChild(panelRow);
  calendar.appendChild(table);

  document.body.appendChild(calendar);
};


function getDaysInMonth(month, year) {
  month += -1;
  var date = new Date(year, month, 1);
  var days = [];
  while (date.getMonth() === month) {
    days.push(new Date(date)); //todo
    date.setDate(date.getDate() + 1);
  }
  return days;
}


createCalendar(2021, 10);
