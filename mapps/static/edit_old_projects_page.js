


















function showSaveBtns(id) {

  console.log("showSaveBtns");

  /* IF multiple save buttons on projects (such as proj 1 and proj 2) have a modal pop up that asks if you want to save changes to all edied projects or just the one */

  var saveBtn = document.getElementById("saveChangesBtnGroup" + id);

  if (saveBtn.classList.contains("remove") || !saveBtn.classList.contains("add")) {
    saveBtn.classList.remove("remove");
    saveBtn.classList.add("add");
  }

}

function editProjTitle(column) {

  console.log("editProjTitle");

  console.log("1 the column number is", column)


  column = column.toLowerCase();
  column = column.replace(/[a-z]/g, '');

  console.log("2 the column number is", column)


  var projTitle = document.getElementById("projTitle" + column);
  var projTitleInput = document.getElementById("projTitle" + column + "Edit");

  console.log("projTitle", projTitle);
  console.log("projTitleInput", projTitleInput);

  if (projTitle.classList.contains("add") || !projTitle.classList.contains("remove")) {
    projTitle.classList.remove("add");
    projTitle.classList.add("remove");
  }
  if (projTitleInput.classList.contains("remove") || !projTitleInput.classList.contains("add")) {
    projTitleInput.classList.remove("remove");
    projTitleInput.classList.add("add");
  }


  showSaveBtns(column);

}

function editProjDueDate(column) {

  console.log("editProjDueDate");
  console.log(column)

  var projDueDate = document.getElementById("projDueDate" + column);
  var projDueDateInput = document.getElementById("projDueDate" + column + "Edit");

  console.log("projDueDate", projDueDate);
  console.log("projDueDateInput", projDueDateInput);

  if (projDueDate) {
    if (projDueDate.classList.contains("add") || !projDueDate.classList.contains("remove")) {
      projDueDate.classList.remove("add");
      projDueDate.classList.add("remove");
    }

  }

  if (projDueDateInput.classList.contains("remove") || !projDueDateInput.classList.contains("add")) {
    projDueDateInput.classList.remove("remove");
    projDueDateInput.classList.add("add");
  }


  showSaveBtns(column);
}

function editProjDescription(column) {

  console.log("editProjDescription");

  console.log(column);

  var projDescription = document.getElementById("projDescription" + column);
  var projDescriptionInput = document.getElementById("projDescription" + column + "Edit");

  console.log("projDescription", projDescription);
  console.log("projDescriptionInput", projDescriptionInput);

  if (projDescription.classList.contains("add") || !projDescription.classList.contains("remove")) {
    projDescription.classList.remove("add");
    projDescription.classList.add("remove");
  }
  if (projDescriptionInput.classList.contains("remove") || !projDescriptionInput.classList.contains("add")) {
    projDescriptionInput.classList.remove("remove");
    projDescriptionInput.classList.add("add");
  }

  showSaveBtns(column);

}

function editProjCustom(column) {
  console.log("editProjCustom");

  var projCustomInput = document.querySelectorAll("#projCustom" + column + "Edit");

  console.log(projCustomInput)

  for (let i = 0; i < projCustomInput.length; i++) {
    projCustomInput[i]
    if (projCustomInput[i].classList.contains("remove") || !projCustomInput[i].classList.contains("add")) {
      projCustomInput[i].classList.add("add");
      projCustomInput[i].classList.remove("remove");
    }
  }


  showSaveBtns(column);

}

function editProjTime(column) {
  console.log("editProjTime");

  var projTime = document.querySelectorAll("#projTime" + column);
  var projTimeInput = document.querySelectorAll("#projTime" + column + "Edit");


  for (let i = 0; i < projTime.length; i++) {
    if (projTime[i].classList.contains("add") || !projTime[i].classList.contains("remove")) {
      projTime[i].classList.remove("add");
      projTime[i].classList.add("remove");
    }
  }

  for (let i = 0; i < projTimeInput.length; i++) {
    if (projTimeInput[i].classList.contains("remove") || !projTimeInput[i].classList.contains("add")) {
      projTimeInput[i].classList.add("add");
      projTimeInput[i].classList.remove("remove");
    }
  }

  showSaveBtns(column);

}

function showProjProg(column) {
  console.log("showProjProg");

  var projShowProgress = document.getElementById("showProgress");
  var projHideProgress = document.getElementById("hideProgress");
  var projProgress = document.getElementById("projProg" + column);


  if (projShowProgress.classList.contains("add") || projProgress.classList.contains("remove")) {
    projShowProgress.classList.remove("add")
    projShowProgress.classList.add("remove")
    projHideProgress.classList.add("add")
    projHideProgress.classList.remove("remove")
    projProgress.classList.add("add")
    projProgress.classList.remove("remove")
  }
}

function hideProjProg(column) {
  console.log("hideProjProg");

  var projShowProgress = document.getElementById("showProgress");
  var projHideProgress = document.getElementById("hideProgress");
  var projProgress = document.getElementById("projProg" + column);

  if (projHideProgress.classList.contains("add") || projProgress.classList.contains("add")) {
    projShowProgress.classList.remove("remove")
    projShowProgress.classList.add("add")
    projHideProgress.classList.remove("add")
    projHideProgress.classList.add("remove")
    projProgress.classList.remove("add")
    projProgress.classList.add("remove")
  }


}

function editProjTopic(column) {
  console.log("editProjTopic");



  var projTopic = document.getElementById("projTopic" + column);
  var projSubtopic = document.getElementById("projSubtopic" + column);
  var projSubject = document.getElementById("projSubject" + column);
  var projTopicInput = document.getElementById("projTopic" + column + "Edit");
  var projSubtopicInput = document.getElementById("projSubtopic" + column + "Edit");
  var projSubjectInput = document.getElementById("projSubject" + column + "Edit");

  console.log("projTopic", projTopic);
  console.log("projSubtopic", projSubtopic);
  console.log("projSubject", projSubject);
  console.log("projTopicInput", projTopicInput);
  console.log("projSubtopicInput", projSubtopicInput);
  console.log("projSubjectInput", projSubjectInput);

  if (projTopic !== null) {
    if (projTopic.classList.contains("add") || !projTopic.classList.contains("remove")) {
      projTopic.classList.remove("add");
      projTopic.classList.add("remove");
    }
  }
  if (projTopicInput.classList.contains("remove") || !projTopicInput.classList.contains("add")) {
    projTopicInput.classList.remove("remove");
    projTopicInput.classList.add("add");
  }

  if (projSubtopic !== null) {
    if (projSubtopic.classList.contains("add") || !projSubtopic.classList.contains("remove")) {
      projSubtopic.classList.remove("add");
      projSubtopic.classList.add("remove");
    }
  }
  if (projSubtopicInput.classList.contains("remove") || !projSubtopicInput.classList.contains("add")) {
    projSubtopicInput.classList.remove("remove");
    projSubtopicInput.classList.add("add");
  }
  if (projSubtopic !== null) {
    if (projSubject.classList.contains("add") || !projSubject.classList.contains("remove")) {
      projSubject.classList.remove("add");
      projSubject.classList.add("remove");
    }
  }
  if (projSubjectInput.classList.contains("remove") || !projSubjectInput.classList.contains("add")) {
    projSubjectInput.classList.remove("remove");
    projSubjectInput.classList.add("add");
  }

  showSaveBtns(column);

}

function editProjNote(column) {
  console.log("editProjNote");

  var projNote = document.querySelectorAll("#projNote" + column);
  var projNoteInput = document.querySelectorAll("#projNote" + column + "Edit");


  for (let i = 0; i < projNote.length; i++) {
    console.log("1")
    if (projNote[i].classList.contains("add") || !projNote[i].classList.contains("remove")) {
      projNote[i].classList.remove("add");
      projNote[i].classList.add("remove");
    }
  }

  for (let i = 0; i < projNoteInput.length; i++) {
    console.log("1")
    if (projNoteInput[i].classList.contains("remove") || !projNoteInput[i].classList.contains("add")) {
      projNoteInput[i].classList.add("add");
      projNoteInput[i].classList.remove("remove");
    }
  }

  showSaveBtns(column);

}

function editProjChild(column) {
  console.log("editProjChild");

  var projChildInput = document.querySelectorAll("#projChild" + column + "Edit");
  var projChildTasksInput = document.getElementById("projChildTasks" + column + "Edit");
  var projChildProjectsInput = document.getElementById("projChildProjects" + column + "Edit");

  console.log("0")

  for (let i = 0; i < projChildInput.length; i++) {
    console.log("1")
    if (projChildInput[i].classList.contains("remove") || !projChildInput[i].classList.contains("add")) {
      projChildInput[i].classList.add("add");
      projChildInput[i].classList.remove("remove");
    }
  }
  console.log("2")


  if (projChildTasksInput.classList.contains("remove") || !projChildTasksInput.classList.contains("add")) {
    console.log("3")
    projChildTasksInput.classList.remove("remove");
    projChildTasksInput.classList.add("add");
  }
  if (projChildProjectsInput.classList.contains("remove") || !projChildProjectsInput.classList.contains("add")) {
    console.log("4")
    projChildProjectsInput.classList.remove("remove");
    projChildProjectsInput.classList.add("add");
  }


  showSaveBtns(column);

}

function editAll(id) {

  var allEdits = document.getElementById("proj_" + id);
  editProjTitle(id)
  editProjDueDate(id);
  editProjDescription(id);
  editProjDueDate(id)
  editProjDescription(id)
  editProjCustom(id)
  editProjTime(id)
  editProjTopic(id)
  editProjNote(id)
  editProjChild(id)

  showSaveBtns(id);

}

function submit_entry() {
  var allProjInputs = document.querySelectorAll(".projEditable");
  var allProjPerm = document.querySelectorAll(".projPerm");

  for (let i = 0; i < allProjInputs.length; i++) {
    allProjInputs[i].classList.add("remove");
    allProjInputs[i].classList.remove("add");
  };
  for (let i = 0; i < allProjPerm.length; i++) {
    allProjPerm[i].classList.remove("remove");
    allProjPerm[i].classList.add("add");
  };

}













/* COLOR */

/* HEX to RGB */



function addCustomColor(column, nestedColor) {

  var r = document.querySelector(':root');

  var colorpicker = document.getElementById('update-custom-color');
  var projCustomColorSixty = document.querySelectorAll("#projCustomColor" + column + "Sixty");

  setInterval(() => {
    let color = colorpicker.value;

    for (let i = 0; i < projCustomColorSixty.length; i++) {
      console.log(projCustomColorSixty)
      projCustomColorSixty[i].style.backgroundColor = color;
    }

  }, 200);

}


