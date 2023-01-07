from models.Instrucciones import Instruccion


class Ast:

    def __init__(self, instrucciones=None):
        if instrucciones is None:
            instrucciones = []

        self.instrucciones = instrucciones

    def ejecutar(self, driver, ts):
        for instruccion in self.instrucciones:
            instruccion.ejecutar(driver, ts)
