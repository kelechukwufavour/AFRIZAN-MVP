#!/usr/bin/python3
# models/reviews.py
class Review(db.Model):
    def __init__(self, db):
        self.db = db
        review_id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
        product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
        rating = db.Column(db.Integer, nullable=False)
        comment = db.Column(db.Text, nullable=True)
        review_date = db.Column(db.DateTime, nullable=False)

        # Relationships
        user = db.relationship("User", backref="reviews")
        product = db.relationship("Product", backref="reviews")

    def serialize(self):
        """Serializes Review object to a dictionary"""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'rating': self.rating,
            'comment': self.comment,
            'review_date': self.review_date.strftime("%Y-%m-%d %H:%M:%S"),
        }
