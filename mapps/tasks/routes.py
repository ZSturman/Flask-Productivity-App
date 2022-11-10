from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, make_response, jsonify, flash
from flask_login import current_user
from mapps import db
from mapps.models import Task, User, Project, Update
from mapps.main.utils import convert_for_model, redirect_url


tasks = Blueprint('tasks', __name__)


@tasks.route('/add_task/<int:project_id>', methods=['POST'])
def add_task(project_id):
    if project_id == None:
        project = None
    else: 
        project = Project.query.get_or_404(project_id)
    title = request.form.get("add-title")
    if title == "" or title == None:
        flash("Task Title cannot be left blank", "warning")
    else:
        description=request.form.get("description")
        new_task = Task(author=current_user, title=title, description=description, complete=False, deleted=False, priority=0)
        new_update = Update(author=current_user)
        db.session.add(new_task)
        db.session.add(new_update)
        project.tasks.append(new_task)
        project.updates.append(new_update)
        db.session.commit()
        return redirect(redirect_url())



@tasks.route('/add_task_no_project', methods=['POST'])
def add_task_no_project():
    if request.get_json():
        req = request.get_json()
        title = req['title']
        if title == "" or title == None:
            return 
        else:
            description = req['description']
            due_date = req['due_date']
            priority = req['priority']
            if due_date == None or due_date=='':
                due_date = None
            else:
                if len(due_date) == 19:
                    due_date=convert_for_model(due_date)
                elif len(due_date) == 14:
                    due_date = due_date[0:10]
                    due_date=convert_for_model(due_date)
                elif len(due_date) < 10:
                    due_date = None
            if priority == None:
                pass
            else:
                priority = priority
            new_task = Task(author=current_user, title=title, description=description, complete=False, deleted=False, priority=priority, due_date=due_date)
            db.session.add(new_task)
            db.session.commit()
            req.update({"id":new_task.id})
            res = make_response(jsonify(req), 200)
            print("req", req)
            print("res",res)
            
            return res


    

@tasks.route("/delete_task/<int:task_id>", methods=['POST'])
def delete_task(task_id):
    if request.get_json():
        req = request.get_json()
        task_item = Task.query.get_or_404(task_id)
        db.session.delete(task_item)
        db.session.commit()
        res = make_response(jsonify(req), 200)
        return res

@tasks.route("/delete_proj_task/<int:task_id>", methods=['POST'])
def delete_task_from_proj(task_id):
    print("task_id", task_id)
    if request.method == 'POST':
        task_item = Task.query.get_or_404(task_id)
        db.session.delete(task_item)
        db.session.commit()
        return redirect(redirect_url())


@tasks.route("/complete_task/<int:task_id>", methods=['POST'])
def complete_task(task_id):
    task_item = Task.query.get_or_404(task_id)
    task_item.complete = True
    db.session.commit()
    return redirect(redirect_url())

@tasks.route("/undo_task/<int:task_id>")
def undo_task(task_id):
    task_item = Task.query.get_or_404(task_id)
    task_item.complete = False
    task_item.deleted = False
    db.session.commit()
    return redirect(redirect_url())




@tasks.route("/update_task/<int:task_id>", methods=['POST'])
def update_task(task_id):
    task_item = Task.query.get_or_404(task_id)
    title = request.form.get("editTaskTitle")
    description = request.form.get("editTaskDescription")
    due_date = request.form.get("editTaskDueDate")
    due_date_time = request.form.get("editTaskDueDateTime")
    priority = request.form.get("editTaskPriority")
    no_due_date = request.form.get("no_due_date")

    if title == "":
        pass
    else:
        task_item.title = title
    if description == "":
        pass
    else:
        task_item.description = description
    if priority == None:
        pass
    else:
        task_item.priority = priority
    if no_due_date == "on":
        task_item.due_date = None
    elif due_date == None or due_date=='':
        task_item.due_date = None
    else:
        due_date=convert_for_model(due_date)
        task_item.due_date = due_date
    db.session.commit()
    return redirect(redirect_url())
