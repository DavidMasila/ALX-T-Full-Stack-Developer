from typing import final
from flask import Flask, render_template, request, url_for, redirect, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/doingstuff'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'stuff'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


db.create_all()
# model


@app.route('/stuff/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        # get_json fetches the json body that was sent to it.
        description = request.get_json()['description']
        # in the index.html we gave json key 'description'
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
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


@app.route('/')
def index():  # our controller
    return render_template('index.html', data=Todo.query.all())


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
