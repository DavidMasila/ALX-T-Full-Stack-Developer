from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app=Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost:5432/exercise"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 

db=SQLAlchemy(app)
migrate=Migrate(app,db)
CORS(app)


class Book(db.Model):
    __tablename__="boooks"
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    author=db.Column(db.String())
    rating=db.Column(db.Integer)


    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def reset(self):
        db.session.rollback()

    def format(self):
        return{
            'id':self.id,
            'title':self.title,
            "author":self.author,
            "rating":self.rating
        }




from app import controllers 