from models.Expresiones.Expresion import Expresion
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

    def __init__(self, exp1: Expresion, operador, exp2: Expresion, linea, columna, expU):

        super().__init__(exp1, operador, exp2, linea, columna, expU, matriz= matriz_operaciones)
