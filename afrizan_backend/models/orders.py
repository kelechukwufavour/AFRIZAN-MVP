# Import db inside functions or methods where it's needed
from . import db

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    # Relationships
    user = db.relationship("User", backref="orders")
    products = db.relationship("Product", secondary="order_products")

    def serialize(self):
        """Serializes Order object to a dictionary"""
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'order_date': self.order_date.strftime("%Y-%m-%d %H:%M:%S"),
            'total_amount': self.total_amount,
            'status': self.status,
        }
