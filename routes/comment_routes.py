from flask import Blueprint
from controllers.comment_controller import (
    create_comment,
    get_all_comments,
    get_comment,
    update_comment,
    delete_comment
)

comment_bp = Blueprint('comment', __name__)

comment_bp.route('/comments', methods=['POST'])(create_comment)
comment_bp.route('/comments', methods=['GET'])(get_all_comments)
comment_bp.route('/comments/<int:id>', methods=['GET'])(get_comment)
comment_bp.route('/comments/<int:id>', methods=['PUT'])(update_comment)
comment_bp.route('/comments/<int:id>', methods=['DELETE'])(delete_comment)