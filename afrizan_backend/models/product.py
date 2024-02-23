#!/usr/bin/python3
# models/product.py
from models import db
from models.association_tables import order_products


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.category_id"), nullable=False
    )
    artisan_id = db.Column(db.Integer, db.ForeignKey("artisan.artisan_id"))

    # Relationships
    orders = db.relationship(
        "Order",
        secondary=order_products,
        backref=db.backref("product_orders", lazy="dynamic"),
    )
    category = db.relationship(
        "Category", backref=db.backref("product_category", lazy=True)
    )
    artisan = db.relationship("Artisan", backref=db.backref("products", lazy=True))

    def serialize(self):
        """Serializes Product object to a dictionary"""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
            "category_id": self.category_id,
            "artisan_id": self.artisan_id,
        }
