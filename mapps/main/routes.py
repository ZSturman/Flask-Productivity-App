from datetime import datetime
import os
import secrets
from flask import Blueprint, render_template, request, make_response, url_for, redirect
from flask_login import current_user
from werkzeug.utils import secure_filename

from mapps import app, db
from mapps.models import *
from mapps.main.utils import *

main = Blueprint('main', __name__)

allowed_extentions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'svg'}



def get_random_icon():
    labels = Label.query.all()
    #get list of all icons
    icons = get_icon_list()
    used_icons = []
    for label in labels:
        used_icons.append(label.icon)
    #remove used icons
    unused_icons = [x for x in icons if x not in used_icons]
    rand_icon = random.choice(unused_icons)
    return rand_icon


def project_view_options(user):
    projects = Project.query.filter_by(author=user).all()
    sortBy = user.sort_by
    if request.method == 'POST':
        sortBy = request.form.get('sortBy')
        if sortBy:
            if sortBy == 'date_updated_new':
                projects = Project.query.order_by(Project.date_updated.desc()).filter_by(author=user).all()
            if sortBy == 'date_updated_old':
                projects = Project.query.order_by(Project.date_updated).filter_by(author=user).all()
            if sortBy == 'date_added_new':
                projects = Project.query.order_by(Project.date_added.desc()).filter_by(author=user).all()
            if sortBy == 'date_added_old':
                projects = Project.query.order_by(Project.date_added).filter_by(author=user).all()
            if sortBy == 'az':
                projects = Project.query.order_by(Project.title).filter_by(author=user).all()

            """ if sortBy == 'labels':
                pass
            if sortBy == 'priority':
                pass
            if sortBy == 'due_date':
                pass """
    return projects, sortBy





@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        today = datetime.utcnow()
        user = User.query.filter_by(email=current_user.email).first()
        notes = Note.query.filter_by(author=user).all()
        sessions = Session.query.filter_by(author=user).all()
        sessions_dates = set()
        for item in sessions:
            sessions_dates.add(datetime.date(item.date))
        images = Pic.query.filter_by(author=user).all()
        all_projects = Project.query.filter_by(author=user).all()
        deleted_projects = Project.query.filter_by(author=user, deleted=True).all()
        completed_projects = Project.query.filter_by(author=user, complete=True).all()
        active_projects = Project.query.filter_by(author=user, complete=False, deleted=False).all()

        for project in all_projects:
            if project.seconds_remaining != None and project.due_date != None:
                duedate = convert_for_model(project.due_date)
                today = convert_for_model(today)
                due_date = convert_to_utc(duedate)
                time_check = round((due_date - today).total_seconds())
                t_diff = abs(project.seconds_remaining - time_check)
                total_seconds, time = check_status(today, project.due_date, "seconds")
                if t_diff > 15:
                    project.seconds_remaining = total_seconds
                    project.time_remaining = time
                    db.session.commit()

        projects_dates_added = set()
        projects_dates_updated = set()
        for item in all_projects:
            projects_dates_added.add(datetime.date(item.date_added))
            projects_dates_updated.add(datetime.date(item.date_updated))
        tasks = Task.query.filter_by(author=user).all()
        tasks_dates_added = set()
        tasks_dates_updated = set()
        for item in tasks:
            tasks_dates_added.add(datetime.date(item.date_added))
            tasks_dates_updated.add(datetime.date(item.date_updated))
        
        todos = Todo.query.filter_by(author=user).all()
        todos_dates = set()
        for item in todos:
            todos_dates.add(datetime.date(item.date_added))
        labels = Label.query.filter_by(author=user).all()
        images = Pic.query.filter_by(author=user).all()
        folder_dir="/Icon_Library/sets/all/"
        user_img_dir = "/images/"+str(user.id)+"/"
        icons = get_icon_list()
        filename_path = "images/icon_svgs/"

        projects, sortBy = project_view_options(user)

        return render_template("home.html", notes=notes, projects=projects, tasks=tasks, todos=todos, labels=labels, folder_dir=folder_dir, images=images, todos_dates=todos_dates, user_img_dir=user_img_dir, projects_dates_added=projects_dates_added, projects_dates_updated=projects_dates_updated, tasks_dates_added=tasks_dates_added, tasks_dates_updated=tasks_dates_updated, sessions_dates=sessions_dates, sessions=sessions, get_random_icon=get_random_icon, deleted_projects=deleted_projects, completed_projects=completed_projects, active_projects=active_projects, icons=icons, filename_path=filename_path, all_projects=all_projects, sortBy=sortBy)
    else:
        return redirect(url_for('user.login'))


  
    




@main.route("/admin_info")
def admin_info():
    language = request.args.get('language')

    res = make_response(render_template("admin_info.html", language=language))

    res.set_cookie(
        'flavor', 
        value = 'vanilla',
        max_age=10
        )

    res.set_cookie("healthy", "no")
    res.set_cookie("chewy", "of course")

    return res