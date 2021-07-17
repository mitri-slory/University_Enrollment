from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restx import Api
from werkzeug.utils import cached_property


app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes


