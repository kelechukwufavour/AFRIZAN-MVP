# app/__init__.py
from flask import Flask
from flask_cors import CORS
from app.routes.customers import users
from app.routes.payments import payments
from app.routes.reservations import orders

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.config.Config')
    app.url_map.strict_slashes = False
    app.debug = True

    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(payments, url_prefix='/payments')
    app.register_blueprint(orders, url_prefix='/orders')
    app.register_blueprint(artisans, url_prefix='/artisans')
    app.register_blueprint(categories, url_prefix='/categories')
    app.register_blueprint(reviews, url_prefix='/reviews')
    app.register_blueprint(products, url_prefix='/products')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
