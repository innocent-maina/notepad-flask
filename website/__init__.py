from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

from config import app_config

db = SQLAlchemy()

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + os.getenv('SQLALCHEMY_DATABASE_URI')):
        db.create_all(app=app)
        print('Created Database!')
