from crypt import methods
from flask import Flask, jsonify, make_response, request, Blueprint
from flask_cors import cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.database import DBSession
from datab import Order, Base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

orders = Blueprint('orders', __name__)

@orders.route('/', methods=['GET'])
def all_orders():
    session = DBSession()
    orders = session.query(Order).all()
    order_list = [
        {
            'id': o.id,
            'user_id': o.user_id,
            'payment_id': o.payment_id,
            'num_of_products': o.num_of_products,
            'created_at': o.created_at,
            'updated_at': o.updated_at
        }
        for o in orders
    ]
    session.close()
    return jsonify(orders=order_list)

@orders.route('/<order_id>', methods=['GET'])
def get_order(order_id):
    session = DBSession()
    order = session.query(Order).filter_by(
        id=order_id).first()
    session.close()
    if order:
        return jsonify(order={'id': order.id, 'user_id': order.user_id, 'payment_id': order.payment_id, 'num_of_products': order.num_of_products, 'created_at': order.created_at, 'updated_at': order.updated_at})
    else:
        return jsonify(message="Order not found"), 404

@cross_origin()
@orders.route('/<user_id>/<payment_id>/orders', methods=['POST', 'OPTIONS']) #type: ignore
def create_order(user_id, payment_id):
    if request.method == 'POST':
        session = DBSession()
        new_order = Order(
            user_id=user_id,
            payment_id=payment_id,
            num_of_products=request.json['num_of_products'], #type: ignore
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        session.add(new_order)
        session.commit()

        order_data = {
            'id': new_order.id,
            'user_id': new_order.user_id,
            'payment_id': new_order.payment_id,
            'num_of_products': new_order.num_of_products,
            'created_at': new_order.created_at,
            'updated_at': new_order.updated_at
        }

        session.close()
        return jsonify(order_data), 201
    elif request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        response.headers.add("Access-Control-Allow-Methods", "POST")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response, 200

@orders.route('/<order_id>', methods=['PUT'])
def update_order(order_id):
    session = DBSession()
    order = session.query(Order).filter_by(
        id=order_id).first()
    if order:
        if request.json is not None:
            order.num_of_products = request.json['num_of_products']
        order.updated_at = datetime.utcnow() #type: ignore
        session.commit()

        new_order = {
            'id': order.id,
            'user_id': order.user_id,
            'payment_id': order.payment_id,
            'num_of_products': order.num_of_products,
            'created_at': order.created_at,
            'updated_at': order.updated_at
        }
        session.close()
        return jsonify(new_order)
    else:
        return jsonify(message="Order not found"), 404
