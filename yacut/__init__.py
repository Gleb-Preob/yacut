from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import BASE_DIR, Config

STATIC_DIR = BASE_DIR / 'html'

app = Flask(
    __name__,
    static_folder=STATIC_DIR,
    template_folder=STATIC_DIR
)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views
