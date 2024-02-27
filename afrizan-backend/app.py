from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.api import user_bp, product_bp, order_bp, category_bp, artisan_bp, review_bp, payment_bp


def create_app():
    app = Flask(__name__)  # Fixed typo here
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///afrizan.db"

    # Initialize Flask-CORS with default options
    CORS(app)

    # Register your blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(artisan_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(payment_bp)

    @app.route('/api/signup', methods=['POST'])
    def signup():
        data = request.json
        # Process signup data
        return jsonify({'message': 'Signup successful'})

    @app.route('/api/data', methods=['GET'])
    def get_data():
        # Retrieve data from the database or other sources
        data = {'example': 'data'}
        return jsonify(data)

    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.json
        # Process login data
        return jsonify({'message': 'Login successful'})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
