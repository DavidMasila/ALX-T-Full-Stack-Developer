from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

database_name = "testingdb"
database_path = "postgresql://{}:{}@{}/{}".format("postgres", "postgres",
                                                  "localhost:5432",
                                                  database_name)
db = SQLAlchemy()
# migrate = Migrate()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    # migrate.db = db
    # migrate.app =
    db.init_app(app)
    # migrate.init_app(app)
    db.create_all()


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    rating = db.Column(db.Integer)

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

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
        }