#coding:utf-8

# 还有点小错误，必须加以改正


import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

tokens=(
    "NOUN","PRONOUN","VERB"
)

def t_VERB(t):
    r"like|help|fuck"
    print(t.value + " is a verb")

def t_NOUN(t):
    r"dog|man|woman"

def t_PRONOUN(t):
    r"i|he|she|item"
    print(t.value + " is a pron")

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

import ply.lex as lex
lexer = lex.lex()


################句法部分#####################3
def p_statement_sentence(p):
    'statement : pronoun verb noun'
    print(p+" is a sentence")


def p_noun(p):
    'noun : NOUN'

def p_pronoun(p):
    'pronoun : PRONOUN'

def p_verb(p):
    'verb : VERB'

# def p_expression_noun(p):
#     "expression : NOUN"

def p_error(p):
    print("Syntax error at '%s'" % p)
    # parser.errok()
    # yacc.yacc().errorok()
    

import ply.yacc as yacc
parser = yacc.yacc(debug=True,debuglog=log)

while True:
    try:
        s = input('yacc1 > ')   # use raw_input() on Python 2
        # s = raw_input('yacc1 > ')
        parser.parse(s)
    except EOFError:
        break
