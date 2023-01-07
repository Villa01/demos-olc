from models.Instrucciones.Instruccion import Instruccion
from models.TablaSimbolos.Simbolo import Simbolo, Simbolos
from models.TablaSimbolos.Tipos import Tipo
from models.Driver import Driver
from models.TablaSimbolos.TablaSimbolos import TablaSimbolos


class Asignacion(Instruccion):

    def __init__(self, identificador: str, variable: Simbolo, tipo: Tipo, linea: int, columna: int,):
        self.columna = columna
        self.linea = linea
        self.tipo = tipo
        self.variable = variable
        self.identificador = identificador

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):

        tipo_var = self.variable.valor.getTipo(driver, ts)
        valor_var = self.variable.valor.getValor(driver, ts)

        # Verificar el tipo
        if self.tipo.tipo != tipo_var:
            driver.append(f"La variable no coincide con el tipo del valor linea: {self.linea}, columna: {self.columna}")
            return

        # Agregar a tabla de simbolos
        simbolo = ts.buscar(self.identificador)

        if simbolo is None:
            # Si no existe la variable
            simbolo_nuevo = Simbolo(Simbolos.VARIABLE, self.tipo, self.identificador, valor_var)
            ts.add(self.identificador, simbolo_nuevo)
        else:
            # Si ya existe la variable
            simbolo.valor = valor_var
            ts.add(self.identificador, simbolo)
