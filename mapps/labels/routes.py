from datetime import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import func
import random

from mapps import app, db
from mapps.models import Label
from mapps.main.utils import getRandomColor, get_icon_list

labels = Blueprint('labels', __name__)

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

@labels.route("/labels")
@login_required
def labels_library():
    icons = get_icon_list()
    folder_dir="/Icon_Library/sets/all/"
    labels = Label.query.all()
    filename_path = "images/icon_svgs/"
    return render_template('labels.html', icons=icons, labels=labels, filename_path=filename_path, folder_dir=folder_dir, get_random_icon=get_random_icon, today=today)

@labels.route('/add_label', methods=['POST'])
@login_required
def add_label():
    label_name = request.form.get("labelName")
    old_label = Label.query.filter(func.lower(Label.name)==label_name.lower()).first()

    icon = request.form.get("labelIcon")
    if icon == "" or icon == None:
        flash("Label must have an icon", "warning")
        return redirect(url_for('labels.labels_library'))
    if current_user.is_authenticated:
        author = current_user
    
    new_label = Label(author=author, name=label_name, color=color, icon=icon)
    db.session.add(new_label)
    db.session.commit()
    print("new label",new_label.icon)
    print("color",new_label.color)

    return redirect(url_for('labels.labels_library'))


@labels.route("/delete_label/<int:label_id>", methods=['POST'])
@login_required
def delete_label(label_id):
    label_item = Label.query.get_or_404(label_id)
    db.session.delete(label_item)
    db.session.commit()
    return redirect(url_for('labels.labels_library'))