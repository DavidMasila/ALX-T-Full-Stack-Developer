from os import abort
import sys
from app import TodoList, app, Todo, db
from flask import render_template, request, jsonify, redirect, url_for

# controllers


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        list_id = request.get_json()['list_id']
        todo = Todo(description=description, completed=False, list_id=list_id)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['complete'] = todo.completed
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)


@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    error = False
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return redirect(url_for('index'))


@app.route('/todos/<todo_id>/delete', methods=['DELETE'])
def delete_todo(todo_id):
    error = False
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify({'success': True})


@app.route('/lists/create', methods=['POST'])
def create_list():
    error = False
    body = {}
    try:
        name = request.get_json()['name']
        todolist = TodoList(name=name)
        db.session.add(todolist)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)


@app.route('/lists/<list_id>/delete', methods=['DELETE'])
def delete_list(list_id):
    error = False
    try:
        list = TodoList.query.get(list_id)
        for todo in list.todos:  # list here is the backref , todos is the children
            db.session.delete(todo)
        db.session.delete(list)
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
        return jsonify({'success': True})


@app.route('/lists/<list_id>/set-completed', methods=['POST'])
def set_completed_list(list_id):
    error = False
    try:
        list = TodoList.query.get(list_id)
        for todo in list.todos:
            todo.completed = True
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return '', 200


@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))


@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html',
                           lists=TodoList.query.all(),
                           active_list=TodoList.query.get(list_id),
                           todos=Todo.query.filter_by(
                               list_id=list_id).order_by('id').all()
                           )
