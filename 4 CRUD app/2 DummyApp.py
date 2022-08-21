from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Todo(db.Model):
    __tablename__= 'stuff'
    id = db.Column(db.Integer, primary_key=True )
    description=db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/stuff/create', methods=['POST']) #listener
def create_todo():
    description = request.form.get('description','')#given an empty default
    todo=Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index')) #enables appending of the new page information on the browser

@app.route('/')
def index(): #our controller
    return render_template('index.html', data=Todo.query.all())

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')