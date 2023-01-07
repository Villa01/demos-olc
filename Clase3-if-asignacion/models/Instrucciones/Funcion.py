from models.TablaSimbolos.Simbolo import Simbolo, Simbolos
from models.TablaSimbolos.TablaSimbolos import TablaSimbolos
from models.Instrucciones.Instruccion import Instruccion
from models.TablaSimbolos.Tipos import Tipo

class Funcion(Simbolo, Instruccion):

    def __init__(self, tipo_simbolo: Simbolos, tipo:Tipo, identificador: str, valor, lista_param, lista_ins,
                 linea, columna):
        super().__init__(tipo_simbolo, tipo, identificador, valor)
        super(Funcion, self).__init__()
        self.columna = columna
        self.lista_ins = lista_ins
        self.linea = linea
        self.valor = valor
        self.lista_param = lista_param
        self.identificador = identificador
        self.tipo_simbolo = tipo_simbolo


    def agregarFuncionSimbolo (self, driver, ts):
        simbolo = ts.buscar(self.id)
        if simbolo is not None:
            ts.add(self.identificador, self)
        else:
            driver.agregarError(f'No se encontró {self.identificador}', self.linea, self.columna)

    def ejecutar(self, driver, ts: TablaSimbolos):
        ts_local = TablaSimbolos(ts, 'Funcion ' + self.identificador)
        for ins in self.lista_ins:
            res = ins.ejecutar(driver, ts_local)

            if res is not None:
                return res
        return None

