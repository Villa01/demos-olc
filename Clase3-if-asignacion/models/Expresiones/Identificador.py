from models.Driver import Driver
from models.Expresiones.Expresion import Expresion
from models.TablaSimbolos.TablaSimbolos import TablaSimbolos


class Identificador(Expresion):

    def __init__(self, identificador: str, linea: int, columna: int):
        self.columna = columna
        self.linea = linea
        self.identificador = identificador

    def getTipo(self, driver: Driver, ts: TablaSimbolos):
        return ts.buscar(self.identificador).tipo.tipo

    def getValor(self, driver: Driver, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)

        if simbolo is not None:
            return simbolo.valor
        else:
            driver.console(f"No se encontró el símbolo linea: {self.linea}, columna: {self.columna}")
            return

