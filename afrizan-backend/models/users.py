from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User  # Assuming User model is defined in models module
from app.database import DBSession
from datab import User, Payment, Order, Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)


users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def get_users():
    session = Session()
    users = session.query(User).all()
    user_list = [{'id': u.id, 'username': u.username, 'email': u.email, 'created_at': u.created_at, 'updated_at': u.updated_at}
                 for u in users]
    session.close()
    return jsonify(users=user_list)

@users.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    if user:
        return jsonify(user={'id': user.id, 'username': user.username, 'email': user.email, 'created_at': user.created_at, 'updated_at': user.updated_at})
    else:
        return jsonify(message="User not found"), 404

@users.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        session.close()
        return jsonify(message="User deleted successfully")
    else:
        session.close()
        return jsonify(message="User not found"), 404

@cross_origin()
@users.route('/', methods=['POST', 'OPTIONS'])
def create_user():
    if request.method == 'POST':
        session = Session()
        if request.json is not None:
            new_user = User(
                username=request.json.get('username'),
                email=request.json.get('email'),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            session.add(new_user)
            session.commit()
            user_data = {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email,
                'created_at': new_user.created_at,
                'updated_at': new_user.updated_at
            }
            session.close()
            return jsonify(user_data), 201
        else:
            return jsonify(message="Invalid request"), 400

@users.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    if request.method == 'PUT':
        session = Session()
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            if request.json is not None:
                user.username = request.json.get('username')
                setattr(user, 'updated_at', datetime.utcnow())
                session.commit()
                session.close()
                return jsonify(message="User updated successfully")
            else:
                return jsonify(message="Invalid request"), 400
        else:
            session.close()
            return jsonify(message="User not found"), 404
