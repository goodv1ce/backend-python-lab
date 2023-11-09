import uuid

from app import app
from flask import request, jsonify

from app.database_implementation import categories


@app.get('/categories')
def get_categories():
    return jsonify(list(categories.values()))


@app.get('/category/<category_id>')
def get_category(category_id):
    return jsonify(categories[category_id])


@app.post('/category')
def add_category():
    category_data = request.get_json()
    category_id = uuid.uuid4().hex
    category = {
        "id": category_id,
        "name": category_data["name"]
    }
    categories[category_id] = category
    return jsonify(status=200, message="Category was added successfully", category=category)


@app.delete('/category/<category_id>')
def delete_category(category_id):
    categories.pop(category_id)
    return jsonify(status=200, message="Category was deleted successfully")
