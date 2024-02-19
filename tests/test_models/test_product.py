import unittest
from unittest.mock import patch
from . import db
from models.product import Product

class TestProduct(unittest.TestCase):
    """Test cases for the Product class"""

    def setUp(self):
        """Set up test fixtures"""
        self.product = Product(name='Test Product', price=10.99, stock_quantity=100,
                                category_id=1, artisan_id=1)

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_product_attributes(self):
        """Test Product object attributes"""
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 10.99)
        self.assertEqual(self.product.stock_quantity, 100)
        self.assertEqual(self.product.category_id, 1)
        self.assertEqual(self.product.artisan_id, 1)

    def test_serialize_method(self):
        """Test serialize method"""
        expected_serialized_product = {
            'product_id': self.product.product_id,
            'name': self.product.name,
            'description': self.product.description,
            'price': self.product.price,
            'stock_quantity': self.product.stock_quantity,
            'category_id': self.product.category_id,
            'artisan_id': self.product.artisan_id,
            # Add other fields as needed
        }
        self.assertEqual(self.product.serialize(), expected_serialized_product)

if __name__ == '__main__':
    unittest.main()
