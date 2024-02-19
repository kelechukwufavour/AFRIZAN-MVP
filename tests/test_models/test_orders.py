import unittest
from unittest.mock import patch
from . import db
from models.order import Order

class TestOrder(unittest.TestCase):
    """Test cases for the Order class"""

    def setUp(self):
        """Set up test fixtures"""
        self.order = Order(user_id=1, order_date='2024-02-20 12:00:00',
                           total_amount=100.00, status='Pending')

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_order_attributes(self):
        """Test Order object attributes"""
        self.assertEqual(self.order.user_id, 1)
        self.assertEqual(self.order.order_date, '2024-02-20 12:00:00')
        self.assertEqual(self.order.total_amount, 100.00)
        self.assertEqual(self.order.status, 'Pending')

    def test_serialize_method(self):
        """Test serialize method"""
        expected_serialized_order = {
            'order_id': self.order.order_id,
            'user_id': self.order.user_id,
            'order_date': '2024-02-20 12:00:00',
            'total_amount': 100.00,
            'status': 'Pending',
            # Add other fields as needed
        }
        self.assertEqual(self.order.serialize(), expected_serialized_order)

if __name__ == '__main__':
    unittest.main()
