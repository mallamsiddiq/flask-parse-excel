import os, sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.urandom(16)
    ASSETS_DEBUG = True
    CSRF_ENABLED = True

class DoleAppConfig(Config):
    """
    Configurations
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    test_directory_path = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(test_directory_path, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        "test": 'sqlite:///' + os.path.join(test_directory_path, 'app.db')
    }

app_config = {
    'config': DoleAppConfig
}
