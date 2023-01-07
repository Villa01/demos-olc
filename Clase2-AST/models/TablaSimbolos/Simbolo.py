from models.TablaSimbolos.Tipos import Tipo
from enum import Enum


class Simbolos(Enum):
    VARIABLE = 1


def getSimbolo(s):
    if s == 1:
        return Simbolos.VARIABLE


class Simbolo:

    def __init__(self, simbolo: int, tipo: Tipo, id: str, value):
        self.value = value
        self.id = id
        self.tipo = tipo
        self.simbolo = getSimbolo(simbolo)
