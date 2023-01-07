
# Declaracion de tokens
from ply import lex



tokens = ('MAS', 'MENOS', 'MULTI', 'DIV', 'PARA', 'PARC', 'NUMERO')


# Caracteres ignorados
t_ignore = '[\t ]'

# Tokens con Regex
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
t_PARA = r'\('
t_PARC = r'\)'


# Tokens con funciones
def t_NUMERO(t):
    r'\d+'
    t.value = float(t.value)
    return t


# Ignora y hace una accion
def t_ignorar_salto(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


# Manejo de errores lexicos
def t_error(t):
    print(f'Caracter no reconocido {t.value[0]!r} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)


lex.lex()
