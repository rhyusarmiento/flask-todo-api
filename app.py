import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "app.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean)
    def __init__(self, title, done):
        self.title = title
        self.done = done

class TodoSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "done")

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

#create todo
@app.route('/api/add-todo', methods=['POST'])
def add_todo():
    title = request.json['title']
    done = request.json['done']
    new_todo = Todo(title=title, done=done)
    db.session.add(new_todo)
    db.session.commit()
    return todo_schema.jsonify(new_todo)

#get all todo
@app.route('/api/get-all-todos', methods=['GET'])
def get_all_todo():
    all_todos = Todo.query.all()
    return jsonify(todos_schema.dump(all_todos))

#edit todo
@app.route('/api/edit-done/<todo_id>', methods=['PATCH'])
def edit_done(todo_id):
    todo = Todo.query.get(todo_id)
    new_done = request.json['done']
    todo.done = new_done
    db.session.commit()
    return todo_schema.jsonify(todo)

#delete todo

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
