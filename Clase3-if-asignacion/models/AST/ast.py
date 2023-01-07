from models.Instrucciones.Funcion import Funcion


class Ast:

    def __init__(self, instrucciones=None):

        if instrucciones is None:
            instrucciones = []

        self.instrucciones = instrucciones

    def ejecutar(self, driver, ts):
        for ins in self.instrucciones:
            if isinstance(ins, Funcion):
                ins.agregarFuncionSimbolo(driver, ts)

        for instruccion in self.instrucciones:
            if not isinstance(ins, Funcion):
                instruccion.ejecutar(driver, ts)
