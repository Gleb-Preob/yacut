from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import BASE_DIR, Config

FRONTEND_DIR = BASE_DIR / 'frontend'

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR / 'static',
    template_folder=FRONTEND_DIR / 'templates'
)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views
