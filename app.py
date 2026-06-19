from flask import Flask
from config.db import db
from models.user import User
from routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from models.category import Category
from routes.category_routes import category_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noticeboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'myjwtsecret'
jwt = JWTManager(app)

db.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(category_bp)

@app.route('/')
def home():
    return {"message": "Student Notice Board API"}

@app.route('/profile')
@jwt_required()
def profile():
    return {"message": "Protected Route Accessed"}

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)