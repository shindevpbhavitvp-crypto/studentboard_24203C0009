from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models.category import Category
from config.db import db


@jwt_required()
def create_category():
    data = request.get_json()

    category = Category(
        name=data["name"]
    )

    db.session.add(category)
    db.session.commit()

    return jsonify({"message": "Category created successfully"}), 201


@jwt_required()
def get_all_categories():
    categories = Category.query.all()

    result = []

    for category in categories:
        result.append({
            "id": category.id,
            "name": category.name
        })

    return jsonify(result), 200


@jwt_required()
def get_category(id):
    category = Category.query.get(id)

    if not category:
        return jsonify({"message": "Category not found"}), 404

    return jsonify({
        "id": category.id,
        "name": category.name
    }), 200


@jwt_required()
def update_category(id):
    category = Category.query.get(id)

    if not category:
        return jsonify({"message": "Category not found"}), 404

    data = request.get_json()

    category.name = data.get("name", category.name)

    db.session.commit()

    return jsonify({"message": "Category updated successfully"}), 200


@jwt_required()
def delete_category(id):
    category = Category.query.get(id)

    if not category:
        return jsonify({"message": "Category not found"}), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({"message": "Category deleted successfully"}), 200