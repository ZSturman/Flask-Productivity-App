from datetime import datetime
from flask import Blueprint, render_template

customization = Blueprint('customization', __name__)

@customization.route("/customization")
def customization_app():
    today = datetime.utcnow().date()
    return render_template("customization.html", today=today)