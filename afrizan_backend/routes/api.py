from flask_restful import Resource
from models import db, User, Product, Order, Review, Category, Artisan

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.serialize() for user in users], 200


class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        return [product.serialize() for product in products], 200


class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return [order.serialize() for order in orders], 200


class ReviewResource(Resource):
    def get(self):
        reviews = Review.query.all()
        return [review.serialize() for review in reviews], 200


class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        return [category.serialize() for category in categories], 200

class ArtisanResource(Resource):
    def get(self):
        artisans = Artisan.query.all()
        return [artisan.serialize() for artisan in artisans], 200