from flask import Flask

app = Flask(__name__)

from app import views
from app.controller import user_controller, category_controller, record_controller
