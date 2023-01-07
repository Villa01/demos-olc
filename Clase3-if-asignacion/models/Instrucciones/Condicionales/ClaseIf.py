from models.Expresiones.Expresion import Expresion
from models.Instrucciones.Instruccion import Instruccion
from models.TablaSimbolos.TablaSimbolos import TablaSimbolos
from models.TablaSimbolos.Tipos import Tipos
from models.Driver import Driver


class ClaseIf(Instruccion, Expresion):

    def __init__(self, condicion: Expresion, ins_if, ins_else, linea: int, columna: int):
        self.ins_else = ins_else
        self.ins_if = ins_if
        self.columna = columna
        self.linea = linea
        self.condicion = condicion

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        ts_local = TablaSimbolos(ts, "IF")
        condicion = self.condicion.getValor(driver, ts)
        tipo_condicion = self.condicion.getTipo(driver, ts)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append(f"La condicion debe ser booleana linea: {self.linea}, columna: {self.columna}")

        if condicion:
            for ins in self.ins_if:
                ins.ejecutar(driver, ts_local)

        else:
            for ins in self.ins_else:
                ins.ejecutar(driver, ts_local)
