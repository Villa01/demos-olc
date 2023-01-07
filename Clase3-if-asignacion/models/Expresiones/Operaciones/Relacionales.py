from models.Expresiones.Expresion import Expresion
from models.Expresiones.Operaciones.Operacion import Operacion, Operador, getOperacion
from models.TablaSimbolos.Tipos import Tipos

matriz_operaciones = {
    Operador.MAYOR: {
        Tipos.INT64: {
            Tipos.INT64: getOperacion(Operador.MAYOR),
            Tipos.FLOAT64: getOperacion(Operador.MAYOR),
        }
    },
    Operador.MENOR: {
        Tipos.INT64: {
            Tipos.INT64: getOperacion(Operador.MENOR),
            Tipos.FLOAT64: getOperacion(Operador.MENOR),
        }
    },
    Operador.IGUALIGUAL: {
        Tipos.INT64: {
            Tipos.INT64: getOperacion(Operador.IGUALIGUAL),
            Tipos.FLOAT64: getOperacion(Operador.IGUALIGUAL),
        }
    }
}


class Relacionales(Operacion):

    def __init__(self, exp1: Expresion, operador, exp2: Expresion, linea, columna, expU):
        super().__init__(exp1, operador, exp2, linea, columna, expU, matriz=matriz_operaciones)



