from models.TablaSimbolos.Simbolo import Simbolo


class TablaSimbolos:

    def __init__(self, anterior, env):
        self.env = env
        self.anterior = anterior
        self.tabla = {}

    def add(self, id: str, simbolo: Simbolo):
        self.tabla[id] = simbolo

    def buscar(self, id: str) -> Simbolo:
        ts = self

        while ts is not None:
            exist = ts.tabla.get(id)

            if exist is not None:
                return exist

            ts = ts.anterior

        return None

    def buscarActual(self, id: str) -> Simbolo:

        return self.tabla.get(id)
