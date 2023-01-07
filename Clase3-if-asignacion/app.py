from flask import Flask, send_from_directory, request
from flask_cors import CORS
import json

from analizador.parser import parser

from models.TablaSimbolos.TablaSimbolos import TablaSimbolos
from models.Driver import Driver
from models.AST.ast import Ast

app = Flask(__name__, static_url_path='', static_folder='frontend/dist')
CORS(app)


# Get
@app.route('/')
def frontend():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/interpretar', methods=['POST'])
def interpretar():
    if request.method == 'POST':
        data = request.json
        ast: Ast = parser.parse(data.get('instrucciones'))

        ts = TablaSimbolos(None, 'Global')
        driver = Driver()

        ast.ejecutar(driver, ts)

        return {
            'resultado': driver.console,
        }
