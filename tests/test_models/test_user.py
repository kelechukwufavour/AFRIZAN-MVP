import unittest
from unittest.mock import patch
from . import db
from models.user import User
from hashlib import sha256

class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test fixtures"""
        self.user = User(username='testuser', email='test@example.com', role='user')

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    def test_user_attributes(self):
        """Test User object attributes"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.role, 'user')

    def test_set_password(self):
        """Test set_password method"""
        self.user.set_password('password123')
        self.assertNotEqual(self.user.password_hash, None)
        self.assertEqual(len(self.user.password_hash), 64)  # SHA-256 hash length

    def test_verify_password(self):
        """Test verify_password method"""
        self.user.set_password('password123')
        self.assertTrue(self.user.verify_password('password123'))
        self.assertFalse(self.user.verify_password('wrongpassword'))

    def test_repr_method(self):
        """Test __repr__ method"""
        self.assertEqual(repr(self.user), '<User testuser>')

    def test_serialize_method(self):
        """Test serialize method"""
        expected_serialized_user = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'role': self.user.role,
            # Add other fields as needed
        }
        self.assertEqual(self.user.serialize(), expected_serialized_user)

if __name__ == '__main__':
    unittest.main()
