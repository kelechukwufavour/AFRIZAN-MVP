from flask import Flask
from flask_restful import Api
from flask_cors import CORS  # Import Flask-CORS
from models import db
from routes.api import (
    UserResource,
    ProductResource,
    OrderResource,
    CategoryResource,
    ArtisanResource,
    ReviewResource,
)


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///afrizan.db"
    db.init_app(app)
    api = Api(app)

    # Initialize Flask-CORS with default options
    CORS(app)

    # API endpoints
    api.add_resource(UserResource, "/api/users")
    api.add_resource(ProductResource, "/api/products")
    api.add_resource(OrderResource, "/api/orders")
    api.add_resource(CategoryResource, "/api/categories")
    api.add_resource(ArtisanResource, "/api/artisans")
    api.add_resource(ReviewResource, "/api/reviews")

    # Create tables
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
