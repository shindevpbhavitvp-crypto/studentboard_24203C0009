from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.notice import Notice
from config.db import db


@jwt_required()
def create_notice():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    notice = Notice(
        title=data["title"],
        content=data["content"],
        created_by=current_user_id,
        category_id=data["category_id"]
    )

    db.session.add(notice)
    db.session.commit()

    return jsonify({"message": "Notice created successfully"}), 201


@jwt_required()
def get_all_notices():
    notices = Notice.query.all()

    result = []

    for notice in notices:
        result.append({
            "id": notice.id,
            "title": notice.title,
            "content": notice.content,
            "created_at": notice.created_at,
            "created_by": notice.created_by,
            "category_id": notice.category_id
        })

    return jsonify(result), 200


@jwt_required()
def get_notice(id):
    notice = Notice.query.get(id)

    if not notice:
        return jsonify({"message": "Notice not found"}), 404

    return jsonify({
        "id": notice.id,
        "title": notice.title,
        "content": notice.content,
        "created_at": notice.created_at,
        "created_by": notice.created_by,
        "category_id": notice.category_id
    }), 200


@jwt_required()
def update_notice(id):
    notice = Notice.query.get(id)

    if not notice:
        return jsonify({"message": "Notice not found"}), 404

    data = request.get_json()

    notice.title = data.get("title", notice.title)
    notice.content = data.get("content", notice.content)
    notice.category_id = data.get("category_id", notice.category_id)

    db.session.commit()

    return jsonify({"message": "Notice updated successfully"}), 200


@jwt_required()
def delete_notice(id):
    notice = Notice.query.get(id)

    if not notice:
        return jsonify({"message": "Notice not found"}), 404

    db.session.delete(notice)
    db.session.commit()

    return jsonify({"message": "Notice deleted successfully"}), 200