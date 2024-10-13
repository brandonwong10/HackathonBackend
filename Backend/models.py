# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'victim' or 'helper'
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    #health_data = db.relationship('HealthData', backref='user', lazy=True)

# class HealthData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     heart_rate = db.Column(db.Integer)
#     blood_sugar = db.Column(db.Integer)
#     timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
