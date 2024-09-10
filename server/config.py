# class Config:
#     SECRET_KEY = 'your_secret_key'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///rps_game.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     CACHE_TYPE = 'simple'  # For caching


import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///rps_game.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
