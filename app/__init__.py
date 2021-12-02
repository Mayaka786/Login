from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.authentication import authentication

# define db var
app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql://admin:AllowMe!2021@localhost/digital_sacco"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'authentication.login'

# BLUEPRINTS
app.register_blueprint(authentication, url_prefix='/auth')

# INITIALIZATION
db.init_app(app)
login_manager.init_app(app)

# AllowMe!2021
