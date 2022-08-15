from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#db configuration dialect, username, password, host, port and db name
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:postgres@localhost:5432/udacity1'
db=SQLAlchemy(app) #database instance

#models and defining models
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0')