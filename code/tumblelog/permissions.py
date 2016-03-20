from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
import flask.ext.login as flask_login

users = {'foo@bar.tld': {'pw': 'secret'}}

class User(flask_login.UserMixin):
    pass

class Login(MethodView):
    def get_context(self, user):
        context = {
            "email": user.id,
            "logged_in": True
        }
        return context

    def get(self):
        return render_template('permissions/login.html')
    def post(self):
        email = request.form['email']
        if request.form['pw'] == users[email]['pw']:
            user = User()
            user.id = email
            flask_login.login_user(user)
            context = self.get_context(user)
            return render_template('permissions/user.html', **context)
        return 'Bad Login'

class Logout(MethodView):
    def get(self):
        flask_login.logout_user()
        return redirect('/')

