from flask import Flask
from flask_restful import Api
from config import config
from models import db
from routes.api import UserResource, ProductResource, OrderResource, CategoryResource, ArtisanResource, ReviewResource

app = Flask(__name__)
app.config.from_object(config)
api = Api(app)

# Initialize SQLAlchemy
db.init_app(app)

# API endpoints
api.add_resource(UserResource, '/api/users')
api.add_resource(ProductResource, '/api/products')
api.add_resource(OrderResource, '/api/orders')
api.add_resource(CategoryResource, '/api/categories')
api.add_resource(ArtisanResource, '/api/artisans')
api.add_resource(ReviewResource, '/api/reviews')

if __name__ == '__main__':
    app.run(debug=True)
