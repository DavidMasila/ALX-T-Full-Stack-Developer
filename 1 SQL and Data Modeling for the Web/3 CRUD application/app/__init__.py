from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost:5432/todoapp2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)
migrate=Migrate(app,db)

#models
class TodoList(db.Model):
    __tablename__ = "todolists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True) #todos is the name of the children. 


    def __repr__(self):
        return f"<todolist {self.id} {self.name}"


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)

    def __repr__(self):
        return f'<todo f{self.id}, {self.description} list {self.list_id}'


from app import views