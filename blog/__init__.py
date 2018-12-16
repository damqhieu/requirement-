from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db) # this

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


from blog.candidates.routes import candidates
from blog.users.routes import users
from blog.posts.routes import posts
from blog.main.routes import main
from blog.plans.routes import plans
app.register_blueprint(plans)
app.register_blueprint(candidates)
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)