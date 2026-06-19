from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.comment import Comment
from config.db import db


@jwt_required()
def create_comment():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    comment = Comment(
        comment_text=data["comment_text"],
        user_id=current_user_id,
        notice_id=data["notice_id"]
    )

    db.session.add(comment)
    db.session.commit()

    return jsonify({"message": "Comment created successfully"}), 201


@jwt_required()
def get_all_comments():
    comments = Comment.query.all()

    result = []

    for comment in comments:
        result.append({
            "id": comment.id,
            "comment_text": comment.comment_text,
            "user_id": comment.user_id,
            "notice_id": comment.notice_id,
            "created_at": comment.created_at
        })

    return jsonify(result), 200


@jwt_required()
def get_comment(id):
    comment = Comment.query.get(id)

    if not comment:
        return jsonify({"message": "Comment not found"}), 404

    return jsonify({
        "id": comment.id,
        "comment_text": comment.comment_text,
        "user_id": comment.user_id,
        "notice_id": comment.notice_id,
        "created_at": comment.created_at
    }), 200


@jwt_required()
def update_comment(id):
    comment = Comment.query.get(id)

    if not comment:
        return jsonify({"message": "Comment not found"}), 404

    data = request.get_json()

    comment.comment_text = data.get("comment_text", comment.comment_text)

    db.session.commit()

    return jsonify({"message": "Comment updated successfully"}), 200


@jwt_required()
def delete_comment(id):
    comment = Comment.query.get(id)

    if not comment:
        return jsonify({"message": "Comment not found"}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "Comment deleted successfully"}), 200