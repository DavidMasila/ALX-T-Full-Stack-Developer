from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/udacity1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)
migrate=Migrate(app, db)

class Todo(db.Model):
    __tablename__='todo'
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'To do {self.id} {self.description}'

db.create_all()

@app.route('/')
def index():
    return 'Hellow Pipos'


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')