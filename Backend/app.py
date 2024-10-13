# app.py
from flask import Flask, request, jsonify
from models import db, User#, HealthData
#from notifications import send_notification
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user = User(name=data['name'], phone_number=data['phone_number'], role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()  # Retrieve all users from the database
    # Convert user objects to a list of dictionaries
    users_list = [{"id": user.id, "name": user.name, "phone_number": user.phone_number, "role": user.role, "latitude": user.latitude} for user in users]
    return jsonify(users_list), 200

# @app.route('/health_data', methods=['POST'])
# def submit_health_data():
#     data = request.json
#     user = User.query.get(data['user_id'])
#     if user:
#         health_data = HealthData(user_id=user.id, heart_rate=data['heart_rate'], blood_sugar=data['blood_sugar'])
#         db.session.add(health_data)
#         db.session.commit()

#         # Check for health issues
#         if health_data.heart_rate < 60 or health_data.blood_sugar < 70:
#             # Notify nearby helpers
#             send_notification(user)

#         return jsonify({"message": "Health data submitted!"}), 200
#     return jsonify({"message": "User not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=9090)

