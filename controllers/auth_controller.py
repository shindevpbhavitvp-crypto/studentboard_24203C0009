from flask import request, jsonify
from models.user import User
from config.db import db
from flask_jwt_extended import create_access_token

def register():
    data = request.get_json()

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )

    

def login():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    if user.password != data["password"]:
        return jsonify({"message": "Invalid password"}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({
        "message": "Login successful",
        "token": token
    })

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})