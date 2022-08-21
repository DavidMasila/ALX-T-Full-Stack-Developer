from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/doingstuff'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Todo(db.Model):
    __tablename__= 'stuff'
    id = db.Column(db.Integer, primary_key=True )
    description=db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()
#model
@app.route('/stuff/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description'] #get_json fetches the json body that was sent to it.
    #in the index.html we gave json key 'description'
    todo=Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return jsonify({ #returns json block that we give to it
        'description':todo.description
    })

@app.route('/')
def index(): #our controller
    return render_template('index.html', data=Todo.query.all())

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')