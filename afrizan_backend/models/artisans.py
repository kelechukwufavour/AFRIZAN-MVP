from . import db

class Artisan(db.Model):
    artisan_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=True)

    # Relationships
    products = db.relationship("Product", backref="artisan")

    def serialize(self):
        """Serializes Artisan object to a dictionary"""
        return {
            'artisan_id': self.artisan_id,
            'name': self.name,
            'location': self.location,
            'contact_info': self.contact_info,
        }
