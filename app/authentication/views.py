from flask.templating import render_template
from flask import request
from app.authentication import authentication
from app.authentication.forms import LoginForm
from flask_login import login_user, current_user, login_required, logout_user


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    from ..models import User, get_by_mail_username

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user: User = get_by_mail_username(form.data.get('email'))

        if user is not None and user.verify_password(
                form.data.get('password')):
            login_user(user, remember=form.data.get('remember'))

    print(form.data)
    return render_template('authentication/login.html', form=form)