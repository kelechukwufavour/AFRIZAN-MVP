#!/usr/bin/python3
# models/user.py
#from . import db
from hashlib import sha256

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        """Sets the user's password with sha256 encryption"""
        self.password_hash = sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """Verifies the user's password"""
        return self.password_hash == sha256(password.encode()).hexdigest()

    def serialize(self):
        """Serializes User object to a dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
        }
