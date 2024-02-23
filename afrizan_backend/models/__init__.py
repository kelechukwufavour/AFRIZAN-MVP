#!/usr/bin/python3
# Import model files
from flask_sqlalchemy import SQLAlchemy

# Initialize db
db = SQLAlchemy()

# Import model files after db is defined
from .association_tables import order_products

from .user import User
from .product import Product
from .orders import Order
from .categories import Category
from .artisans import Artisan
from .reviews import Review
