#!/usr/bin/python3
# models/orders.py
from models import db
from models.association_tables import order_products


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    # Relationships
    products = db.relationship("Product", secondary=order_products)

    def serialize(self):
        """Serializes Order object to a dictionary"""
        return {
            "order_id": self.order_id,
            "user_id": self.user_id,
            "order_date": self.order_date.strftime("%Y-%m-%d %H:%M:%S"),
            "total_amount": self.total_amount,
            "status": self.status,
        }
