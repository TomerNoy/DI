let listTasks = [];

const form = document.forms.mytodo;
const listTasksDiv = document.getElementsByClassName("listTasks")[0];

const addTask = () => {
  const task = form.input.value;
  if (task == "") return null;
  listTasks.push(task);

  const div = document.createElement("div");
  div.classList.add("task");


  /// input
  const input = document.createElement("input");
  const p = document.createElement("p");


  /// x button
  const button = document.createElement('button');
  button.style.border = 'none';
  button.style.backgroundColor = 'transparent';
  const icon = document.createElement("i");
  icon.classList.add("fas", "fa-times-circle", 'fa-lg');
  button.append(icon);

  icon.style.color = "red";

  p.style.paddingLeft = "5px";

  div.append(button);
  div.append(input);
  div.append(p);

  div.style.padding = '10px 0px';

  hr = document.createElement("hr");
  input.type = "checkbox";

  p.textContent = task;
  listTasksDiv.append(div);
  listTasksDiv.append(hr);

  form.input.value = "";
};

document.getElementById("submit").addEventListener("click", addTask);
