from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
db=SQLAlchemy(app)
migrate=Migrate(app,db)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/many'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True



order_items=db.Table('order_items',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True))

class Order(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    status=db.Column(db.String(), nullable=False)
    products = db.relationship('Product', secondary=order_items, backref=db.backref('orders', lazy=True))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(), nullable=False)

if __name__ == '__main__':
    app.run(debug=True)

'''
>>> order = Order(status="ready")
>>> product = Product(name="Great widget")
>>> order.products = [product]
>>> product.orders = [order]
'''

