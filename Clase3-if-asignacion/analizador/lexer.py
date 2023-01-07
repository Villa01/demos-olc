# Declaracion de tokens
from ply import lex

reservadas = {
    'ejecutar': 'EJECUTAR',
    'if': 'IF',
    'else': 'ELSE',
    'let': 'LET',
    'int64': 'INT64',
    'float64': 'FLOAT64',
    'bool': 'BOOL',
    'func': 'FUNC'
}

tokens = [
             'DIV',
             'DECIMAL',
             'ENTERO',
             'MAS',
             'MENOS',
             'MULTI',
             'PARA',
             'PARC',
             'PYC',
             'LLAVA',
             'LLAVC',
             'TRUE',
             'FALSE',
             'MENOR',
             'MAYOR',
             'IGUALIGUAL',
             'DOSPTS',
             'IGUAL',
             'COMA',
             'ID'
         ] + list(reservadas.values())

# Caracteres ignorados
t_ignore = '[\r\t ]'

# Tokens con Regex
t_MAS = r'\+'
t_MENOS = r'-'
t_DIV = r'/'
t_MULTI = r'\*'
t_PARA = r'\('
t_PARC = r'\)'
t_PYC = r'\;'
t_LLAVA = r'\{'
t_LLAVC = r'\}'
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_IGUAL = r'\='
t_IGUALIGUAL = r'\=\='
t_DOSPTS = r'\:'
t_COMA = r'\,'


def t_DECIMAL(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


# Tokens con funciones
def t_ENTERO(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_TRUE(t):
    r"""true"""
    t.value = True
    return t


def t_FALSE(t):
    r"""false"""
    t.value = False
    return t


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reservadas.get(t.value, 'ID')  # Check for reserved words
    return t


# Ignora y hace una accion
def t_ignorar_salto(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


# Manejo de errores lexicos
def t_error(t):
    print(f'Caracter no reconocido {t.value[0]!r} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)


lex.lex()
