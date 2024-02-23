from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

def gen_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True, default=gen_uuid, unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
    
    """ One-to-many relationship between a user and his/her orders """
    orders = relationship('Order', back_populates='user')

    """ One-to-many relationship between an artisan and his/her products """
    products = relationship('Product', back_populates='artisan')

    """ One-to-many relationship between a user and reviews """
    reviews = relationship('Review', back_populates='user')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    """ One-to-many relationship with Order """
    orders = relationship("Order", back_populates="product")
    
    """ Many-to-one relationship with User (artisan) """
    user_id = Column(String(36), ForeignKey('users.id'))
    artisan = relationship("User", back_populates="products")

    """ One-to-many relationship with Review """
    reviews = relationship("Review", back_populates="product")

class Artisan(Base):
        __tablename__ = 'artisans'
    id = Column(String(36), primary_key=True, default=gen_uuid, unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
    specialty = Column(String(50), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'))  
    """ Foreign key referencing the User table """
    user = relationship("User", back_populates="artisan", uselist=False) 
     """ One-to-one relationship with User """


class Payment(Base):
    __tablename__ = 'payments'
    id = Column(String(36, collation='utf8_bin'), primary_key=True,
                default=gen_uuid, unique=True, nullable=False)
    customer_id = Column(String(36, collation='utf8_bin'), ForeignKey(
        'customers.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    """ one-to-many relationshio betweeen user payments and user order """
    user = relationship('user', back_populates="payments"

class Order(Base):
    __tablename__ = 'orders'
    id = Column(String(36, collation='utf8_bin'), primary_key=True,
                default=gen_uuid, unique=True, nullable=False)
    order_id = Column(String(36, collation='utf8_bin'), ForeignKey(
        'orders.id'), nullable=False)
    user_id = Column(String(36, collation='utf8_bin'), ForeignKey(
        'customers.id', ondelete='CASCADE'), nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    
    """ Many-to-one relationship with Product """
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="orders")
    
    """  Many-to-one relationship with User """
    user_id = Column(String(36), ForeignKey('users.id'))
    user = relationship("User", back_populates="orders")

class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    """ One-to-many relationship with Product """
    products = relationship("Product", back_populates="category")

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(String(36), primary_key=True, default=gen_uuid, unique=True, nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    rating = Column(Integer)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    """ Many-to-one relationship with User """
    user = relationship("User", back_populates="reviews")

    """ Many-to-one relationship with Product """
    product = relationship("Product", back_populates="reviews")

# Define your database connection URL
DB_URL = 'sqlite:///database.db'

# Create the engine
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user and associate with an artisan
new_user1 = User(
    first_name='John',
    last_name='Doe',
    email='john.doe@example.com',
    phone_number='1234567890'
)

new_user3 = User(
    first_name='Danny',
    last_name='Joe',
    email='danny.joe@example.com',
    phone_number='0224567890'
)

new_user4 = User(
    first_name='Wells',
    last_name='peace',
    email='wells.peace@example.com',
    phone_number='7724567890'
)

new_artisan = Artisan(
    user=new_user1,
    specialty='Beading')

session.add(new_user2)
session.add(new_user3)
session.add(new_user4)

#adding a new order
new_order = Order(
    User_id='112ab436-8eb2-446b-8a99-6fccd251e259',
    status='complete'
)

#Adding a new product category
new_category = ProductCategory(
    name='Raffia craft'
)

#adding new product
new_product = Product(
artisan_id='112ab436-8eb2-446b-8a99-6fccd251e259',
product_id='ef328523-df4b-4e5c-b50a-fe51e2d36652',
num_of_products=4
)

#Adding a new review
new_review = Review(
    user=new_user1,
    product=new_product,
    rating=5,
    comment='Great product!'
)

session.add(new_user1)
session.add(new_product)
session.add(new_review)

session.commit()
session.close()
