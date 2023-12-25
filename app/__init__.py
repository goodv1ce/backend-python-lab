from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pylab_user:password@localhost/pylab_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import User, Category, Record
import app.views
