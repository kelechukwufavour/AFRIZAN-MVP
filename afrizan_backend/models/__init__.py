# Import db inside functions or methods where it's needed
from . import db

# Import other models inside functions or methods where they're needed
def load_models():
    from .user import User
    from .product import Product
    from .orders import Order
    from .categories import Category
    from .artisans import Artisan
    from .reviews import Review

# Call the function to load models
load_models()
