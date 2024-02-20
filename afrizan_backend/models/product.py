# Import db inside functions or methods where it's needed
from . import db

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    artisan_id = db.Column(db.Integer, db.ForeignKey('artisans.artisan_id'), nullable=False)

    # Relationships
    orders = db.relationship("Order", backref="product", cascade="all, delete-orphan")
    category = db.relationship("Category", backref="products")
    artisan = db.relationship("Artisan", backref="products")

    def serialize(self):
        """Serializes Product object to a dictionary"""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock_quantity': self.stock_quantity,
            'category_id': self.category_id,
            'artisan_id': self.artisan_id,
            }
