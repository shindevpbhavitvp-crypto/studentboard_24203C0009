from flask import Blueprint
from controllers.category_controller import (
    create_category,
    get_all_categories,
    get_category,
    update_category,
    delete_category
)

category_bp = Blueprint('category', __name__)

category_bp.route('/categories', methods=['POST'])(create_category)
category_bp.route('/categories', methods=['GET'])(get_all_categories)
category_bp.route('/categories/<int:id>', methods=['GET'])(get_category)
category_bp.route('/categories/<int:id>', methods=['PUT'])(update_category)
category_bp.route('/categories/<int:id>', methods=['DELETE'])(delete_category)