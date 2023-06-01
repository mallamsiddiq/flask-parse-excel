from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import datetime
# Import the configurations
from instance.config import app_config

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

bcrypt = Bcrypt(None)

application = Flask(
        import_name="app",
        template_folder="templates",
        static_folder='static',
        instance_relative_config=True)

database = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    application.config.from_object(app_config[config_name])
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(application)

    login_manager.init_app(application)
    login_manager.login_view = 'auth.login'

    bcrypt.__init__(application)

    csrf.init_app(application)

    migrate = Migrate(app = application, db = database, directory="dole_migrations")

    register_blueprints()

    # hello_world()

    return application


"""
 The following registers the Blueprints with the application.
"""
def register_blueprints():
    # Import all BluePrints
    from .home import home_blueprint
    application.register_blueprint(home_blueprint, url_prefix='/home')

    from .auth import auth_blueprint
    application.register_blueprint(auth_blueprint, url_prefix='/auth')
