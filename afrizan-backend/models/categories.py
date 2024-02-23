from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import ProductCategory 
from app.database import DBSession
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

product_categories = Blueprint('product_categories', __name__)

@product_categories.route('/', methods=['GET'])
def get_product_categories():
    session = DBSession()
    categories = session.query(ProductCategory).all()
    category_list = [{'id': c.id, 'name': c.name} for c in categories]
    session.close()
    return jsonify(product_categories=category_list)

@product_categories.route('/<category_id>', methods=['GET'])
def get_product_category(category_id):
    session = DBSession()
    category = session.query(ProductCategory).filter_by(id=category_id).first()
    session.close()
    if category:
        return jsonify(product_category={'id': category.id, 'name': category.name})
    else:
        return jsonify(message="Product category not found"), 404

@product_categories.route('/<category_id>', methods=['DELETE'])
def delete_product_category(category_id):
    session = DBSession()
    category = session.query(ProductCategory).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        session.close()
        return jsonify(message="Product category deleted successfully")
    else:
        session.close()
        return jsonify(message="Product category not found"), 404

@cross_origin()
@product_categories.route('/', methods=['POST', 'OPTIONS'])
def create_product_category():
    if request.method == 'POST':
        session = DBSession()
        if request.json is not None:
            new_category = ProductCategory(
                name=request.json.get('name')
            )
            session.add(new_category)
            session.commit()
            category_data = {
                'id': new_category.id,
                'name': new_category.name
            }
            session.close()
            return jsonify(category_data), 201
        else:
            return jsonify(message="Invalid request"), 400

@product_categories.route('/<category_id>', methods=['PUT'])
def update_product_category(category_id):
    if request.method == 'PUT':
        session = DBSession()
        category = session.query(ProductCategory).filter_by(id=category_id).first()
        if category:
            if request.json is not None:
                category.name = request.json.get('name')
                session.commit()
                session.close()
                return jsonify(message="Product category updated successfully")
            else:
                return jsonify(message="Invalid request"), 400
        else:
            session.close()
            return jsonify(message="Product category not found"), 404
