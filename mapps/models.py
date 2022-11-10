from sqlalchemy import null
from mapps import db
from datetime import datetime
from mapps import login_manager 
from flask_login import UserMixin
from mapps.main.utils import getRandomColor
from mapps import app
from itsdangerous import URLSafeTimedSerializer, URLSafeSerializer
from itsdangerous import SignatureExpired, BadTimeSignature

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

label_project = db.Table('label_project',
    db.Column('label_id', db.Integer, db.ForeignKey('label.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)
 
label_note = db.Table('label_note',
    db.Column('label_id', db.Integer, db.ForeignKey('label.id')),
    db.Column('note_id', db.Integer, db.ForeignKey('note.id'))
)
 
project_note = db.Table('project_note',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('note_id', db.Integer, db.ForeignKey('note.id'))
)
 
project_task = db.Table('project_task',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    email_confirmed = db.Column(db.Boolean, default = False)
    birthday = db.Column(db.Date, default=None)
    phone_num = db.Column(db.Integer, default=None)
    notes = db.relationship('Note', backref="author", lazy=True)
    projects = db.relationship('Project', backref="author", lazy=True)
    tasks = db.relationship('Task', backref="author", lazy=True)
    todos = db.relationship('Todo', backref="author", lazy=True)
    labels = db.relationship('Label', backref="author", lazy=True)
    images = db.relationship('Pic', backref="author", lazy=True)
    sessions = db.relationship('Session', backref="author", lazy=True)
    updates = db.relationship('Update', backref="author", lazy=True)
    color = db.Column(db.String(10), default = '#6C757D')
    dark_mode = db.Column(db.Boolean, unique = False, default = False)
    sort_by = db.Column(db.String(25), default = "date_updated_new")

    def __repr__(self):
        return f'User("{self.name}")'


    def get_reset_token(self):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except SignatureExpired:
            return '<h1>The token is expired pw</h1>'
        except BadTimeSignature:
            return '<h1>That token is invalid pw</h1>'
        return User.query.get(user_id)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable = False, default="Note")
    content = db.Column(db.Text)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updates = db.relationship('Update', backref='note', lazy=True, cascade='all, delete, delete-orphan')
    labels = db.relationship('Label', secondary=label_note, back_populates='notes')
    projects = db.relationship('Project', secondary=project_note, back_populates='notes')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(20))
    description = db.Column(db.String(100), nullable=True, default="")
    priority = db.Column(db.String(12))
    complete = db.Column(db.Boolean, unique = False, default = False)
    deleted = db.Column(db.Boolean, unique = False, default = False)
    
    due_date = db.Column(db.DateTime, nullable=True, default=None)
    status = db.Column(db.String(10), default="none")
    late = db.Column(db.Boolean, unique = False, default = False)
    upcoming = db.Column(db.Integer, default = None)
    seconds_remaining = db.Column(db.Integer, default = None)
    time_remaining = db.Column(db.Text, default = None)
    
    goal_time = db.Column(db.Integer, default=0)
    goal_per = db.Column(db.String(15))
    last_session = db.Column(db.Integer)
    color = db.Column(db.String(10), default = '#6C757D')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    labels = db.relationship('Label', secondary=label_project, back_populates='projects')
    notes = db.relationship('Note', secondary=project_note, back_populates='projects')
    tasks = db.relationship('Task', secondary=project_task, back_populates='projects')
    updates = db.relationship('Update', backref='project', lazy=True, cascade='all, delete, delete-orphan')
    sessions = db.relationship('Session', backref='project', lazy=True, cascade='all, delete, delete-orphan')
    images = db.relationship('Pic', backref='project', lazy=True, cascade='all, delete, delete-orphan')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100), nullable=True, default="")
    due_date = db.Column(db.DateTime, nullable=True, default=None)
    priority = db.Column(db.String(15))
    complete = db.Column(db.Boolean, unique = False, default = False)
    status = db.Column(db.String(15), default="none")
    late = db.Column(db.Boolean, unique = False, default = False)
    deleted = db.Column(db.Boolean, unique = False, default = False)
    color = db.Column(db.String(10), default = '#6C757D')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    projects = db.relationship('Project', secondary=project_task, back_populates='tasks')
    updates = db.relationship('Update', backref='task', lazy=True, cascade='all, delete, delete-orphan')

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seconds = db.Column(db.Integer, default=0)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    item = db.Column(db.String(30))
    complete = complete = db.Column(db.Boolean, unique = False, default = False)

class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    column = db.Column(db.String(20))
    message = db.Column(db.String(30))

class Pic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    filename = db.Column(db.String(255), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    color = db.Column(db.String(10), default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    icon = db.Column(db.String(200))
    projects = db.relationship('Project', secondary=label_project, back_populates='labels')
    notes = db.relationship('Note', secondary=label_note, back_populates='labels')










""" was un pic model """
#location = db.Column(db.String(255), nullable=False)