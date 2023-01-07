from models.Expresiones.Expresion import  Expresion
from models.Instrucciones.Instruccion import Instruccion
from models.TablaSimbolos.TablaSimbolos import TablaSimbolos
from models.TablaSimbolos.Simbolo import Simbolo, Simbolos

class Llamada (Instruccion, Expresion):

    def __init__(self, identificador: str, lista_param, linea, columna) -> None:
        super().__init__()
        self.identificador = identificador
        self.lista_param = lista_param
        self.linea = linea
        self.columna = columna

    def getTipo(self, driver, ts):
        value = ts.buscar(self.identificador)
        return value.tipo.tipo

    def getValue(self, driver, ts):
        value = self.ejecutar(driver, ts)
        return value

    def ejecutar(self, driver, ts: TablaSimbolos):
        ts_local = TablaSimbolos(ts, 'Llamada a ' + self.identificador)

        func_simb = ts_local.buscar(self.identificador)

        func_param = func_simb.param_list
        # TODO: verificar los parametros
        names = []
        for symb in func_param:
            names.append(symb.identifier)

        cont = 0
        for param in self.lista_param:
            t = param.getTipo(driver, ts_local)
            val = param.getValor(driver, ts_local)
            new_symbol = Simbolo(Simbolos.PARAMETRO, t, names[cont], val, None)
            ts_local.add(names[cont], new_symbol)
            cont += 1

        res = func_simb.ejecutar(driver, ts_local)

        return res




