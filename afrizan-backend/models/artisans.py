from flask import Flask, jsonify, request, Blueprint
from sqlalchemy.orm import sessionmaker
from models import Artisan  
from app.database import DBSession
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

artisans = Blueprint('artisans', __name__)

@artisans.route('/', methods=['GET'])
def get_artisans():
    session = DBSession()
    artisans = session.query(Artisan).all()
    artisan_list = [{'id': a.id, 'username': a.username, 'email': a.email, 'created_at': a.created_at, 'updated_at': a.updated_at}
                    for a in artisans]
    session.close()
    return jsonify(artisans=artisan_list)

@artisans.route('/<artisan_id>', methods=['GET'])
def get_artisan(artisan_id):
    session = DBSession()
    artisan = session.query(Artisan).filter_by(id=artisan_id).first()
    session.close()
    if artisan:
        return jsonify(artisan={'id': artisan.id, 'username': artisan.username, 'email': artisan.email, 'created_at': artisan.created_at, 'updated_at': artisan.updated_at})
    else:
        return jsonify(message="Artisan not found"), 404

@artisans.route('/<artisan_id>', methods=['DELETE'])
def delete_artisan(artisan_id):
    session = DBSession()
    artisan = session.query(Artisan).filter_by(id=artisan_id).first()
    if artisan:
        session.delete(artisan)
        session.commit()
        session.close()
        return jsonify(message="Artisan deleted successfully")
    else:
        session.close()
        return jsonify(message="Artisan not found"), 404

@artisans.route('/', methods=['POST'])
def create_artisan():
    if request.method == 'POST':
        session = DBSession()
        if request.json is not None:
            new_artisan = Artisan(
                username=request.json.get('username'),
                email=request.json.get('email'),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            session.add(new_artisan)
            session.commit()
            artisan_data = {
                'id': new_artisan.id,
                'username': new_artisan.username,
                'email': new_artisan.email,
                'created_at': new_artisan.created_at,
                'updated_at': new_artisan.updated_at
            }
            session.close()
            return jsonify(artisan_data), 201
        else:
            session.close()
            return jsonify(message="Invalid request"), 400

@artisans.route('/<artisan_id>', methods=['PUT'])
def update_artisan(artisan_id):
    if request.method == 'PUT':
        session = DBSession()
        artisan = session.query(Artisan).filter_by(id=artisan_id).first()
        if artisan:
            if request.json is not None:
                artisan.username = request.json.get('username')
                artisan.email = request.json.get('email')
                artisan.updated_at = datetime.utcnow()
                session.commit()
                session.close()
                return jsonify(message="Artisan updated successfully")
            else:
                session.close()
                return jsonify(message="Invalid request"), 400
        else:
            session.close()
            return jsonify(message="Artisan not found"), 404
