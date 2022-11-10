let currentlySelectedProj;
let previouslySelectedProj;
let prevSel;

function setActive(proj_id) {

  if (currentlySelectedProj != proj_id) {
    previouslySelectedProj = currentlySelectedProj;
    currentlySelectedProj = proj_id;
  }


  if (prevSel === proj_id) {

  } else {
    previousProj = document.getElementById("project" + prevSel);

    if (previousProj === null) {

    } else {
      previousProj.classList.remove("panel-project-selected", "sticky-top", "sticky-bottom", "border-end-0",
        "display-6");
      previousProj.classList.add("d-none");

    }
    prevSel = proj_id;
  }

  var selectedProj = document.getElementById("project" + proj_id);


  if (selectedProj.classList.contains("d-none")) {
    selectedProj.classList.remove("d-none")
  }

  var medSizeView = document.querySelectorAll(".proj-section-med-size");
  if (medSizeView) {
    for (let i = 0; i < medSizeView.length; i++) {
      if (medSizeView[i].classList.contains("d-none")) {
        medSizeView[i].classList.remove("d-none");
      }
    }
  }

}

function adujustHeight() {
  let windowHeight = window.innerHeight
  document.body.style.minHeight = windowHeight

  var mainArea = document.getElementById("mainPageArea")
  var mainTopBar = document.getElementById("mainTopBar").offsetHeight

  let mainAreaHeight = windowHeight - mainTopBar

  mainArea.style.minHeight = mainAreaHeight + "px"

  console.log("windowHeight", windowHeight)
  console.log("mainTopBar", mainTopBar)
  console.log("mainArea.style.minHeight", mainArea.style.minHeight)

}

window.onload = function () {

  adujustHeight()
  var onLoadProject = document.getElementById("recentUpdProj-id")

  if (onLoadProject.innerText === '') {
    console.log("Add a new project to get started")
  } else {
    setActive(onLoadProject.innerText)
  }

}

/* if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
} */



function resizeProj(btn) {

  var mainProjArea = document.getElementById("mainProjArea")
  var resizeProjList = document.getElementById("resizeProjList")
  var projListSmall = document.querySelectorAll(".proj-list-small")
  var projListLarge = document.querySelectorAll(".proj-list-large")

  var projectListItem = document.querySelectorAll(".project-list-item")

  if (btn.value == "small") {
    mainProjArea.classList.add("d-none")
    resizeProjList.classList.remove("d-none", "d-lg-inline", "col-lg-4", "col-xl-3", "col-xxl-3")
    resizeProjList.classList.add("col-auto", "mx-auto", "w-100")
    for (let i = 0; i < projListSmall.length; i++) {
      if (!projListSmall[i].classList.contains("d-none")) {
        projListSmall[i].classList.add("d-none");
      }
      for (let i = 0; i < projListLarge.length; i++) {
        if (projListLarge[i].classList.contains("d-none")) {
          projListLarge[i].classList.remove("d-none");
        }
      }
    }

  }
  if (btn.value == "big") {
    mainProjArea.classList.remove("d-none")
    resizeProjList.classList.add("d-none", "d-lg-inline", "col-lg-4", "col-xl-3", "col-xxl-3")
    resizeProjList.classList.remove("col-auto", "mx-auto", "w-100")
    for (let i = 0; i < projListSmall.length; i++) {
      if (projListSmall[i].classList.contains("d-none")) {
        projListSmall[i].classList.remove("d-none");
      }
      for (let i = 0; i < projListLarge.length; i++) {
        if (!projListLarge[i].classList.contains("d-none")) {
          projListLarge[i].classList.add("d-none");
        }
      }
    }
  }


}



function addLabel(label_card, label_id, parent_id) {

  var label = {
    label: label_id
  }

  fetch(`/update_labels/project/${parent_id}`, {
      method: 'POST',
      credentials: "include",
      body: JSON.stringify(label),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
    .then(function (response) {
      if (response.status !== 200) {
        console.log(`Response status was not 200:, ${response.status}`);
        return;
      }
      response.json().then(function (data) {
        label_card.classList.add('d-none');
        var addedlabel = document.getElementById("addedlabel" + label_id + parent_id)

        console.log("addedlabel", addedlabel)
        addedlabel.classList.remove("d-none")

      })
    })

}


function removeLabel(label_card, label_id, parent_id) {

  var label = {
    label: label_id
  }

  fetch(`/remove_labels/project/${parent_id}`, {
      method: 'POST',
      credentials: "include",
      body: JSON.stringify(label),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
    .then(function (response) {
      if (response.status !== 200) {
        console.log(`Response status was not 200:, ${response.status}`);
        return;
      }
      response.json().then(function (data) {
        label_card.classList.add('d-none');

        var removedlabel = document.getElementById("removedlabel" + label_id + parent_id)

        console.log("removedlabel", removedlabel)
        removedlabel.classList.remove("d-none")

      })
    })

}






function submitForm(id) {
  var todoComplete = document.getElementById('todoComplete' + id)

  todoComplete.submit()
}





/* Home page --- 

----------------------

Notes Section

---------------------*/


function showNoteInputs(btn) {

  if (btn.classList.contains("d-md-block")) {
    btn.classList.remove("d-md-block")
    btn.classList.add("d-none")
  }

  var newNoteForm = document.querySelectorAll("#newNoteForm");

  for (let i = 0; i < newNoteForm.length; i++) {
    if (newNoteForm[i].classList.contains("d-none")) {

      newNoteForm[i].classList.remove("d-none");
    }
  }

};

function removeNoteInputs() {

  var newNoteForm = document.querySelectorAll("#newNoteForm");
  var newNoteBtn = document.getElementById("newNoteBtnLg");

  if (!newNoteBtn.classList.contains("d-md-block")) {
    newNoteBtn.classList.add("d-md-block")
  }

  for (let i = 0; i < newNoteForm.length; i++) {
    if (!newNoteForm[i].classList.contains("d-none")) {
      newNoteForm[i].classList.add("d-none");
    }
  }


};

















/* Home page --- 

----------------------

Project-Tasks Section

---------------------*/


function edittaskItem(task_id) {
  let permtaskBody = document.getElementById("card-body-perm-task" + task_id)
  let edittaskBody = document.getElementById("card-body-edit-task" + task_id)
  if (edittaskBody.classList.contains("d-none")) {
    edittaskBody.classList.remove("d-none")
  }
  if (!permtaskBody.classList.contains("d-none")) {
    permtaskBody.classList.add("d-none")
  }
}

function savetaskItem(task_id) {
  let permtaskBody = document.getElementById("card-body-perm-task" + task_id)
  let edittaskBody = document.getElementById("card-body-edit-task" + task_id)
  if (!edittaskBody.classList.contains("d-none")) {
    edittaskBody.classList.add("d-none")
  }
  if (permtaskBody.classList.contains("d-none")) {
    permtaskBody.classList.remove("d-none")
  }
}

function markAsComplete(task_id) {
  let form = document.getElementById("markAsComplete-task" + task_id)

  form.submit()

  alert("Submitted")

}

function showUndoBtns(task_id) {
  let undoBtn = document.getElementById('undo' + task_id)

  if (undoBtn.classList.contains('d-none')) {
    undoBtn.classList.remove('d-none')
  }
}

function hideUndoBtns(task_id) {
  let undoBtn = document.getElementById('undo' + task_id)

  if (!undoBtn.classList.contains('d-none')) {
    undoBtn.classList.add('d-none')
  }
}

function puttaskItemBack(task_id) {
  let form = document.getElementById("undoForm" + task_id)

  form.submit()
}

















/* Home page --- 

----------------------

Timer

---------------------*/



function editGoal(id) {
  var goalInputSection = document.getElementById("goalInputSection" + id);

  if (goalInputSection.classList.contains("d-none")) {
    goalInputSection.classList.remove("d-none")
  }

}


function saveGoal(id) {
  var goalInputSection = document.getElementById("goalInputSection" + id)
  var goal = document.getElementById("goal" + id)
  var goalToHit = document.getElementById("goalToHit" + id)
  var perSelect = document.getElementById("perSelect" + id)
  var goalPer = document.getElementById("goalper" + id)

  goalPer.innerHTML = "per " + perSelect.value;

  goalToHit.innerHTML = goal.innerHTML

  goalInputSection.classList.add("d-none")
}


function timePer(elem) {

  var goalRange = elem.previousElementSibling;
  var goalPer = elem
  var goalElem = goalRange.firstElementChild;
  var goalTime = goalRange.children[1]

  goalPer.setAttribute("name", "goal-per");
  goalTime.setAttribute("name", "goal-time");

  if (elem.value == "day") {
    if (goalTime.value > 43201) {
      goalElem.innerText = `12:00:00`;
    }
    goalTime.classList.remove("d-none");
    goalRange.classList.remove("d-none");
    /* saveGoalBtn.classList.remove("d-none"); */
    goalTime.max = 43201;
    goalTime.step = 900;
  }
  if (elem.value == "week") {
    if (goalTime.value > 216001) {
      goalElem.innerText = `60:00:00`;
    }
    /* saveGoalBtn.classList.remove("d-none"); */
    goalTime.classList.remove("d-none");
    goalRange.classList.remove("d-none");
    goalTime.max = 216001;
    goalTime.step = 1800;
  }
  if (elem.value == "month") {
    /* saveGoalBtn.classList.remove("d-none"); */
    goalTime.classList.remove("d-none");
    goalRange.classList.remove("d-none");
    goalTime.max = 576001;
    goalTime.step = 3600;
  }
  if (elem.value == 0) {
    goalTime.classList.add("d-none");
    goalRange.classList.add("d-none");
    /* saveGoalBtn.classList.add("d-none"); */
  }
}


function showGoal(elem) {
  var inputGoal = elem

  var tempGoalTime = document.getElementById("tempGoalTime")

  if (tempGoalTime) {
    tempGoalTime.classList.add('d-none')
  }

  console.log("inputGoal", inputGoal)

  var goalElem = inputGoal.previousElementSibling;
  console.log("goalElem", goalElem)

  console.log(inputGoal.value)

  let hrs = Math.floor(inputGoal.value / 3600);
  let mins = Math.floor((inputGoal.value - (hrs * 3600)) / 60);
  let secs = inputGoal.value % 60;

  if (secs < 10) secs = '0' + secs;
  if (mins < 10) mins = '0' + mins;
  if (hrs < 10) hrs = '0' + hrs;


  goalElem.innerText = `${hrs}:${mins}:00`;
  goalToHit = `${hrs}:${mins}:${secs}`;
}





function startTimer(id, proj_secs) {

  var timeElem = document.getElementById("time" + id);
  var startBtn = document.getElementById("start" + id);
  var stopBtn = document.getElementById("stop" + id);
  var last_session = document.getElementById("last-session-temp" + id);

  var totalSeconds = document.getElementById("totalSeconds" + id)
  var timerTextArea = document.getElementById("hidden-value" + id)

  startBtn.classList.add("d-none")
  stopBtn.classList.remove("d-none")


  stopBtn.type = "submit";

  let seconds = proj_secs;
  let interval = null;

  function timer() {
    seconds++;

    let hrs = Math.floor(seconds / 3600);
    let mins = Math.floor((seconds - (hrs * 3600)) / 60);
    let secs = seconds % 60;

    if (secs < 10) secs = '0' + secs;
    if (mins < 10) mins = '0' + mins;
    if (hrs < 10) hrs = '0' + hrs;

    timeElem.innerText = `${hrs}:${mins}:${secs}`;
    timeElem.value = seconds + totalSeconds

    timerTextArea.value = seconds
    current_session = seconds - proj_secs


    var startTimerUniversalBtn = document.getElementById("startTimerUniversalBtn")
    var stopTimerUniversalBtn = document.getElementById("stopTimerUniversalBtn")
    var navBarTimer = document.getElementById("navBarTimer")



    startTimerUniversalBtn.addEventListener("click", function () {
      if (navBarTimer.classList.contains("bg-success")) {
        navBarTimer.classList.remove("bg-success")
      }
    })

    stopTimerUniversalBtn.addEventListener("click", function () {
      if (!navBarTimer.classList.contains("bg-success")) {
        navBarTimer.classList.add("bg-success")
      }
    })


    last_session.value = current_session;

  }


  if (interval) {
    return
  }
  interval = setInterval(timer, 1000);

  function stop(id) {
    clearInterval(interval);
    interval = null;
    /* last_session.innerText = timeElem.innerText */
    last_session.innerText = current_session;
    startBtn.classList.remove("d-none");
    stopBtn.classList.add("d-none");

  }
  stopBtn.addEventListener('click', stop)
}


function showEditableProducivityGoal(btn, id, goal_time, goal_per) {

  var editableGoal = document.getElementById('editProductivityTime' + id)

  if (editableGoal.classList.contains('d-none')) {
    editableGoal.classList.remove('d-none')
  }
  btn.classList.add('d-none');

  var goalPer = document.getElementById('perSelect' + id);

  console.log("goalPer", goalPer)

  timePer(goalPer);

}







/* Home page --- 

----------------------

Projects Section

---------------------*/


function showTimeAllotments(id) {
  var goalSection = document.getElementById("goalInputSection" + id);
  var timeAllotmentBtn = document.getElementById("showTimeAllot" + id)
  goalSection.classList.remove("d-none");
  timeAllotmentBtn.classList.add("d-none");
}

let labels_list = [];

function update_labels(model, id, label_id) {

  var entry = {
    label: label_id
  };


  if (id === 'new') {
    console.log("new");
    labels_list.push(label_id);
    console.log("labels_list", labels_list)
    var newNoteLabelsList = document.getElementById("newNoteLabelsList");
    newNoteLabelsList.value = labels_list

  } else {
    fetch(`/update_labels/${model}/${id}`, {
        method: 'POST',
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json"
        })
      })
      .then(function (response) {
        if (response.status !== 200) {
          console.log(`Response status was not 200:, ${response.status}`);
          return;
        }
        response.json().then(function (data) {
          console.log(data)
        })
      })
  }
}


function remove_labels(model, id, label_id) {

  var entry = {
    label: label_id
  };

  fetch(`/remove_labels/${model}/${id}`, {
      method: 'POST',
      credentials: "include",
      body: JSON.stringify(entry),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
    .then(function (response) {
      if (response.status !== 200) {
        console.log(`Response status was not 200:, ${response.status}`);
        return;
      }
      response.json().then(function (data) {
        console.log(data)
      })
    })
}

function labelName(elem) {

  elem.setAttribute("name", "labelName")

}




function editprojectItem(project_id) {
  let permprojectBody = document.getElementById("card-body-perm-project" + project_id)
  let editprojectBody = document.getElementById("card-body-edit-project" + project_id)

  console.log("editprojectBody", editprojectBody)


  if (editprojectBody.classList.contains("d-none")) {
    editprojectBody.classList.remove("d-none")
    console.log("editprojectBody.classList", editprojectBody.classList)
  }
  if (!permprojectBody.classList.contains("d-none")) {
    permprojectBody.classList.add("d-none")
  }
}

function saveprojectItem(project_id) {
  let permprojectBody = document.getElementById("card-body-perm-project" + project_id)
  let editprojectBody = document.getElementById("card-body-edit-project" + project_id)
  if (!editprojectBody.classList.contains("d-none")) {
    editprojectBody.classList.add("d-none")
  }
  if (permprojectBody.classList.contains("d-none")) {
    permprojectBody.classList.remove("d-none")
  }
}

function markAsComplete(project_id) {
  let form = document.getElementById("markAsComplete" + project_id)

  form.submit()

}

function showUndoBtns(project_id) {
  let undoBtn = document.getElementById('undo' + project_id)

  if (undoBtn.classList.contains('d-none')) {
    undoBtn.classList.remove('d-none')
  }
}

function hideUndoBtns(project_id) {
  let undoBtn = document.getElementById('undo' + project_id)

  if (!undoBtn.classList.contains('d-none')) {
    undoBtn.classList.add('d-none')
  }
}

function putprojectItemBack(project_id) {
  let form = document.getElementById("undoForm" + project_id)

  form.submit()
}










function toggleCancelBtn(btn, id) {
  var cancelBtn = document.getElementById(btn.id + "cancel")
  btn.classList.add("d-none")
  cancelBtn.addEventListener('click', function () {
    btn.classList.remove("d-none")
  })
}

function changeIconImage(elem, proj_id) {
  var newIcon = elem.value;
  var newIconSrc = elem.firstElementChild.src
  var displayedIcon = document.getElementById("displayedIcon" + proj_id);

  displayedIcon.src = newIconSrc

  var iconInput = document.getElementById('iconInput' + proj_id)
  iconInput.value = newIcon;

  console.log("iconInput.value", iconInput.value)
}

function addCustomColor(elem, proj_id) {

  var r = document.querySelector(':root');
  var colorpicker = document.getElementById('newLabelColor' + proj_id);
  var newLabel = document.getElementById("newLabel" + proj_id);

  setInterval(() => {
    let color = colorpicker.value;
    newLabel.style.backgroundColor = color;

    var colorInput = document.getElementById('colorInput' + proj_id)
    colorInput.value = color;

    console.log("colorInput.value", colorInput.value)

  }, 200);

}


function addTaskNoProject() {
  var numProjTasks = document.getElementById('numProjTasks')
  var newProjTasks = document.getElementById("newProjTasks")
  var newTaskNoProjForm = document.getElementById("newTaskNoProjForm")

  console.log("numProjTasks", numProjTasks)
  console.log("newProjTasks", newProjTasks)
  console.log("newTaskNoProjForm", newTaskNoProjForm)

  var entry = {
    title: newTaskNoProjForm.newTaskTitle.value,
    description: newTaskNoProjForm.newTaskDescription.value,
    due_date: newTaskNoProjForm.new_task_due_date.value + " " + newTaskNoProjForm.new_task_due_date_time.value +
      ":00",
    due_date_date: newTaskNoProjForm.new_task_due_date.value,
    due_date_time: newTaskNoProjForm.new_task_due_date_time.value,
    priority: newTaskNoProjForm.newTaskPriority.value,

  };

  fetch(`/add_task_no_project`, {
      method: 'POST',
      credentials: "include",
      body: JSON.stringify(entry),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
    .then(function (response) {
      if (response.status !== 200) {
        console.log(`Response status was not 200:, ${response.status}`);
        return;
      }
      response.json().then(function (data) {
        console.log("DATA: ", data)

        title = data.title
        description = data.description
        due_date = data.due_date_date
        due_date_time = data.due_date_time
        priority = data.priority
        taskID = data.id

        let li = document.createElement("li");
        let div = document.createElement("div");
        let titleDiv = document.createElement("div");
        let deleteTaskBtn = document.createElement("button");
        let deleteIcon = document.createElement("i");
        let taskTitle = document.createElement("span");

        div.classList.add("d-inline-flex");
        div.classList.add("w-100");
        div.classList.add("justify-content-between");

        li.classList.add("w-100");

        deleteIcon.classList.add("fa-solid")
        deleteIcon.classList.add("fa-trash")

        deleteTaskBtn.classList.add("border-0")
        deleteTaskBtn.classList.add("bg-transparent")
        deleteTaskBtn.classList.add("me-3")
        deleteTaskBtn.setAttribute("type", "button")
        deleteTaskBtn.setAttribute("onclick", "deleteTask(this)")
        deleteTaskBtn.setAttribute("value", taskID)

        li.setAttribute("id", "task" + taskID)



        taskTitle.classList.add("h5")

        deleteTaskBtn.appendChild(deleteIcon)

        taskTitle.innerText = title;


        titleDiv.appendChild(deleteTaskBtn)
        titleDiv.appendChild(taskTitle)

        div.appendChild(titleDiv)



        if ((!due_date == "") && (!due_date_time == "")) {
          let taskDueDate = document.createElement("span");
          taskDueDate.innerText = due_date + "  " + due_date_time;
          div.appendChild(taskDueDate)
        } else {


          if (!due_date == "") {
            let taskDueDate = document.createElement("span");
            taskDueDate.innerText = due_date;
            div.appendChild(taskDueDate)
          }
          if (!due_date_time == "") {
            let taskDueDateTime = document.createElement("span");
            taskDueDateTime.innerText = due_date_time;
            div.appendChild(taskDueDateTime)
          }
        }
        if (!priority == "") {
          let taskPriority = document.createElement("span");
          taskPriority.innerText = priority;
          div.appendChild(taskPriority)
        }
        li.appendChild(div)
        if (!description == "") {
          let taskDescription = document.createElement("div");
          taskDescription.innerText = description;
          taskDescription.classList.add('text-muted')
          taskDescription.classList.add('ms-5')
          let br = document.createElement("br");
          li.appendChild(taskDescription)
        }

        let hr = document.createElement("hr");
        li.appendChild(hr)

        newProjTasks.appendChild(li);

        newTaskNoProjForm.newTaskTitle.value = ''
        newTaskNoProjForm.newTaskDescription.value = ''
        newTaskNoProjForm.new_task_due_date.value = ''
        newTaskNoProjForm.new_task_due_date_time.value = ''
        newTaskNoProjForm.newTaskPriority.value = 'None'

        numProjTasks.value = document.querySelectorAll('#newProjTasks li').length
      })
    })
}

function deleteTask(task) {

  var numProjTasks = document.getElementById('numProjTasks')
  let delTask = task.value

  var task_id = {
    task: delTask
  }

  fetch(`/delete_task/${delTask}`, {
      method: 'POST',
      credentials: "include",
      body: JSON.stringify(task_id),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
    .then(function (response) {
      if (response.status !== 200) {
        console.log(`Response status was not 200:, ${response.status}`);
        return;
      }
      response.json().then(function (data) {
        let delTaskLi = document.getElementById("task" + delTask)
        delTaskLi.remove();

        numProjTasks.value = document.querySelectorAll('#newProjTasks li').length

      })
    })

}

function addTruncate(elem) {
  if (!elem.classList.contains('text-truncate')) {
    elem.classList.add('text-truncate')
  }
}

function toggleProjectView(elem) {
  var projectCards = document.querySelectorAll("#projectCard")
  var projectSmalls = document.querySelectorAll("#projectSmall")

  if ((projectSmalls) && (projectCards)) {
    if (elem.value == 'big') {
      for (let i = 0; i < projectSmalls.length; i++) {
        console.log(projectSmalls.length)
        if (!projectSmalls[i].classList.contains("d-none")) {
          projectSmalls[i].classList.add("d-none")
        }
      }
      for (let i = 0; i < projectCards.length; i++) {
        if (projectCards[i].classList.contains("d-none")) {
          projectCards[i].classList.remove("d-none")
        }
      }
    }

    if (elem.value == 'small') {
      for (let i = 0; i < projectSmalls.length; i++) {
        if (projectSmalls[i].classList.contains("d-none")) {
          projectSmalls[i].classList.remove("d-none")
        }
      }
      for (let i = 0; i < projectCards.length; i++) {
        if (!projectCards[i].classList.contains("d-none")) {
          projectCards[i].classList.add("d-none")
        }
      }
    }

  }


}

function removeTruncate(elem) {
  if (elem.classList.contains('text-truncate')) {
    elem.classList.remove('text-truncate')
  } else {
    elem.classList.add('text-truncate')
  }
}

function handleThis(radio, model, id, column) {
  console.log(radio.value)

  var showOptions = document.getElementById(model + id + column);

  console.log("showOptions", showOptions)
  if (radio.value == "true") {
    console.log("SHOWING")
    showOptions.classList.remove("d-none")
  }
  if (radio.value == "false") {
    console.log("Not SHOWING")
    showOptions.classList.add("d-none")
  }


}

function showChange(elem) {

  if (elem.nextElementSibling) {
    if (elem.value == "") {
      if (!elem.nextElementSibling.classList.contains('d-none')) {
        elem.nextElementSibling.classList.add('d-none')
      }
    } else {
      if (elem.nextElementSibling.classList.contains('d-none')) {
        elem.nextElementSibling.classList.remove('d-none')
      }
    }
  }
}

function showOptions(modal, id, column, options) {
  var optionsToShow = document.getElementById(options + id);
  var optionsToShowValue = document.getElementById(modal + column)

  if (optionsToShow.classList.contains('d-none')) {
    optionsToShow.classList.remove('d-none')
  }
}