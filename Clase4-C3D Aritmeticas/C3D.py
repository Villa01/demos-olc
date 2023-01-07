tokens = [
    'PARA',
    'PARC',
    'MAS',
    'MENOS',
    'MULTI',
    'DIV',
    'MENOR',
    'MAYOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'DIFF',
    'ENTERO',
]

reserved = {
    'AND' : 'AND',
    'OR': 'OR',
    'NOT':'NOT'
}

tokens += reserved.values()

t_PARA = r'\('
t_PARC = r'\)'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTI = r'\*'
t_DIV = r'\/'
t_MAYOR = r'\<'
t_MENOR = r'\>'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_IGUALIGUAL = r'\=\='
t_DIFF = r'\!\='


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = t.value
    except ValueError:
        print("Error en el entero")

    return t

t_ignore = " \t"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t  

def t_error(t):
    print("No se reconoce el caracter " + t.value[0])


import ply.lex as lex
from temp import temp
lexer = lex.lex()

precedence = (
    ('left', 'AND', 'OR'),
    ('right', 'UNARIO'),
)
def p_inicio(t):
    'S : L'
    print(t[1].C3D)
def p_logicas(t):
    '''
    L :  L AND L
      |  L OR L
      |  NOT L %prec UNARIO
    '''
    if t[2] == 'AND':
        t[0] = temp()
        t[0].C3D = t[1].C3D + t[1].LV + ":" + t[3].C3D 
        t[0].LV = t[3].LV
        t[0].LF = t[1].LF + " " + t[3].LF
        t[0].C3D += "----------AND--------\n"
        t[0].C3D += "LV : " + t[0].LV + " \n"
        t[0].C3D += "LF : " + t[0].LF + " \n"
        t[0].C3D += "---------------------\n"
    elif t[2] == 'OR':
        t[0] = temp()
        t[0].C3D = t[1].C3D + t[1].LV + ":" + t[3].C3D 
        t[0].LV = t[1].LV + " " + t[3].LV
        t[0].LF = t[3].LF    
        t[0].C3D += "----------OR---------\n"
        t[0].C3D += "LV : " + t[0].LV + " \n"
        t[0].C3D += "LF : " + t[0].LF + " \n"
        t[0].C3D += "---------------------\n"
        
    elif t[1] == 'NOT':
        t[0] = temp()
        t[0].C3D = t[2].C3D
        t[0].LV = t[2].LF
        t[0].LF = t[2].LV    
        t[0].C3D += "----------NOT--------\n"
        t[0].C3D += "LV : " + t[0].LV + " \n"
        t[0].C3D += "LF : " + t[0].LF + " \n"
        t[0].C3D += "---------------------\n"

def p_sin_l(t):
    'L : R'
    t[0] = t[1]

def p_r(t):
    '''R : E MENOR E
        | E MAYOR E
        | E MAYORIGUAL E
        | E MENORIGUAL E
        | E IGUALIGUAL E
        | E DIFF E    
    '''
    t[0] = temp()
    t[0].new_label_v()
    t[0].new_label_f()
    t[0].C3D = t[1].C3D + t[3].C3D + "\n" + "if "+ t[1].TMP + t[2] + t[3].TMP+ " goto " + t[0].LV + "\ngoto " + t[0].LF + "\n"
    
    t[0].C3D += "--LV : " + t[0].LV + " \n"
    t[0].C3D += "--LF : " + t[0].LF + " \n"

def p_sin_r(t):
    'R : E'
    t[0] = t[1]

def p_e(t):
    '''
    E   : E MAS T
        | E MENOS T
    '''
    t[0] = temp()
    t[0].nuevo_temp()
    t[0].C3D = t[1].C3D + t[3].C3D + "\n" + t[0].TMP + "=" + t[1].TMP + t[2] + t[3].TMP

def p_e_sin(t):
    'E : T'
    t[0] = t[1]

def p_T(t):
    '''
    T   : T MULTI F
        | T DIV F
    '''
    t[0] = temp()
    t[0].nuevo_temp()
    t[0].C3D = t[1].C3D + t[3].C3D + "\n" + t[0].TMP + "=" + t[1].TMP + t[2] + t[3].TMP
       

def p_sin(t):
    ' T : F'
    t[0] = t[1]

def p_F(t):
    'F   : PARA L PARC'
    t[0] = t[2]

def p_F_num(t):
    'F   : ENTERO '
    t[0] = temp()
    t[0].TMP = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

input = "NOT (3>3 AND 3!= 5) OR 9>1"
parser.parse(input)
input = "23 + 234 / 23 * ( 5 + 5)"
parser.parse(input)