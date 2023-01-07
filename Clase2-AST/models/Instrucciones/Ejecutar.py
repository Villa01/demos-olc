from models.Instrucciones.Instruccion import Instruccion
from models.Expresiones.Expresion import Expresion


class Ejecutar(Instruccion):

    def __init__(self, exp: Expresion, linea, columna):
        self.columna = columna
        self.linea = linea
        self.exp = exp

    def ejecutar(self, driver, ts):
        driver.append(str(self.exp.getValor(driver, ts)))
