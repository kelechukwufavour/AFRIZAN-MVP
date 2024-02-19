import unittest
from unittest.mock import patch
from . import db
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up test fixtures"""
        self.review = Review(user_id=1, product_id=1, rating=5, comment='Great product!',
                             review_date='2024-02-20 12:00:00')

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_review_attributes(self):
        """Test Review object attributes"""
        self.assertEqual(self.review.user_id, 1)
        self.assertEqual(self.review.product_id, 1)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'Great product!')
        self.assertEqual(self.review.review_date, '2024-02-20 12:00:00')

    def test_serialize_method(self):
        """Test serialize method"""
        expected_serialized_review = {
            'review_id': self.review.review_id,
            'user_id': self.review.user_id,
            'product_id': self.review.product_id,
            'rating': self.review.rating,
            'comment': 'Great product!',
            'review_date': '2024-02-20 12:00:00',
            # Add other fields as needed
        }
        self.assertEqual(self.review.serialize(), expected_serialized_review)

if __name__ == '__main__':
    unittest.main()
