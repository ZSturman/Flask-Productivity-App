


















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



function addCurSelListToPrev(currentList, previousList) {
  /* console.log("0000") */
  for (let i = 0; i < currentList.Length; i++) {
    previousList.push(currentList[i]);
  }
  currentList = [];
  return currentList;
}

function addCurSelNotesListToPrev(currentNotesList, previousNotesList) {
  /* console.log("0000") */
  for (let i = 0; i < currentNotesList.Length; i++) {
    previousNotesList.push(currentNotesList[i]);
  }
  currentNotesList = [];
  return currentNotesList;
}

let currentlySelectedProj;
let previouslySelectedProj;
let prevSel;
let prevSelUpd = [];
let currSelUpd = [];

let prevSelNotes = [];
let currSelNotes = [];
let prevSelNote = [];
let currSelNote = [];

/* (___, ____, nested.id, nested.updates) */
function setActive(color1, color2, proj_id, updates_list, notes_list) {

  /* send currently selected to previously selected */
  /* clear out currently selected */
  currSelUpd = addCurSelListToPrev(currSelUpd, prevSelUpd)
  currSelNote = addCurSelNotesListToPrev(currSelNote, prevSelNote)

  if (currentlySelectedProj != proj_id) {
    previouslySelectedProj = currentlySelectedProj;
    currentlySelectedProj = proj_id;
  }


  if (prevSel === proj_id) {
    console.log("same. previously selected =" + prevSel);
  } else {
    previousProj = document.getElementById("proj-" + prevSel);

    if (previousProj === null) {
      console.log("previousProj = null")
    } else {
      previousProj.classList.remove("panel-project-selected", "sticky-top", "sticky-bottom", "border-end-0",
        "display-6");
      previousProj.classList.add("ms-4", "panel-project", "h2", "fw-light");
    }
    prevSel = proj_id;
    /* console.log("new previously selected = " + prevSel) */
  }


  replaced_notes_list = notes_list.replaceAll('[', '')
  replaced_notes_list = replaced_notes_list.replaceAll(']', '')
  selProjNotesList = replaced_notes_list.replaceAll('Note("', '')
  selProjNotesList = selProjNotesList.replaceAll('")', '')
  selProjNotesList = selProjNotesList.split(", ")

  console.log("NOTES 2 ", selProjNotesList)



  for (let i = 0; i < selProjNotesList.length; i++) {

    var projNote = document.getElementById("note" + proj_id + selProjNotesList[i])

    console.log("projNote", projNote);

    if (projNote) {
      if (projNote.classList.contains("remove") || !projNote.classList.contains("add")) {
        projNote.classList.add("add");
        projNote.classList.remove("remove");
      }

      prevSelNotes.push(selProjNotesList[i]);
      currSelNotes.push(selProjNotesList[i]);
    }
  }

  console.log("prevSelNotes", prevSelNotes)
  console.log("currSelNotes", currSelNotes)







  /* START NOTES */





  for (let i = 0; i < selProjNotesList.length; i++) {

    function checkCurrenlySelectedNotes(noteItem) {
      if (currSelNote.includes(noteItem)) {
        console.log("currently selected list contains note item")
      } else {
        console.log("pushing note item to currently selected list")
        currSelNote.push(noteItem);
      }
    }

    checkCurrenlySelectedNotes(selProjNotesList[i]);
    console.log("currSelNote", currSelNote)


    function checkPreviouslySelectedNotes(noteItem) {
      if (prevSelNote.includes(noteItem)) {
        console.log("removing note item from previously selected")
        var prevSelNoteIndex = prevSelNote.indexOf(noteItem);
        if (prevSelNoteIndex > -1) {
          prevSelNote.splice(prevSelNoteIndex, 1)
        }
      } else {
        console.log("previously selected does not contain note item")
      }
    }

    checkPreviouslySelectedNotes(selProjNotesList[i]);

    /* set previously selected items to hidden */

    function setPreviouslySelectedNoteItemToHidden() {

      for (let i = 0; i < prevSelNote.length; i++) {
        var noteHTMLItem = document.getElementById("note-item" + prevSelNote[i]);
        if (noteHTMLItem) {
          if (noteHTMLItem.classList.contains("add") || !noteHTMLItem.classList.contains("remove")) {
            noteHTMLItem.classList.remove("add");
            noteHTMLItem.classList.add("remove");
          }

        }

      }
    }

    setPreviouslySelectedNoteItemToHidden()


    /* set currently selected items to show */

    function setCurrentlySelectedNoteItemToShow() {

      for (let i = 0; i < currSelNote.length; i++) {
        var noteHTMLItem = document.getElementById("note-item" + currSelNote[i]);
        if (noteHTMLItem) {
          if (noteHTMLItem.classList.contains("remove") || !noteHTMLItem.classList.contains("add")) {
            noteHTMLItem.classList.remove("remove");
            noteHTMLItem.classList.add("add");
          }

        }

      }
    }

    setCurrentlySelectedNoteItemToShow()


    /* add currenly selected items to previously selected  */

    function addCurrentlySelectedNoteToPreviouslySelected() {

      for (let i = 0; i < currSelNote.length; i++) {
        if (prevSelNote.includes(currSelNote[i])) {
          console.log("previously selected includes currently selected [i]")
        } else {
          prevSelNote.push(currSelNote[i])
        }
      }
    }

    addCurrentlySelectedNoteToPreviouslySelected()
    console.log("prevSelNote", prevSelNote);

    /* reset currently selected to empty */

    function clearCurrentlySelectedNoteList() {

      for (let i = 0; i < selProjNotesList; i++) {
        if (currSelNote.includes(selProjNotesList[i])) {
          console.log("current includes selProjNotesList[i]")
        } else {
          var currSelNoteIndexToDelete = currSelNote.indexOf(i);
          if (currSelNoteIndexToDelete > -1) {
            currSelNote.splice(curSelNoteIndexToDelete, 1)
          }
        }
      }

      return currSelNote;
    }

    currSelNote = clearCurrentlySelectedNoteList();
    console.log("currSelNote", currSelNote);


  }



  replaced_list = updates_list.replaceAll('[', '')
  replaced_list = replaced_list.replaceAll(']', '')
  selProjUpdList = replaced_list.replaceAll('<Updates ', '')
  selProjUpdList = selProjUpdList.replaceAll('>', '')
  selProjUpdList = selProjUpdList.split(", ")


  for (let i = 0; i < selProjUpdList.length; i++) {

    function checkCurrenlySelected(updateItem) {
      if (currSelUpd.includes(updateItem)) {
        console.log("currently selected list contains update item")
      } else {
        console.log("pushing update item to currently selected list")
        currSelUpd.push(updateItem);
      }
    }

    checkCurrenlySelected(selProjUpdList[i]);
    console.log("currSelUpd", currSelUpd)


    /* check if previously selected contains i */
    /* if SO, remove i */

    function checkPreviouslySelected(updateItem) {
      if (prevSelUpd.includes(updateItem)) {
        console.log("removing update item from previously selected")
        var prevSelUpdIndex = prevSelUpd.indexOf(updateItem);
        if (prevSelUpdIndex > -1) {
          prevSelUpd.splice(prevSelUpdIndex, 1)
        }
      } else {
        console.log("previously selected does not contain update item")
      }
    }

    checkPreviouslySelected(selProjUpdList[i]);

    /* set previously selected items to hidden */

    function setPreviouslySelectedItemToHidden() {

      for (let i = 0; i < prevSelUpd.length; i++) {
        var updHTMLItem = document.getElementById("update-item" + prevSelUpd[i]);
        if (updHTMLItem.classList.contains("add") || !updHTMLItem.classList.contains("remove")) {
          updHTMLItem.classList.remove("add");
          updHTMLItem.classList.add("remove");
        }
      }
    }

    setPreviouslySelectedItemToHidden()


    /* set currently selected items to show */

    function setCurrentlySelectedItemToShow() {

      for (let i = 0; i < currSelUpd.length; i++) {
        var updHTMLItem = document.getElementById("update-item" + currSelUpd[i]);
        if (updHTMLItem){
          if (updHTMLItem.classList.contains("remove") || !updHTMLItem.classList.contains("add")) {
            updHTMLItem.classList.remove("remove");
            updHTMLItem.classList.add("add");
          }

        }
       
      }
    }

    setCurrentlySelectedItemToShow()


    /* add currenly selected items to previously selected  */

    function addCurrentlySelectedToPreviouslySelected() {

      for (let i = 0; i < currSelUpd.length; i++) {
        if (prevSelUpd.includes(currSelUpd[i])) {
          console.log("previously selected includes currently selected [i]")
        } else {
          prevSelUpd.push(currSelUpd[i])
        }
      }
    }

    addCurrentlySelectedToPreviouslySelected()
    console.log("prevSelUpd", prevSelUpd);

    /* reset currently selected to empty */

    function clearCurrentlySelectedList() {

      for (let i = 0; i < selProjUpdList; i++) {
        if (currSelUpd.includes(selProjUpdList[i])) {
          console.log("current includes selProjUpdList[i]")
        } else {
          var curSelUpdIndexToDelete = currSelUpd.indexOf(i);
          if (curSelUpdIndexToDelete > -1) {
            curSelUpd.splice(curSelUpdIndexToDelete, 1)
          }
        }
      }

      return currSelUpd;
    }

    currSelUpd = clearCurrentlySelectedList();
    console.log("currSelUpd", currSelUpd);


  }




  var activeProj = document.getElementById("proj-" + proj_id);
  var selectedArea = document.getElementById("selectedArea");

  activeProj.classList.add("panel-project-selected", "sticky-top", "sticky-bottom", "border-end-0", "display-6")
  activeProj.classList.remove("ms-4", "panel-project", "h2", "fw-light")

  console.log("active proj", activeProj)

  selectedArea.style.backgroundColor = color2;
  selectedArea.style.border = "5px solid " + color1;

  var selectedProjLi = document.getElementById("proj-" + proj_id)

  if (selectedProjLi.id == activeProj.id) {
    selectedProjLi.classList.remove("remove")
  }







  var entry = {
    id: proj_id
  };

  fetch('/home2/select-proj', {
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

      response.json().then(function (project) {
        let selectedProject = document.getElementById("selected-project" +
          currentlySelectedProj);

        let previouslySelectedProject = document.getElementById("selected-project" +
          previouslySelectedProj);

        console.log("selectedProject", selectedProject)
        console.log("previouslySelectedProject", previouslySelectedProject)



        selectedProject.classList.remove("remove");
        selectedProject.classList.add("add");
        if (previouslySelectedProject) {
          previouslySelectedProject.classList.remove("add");
          previouslySelectedProject.classList.add("remove");

        }

      })

    })

}











function updateData(id, updatedData, oldData, dataModel, dataColumn, dataParent) {

  var dataUpdated = {
    id: id,
    oldData: oldData,
    updatedData: updatedData,
    dataModel: dataModel,
    dataColumn: dataColumn,
    dataParent: dataParent
  };
  $.ajax({
    type: "POST",
    url: "/updating",
    data: dataUpdated
  })

} 


function onBlurFunction(id, model, column) {

  let editData = document.getElementById("update-element" + id + model, column);

  dataModel = editData.dataset.model;
  dataColumn = editData.dataset.column;

  dataParent = editData.dataset.parent;

  if (!dataParent) {
    dataParent = id;
  }

  console.log("editData", editData)
  console.log("dataModel", dataModel)
  console.log("dataColumn", dataColumn)
  console.log("dataParent", dataParent)


  var hiddenTextArea = document.getElementById("hiddenTextarea" + id + dataModel);

  var completedCheckOne = document.getElementById("completed-check-" + id + dataModel + "-one");
  var completedCheckTwo = document.getElementById("completed-check-" + id + dataModel + "-two");


  if (completedCheckOne) {
    completedCheckOne.classList.remove("remove")
  }
  if (completedCheckTwo) {
    completedCheckTwo.classList.remove("remove")
  }

  editData.classList.remove("text-muted")

  hiddenTextArea.value = editData.innerText;

  var updatedData = hiddenTextArea.value;

  editData.contentEditable = true;

  updateData(id, updatedData, oldData, dataModel, dataColumn, dataParent);
}
 


function onFocusFunction(id, model) {

  let completedCheckOne = document.getElementById("completed-check-" + id + model + "-one");
  let completedCheckTwo = document.getElementById("completed-check-" + id + model + "-two");

  console.log("completedCheckOne", completedCheckOne)
  console.log("completedCheckTwo", completedCheckTwo)


  let editData = document.getElementById("update-element" + id + model);

  editData.classList.add("text-muted")

  console.log("editData.innerText", editData.innerText)
  oldData = editData.innerText;

  if (completedCheckOne) {
    completedCheckOne.classList.add("remove")
  }
  if (completedCheckTwo) {
    completedCheckTwo.classList.add("remove")
  }



  editData.addEventListener('keypress', function (e) {
    if (e.key == 'Enter') {
      e.preventDefault();
      e.stopPropagation();
      editData.contentEditable = false;
      onBlurFunction(id, model, oldData)
    }
  })

}
 





function newUpdateData(id, updatedData, oldData, dataModel, dataColumn, dataParent) {

  console.log('update data updateElement', updatedData)
  console.log('update data dataModel', dataModel)
  console.log('update data dataColumn', dataColumn)
  console.log('update data dataParent', dataParent)
  console.log('update data oldData', oldData)

  var dataUpdated = {
    id: id,
    oldData: oldData,
    updatedData: updatedData,
    dataModel: dataModel,
    dataColumn: dataColumn,
    dataParent: dataParent
  };
  $.ajax({
    type: "POST",
    url: "/updating",
    data: dataUpdated
  })

}
 
function newOnBlurFunction(id, model, column) {

  var updateElement = document.getElementById('update-' + model + id + column)
  console.log("2222222222222", updateElement)

  if (!updateElement) {
    console.log("On blur already ran")
  } else {

    dataModel = updateElement.dataset.model;
    dataColumn = updateElement.dataset.column;
    dataParent = updateElement.dataset.parent;
    oldData = updateElement.dataset.olddata;

    if (oldData == "") {
      oldData = "None";
    }

    var hiddenTextArea = document.getElementById("hiddenTextarea-" + model + id + column);

    hiddenTextArea.innerText = updateElement.innerText;
    var updatedData = hiddenTextArea.innerText;

    updateElement.contentEditable = true;

    newUpdateData(id, updatedData, oldData, dataModel, dataColumn, dataParent);


  }
} 

function newOnFocus(id, model, column) {
  var updateElement = document.getElementById('update-' + model + id + column)
  dataModel = updateElement.dataset.model;
  dataColumn = updateElement.dataset.column;
  dataParent = updateElement.dataset.parent;
  oldData = updateElement.dataset.olddata;

  if (oldData == "") {
    oldData = "None";
  }

  if (dataColumn == 'title') {
    console.log("dataColumn = title")

    updateElement.classList.add('text-muted')

    let completedChecked = document.getElementById("update-" + model + id + "complete-checked")
    let completedNotChecked = document.getElementById("update-" + model + id + "complete-not-checked")

    if (completedChecked) {
      completedChecked.classList.add("remove");
    }
    if (completedNotChecked) {
      completedNotChecked.classList.add("remove");
    }

    updateElement.addEventListener('keypress', function (e) {
      if (e.key == 'Enter') {
        e.preventDefault();
        e.stopPropagation();
        updateElement.contentEditable = false;
        newOnBlurFunction(id, model, column)
        if (completedChecked) {
          completedChecked.classList.remove("remove");
        }
        if (completedNotChecked) {
          completedNotChecked.classList.remove("remove");
        }
        updateElement.classList.remove('text-muted')

      }
    })
  }


  if (column == 'description' || column == 'description-one') {
    console.log("dataColumn = description")

    updateElement.classList.add('text-muted')

    updateElement.addEventListener('keypress', function (e) {
      if (e.key == 'Enter') {
        e.stopPropagation();
        updateElement.contentEditable = false;
        newOnBlurFunction(id, model, column)
        updateElement.classList.remove('text-muted')
      }
    })
  }
} 

function updateOnClick(id, model, column) {
  var updateElement = document.getElementById('update-' + model + id + column)
  dataModel = updateElement.dataset.model;
  dataColumn = updateElement.dataset.column;
  dataParent = updateElement.dataset.parent;
  oldData = updateElement.dataset.olddata;

  console.log('updateElement', updateElement)
  console.log('dataModel', dataModel)
  console.log('dataColumn', dataColumn)
  console.log('dataParent', dataParent)
  console.log('oldData', oldData)

  if (dataColumn == "complete") {
    if (oldData == "False") {
      var updatedData = "True";
      newUpdateData(id, updatedData, oldData, dataModel, dataColumn, dataParent);
    }
    if (oldData == "True") {
      var updatedData = "False";
      newUpdateData(id, updatedData, oldData, dataModel, dataColumn, dataParent);
    }
  }

  if (dataColumn == "due_date") {
    if (updateElement.value == '') {
      var updatedData = "None";
    } else {
      var updatedData = updateElement.value;
    }
    newUpdateData(id, updatedData, oldData, dataModel, dataColumn, dataParent);

    var addDueDateBtn1 = document.getElementById('addProjectDueDateBtn' + id + "-one");
    var addDueDateBtn2 = document.getElementById('addProjectDueDateBtn' + id + "-two");
    var editableDueDateOne = document.getElementById('projDueDate' + id + 'Edit1');
    var editableDueDateTwo = document.getElementById('projDueDate' + id + 'Edit2');

    if (editableDueDateOne) {

      if (editableDueDateOne.classList.contains("add") || !editableDueDateOne.classList.contains("remove")) {
        editableDueDateOne.classList.remove("add");
        editableDueDateOne.classList.add("remove");

      }
    }
    if (editableDueDateTwo) {

      if (editableDueDateTwo.classList.contains("add") || !editableDueDateTwo.classList.contains("remove")) {
        editableDueDateTwo.classList.remove("add");
        editableDueDateTwo.classList.add("remove");

      }
    }
    if (addDueDateBtn1) {

      if (addDueDateBtn1.classList.contains("remove") || !addDueDateBtn1.classList.contains("add")) {
        addDueDateBtn1.classList.remove("remove");
        addDueDateBtn1.classList.add("add");

      }
    }
    if (addDueDateBtn2) {

      if (addDueDateBtn2.classList.contains("remove") || !addDueDateBtn2.classList.contains("add")) {
        addDueDateBtn2.classList.remove("remove");
        addDueDateBtn2.classList.add("add");

      }
    }
  }

} 

function revealInputs(id, model, column) {

  var addDescriptionBtn = document.getElementById('add-' + model + '-' + id + '-btns-for-' + column)
  var editableDescription = document.getElementById('update-' + model + id + column + '-one');


  var addDueDateBtn1 = document.getElementById('add-' + model + '-' + id + '-btns-for-' + column + "-one");
  var addDueDateBtn2 = document.getElementById('add-' + model + '-' + id + '-btns-for-' + column + "-two");
  var editableDueDateOne = document.getElementById('projDueDate' + id + 'Edit1');
  var editableDueDateTwo = document.getElementById('projDueDate' + id + 'Edit2');


  if (addDescriptionBtn) {
    if (addDescriptionBtn.classList.contains("add") || !addDescriptionBtn.classList.contains("remove")) {
      addDescriptionBtn.classList.remove("add");
      addDescriptionBtn.classList.add("remove");
    }
  }
  if (editableDescription) {
    if (editableDescription.classList.contains("remove") || !editableDescription.classList.contains("add")) {
      editableDescription.classList.remove("remove");
      editableDescription.classList.add("add");
    }
  }
  



  if (editableDueDateOne) {
    if (editableDueDateOne.classList.contains("remove") || !editableDueDateOne.classList.contains("add")) {
      editableDueDateOne.classList.remove("remove");
      editableDueDateOne.classList.add("add");
    }
  }
  if (editableDueDateTwo) {
    if (editableDueDateTwo.classList.contains("remove") || !editableDueDateTwo.classList.contains("add")) {
      editableDueDateTwo.classList.remove("remove");
      editableDueDateTwo.classList.add("add");
    }
  }
  if (addDueDateBtn1) {
    if (addDueDateBtn1.classList.contains("add") || !addDueDateBtn1.classList.contains("remove")) {
      addDueDateBtn1.classList.remove("add");
      addDueDateBtn1.classList.add("remove");
    }
  }
  if (addDueDateBtn2) {
    if (addDueDateBtn2.classList.contains("add") || !addDueDateBtn2.classList.contains("remove")) {
      addDueDateBtn2.classList.remove("add");
      addDueDateBtn2.classList.add("remove");
    }
  }


}

function revealChildInputs(id, model, column) {


  var addChildBtn = document.getElementById('add-'+model + '-' + id + '-btns-for-' + column )
  var childrenDropdown = document.getElementById('projChild' + id + 'Edit');
  
  
  if (addChildBtn) {
    if (addChildBtn.classList.contains("add") || !addChildBtn.classList.contains("remove")) {
      addChildBtn.classList.remove("add");
      addChildBtn.classList.add("remove");
    }
  }
  if (childrenDropdown) {
    if (childrenDropdown.classList.contains("remove") || !childrenDropdown.classList.contains("add")) {
      childrenDropdown.classList.remove("remove");
      childrenDropdown.classList.add("add");
    }
  }


}



function revealInputArea(id, model, column){
  var addBtn = document.getElementById("add-"+model+id+column);
  var updateArea = document.getElementById("update-"+model+id+column)

  addBtn.classList.add("remove");
  addBtn.classList.remove("add");

  updateArea.classList.add("add");
  updateArea.classList.remove("remove");

  updateArea.contentEditable=true;

}










window.onload = function () {

  var onLoadProjCCDark = document.getElementById("recUpdProj-cc-bg-dark").innerText;
  var onLoadProjCCLight = document.getElementById("recUpdProj-cc_bg_light").innerText;
  var onLoadProjCCID = document.getElementById("recUpdProj-id").innerText;
  var onLoadProjCCUpdates = document.getElementById("recUpdProj-updates").innerText;
  var onLoadProjCCNote = document.getElementById("recUpdProj-note").innerText;

  setActive(onLoadProjCCDark, onLoadProjCCLight, onLoadProjCCID, onLoadProjCCUpdates, onLoadProjCCNote);
};








































/* ------------------------------------------------------------






FOR OLD PROJECTS PAGE 






--------------------------------------------------------------*/






















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
  column = column.toLowerCase();
  column = column.replace(/[a-z]/g, '');


  var projTitle = document.getElementById("projTitle" + column);
  var projTitleInput = document.getElementById("projTitle" + column + "Edit");


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