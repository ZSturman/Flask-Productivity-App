from datetime import datetime
import re
from flask import Blueprint, render_template, redirect, url_for, request, flash, make_response, json, jsonify
from flask_login import current_user, login_required

from mapps import db

from mapps.models import Note, Label, User, Update
from mapps.main.utils import redirect_url

notes = Blueprint('notes', __name__)

def getNumbers(str):
    array = re.findall(r'[0-9]+', str)
    return array

@notes.route("/notes")
@login_required
def notes_app():
    if current_user.is_authenticated:
        labels = Label.query.filter_by(author=current_user).all()
        notes = Note.query.filter_by(author=current_user).all()
        folder_dir="/Icon_Library/sets/all/"
        return render_template("notes.html", notes=notes, labels=labels, folder_dir=folder_dir, today=today)
    else:
        flash("You must be looged in to view this page", "info")
        return redirect(redirect_url())

@notes.route("/add_note", methods=['POST'])
@login_required
def add_note():
    if current_user.is_authenticated:
        user = User.query.filter_by(email=current_user.email).first()
        title = request.form.get("noteTitle")
        content = request.form.get("noteContent")
        labels = request.form.get("labels-list")

        if content == None or content == "":
            return redirect(redirect_url())
        newNote = Note(author=user, title=title, content=content)
        db.session.add(newNote)
        new_update = Update(author=user, column = None, message = "created")
        db.session.add(new_update)
        newNote.updates.append(new_update)

        if labels:
            label_ids = getNumbers(labels)
            print("label_ids", label_ids)
            for label in label_ids:
                new_label = Label.query.get_or_404(label)
                newNote.labels.append(new_label)
        else:
            print("no labels")
       
        print("newNote", newNote)
        print("new_update", new_update)
        print("newNote.updates.", newNote.updates)
        print("note labels", labels)
        print("note labels", labels)
        db.session.commit()
        flash("Note has been created", "success")
        return redirect(redirect_url())




@notes.route("/update_labels/note/<int:note_id>", methods=['POST'])
def update_labels(note_id):
    if current_user.is_authenticated:
        note_item = Note.query.get_or_404(note_id)
        if request.get_json():
            req = request.get_json()
            res = make_response(jsonify(req), 200)
            print(req)
            print("res", res)
            for _,v in req.items():
                proj_label = Label.query.get_or_404(int(v))
                proj_label.notes.append(note_item)
                db.session.commit()
            return res

@notes.route("/remove_labels/note/<int:note_id>", methods=['POST'])
def remove_labels(note_id):
    if current_user.is_authenticated:
        note_item = Note.query.get_or_404(note_id)
        if request.get_json():
            req = request.get_json()
            res = make_response(jsonify(req), 200)
            print(req)
            print("res", res)
            for _,v in req.items():
                proj_label = Label.query.get_or_404(int(v))
                proj_label.notes.remove(note_item)
                db.session.commit()
            return res





@notes.route("/update_note/<int:note_id>", methods=['POST'])
@login_required
def update_note(note_id):
    note_item = Note.query.get_or_404(note_item)
    title = request.form.get("noteTitle")
    content = request.form.get("noteContent")
    labels = request.form.get("noteLabels")
    if content == None or content == "":
        if title == None or title == "":
            db.session.delete(note_item)
            db.session.commit()
            return redirect(redirect_url())
    if title != note_item.title:
        note_title_update = Update(column = "title", message = "changed")
        db.session.add(note_title_update)
        note_item.title = title
        note_item.updates.append(note_title_update)
    if content != note_item.content:
        note_content_update = Update(column = "content", message = "changed")
        db.session.add(note_content_update)
        note_item.content = content
        note_item.updates.append(note_content_update)
    db.session.commit()
    flash("Note has been updated", "success")
    return redirect(redirect_url())




@notes.route("/delete_note/<int:note_id>", methods=['POST'])
@login_required
def delete_note(note_id):
    if current_user.is_authenticated:
        note_item = Note.query.get_or_404(note_id)
        db.session.delete(note_item)
        db.session.commit()
        return redirect(redirect_url())

""" 

def delete_note()

def update_note()

def add_note_note()
 """