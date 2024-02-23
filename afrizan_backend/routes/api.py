#!/usr/bin/python3
from flask_restful import Resource
from models.user import User
from models.product import Product
from models.orders import Order
from models.categories import Category
from models.artisans import Artisan
from models.reviews import Review

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

class ArtisanResource(Resource):
    def get(self):
        artisans = Artisan.query.all()
