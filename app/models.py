from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phonenumber = db.Column(db.String(200))
    feedback = db.Column(db.String(200))

    def __repr__(self):
        return '<User %r>' % self.username