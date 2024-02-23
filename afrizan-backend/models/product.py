from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Product  # Assuming Product model is defined in models module
from app.database import DBSession
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

products = Blueprint('products', __name__)

@products.route('/', methods=['GET'])
def get_products():
    session = DBSession()
    products = session.query(Product).all()
    product_list = [{'id': p.id, 'name': p.name} for p in products]
    session.close()
    return jsonify(products=product_list)

@products.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    session = DBSession()
    product = session.query(Product).filter_by(id=product_id).first()
    session.close()
    if product:
        return jsonify(product={'id': product.id, 'name': product.name})
    else:
        return jsonify(message="Product not found"), 404

@products.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    session = DBSession()
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        session.close()
        return jsonify(message="Product deleted successfully")
    else:
        session.close()
        return jsonify(message="Product not found"), 404

@cross_origin()
@products.route('/', methods=['POST', 'OPTIONS'])
def create_product():
    if request.method == 'POST':
        session = DBSession()
        if request.json is not None:
            new_product = Product(
                name=request.json.get('name')
            )
            session.add(new_product)
            session.commit()
            product_data = {
                'id': new_product.id,
                'name': new_product.name
            }
            session.close()
            return jsonify(product_data), 201
        else:
            return jsonify(message="Invalid request"), 400

@products.route('/<product_id>', methods=['PUT'])
def update_product(product_id):
    if request.method == 'PUT':
        session = DBSession()
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            if request.json is not None:
                product.name = request.json.get('name')
                session.commit()
                session.close()
                return jsonify(message="Product updated successfully")
            else:
                return jsonify(message="Invalid request"), 400
        else:
            session.close()
            return jsonify(message="Product not found"), 404
