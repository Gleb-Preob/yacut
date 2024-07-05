import os
from pathlib import Path
import string

BASE_DIR = Path(__file__).parent / 'yacut'
CHAR_CHOICES = string.ascii_lowercase + string.digits + string.ascii_uppercase
GENERATED_ID_LENGTH = 6
MAX_SHORT_ID_LENGTH = 16
MAX_ORIGINAL_ID_LENGTH = 512
MAX_GENERATION_ATTEMPTS = 1000
REGEX_ALPHANUMERIC = r'^[A-Za-z0-9]+$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'VEERY_SECRET_KEY')
