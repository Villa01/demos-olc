from ply.yacc import yacc
from analizador import lexer

from models.Expresiones.Operaciones.Aritmeticas import Aritmeticas
from models.Expresiones.Operaciones.Relacionales import Relacionales
from models.Expresiones.Primitivo import Primitivo
from models.Expresiones.Identificador import Identificador

from models.Instrucciones.Ejecutar import Ejecutar
from models.Instrucciones.Condicionales.ClaseIf import ClaseIf
from models.Instrucciones.Asignacion import Asignacion
from models.Instrucciones.Funcion import Funcion

from models.AST.ast import Ast
from models.TablaSimbolos.Simbolo import Simbolo, Simbolos
from models.TablaSimbolos.Tipos import Tipo

tokens = lexer.tokens

# precedencia

precedence = (
    ('left', 'MENOR', 'MAYOR', 'IGUALIGUAL'),
    ('left', 'MENOS', 'MAS'),
    ('left', 'MULTI', 'DIV'),
    ('right', 'UNARIO'),
)


# DEFINICION DE LA GRAMATICA
# inicio : instrucciones
# instrucciones: instrucciones instruccion PYC
#               | instruccion PYC
# instruccion   : ejecutar
#               | sent_if
#               | asignacion
#               | funcion
# asignacion : LET ID DOSPTS tipo IGUAL expresion
# sent_if : IF expresion LLAVA instrucciones LLAVC
# sent_if : IF expresion LLAVA instrucciones LLAVC ELSE LLAVA instrucciones LLAVC
# sent_if : IF expresion LLAVA instrucciones else_if
# else_if : ELSE IF expresion LLAVA instrucciones LLAVC
# ejecutar: EJECUTAR PARA expresion PARC
# expresion : expresion MAS expresion
#           | expresion MENOS expresion
#           | expresion MULTI expresion
#           | expresion DIV expresion
#           | expresion MENOR IGUAL expresion
#           | expresion IGUALIGUAL expresion
#           | expresion MAYOR IGUAL expresion
#           | PARA expresion PARC
#           | MENOS expresion
#           | ENTERO
#           | DECIMAL
#           | FALSE
#           | TRUE
#           | ID
# funcion | FUNC PARA parametros PARC LLAVA instrucciones LLAVC
# funcion | FUNC PARA PARC LLAVA instrucciones LLAVC
# parametros | parametros ID
# parametros | ID


def p_inicio(p):
    """
    inicio : instrucciones
    """
    p[0] = Ast(p[1])


def p_lista_instrucciones(p):
    """
    instrucciones : instrucciones instruccion PYC
    """
    p[1].append(p[2])
    p[0] = p[1]


def p_instrucciones_instruccion(p):
    """
    instrucciones : instruccion PYC
    """
    p[0] = [p[1]]


def p_instruccion(p):
    """
    instruccion : ejecutar
                | sent_if
                | asignacion
                | funcion
    """
    p[0] = p[1]


def p_instruccion_asignacion(p):
    """
    asignacion : LET ID DOSPTS tipo IGUAL expresion
    """
    p[0] = Asignacion(
        identificador=p[2],
        variable=Simbolo(Simbolos.VARIABLE, p[4], p[2], p[6]),
        tipo=p[4],
        linea=p.lineno(1),
        columna=0
    )


def p_tipo(p):
    """
    tipo : INT64
        | FLOAT64
        | BOOL
    """
    p[0] = Tipo(p[1])


def p_instruccion_ejecutar(p):
    """
    ejecutar : EJECUTAR PARA expresion PARC
    """
    p[0] = Ejecutar(p[3], p.lineno(1), 0)


def p_instruccion_if(p):
    """
    sent_if : IF expresion LLAVA instrucciones LLAVC
    """
    p[0] = ClaseIf(condicion=p[2], ins_if=p[4], ins_else=[], linea=p.lineno(1), columna=0)


def p_instruccion_if_else(p):
    """
    sent_if : IF expresion LLAVA instrucciones LLAVC ELSE LLAVA instrucciones LLAVC
    """
    p[0] = ClaseIf(condicion=p[2], ins_if=p[4], ins_else=p[8], linea=p.lineno(1), columna=0)


def p_instruccion_if_elseif(p):
    """
    sent_if : IF expresion LLAVA instrucciones else_if
    """
    p[0] = ClaseIf(condicion=p[2], ins_if=p[4], ins_else=[p[6]], linea=p.lineno(1), columna=0)


def p_instruccion_elseif(p):
    """
    else_if : ELSE IF expresion LLAVA instrucciones LLAVC
    """
    p[0] = ClaseIf(condicion=p[2], ins_if=p[4], ins_else=[], linea=p.lineno(1), columna=0)


def p_exp_aritmeticas(p):
    """
    expresion : expresion MAS expresion
              | expresion MENOS expresion
              | expresion MULTI expresion
              | expresion DIV expresion
    """
    p[0] = Aritmeticas(exp1=p[1], operador=p[2], exp2=p[3], expU=False, linea=p.lineno(1), columna=0)


def p_exp_relacionales(p):
    """
    expresion   : expresion MENOR expresion
                | expresion IGUALIGUAL expresion
                | expresion MAYOR expresion
    """
    p[0] = Relacionales(exp1=p[1], operador=p[2], exp2=p[3], expU=False, linea=p.lineno(1), columna=0)


def p_exp_parentesis(p):
    """
    expresion : PARA expresion PARC
    """
    p[0] = p[2]


def p_exp_unario(p):
    """
    expresion : MENOS expresion %prec UNARIO
    """
    p[0] = Aritmeticas(exp1=p[2], operador=p[1], exp2=None, expU=True, linea=p.lineno(1), columna=0)


def p_exp_primitivo(p):
    """
    expresion : ENTERO
              | DECIMAL
              | TRUE
              | FALSE
    """
    p[0] = Primitivo(p[1], p.lineno(1), 0)


def p_exp_id(p):
    """
    expresion : ID
    """
    p[0] = Identificador(p[1], p.lineno(1), 0)


def p_sent_function(t):
    """
    funcion : FUNC ID PARA parametros PARC LLAVA instrucciones LLAVC
    """
    t[0] = Funcion(Simbolos.FUNCION, Tipo('default'), t[2], None, t[4], t[7], t.lineno(1), 0)


def p_sent_function_no_p(t):
    """
    funcion : FUNC ID PARA PARC LLAVA instrucciones LLAVC
    """
    t[0] = Funcion(Simbolos.FUNCION, Tipo('default'), t[2], None, [], t[6], t.lineno(1), 0)


def p_lista_parametros(t):
    """
    parametros : parametros COMA ID
    """
    t[0] = t[1]
    t[0].append(Simbolo(Simbolos.PARAMETRO, Tipo('default'), t[3], None))


def p_parametro(t):
    """
    parametros : ID
    """
    t[0] = [Simbolo(Simbolos.PARAMETRO, Tipo('default'), t[3], None)]


# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r}')


# Build the parser
parser = yacc(debug=True)
