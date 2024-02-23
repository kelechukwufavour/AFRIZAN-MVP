# models/association_tables.py
from models import db

order_products = db.Table(
    "order_products",
    db.Column(
        "order_id", db.Integer, db.ForeignKey("order.order_id"), primary_key=True
    ),
    db.Column(
        "product_id", db.Integer, db.ForeignKey("product.product_id"), primary_key=True
    ),
)
