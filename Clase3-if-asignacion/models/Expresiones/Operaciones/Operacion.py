from enum import Enum
from models.Expresiones.Expresion import Expresion
from models.TablaSimbolos.Tipos import definirTipo


class Operador(Enum):
    SUMA = 1
    RESTA = 2
    MULTI = 3
    DIV = 4
    UNARIO = 5
    MAYOR = 6
    MENOR = 7
    IGUALIGUAL = 10


def getOperador(op) -> Operador:
    if op == '+':
        return Operador.SUMA
    elif op == '-':
        return Operador.RESTA
    elif op == '*':
        return Operador.MULTI
    elif op == '/':
        return Operador.DIV
    elif op == '>':
        return Operador.MAYOR
    elif op == '<':
        return Operador.MENOR
    elif op == '==':
        return Operador.IGUALIGUAL
    elif op == 'UNARIO':
        return Operador.UNARIO


def getOperacion(op: Operador):
    if op == Operador.SUMA:
        return lambda num1, num2: num1 + num2
    elif op == Operador.RESTA:
        return lambda num1, num2: num1 - num2
    elif op == Operador.MULTI:
        return lambda num1, num2: num1 * num2
    elif op == Operador.DIV:
        return lambda num1, num2: num1 / num2
    elif op == Operador.MAYOR:
        return lambda num1, num2: num1 > num2
    elif op == Operador.MENOR:
        return lambda num1, num2: num1 < num2
    elif op == Operador.IGUALIGUAL:
        return lambda num1, num2: num1 == num2


class Operacion(Expresion):

    def __init__(self, exp1: Expresion, operador, exp2: Expresion, linea, columna, expU, matriz=None):
        super().__init__()
        if matriz is None:
            matriz = {}
        self.expU = expU
        self.columna = columna
        self.linea = linea
        self.exp2 = exp2
        self.operador = getOperador(operador)
        self.exp1 = exp1
        self.matriz_operaciones = matriz

    def getValor(self, driver, ts):
        if not self.expU:
            valor_exp1 = self.exp1.getValor(driver, ts)
            valor_exp2 = self.exp2.getValor(driver, ts)

            operacion = self.matriz_operaciones.get(self.operador, None)
            if operacion is None:
                driver.append(
                    f"No se permite la operacion {self.operador} linea: {self.linea}, columna: {self.columna}")
                return
            tipo_exp1 = self.exp1.getTipo(driver, ts)
            operaciones_exp1 = operacion.get(tipo_exp1, None)
            if operaciones_exp1 is None:
                driver.append(
                    f"No se permite la operacion con el tipo {tipo_exp1} linea: {self.linea}, columna: {self.columna}")
                return
            tipo_exp2 = self.exp2.getTipo(driver, ts)
            funcion = operaciones_exp1.get(tipo_exp2, None)
            if funcion is None:
                driver.append(
                    f"No se permite la operacion con el tipo {tipo_exp2} linea: {self.linea}, columna: {self.columna}")
                return
            return funcion(valor_exp1, valor_exp2)

    def getTipo(self, driver, ts):
        value = self.getValor(driver, ts)
        return definirTipo(value)
