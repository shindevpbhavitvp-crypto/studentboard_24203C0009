from flask import Blueprint
from controllers.auth_controller import (
    register,
    login,
    get_all_users,
    get_user,
    update_user,
    delete_user
)

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)

auth_bp.route('/users', methods=['GET'])(get_all_users)
auth_bp.route('/users/<int:id>', methods=['GET'])(get_user)
auth_bp.route('/users/<int:id>', methods=['PUT'])(update_user)
auth_bp.route('/users/<int:id>', methods=['DELETE'])(delete_user)