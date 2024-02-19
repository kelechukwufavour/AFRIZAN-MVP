from flask_restful import Resource
from models import db, User, Product, Order

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.__dict__ for user in users], 200

    # Implement other HTTP methods as needed (POST, PUT, DELETE)

class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        return [product.__dict__ for product in products], 200

    # Implement other HTTP methods as needed (POST, PUT, DELETE)

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return [order.__dict__ for order in orders], 200
