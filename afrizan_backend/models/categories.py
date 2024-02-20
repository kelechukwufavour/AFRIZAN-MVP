#!/usr/bin/python3
# models/categories.py
from models import db
class Category(db.Model):
    def __init__(self, db):
        self.db = db
        category_id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)

        # Relationships
        products = db.relationship("Product", backref="category")

    def serialize(self):
        """Serializes Category object to a dictionary"""
        return {
            'category_id': self.category_id,
            'name': self.name,
        }
