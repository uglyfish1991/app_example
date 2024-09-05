from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "databse.db"

# this function is called when app.py runs, and is returned. Lets you do some config bits here

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import my_view

    app.register_blueprint(my_view, url_prefix="/")

    from .models import Todo

    with app.app_context():
        db.create_all()

    return app