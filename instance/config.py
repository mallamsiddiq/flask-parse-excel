import os, sys
from pathlib import Path
# from decouple import config, Csv
from dotenv import load_dotenv

dotenv_path = Path('instance/.env')
load_dotenv(dotenv_path=dotenv_path)


BASE_DIR = Path(__file__).resolve().parent.parent



# email settup

import os, sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.getenv('SECRET_KEY')

    FlASK_DEBUG = os.getenv('DEBUG')

    ASSETS_DEBUG = os.getenv('ASSETS_DEBUG')
    CSRF_ENABLED = os.getenv('CSRF_ENABLED')

class DoleAppConfig(Config):
    """
    Configurations

    """

    TESTING = os.getenv('TESTING')
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO')
    test_directory_path = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(test_directory_path, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_BINDS = {
        "test": SQLALCHEMY_DATABASE_URI
    }

app_config = {
    'config': DoleAppConfig
}
