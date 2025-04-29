from flask_sqlalchemy import SQLAlchemy

# Initialize db object - we'll configure the pool pre-ping in app.py
db = SQLAlchemy()

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    fullname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=True)
    points = db.Column(db.Integer, default=50)
    upvotes = db.Column(db.Integer, default=0)
    Badge = db.Column(db.String(20), default="Rookie")
    profile_pic = db.Column(db.String(255), default='')

class Task(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    Description = db.Column(db.String(240), nullable=False)

class Post(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    Description = db.Column(db.String(240), nullable=False)
    img_url = db.Column(db.String(120), nullable=False)

class Post_Participant(db.Model):
    qid = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, nullable=True)
    tid = db.Column(db.Integer, nullable=False)
    user = db.Column(db.String(120), nullable=False)
    Participating = db.Column(db.Boolean, default=False)
    Posted = db.Column(db.Boolean, default=False)