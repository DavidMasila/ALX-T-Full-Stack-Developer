from flask import Flask, render_template, request, url_for, redirect, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/doingstuff'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate=Migrate(app,db)

#parent model
class TodoList(db.Model):
    __tablename__ = 'todolist'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)

    def __repr__(self):
        return f"<Todolist {self.id} {self.name}"

#child model
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolist.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

@app.route('/stuff/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        # get_json fetches the json body that was sent to it.
        description = request.get_json()['description']
        # in the index.html we gave json key 'description'
        list_id=request.get_json()['list_id']
        todo = Todo(description=description, complete=False, list_id=list_id)
        db.session.add(todo)
        db.session.commit()
        body['id']=todo.id
        body['description'] = todo.description
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/stuff/<todo_id>/set-completed', methods=['POST']) #we need to grab the existing to do item i.e. get the todo ID
def set_completed_todo(todo_id):
    error = False
    try:
        completed = request.get_json()['completed']
        todo=Todo.query.get(todo_id)
        print('Todo: '. todo)
        todo.completed = completed
        db.session.commit()
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return redirect(url_for('index'))


@app.route('/stuff/<todo_id>', methods=['DELETE'])
def deleted_item(todo_id):
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({'success':True})

    
@app.route('/lists/<list_id>')
def get_list_todos(list_id):  # our controller
    return render_template('index.html',
    lists=TodoList.query.all(),
    active_list=TodoList.query.get(list_id),
    todos=Todo.query.filter_by(list_id=list_id).order_by('id').all()
)

@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
