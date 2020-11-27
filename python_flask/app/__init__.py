from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from .forms import LoginForm
from ..config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from python_flask.app.models import User

login = LoginManager(app)
login.login_view = 'login'
