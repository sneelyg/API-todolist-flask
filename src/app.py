from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



@app.route('/todos', methods=['GET'])
def hello_world():
    todos_json = jsonify(todos)
    return todos_json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body =request.get_json(force=True)  #se obliga que lody leuen JSON
    todos.append(request_body)  #agrega le body al arreode a
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    todos_json = jsonify(todos)
    return todos_json


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)