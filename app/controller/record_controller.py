import datetime
import uuid

from app import app
from flask import request, jsonify

from app.database_implementation import records


@app.get('/record')
def get_record_by_params():
    target_user_id = request.args.get('user_id', default=-1)
    target_category_id = request.args.get('category_id', default=-1)
    if target_user_id == -1 and target_category_id == -1:
        return jsonify(message='No query parameters provided.', status=400)
    if target_user_id != -1 and target_category_id != -1:
        filtered_records = [record for record in records.values() if
                            record.get("user_id") == target_user_id and record.get("category_id") == target_category_id]

    elif target_user_id != -1:
        filtered_records = [record for record in records.values() if record.get("user_id") == target_user_id]

    else:
        filtered_records = [record for record in records.values() if record.get("category_id") == target_category_id]

    return jsonify(filtered_records)


@app.get('/record/<record_id>')
def get_record_by_id(record_id):
    return jsonify(records[record_id])


@app.post('/record')
def add_record():
    record_data = request.get_json()
    record_id = uuid.uuid4().hex
    current_time = datetime.datetime.now()
    record = {
        "id": record_id,
        "user_id": record_data["user_id"],
        "category_id": record_data["category_id"],
        "record_creation_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "amount": record_data["amount"],

    }
    records[record_id] = record
    return jsonify(status=200, message="Record was added successfully", record=record)


@app.delete('/record/<record_id>')
def delete_record(record_id):
    records.pop(record_id)
    return jsonify(status=200, message="Record   was deleted successfully")
