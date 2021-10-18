const createCalendar = (year, month) => {
  const date = new Date(year, month);
  console.log(date);

  const days = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"];

  const calendar = document.createElement("div");
  calendar.classList.add("calendar");

  const table = document.createElement("table");
  table.style.border = "1px solid gray";
  table.style.borderRadius = "8px";
  table.style.backgroundColor = "lightgray";
  const panelRow = document.createElement("tr");

  days.forEach((e) => {
    const day = document.createElement("th");
    day.textContent = e;
    day.style.padding = "16px";
    day.style.border = "1px solid gray";
    day.style.borderRadius = "8px";
    day.style.backgroundColor = "white";
    panelRow.appendChild(day);
  });

  //   const headFirstName = document.createElement("th");
  //   const headLastName = document.createElement("th");

  //   headFirstName.textContent = "MO";

  //   panelRow.appendChild(headFirstName);
  //   panelRow.appendChild(headLastName);

  table.appendChild(panelRow);

  calendar.appendChild(table);

  document.body.appendChild(calendar);
};

createCalendar(2001, 12);
console.log("ok");

{
  /* <table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  <tr>
    <td>Peter</td>
    <td>Griffin</td>
  </tr>
  <tr>
    <td>Lois</td>
    <td>Griffin</td>
  </tr>
</table> */
}
