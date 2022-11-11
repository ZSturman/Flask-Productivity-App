import os
import os.path
from os import listdir, path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Bundle, Environment
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

from mapps.config import DevelopmentConfig
from mapps.main.utils import *


db=SQLAlchemy()

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

mail = Mail(app)
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])


bcrypt = Bcrypt(app)

scss = Bundle('bootstrap-dist/css/bootstrap.css','bootstrap-dist/css/bootstrap-grid.css','bootstrap-dist/css/bootstrap-reboot.css','bootstrap-dist/css/bootstrap-utilities.css','custom.scss', filters="libsass", output='all.css')
assets = Environment(app)
assets.register('scss_all', scss)

login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

from mapps.main.routes import main
from mapps.tasks.routes import tasks
from mapps.projects.routes import projects
from mapps.notes.routes import notes
from mapps.todos.routes import todos
from mapps.user.routes import user
from mapps.customization.routes import customization
from mapps.labels.routes import labels
from mapps.errors.handlers import errors


app.register_blueprint(main)
app.register_blueprint(tasks)
app.register_blueprint(projects)
app.register_blueprint(notes)
app.register_blueprint(todos)
app.register_blueprint(user)
app.register_blueprint(customization)
app.register_blueprint(labels)
app.register_blueprint(errors)

@app.context_processor
def context_processor():
    return dict(hh_mm_ss_am=hh_mm_ss_am, check_status=check_status,convert_to_local=convert_to_local, yyyy_mm_dd_hh_mm_ss_zz_local=yyyy_mm_dd_hh_mm_ss_zz_local, yyyy_mm_dd_local=yyyy_mm_dd_local, yyyy_mm_dd=yyyy_mm_dd, yyyy_mm_dd_hh_mm_ss_zz=yyyy_mm_dd_hh_mm_ss_zz, wkd_mon_dd_hh_mm_ss_yyy_local=wkd_mon_dd_hh_mm_ss_yyy_local, wkd_mon_dd_yyy_local=wkd_mon_dd_yyy_local, weekday_month_dd_yyy_local=weekday_month_dd_yyy_local, wkd_mon_dd_hh_mm_ss_yyyy_local=wkd_mon_dd_hh_mm_ss_yyyy_local, weekday_month_dd_yyyy=weekday_month_dd_yyyy, getRandomColor=getRandomColor, hh_mm_ss_am_local=hh_mm_ss_am_local, convert_time=convert_time, add_padding=add_padding, today=today)

def create_icons_list():
    icons = get_icons()
    os.chdir('./mapps/')
    if os.path.exists("icon_list.txt"):
        pass
    else:
        with open("icon_list.txt", "w") as f:
            for icon in icons:
                f.writelines(icon + '\n')
    os.chdir("..")




with app.app_context():
    db.init_app(app)
    #db.drop_all()
    #db.create_all()
    #create_icons_list()
    
    

   