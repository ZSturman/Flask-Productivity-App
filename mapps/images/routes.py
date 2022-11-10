from datetime import datetime
import os
import secrets
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename
from mapps import app, db

from mapps.models import *
from mapps.main.utils import *



images = Blueprint('images', __name__)

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



@images.route("/images")
def images_app():
    if current_user.is_authenticated:
        user = User.query.filter_by(email=current_user.email).first()
        notes = Note.query.filter_by(author=user).all()
        sessions = Session.query.filter_by(author=user).all()
        sessions_dates = set()
        for item in sessions:
            sessions_dates.add(datetime.date(item.date))
        images = Pic.query.filter_by(author=user).all()

        projects = Project.query.filter_by(author=user).all()
        deleted_projects = Project.query.filter_by(author=user, deleted=True).all()
        completed_projects = Project.query.filter_by(author=user, complete=True).all()
        active_projects = Project.query.filter_by(author=user, complete=False, deleted=False).all()
        projects_dates_added = set()
        projects_dates_updated = set()
        for item in projects:
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

        return render_template("home.html", notes=notes, projects=projects, tasks=tasks, todos=todos, labels=labels, folder_dir=folder_dir, images=images, icons=icons, filename_path=filename_path, todos_dates=todos_dates, today=today, user_img_dir=user_img_dir, projects_dates_added=projects_dates_added, projects_dates_updated=projects_dates_updated, deleted_projects=deleted_projects, active_projects=active_projects, completed_projects=completed_projects,   tasks_dates_added=tasks_dates_added, tasks_dates_updated=tasks_dates_updated, sessions_dates=sessions_dates, sessions=sessions, get_random_icon=get_random_icon)
    else:
        return redirect(url_for('user.login'))
    
    


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extentions


@images.route("/add_image", methods=['POST'])
def add_image():
    if current_user.is_authenticated:
        user = User.query.filter_by(email=current_user.email).first()
        if request.method == 'POST':
            print(request.form)
            if 'upload-img' not in request.files:
                flash('No upload-img part')
                return redirect(request.url)
            img = request.files['upload-img']
            if img.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if img and allowed_file(img.filename):
                random_hex = secrets.token_hex(8)
                _, f_ext = os.path.splitext(img.filename)
                picture_fn = random_hex + f_ext
                save_img_path = os.path.join('/Users/zacharysturman/Library/Mobile Documents/com~apple~CloudDocs/miniapps/mapps/static/images', picture_fn)
                img.save(save_img_path)
                newImg = Pic(author=user, location=save_img_path, filename=picture_fn)
                print("newImg", newImg)
                db.session.add(newImg)
                db.session.commit()
                flash("Image upload success.", "success")
                return redirect(url_for('images.images_app'))
        flash("Image upload failed. Please try again", "warning")
        return redirect(url_for('images.images_app'))
