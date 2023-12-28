import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pylab_user:xRcMuvQSZrjdMBiMczHYn66XSXc8IRpr@dpg-cm50k0un7f5s73c2e300-a.frankfurt-postgres.render.com/pylab_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

db = SQLAlchemy(app)

jwt = JWTManager(app)

migrate = Migrate(app, db)

from myapp.models import User, Category, Record
import myapp.views
