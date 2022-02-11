let input = document.getElementById('user_input');
let btnAdd = document.getElementById('btn');
let remove = document.getElementById('completed');
let toDoList = document.getElementById('todo_list');
let completedList = document.getElementById('completed');

btnAdd.addEventListener('click', function (event) {
    let newLi = document. createElement('LI');
    newLi.innerText = input.value;
    toDoList.appendChild(newLi);
});

toDoList.addEventListener('click', function (event) {
    if (event.target.tagName == 'LI') {
        completedList.appendChild(event.target);
    }
});

remove.addEventListener('click', function(event) {
    if (event.target.tagName === 'LI'){
        // console.log(event.target.tagName);
        completedList.removeChild(event.target);
    }
});
