from flask import Flask
import os
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config.DevConfig')
app.config["JWT_SECRET_KEY"] = "u8i9qufcfLuDKCn1zh8BBZpg8XX8UPrG"


db_path=os.path.join(os.path.dirname(__file__),"profileflask.db")
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///{}'.format(db_path)

jwt = JWTManager(app)

from app.models import db

db.create_all()

from app import routes