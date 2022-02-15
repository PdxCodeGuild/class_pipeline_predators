

const textfield = document.getElementById('userinput');
const addButton = document.getElementsByTagName("button")[0];

const compList = document.getElementById('compli');
const incomList = document.getElementById('incompli');



var createTodo = function (todostring) {
  var listItem = document.createElement("li");
  var compBtn = document.createElement("button");
  var deleteBtn = document.createElement('button');
  var label = document.createElement('label');
  label.innerText = todostring;
  compBtn.innerText = 'Complete Task';
  compBtn.className = "complete";
  deleteBtn.innerText = "Delete";
  deleteBtn.className = "delete";

  listItem.appendChild(label);
  listItem.appendChild(compBtn);
  listItem.appendChild(deleteBtn);
  console.log("todo Function run")
  return listItem;
}

var addTodo = function () {
  console.log("add todo");
  var listItem = createTodo(textfield.value);
  incomList.appendChild(listItem);
  bindTaskEvents(listItem, taskCompleted);

  textfield.value = ""
}

var taskCompleted = function () {
  console.log("Complete Task...");
  var listItem = this.parentNode;
  compList.appendChild(listItem);
  console.log(listItem)
  bindTaskEvents(listItem, taskIncomplete);
}

var deleteTodo = function () {
  console.log("Delete Task...");
  var listItem = this.parentNode;
  var ul = listItem.parentNode;
  ul.removeChild(listItem);

}

var taskIncomplete = function () {
  console.log("Incomplete Task...");
  var listItem = this.parentNode;
  incomList.appendChild(listItem);
  bindTaskEvents(listItem, taskCompleted);
}



addButton.onclick = addTodo;


var bindTaskEvents = function (taskListItem, compBtn) {
  console.log("bind list item events");
  var compBtn = taskListItem.querySelector("button.complete");
  var deleteBtn = taskListItem.querySelector("button.delete");
  compBtn.onclick = taskCompleted;
  deleteBtn.onclick = deleteTodo;
}

// for (var i = 0; i < incomList.children.length; i++) {
//   bindTaskEvents(compList.children[i], taskIncomplete);
// }



