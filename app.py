from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Add this to fix the 404 on /
@app.route('/')
def home():
    return jsonify({"message": "API is running!"})

# 👇 Example actual API endpoint
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify([])  # Just an example

if __name__ == '__main__':
    app.run(debug=True)


todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if 'task' not in data:
        return jsonify({'error': 'Task is required'}), 400
    todos.append({'id': len(todos) + 1, 'task': data['task'], 'done': False})
    return jsonify({'message': 'Todo added'}), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = True
            return jsonify({'message': 'Todo updated'})
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
