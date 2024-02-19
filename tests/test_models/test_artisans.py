import unittest
from unittest.mock import patch
from . import db
from models.artisan import Artisan

class TestArtisan(unittest.TestCase):
    """Test cases for the Artisan class"""

    def setUp(self):
        """Set up test fixtures"""
        self.artisan = Artisan(name='Test Artisan', location='Test Location',
                               contact_info='test@example.com')

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_artisan_attributes(self):
        """Test Artisan object attributes"""
        self.assertEqual(self.artisan.name, 'Test Artisan')
        self.assertEqual(self.artisan.location, 'Test Location')
        self.assertEqual(self.artisan.contact_info, 'test@example.com')

    def test_serialize_method(self):
        """Test serialize method"""
        expected_serialized_artisan = {
            'artisan_id': self.artisan.artisan_id,
            'name': 'Test Artisan',
            'location': 'Test Location',
            'contact_info': 'test@example.com',
            # Add other fields as needed
        }
        self.assertEqual(self.artisan.serialize(), expected_serialized_artisan)

if __name__ == '__main__':
    unittest.main()
