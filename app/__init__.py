import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# heroku has database url stored in environment variable DATABASE_URL
db_url = os.environ.get('DATABASE_URL', None)
if not db_url:
    db_url = 'postgresql://postgres:password@localhost:5433/oneome'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

#flask-migrate used to apply database schema changes on DB
migrate = Migrate(app, db)

#flask-marshmallow is used to convert sqlalchemy db object to json
ma = Marshmallow(app)

from app import routes, models, exceptions
