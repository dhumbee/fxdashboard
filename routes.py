from app import app
from flask import render_template, flash, redirect, url_for, request
from forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from models import User
from werkzeug.urls import url_parse

#view for login screen
@app.route('/', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.rememberMe.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main')
        return redirect(next_page)
    return render_template('login.html', title = 'FintronX LED User Dashboard', form = form)

#view for logout option
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#view for login successful
@app.route('/main', methods = ['GET', 'POST'])
@login_required
def main():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)
