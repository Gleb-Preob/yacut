import os
from pathlib import Path

BASE_DIR = Path(__file__).parent


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'VEERY_SECRET_KEY')
