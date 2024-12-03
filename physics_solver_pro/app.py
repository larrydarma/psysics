
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    physics_problem = data.get('problem', '')
    
    # Placeholder response: aquí integrarías la API para resolver problemas de física.
    response = {
        "problem": physics_problem,
        "solution": "Esta es una solución de ejemplo con el procedimiento detallado."
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
