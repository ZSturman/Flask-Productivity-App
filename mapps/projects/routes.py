from crypt import methods
from datetime import *
from dateutil.tz import *
from pathlib import Path
from werkzeug.utils import secure_filename
import uuid as uuid
import secrets
import os
import re
from flask import Blueprint, render_template, request, redirect, url_for, make_response, jsonify, flash
from flask_login import current_user
from mapps import db, app
from mapps.models import Pic, Project, User, Session, Label, Update, Task
from mapps.main.utils import *

projects = Blueprint('projects', __name__)


@projects.route("/delete_project/<int:project_id>", methods=['POST'])
def delete_project(project_id):
    if current_user.is_authenticated:
        user = User.query.filter_by(email=current_user.email).first()
        project_item = Project.query.get_or_404(project_id)
        project_item.deleted = True
        new_update = Update(author=user, column='project', message="deleted")
        db.session.add(new_update)
        project_item.updates.append(new_update)
        db.session.commit()
        return redirect(redirect_url())

@projects.route("/complete_project/<int:project_id>")
def complete_project(project_id):
    if current_user.is_authenticated:
        user = User.query.filter_by(email=current_user.email).first()
        project_item = Project.query.get_or_404(project_id)
        project_item.complete = True
        new_update = Update(author=user, column='project', message="completed")
        db.session.add(new_update)
        project_item.updates.append(new_update)
        db.session.commit()
        return redirect(redirect_url())


@projects.route("/undo_project/<int:project_id>")
def undo_project(project_id):
    user = User.query.filter_by(email=current_user.email).first()
    project_item = Project.query.get_or_404(project_id)
    project_item.complete = False
    project_item.deleted = False
    new_update = Update(author=user, column='project', message="put back")
    db.session.add(new_update)
    project_item.updates.append(new_update)
    db.session.commit()
    return redirect(redirect_url())




def add_task(user, project_item, new_task, task_description, task_priority, task_due_date):
    task_due_date = convert_for_model(task_due_date)
    new_task = Task(author=user, title=new_task, description=task_description, due_date=task_due_date, complete=False, deleted=False, priority=task_priority)
    db.session.add(new_task)
    new_task_update = Update(author=user, column='task', message="created")
    db.session.add(new_task_update)
    project_item.tasks.append(new_task)
    project_item.updates.append(new_task_update)
    return new_task


def create_label(user, parent, newLabelName, newLabelIcon, newLabelColor):
    label_name = newLabelName
    icon = newLabelIcon
    color = newLabelColor
    new_label = Label(author=user, name=label_name, color=color, icon=icon)
    db.session.add(new_label)
    parent.labels.append(new_label)
    print(new_label)
    print()
    return new_label

@projects.route("/update_labels/project/<int:project_id>", methods=['POST'])
def update_labels(project_id):
    if current_user.is_authenticated:
        project_item = Project.query.get_or_404(project_id)
        if request.get_json():
            req = request.get_json()
            res = make_response(jsonify(req), 200)
            print(req)
            print("res", res)
            for _,v in req.items():
                proj_label = Label.query.get_or_404(int(v))
                proj_label.projects.append(project_item)
                db.session.commit()
            return res

@projects.route("/remove_labels/project/<int:project_id>", methods=['POST'])
def remove_labels(project_id):
    if current_user.is_authenticated:
        project_item = Project.query.get_or_404(project_id)
        if request.get_json():
            req = request.get_json()
            res = make_response(jsonify(req), 200)
            print(req)
            print("res", res)
            for _,v in req.items():
                proj_label = Label.query.get_or_404(int(v))
                proj_label.projects.remove(project_item)
                db.session.commit()
            return res

allowed_extentions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'svg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extentions

def add_image(user, project_item, img):
    img_filename = secure_filename(img.filename)
    if img_filename == '':
        flash('No selected file')
        return redirect(request.url)
    if img and allowed_file(img_filename):
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(img.filename)
        picture_fn = random_hex + f_ext
        Path("./mapps/static/images/")
        save_img_path = os.path.join('./mapps/static/images/', picture_fn)
        """ Path("./mapps/static/images/", str(user.id)).mkdir(parents=True, exist_ok=True)
        save_img_path = os.path.join('./mapps/static/images/'+str(user.id), picture_fn) """
        img.save(save_img_path)
        newImg = Pic(author=user, filename=picture_fn)
        db.session.add(newImg)
        newImg.project = project_item
        new_img_update = Update(author=user, column='image', message="added")
        db.session.add(new_img_update)
        project_item.updates.append(new_img_update)
        return newImg
    flash("Image upload failed. Please try again", "warning")
    return redirect(redirect_url())

@projects.route('/add_project', methods=['GET','POST'])
def add_project():
    if current_user.is_authenticated:
        today = datetime.utcnow()
        user = User.query.filter_by(email=current_user.email).first()
        title = request.form.get("new_title")
        description = request.form.get("description")
        due_date = request.form.get("new_proj_due_date")
        due_date_time = request.form.get("new_proj_due_date_time")
        priority = request.form.get("priority")
        goal_per = request.form.get('goal-per')
        goal_time = request.form.get('goal-time')
        numProjTasks = request.form.get("numProjTasks")
        projColor = request.form.get("projColor")
        #print(request.form)
        total_seconds = 0
        time_remaining = None
        if 'upload-img' not in request.files:
            new_image = None
        else:
            new_image = request.files['upload-img']

        if goal_time == "" or goal_time == None or goal_time == "0" or goal_time == "1" or goal_time == "51":
            pass
        else:
            goal_time = int(goal_time) - 1

        if goal_per == "" or goal_per == None:
            pass
        elif goal_per == "0":
            goal_per = None
            goal_time = None
        else:
            goal_per = goal_per

        if title == "" or title == None:
            pass
        else:
            title = title
        if description == "":
            pass
        else:
            description = description

        if projColor:
            color = projColor

        
        if due_date == None or due_date=='':
            due_date = None
            late = 0
            upcoming = None
            status = None
        else:
            if due_date_time == None or due_date_time == '':
                due_date_time = time(0)
                due_date = convert_for_model(due_date)
                due_date = datetime.combine(due_date, due_date_time)
            else:
                due_date = str(due_date) + " " + str(due_date_time) + ":00"
                due_date = convert_for_model(due_date)
            late, upcoming, status= check_status(today, due_date)
            total_seconds, time_remaining = check_status(today, due_date, "seconds")
            
        if priority == None:
            pass
        else:
            priority = priority

        new_project = Project(author=user, title=title, description=description, goal_time=goal_time, goal_per=goal_per, last_session=0, due_date=due_date, late=late, upcoming = upcoming, status=status, complete=False, seconds_remaining=total_seconds, time_remaining=time_remaining,  deleted=False, priority=priority, color=color, date_updated = today)
        db.session.add(new_project)

        if new_image:
            add_image(user, new_project, new_image)

        if numProjTasks:
            numProjTasks = int(numProjTasks)
            if numProjTasks > 0:
                add_tasks = Task.query.filter_by(author=user).order_by(Task.date_added.desc()).limit(numProjTasks).all()
                for task in add_tasks:
                    new_project.tasks.append(task)

        new_update = Update(author=user, column=None, message="created")
        db.session.add(new_update)
        new_project.updates.append(new_update)
        db.session.commit()
        return redirect(redirect_url())

@projects.route("/delete_img/<int:project_id>/<int:img_id>", methods=['POST'])
def delete_img(project_id, img_id):
    if current_user.is_authenticated:
        delete_img = request.form.get('projectImageDelete')
        if delete_img == "true":
            project_item = Project.query.get_or_404(project_id)
            img_item = Pic.query.get_or_404(img_id)
            project_item.images.remove(img_item)
            db.session.delete(img_item)
            new_update = Update(author=current_user, column='attachment', message="deleted")
            db.session.add(new_update)
            project_item.updates.append(new_update)
            db.session.commit()
            return redirect(redirect_url())
        return redirect(redirect_url())


@projects.route("/update_project/<int:project_id>", methods=['POST'])
def update_project(project_id):
    if current_user.is_authenticated:
        today = datetime.utcnow()
        today = convert_for_model(today)
        user = User.query.filter_by(email=current_user.email).first()
        project_item = Project.query.get_or_404(project_id)
        title = request.form.get("new_title")
        description = request.form.get("description")
        due_date = request.form.get("editProjectDueDate")
        due_date_time = request.form.get("editProjectDueDateTime")
        no_due_date = request.form.get("no_due_date")
        priority = request.form.get("editProjectPriority")
        goal_per = request.form.get('goal-per')
        goal_time = request.form.get('goal-time')
        last_session = request.form.get('last-session')
        complete = request.form.get('projectComplete')
        deleted = request.form.get('projectDelete')

        newLabelName = request.form.get('labelName')
        newLabelIcon = request.form.get('newLabelIcon')
        newLabelColor = request.form.get('newLabelColor')
        projColor = request.form.get('projColor')

        putBack = request.form.get('putBack')


        if putBack == "true":
            project_item.complete = False
            project_item.deleted = False

        
        projectTaskComplete = request.form.get('projecttask-Complete')

        if projectTaskComplete:
            if projectTaskComplete == 'false':
                for task in project_item.tasks:
                    task.complete = False
            elif projectTaskComplete == 'true':
                for key in request.form.keys():
                    if key.startswith("task-markedascomplete"):
                        #print(key)
                        task_id = key.replace("task-markedascomplete", "")
                        #print("task_id", task_id)
                        task_for_complete = Task.query.get_or_404(task_id)
                        task_for_complete.complete = True


        if newLabelName!=None and newLabelIcon != None and newLabelColor != None:
            create_label(user, project_item, newLabelName, newLabelIcon, newLabelColor)

        if projColor == None:
            pass
        elif projColor != project_item.color:
            project_item.color = projColor
        
        if 'upload-img' not in request.files:
            new_image = None
        else:
            new_image = request.files['upload-img']

        #Do updates for each thing
        if complete == "true":
            project_item.complete = True
        if deleted == "true":
            project_item.deleted = True
        if goal_time == "" or goal_time == None or goal_time == project_item.goal_time or goal_time == "0" or goal_time == "1" or goal_time == "51":
            pass
        else:
            project_item.goal_time = int(goal_time) - 1

        if goal_per == "" or goal_per == None or goal_per == project_item.goal_per:
            pass
        elif goal_per == "0":
            goal_per = None
            project_item.goal_time = None
        else:
            project_item.goal_per = goal_per
            new_goal_update = Update(author=user, column='goal', message="added")
            db.session.add(new_goal_update)
            project_item.updates.append(new_goal_update)
        if last_session == "" or last_session == None:
            last_session = None
        else:
            new_session = Session(project_id=project_id, seconds = last_session, author=user)
            db.session.add(new_session)
            project_item.last_session = new_session.seconds
            new_session_update = Update(author=user, column='session', message="added")
            db.session.add(new_session_update)
            project_item.updates.append(new_session_update)
        if title == "" or title == None:
            pass
        else:
            project_item.title = title
        if description == None:
            pass
        else:
            project_item.description = description
            new_description_update = Update(author=user, column='description', message="added")
            db.session.add(new_description_update)
            project_item.updates.append(new_description_update)

        if no_due_date:
            project_item.due_date = None
        else:
            if due_date == None or due_date=='' or due_date==project_item.due_date:
                project_item.due_date = project_item.due_date
                project_item.late = project_item.late
                project_item.status = project_item.status
                project_item.upcoming = project_item.upcoming
            else:
                if due_date_time == None or due_date_time == '':
                    due_date_time = time(0)
                    due_date = convert_for_model(due_date)
                    due_date = datetime.combine(due_date, due_date_time)
                else:
                    due_date = str(due_date) + " " + str(due_date_time) + ":00"
                    due_date = convert_for_model(due_date)

                late, upcoming, status= check_status(today, due_date)

                total_seconds, time_remaining = check_status(today, due_date, "seconds")

                project_item.due_date = due_date
                project_item.late = late
                project_item.upcoming = upcoming
                project_item.status = status
                project_item.seconds_remaining = total_seconds
                project_item.time_remaining = time_remaining
                new_due_date_update = Update(author=user, column='due date', message="added")
                db.session.add(new_due_date_update)
                project_item.updates.append(new_due_date_update)
        
        if priority == None:
            pass
        else:
            project_item.priority = priority
            new_priority_update = Update(author=user, column='priority', message="added")
            db.session.add(new_priority_update)
            project_item.updates.append(new_priority_update)
        
        project_item.date_updated = today
        if new_image:
            add_image(user, project_item, new_image)
        if "add-task" in request.form:
            task_title = request.form.get('taskTitle')
            if task_title == "" or task_title == None:
                flash("Task Title cannot be left blank", "warning")
            else:
                task_description = request.form.get('taskDescription')
                task_priority = request.form.get('taskPriority')
                task_due_date = request.form.get('taskDueDate')
                add_task(user, project_item, task_title, task_description, task_priority, task_due_date)
        db.session.commit()
        return redirect(redirect_url())


