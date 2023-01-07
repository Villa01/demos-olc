from enum import Enum


class Tipos(Enum):
    INT64 = 1
    FLOAT64 = 2
    BOOLEAN = 3
    DEFAULT = 4


def getTipo(s: str):
    if s == "int64":
        return Tipos.INT64
    if s == "float64":
        return Tipos.FLOAT64
    if s == "bool":
        return Tipos.BOOLEAN
    elif s == "default":
        return Tipos.DEFAULT


def definirTipo(value):
    if type(value) == float:
        return Tipos.FLOAT64
    elif type(value) == int:
        return Tipos.INT64
    elif type(value) == bool:
        return Tipos.BOOLEAN
    else:
        return Tipos.DEFAULT


class Tipo:

    def __init__(self, stipo: str):
        self.stipo = stipo
        self.tipo = getTipo(stipo)

    def getSTipo(self):
        return self.stipo
