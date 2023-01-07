from flask import Flask, render_template, request
from flask_cors import CORS

from analizador.parser import parser

from models.TablaSimbolos.TablaSimbolos import TablaSimbolos
from models.Driver import Driver
from models.AST.ast import Ast

app = Flask(__name__)
CORS(app)


# Get
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/interpretar', methods=['POST'])
def interpretar():
    if request.method == 'POST':
        data = request.json
        print(data)
        ast: Ast = parser.parse(data.get('instrucciones'))

        ts = TablaSimbolos(None, 'Global')
        driver = Driver()

        ast.ejecutar(driver, ts)

        return {
            'resultado': driver.console
        }
