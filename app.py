import json
from flask import Flask
from models import Schema
from service import ToDoService
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/create_todo', methods=['POST',])

def create_todo():
    request_values = {"text": "Teste", "Description": "Descricao texte"}
    print(request_values)
    return 'Inserido com sucesso' if ToDoService().create(request_values) else 'Naum foi inserido '
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    Schema()
    app.run(host='127.0.0.1', port=5000, debug=True)