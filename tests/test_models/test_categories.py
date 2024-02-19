import unittest
from unittest.mock import patch
from . import db
from models.category import Category

class TestCategory(unittest.TestCase):
    """Test cases for the Category class"""

    def setUp(self):
        """Set up test fixtures"""
        self.category = Category(name='Test Category')

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_category_attributes(self):
        """Test Category object attributes"""
        self.assertEqual(self.category.name, 'Test Category')

    def test_serialize_method(self):
        """Test serialize method"""
        expected_serialized_category = {
            'category_id': self.category.category_id,
            'name': 'Test Category',
            # Add other fields as needed
        }
        self.assertEqual(self.category.serialize(), expected_serialized_category)

if __name__ == '__main__':
    unittest.main()
