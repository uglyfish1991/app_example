from . import db 
from sqlalchemy.sql import func


#includes one-to-many relationships - one user can have many posts, one post can have many comments
class Todo(db.Model):
    # the variable id is a column of a unique int, used to look up users
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    complete = db.Column(db.Boolean())
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())

