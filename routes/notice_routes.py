from flask import Blueprint
from controllers.notice_controller import (
    create_notice,
    get_all_notices,
    get_notice,
    update_notice,
    delete_notice
)
notice_bp = Blueprint('notice', __name__)

notice_bp.route('/notices', methods=['POST'])(create_notice)
notice_bp.route('/notices', methods=['GET'])(get_all_notices)
notice_bp.route('/notices/<int:id>', methods=['GET'])(get_notice)
notice_bp.route('/notices/<int:id>', methods=['PUT'])(update_notice)
notice_bp.route('/notices/<int:id>', methods=['DELETE'])(delete_notice)