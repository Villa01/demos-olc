from models.TablaSimbolos.Tipos import Tipo
from enum import Enum


class Simbolos(Enum):
    VARIABLE = 1
    FUNCION = 2
    PARAMETRO = 3


def getSimbolo(s):
    if s == 1:
        return Simbolos.VARIABLE
    elif s==2:
        return Simbolos.FUNCION


class Simbolo:

    def __init__(self, simbolo: Simbolos, tipo: Tipo, id: str, valor, param_list = []):
        self.param_list = param_list
        self.valor = valor
        self.id = id
        self.tipo = tipo
        self.simbolo = getSimbolo(simbolo)
