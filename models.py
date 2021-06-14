from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from appinit import db

class users(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password



class Post(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

