import os

file_path = os.path.abspath(os.getcwd())+"/app/database.db"

class Config:
    SECRET_KEY="u8i9qufcfLuDKCn1zh8BBZpg8XX8UPrG"
    DEVELOPMENT=False
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI=""
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class DevConfig(Config):
    DEVELOPMENT=True
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{file_path}"

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=f"sqlite:///"
