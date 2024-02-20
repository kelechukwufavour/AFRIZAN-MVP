# Import db inside functions or methods where it's needed
from . import db

class Category(db.Model):
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
