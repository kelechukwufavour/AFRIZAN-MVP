from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from routes.api import UserResource, ProductResource, OrderResource

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# Initialize SQLAlchemy
db.init_app(app)

# API endpoints
api.add_resource(UserResource, '/api/users')
api.add_resource(ProductResource, '/api/products')
api.add_resource(OrderResource, '/api/orders')

if __name__ == '__main__':
    app.run(debug=True)
