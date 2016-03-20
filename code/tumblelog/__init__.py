from flask import Flask
from flask.ext.mongoengine import MongoEngine
import flask.ext.login as flask_login
from tumblelog.permissions import User, users

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'host': "flask-mongo-db", 'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user

def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin
    from tumblelog.test import test
    app.register_blueprint(posts)
    app.register_blueprint(admin)
    app.register_blueprint(test)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
