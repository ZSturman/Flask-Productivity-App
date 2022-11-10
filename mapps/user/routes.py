from datetime import datetime
from email.message import EmailMessage
import smtplib

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required

from mapps import db, bcrypt
from mapps.user.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm, UpdateAccountForm

from mapps.models import User
from mapps.main.utils import redirect_url

user = Blueprint('user', __name__)


def ResetPW(email, token):
    EMAIL_ADDRESS = "zacharysturman@zsdynamics.com"
    EMAIL_PASSWORD = "gbahpqqbovaoavik"

    msg = EmailMessage()
    msg['Subject'] = 'Reset Password'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    link = url_for('user.reset_password', token=token, _external=True)
    msg.set_content(f"""To reset your password, visit the following link: {link}

If you did not make this request then simply ignore this email and no changes will take place
""")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)




@user.route("/register", methods=['GET', 'POST'])
def register():
    today = datetime.utcnow().date()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. You may now log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('register.html', title='Register', form=form, today=today)




@user.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user == None:
            flash("No user exists with that email. Please try again or create a new account.")
            return redirect(redirect_url())
        token = user.get_reset_token()
        email = form.email.data
        ResetPW(email, token)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('user.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@user.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.verify_reset_token(token)
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated. You may now log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

 



@user.route("/login", methods=['GET', 'POST'])
def login():
    today = datetime.utcnow().date()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form, today=today)

@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))









@user.route("/account", methods=['GET', 'POST'])
@login_required
def user_account():
    if current_user.is_authenticated:
        today = datetime.utcnow().date()
        form = UpdateAccountForm()
       
        if form.validate_on_submit():
            current_user.name = form.name.data
            current_user.email = form.email.data
            current_user.password = form.new_password.data
        elif request.method == 'GET':
            form.name.data = current_user.name
            form.email.data = current_user.email
        
        
        return render_template("user.html", today=today, form=form)
    return render_template('login.html', title='Login', today=today )


