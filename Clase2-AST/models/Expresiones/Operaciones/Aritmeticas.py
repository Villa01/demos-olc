from models.Expresiones.Operaciones.Operacion import Operacion, Operador, getOperacion
from models.TablaSimbolos.Tipos import Tipos, definirTipo

matriz_operaciones = {
    Operador.SUMA: {
        Tipos.INT64: {
            Tipos.INT64: getOperacion(Operador.SUMA),
            Tipos.FLOAT64: getOperacion(Operador.SUMA),
        },
        Tipos.FLOAT64: {
            Tipos.INT64: getOperacion(Operador.SUMA),
            Tipos.FLOAT64: getOperacion(Operador.SUMA),
        }
    },
    Operador.RESTA: {
        Tipos.INT64: {
            Tipos.INT64: getOperacion(Operador.RESTA),
            Tipos.FLOAT64: getOperacion(Operador.RESTA),
        },
        Tipos.FLOAT64: {
            Tipos.INT64: getOperacion(Operador.RESTA),
            Tipos.FLOAT64: getOperacion(Operador.RESTA),
        }
    },
    Operador.MULTI: {
        Tipos.INT64: {
            Tipos.INT64: getOperacion(Operador.MULTI),
            Tipos.FLOAT64: getOperacion(Operador.MULTI),
        },
        Tipos.FLOAT64: {
            Tipos.INT64: getOperacion(Operador.MULTI),
            Tipos.FLOAT64: getOperacion(Operador.MULTI),
        }
    },

    Operador.DIV: {
        Tipos.INT64: {
            Tipos.INT64: getOperacion(Operador.DIV),
            Tipos.FLOAT64: getOperacion(Operador.DIV),
        },
        Tipos.FLOAT64: {
            Tipos.INT64: getOperacion(Operador.DIV),
            Tipos.FLOAT64: getOperacion(Operador.DIV),
        }
    },
}


class Aritmeticas(Operacion):

    def getTipo(self, driver, ts):
        value = self.getValor(driver, ts)
        return definirTipo(value)

    # get Valor con Diccionarios
    def getValor(self, driver, ts):
        if not self.expU:
            valor_exp1 = self.exp1.getValor(driver, ts)
            valor_exp2 = self.exp2.getValor(driver, ts)

            operacion = matriz_operaciones[self.operador]
            tipo_exp1 = operacion[self.exp1.getTipo(driver, ts)]
            funcion = tipo_exp1[self.exp2.getTipo(driver, ts)]

            return funcion(valor_exp1, valor_exp2)

    # get valor con condicionales
    def getValor2(self, driver, ts):
        tipo_exp1 = self.exp1.getTipo(driver, ts)
        tipo_exp2 = self.exp2.getTipo(driver, ts) if not self.expU else None

        if self.expU is not None:
            if self.operador == Operador.UNARIO:
                return - self.exp1.getValor(driver, ts)
            else:
                # Error: la expresion unaria solo acepta el operador -
                pass

        if self.operador == Operador.SUMA:
            # INT + ?
            # FLOAT + ?
            if tipo_exp1 in [Tipos.INT64, Tipos.FLOAT64]:
                # INT + INT
                # INT + FLOAT
                # FLOAT + INT
                # FLOAT + FLOAT
                if tipo_exp2 in [Tipos.INT64, Tipos.FLOAT64]:
                    return self.exp1.getValor(driver, ts) + self.exp2.getValor(driver, ts)
                else:
                    print(f'La 2da expresion de la suma debe ser un integer o float ', self.exp2.linea,
                          self.exp2.columna)
            else:
                print(f'La 1er expresion de la suma debe ser un integer o float ', self.exp2.linea, self.exp2.columna)

        elif self.operador == Operador.RESTA:
            if tipo_exp1 == Tipos.INT64:
                if tipo_exp2 == Tipos.INT64:
                    return self.exp1.getValor(driver, ts) - self.exp2.getValor(driver, ts)
                else:
                    print(f'La 2da expresion de la resta debe ser del mismo tipo')

            elif tipo_exp1 == Tipos.FLOAT64:
                if tipo_exp2 == Tipos.FLOAT64:
                    return self.exp1.getValor(driver, ts) - self.exp2.getValor(driver, ts)
                else:
                    print(f'La 2da expresion de la resta debe ser del mismo tipo')
            else:
                print(f'La 1er expresion de la resta debe ser un integer o float ', self.exp2.linea, self.exp2.columna)

        elif self.operador == Operador.MULTI:
            if tipo_exp1 in [Tipos.INT64, Tipos.FLOAT64]:
                if tipo_exp2 in [Tipos.INT64, Tipos.FLOAT64]:
                    return self.exp1.getValor(driver, ts) * self.exp2.getValor(driver, ts)
                else:
                    print(f'La 2da expresion de la multiplicacion debe ser un integer o float ', self.exp2.linea,
                          self.exp2.columna)
            else:
                print(f'La 1er expresion de la multiplicacion debe ser un integer o float ', self.exp2.linea,
                      self.exp2.columna)

        elif self.operador == Operador.DIV:
            if tipo_exp1 in [Tipos.INT64, Tipos.FLOAT64]:
                if tipo_exp2 in [Tipos.INT64, Tipos.FLOAT64]:
                    return self.exp1.getValor(driver, ts) / self.exp2.getValor(driver, ts)
                else:
                    print(f'La 2da expresion de la division debe ser un integer o float ', self.exp2.linea,
                          self.exp2.columna)
            else:
                print(f'La 1er expresion de la division debe ser un integer o float', self.exp2.linea,
                      self.exp2.columna)

        else:
            print(f'La operacion {self.operador} no es soportado')
