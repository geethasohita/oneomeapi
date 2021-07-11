import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_url = os.environ.get('DATABASE_URL', None)
if not db_url:
    db_url = 'postgresql://postgres:password@localhost:5433/oneome'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from app import routes, models, exceptions
