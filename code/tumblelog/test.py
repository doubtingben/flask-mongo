from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
import flask.ext.login as flask_login

from tumblelog.models import Post, Comment
from tumblelog import login_manager
from tumblelog.permissions import Login, Logout

test = Blueprint('test', __name__, template_folder='templates')

class List(MethodView):
    decorators = [flask_login.login_required]
    cls = Post

    def get(self):
        posts = self.cls.objects.all()
        return render_template('posts/list.html', posts=posts)


test.add_url_rule('/test/', view_func=List.as_view('index'))
test.add_url_rule('/test/login', view_func=Login.as_view('login'))
test.add_url_rule('/test/logout', view_func=Logout.as_view('logout'))
