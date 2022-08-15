from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/udacity1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(), nullable=False)
    category=db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Person ID: {self.id}, Name: {self.name}, User_type: {self.category}'
db.create_all()


@app.route('/')
def index():
    user=User.query.filter_by(category="Admin").first()
    return f'{user.name} is an Admin'
if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
