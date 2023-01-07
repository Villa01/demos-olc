from models.Expresiones.Expresion import Expresion
from models.TablaSimbolos.Tipos import definirTipo


class Primitivo(Expresion):

    def __init__(self, primitivo, linea: int, columna: int):
        self.tipo = None
        self.primitivo = primitivo
        self.linea = linea
        self.columna = columna

    def getTipo(self, driver, ts):
        if self.tipo is None:
            value = self.getValor(driver, ts)
            return definirTipo(value)
        else:
            return self.tipo

    def getValor(self, driver, ts):
        value = self.primitivo
        self.tipo = definirTipo(value)
        return value

