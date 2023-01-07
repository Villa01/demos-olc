from flask import Flask, render_template, request
from analizador.parser import parser

app = Flask(__name__)

# Get
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/interpretar', methods=['POST'])
def interpretar():
    if request.method == 'POST':
        result = parser.parse('2 * 3 + 4 * (5 - 4) / 23')
        return {
            'resultado': result
        }
