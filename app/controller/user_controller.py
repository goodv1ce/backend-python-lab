import uuid

from flask import jsonify, request
from app import app
from app.database_implementation import users


@app.get('/users')
def get_users():
    return jsonify(list(users.values()))


@app.get('/user/<user_id>')
def get_user(user_id):
    return jsonify(users[user_id])


@app.post('/user')
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {
        "id": user_id,
        "name": user_data["name"]
    }

    users[user_id] = user
    return jsonify(status=200, message="User was added successfully", user=user)


@app.delete('/user/<user_id>')
def delete_user(user_id):
    users.pop(user_id)
    return jsonify(status=200, message="User was deleted successfully")
