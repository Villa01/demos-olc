from enum import Enum


class Tipos(Enum):
    INT64 = 1
    FLOAT64 = 2


def getTipo(s: str):
    if s == "INT64":
        return Tipos.INT64
    if s == "FLOAT64":
        return Tipos.FLOAT64


def definirTipo(value):
    if type(value) == float:
        return Tipos.FLOAT64
    elif type(value) == int:
        return Tipos.INT64
    else:
        return None


class Tipo:

    def __init__(self, stipo: str):
        self.stipo = stipo
        self.tipo = getTipo(stipo)

    def getSTipo(self):
        return self.stipo
