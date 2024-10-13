# config.py

import os

class Config:
    # Define the path for the SQLite database file
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')  # Create app.db in the current directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
