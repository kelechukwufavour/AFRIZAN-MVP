from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Review 
from app.database import DBSession
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

reviews = Blueprint('reviews', __name__)

@reviews.route('/', methods=['GET'])
def get_reviews():
    session = DBSession()
    reviews = session.query(Review).all()
    review_list = [{'id': r.id, 'product_id': r.product_id, 'rating': r.rating, 'comment': r.comment, 'created_at': r.created_at, 'updated_at': r.updated_at}
                   for r in reviews]
    session.close()
    return jsonify(reviews=review_list)

@reviews.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    session = DBSession()
    review = session.query(Review).filter_by(id=review_id).first()
    session.close()
    if review:
        return jsonify(review={'id': review.id, 'product_id': review.product_id, 'rating': review.rating, 'comment': review.comment, 'created_at': review.created_at, 'updated_at': review.updated_at})
    else:
        return jsonify(message="Review not found"), 404

@reviews.route('/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    session = DBSession()
    review = session.query(Review).filter_by(id=review_id).first()
    if review:
        session.delete(review)
        session.commit()
        session.close()
        return jsonify(message="Review deleted successfully")
    else:
        session.close()
        return jsonify(message="Review not found"), 404

@cross_origin()
@reviews.route('/', methods=['POST', 'OPTIONS'])
def create_review():
    if request.method == 'POST':
        session = DBSession()
        if request.json is not None:
            new_review = Review(
                product_id=request.json.get('product_id'),
                rating=request.json.get('rating'),
                comment=request.json.get('comment'),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            session.add(new_review)
            session.commit()
            review_data = {
                'id': new_review.id,
                'product_id': new_review.product_id,
                'rating': new_review.rating,
                'comment': new_review.comment,
                'created_at': new_review.created_at,
                'updated_at': new_review.updated_at
            }
            session.close()
            return jsonify(review_data), 201
        else:
            return jsonify(message="Invalid request"), 400

@reviews.route('/<review_id>', methods=['PUT'])
def update_review(review_id):
    if request.method == 'PUT':
        session = DBSession()
        review = session.query(Review).filter_by(id=review_id).first()
        if review:
            if request.json is not None:
                review.rating = request.json.get('rating')
                review.comment = request.json.get('comment')
                review.updated_at = datetime.utcnow()
                session.commit()
                session.close()
                return jsonify(message="Review updated successfully")
            else:
                return jsonify(message="Invalid request"), 400
        else:
            session.close()
            return jsonify(message="Review not found"), 404
