from flask import request, jsonify
from models.user import User
from config.db import db

def register():
    data = request.get_json()

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})