from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required

from mapps import db

from mapps.models import Todo, User
from mapps.main.utils import redirect_url

todos = Blueprint('todos', __name__)



@todos.route("/add_todo", methods=['POST'])
@login_required
def add_todo():
    if current_user.is_authenticated:
        user = User.query.filter_by(email=current_user.email).first()
        item = request.form.get("todo-item")
        if item == "" or item == None:
            flash("No To-Do item created", "warning")
            return redirect(redirect_url())
        newtodo = Todo(author=user, item=item)
        db.session.add(newtodo)
        db.session.commit()
        flash("todo has been created", "success")
        return redirect(redirect_url())

@todos.route("/delete_todo/<int:todo_id>", methods=['POST'])
@login_required
def delete_todo(todo_id):
    todo_item = Todo.query.get_or_404(todo_id)
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(redirect_url())

@todos.route("/update_todo/<int:todo_id>", methods=['POST'])
@login_required
def update_todo(todo_id):
    if current_user.is_authenticated:
        todo_item = Todo.query.get_or_404(todo_id)
        item = request.form.get("todo-item")
        complete = request.form.get("todo-complete")
        if item != todo_item.item:
            if item == "" or item == None:
                pass
            else:
                todo_item.item = item
        if complete == 'on':
            todo_item.complete = True
        if complete != 'on':
            todo_item.complete = False
        print("complete", complete)
        db.session.commit()
        return redirect(redirect_url())




