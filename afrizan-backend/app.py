from flask import Flask
from flask_cors import CORS
from routes.api import user_bp, product_bp, order_bp, category_bp, artisan_bp, review_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///afrizan.db"

    # Initialize db objects from each model file
    #user_db.init_app(app)
    #review_db.init_app(app)

    # Initialize Flask-CORS with default options
    CORS(app)

    # Register your blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(artisan_bp)
    app.register_blueprint(review_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Run the Flask app in debug mode
