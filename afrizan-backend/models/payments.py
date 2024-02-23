from flask import Flask, jsonify, make_response, request, Blueprint
from flask_cors import cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from datetime import datetime
from app.database import DBSession
from datab import Payment, User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

payments = Blueprint('payments', __name__)


@payments.route('/', methods=['GET'])
def all_payments():
    session = DBSession()
    payments = session.query(Payment).options(
        joinedload(Payment.user)).all()
    payment_list = [
        {
            'id': p.id,
            'user_id': p.user_id,
            'amount': p.amount,
            'status': p.status,
            'created_at': p.created_at,
            'updated_at': p.updated_at
        }
        for p in payments
    ]
    session.close()
    return jsonify(payments=payment_list)


@payments.route('<payment_id>', methods=['GET'])
def get_payment(payment_id):
    session = DBSession()
    payment = session.query(Payment).filter_by(id=payment_id).first()
    session.close()

    if payment:
        payment_info = {
            'id': payment.id,
            'customer_id': payment.customer_id,
            'amount': payment.amount,
            'status': payment.status,
            'created_at': payment.created_at,
            'updated_at': payment.updated_at
        }
        return jsonify(payment=payment_info)
    else:
        return jsonify(message="Payment not found"), 404

@cross_origin()
@payments.route('/<string:user_id>/payments', methods=['POST', 'OPTIONS']) # type: ignore
def create_payment(user_id):
    if request.method == 'POST':
        session = DBSession()
        user = session.query(User).filter_by(id=User_id).first()
        if not user:
            session.close()
            return jsonify(message=f"User with id {User_id} not found"), 404

        amount = int(request.json.get('amount')
                     ) if request.json and 'amount' in request.json else None
        print("Amount:", amount)
        print("Type of amount:", type(amount))
        status = 'completed' if amount == 100 else 'pending'

        new_payment = Payment(
            user_id=user_id,
            amount=amount,
            status=status,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        if amount != 100:
            setattr(new_payment, 'status', 'pending')

        session.add(new_payment)
        session.commit()

        payment_data = {
            'id': new_payment.id,
            'user_id': new_payment.user_id,
            'amount': new_payment.amount,
            'status': new_payment.status,
            'created_at': new_payment.created_at,
            'updated_at': new_payment.updated_at
        }
        session.close()
        return jsonify(payment_data), 201
    elif request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        response.headers.add("Access-Control-Allow-Methods", "POST")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response


@payments.route('/<payment_id>', methods=['PUT'])
def update_payment(payment_id):
    session = DBSession()
    payment = session.query(Payment).filter_by(id=payment_id).first()
    if payment:
        if request.json:
            payment.amount = request.json.get('amount')
            payment.status = request.json.get('status')
        payment.updated_at = datetime.utcnow() # type: ignore
        session.commit()
        session.close()
        return jsonify(message="Payment updated successfully")
    else:
        session.close()
        return jsonify(message="Payment not found"), 404
