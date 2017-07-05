# coding:utf-8

# 还有点小错误，必须加以改正
tokens = (
    "NOUN", "PRONOUN", "VERB"
)

t_NOUN = r"dog|man|woman"
t_PRONOUN = r"i|he|she|item"
t_VERB = r"like|help|fuck"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

import ply.lex as lex
lexer = lex.lex()

# 句法部分#####################
def p_statement_default(p):
    'statement : PRONOUN VERB NOUN'
    print(p[1]+p[2]+p[3]+"是有效语句") #toString对应的是str()

def p_error(p):
    print("Syntax error at '%s'" % p)


import ply.yacc as yacc
# parser = yacc.yacc()
yacc.yacc()

while True:
    try:
        s = input('yacc1 > ')
        # parser.parse(s)
        yacc.parse(s)
    except EOFError:
        break
