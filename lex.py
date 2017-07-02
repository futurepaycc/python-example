# coding:utf-8
import ply.lex as lex

tokens = (
    "VERB",
    "PRON"
)


def t_VERB(t):
    r"go|do|fuck"
    print(t.value, " is a verb")


def t_PRON(t):
    r"i|he|she|item"
    print(t.value, " is a pron")


def t_error(t):
    print("illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

lexer = lex.lex()

while True:
    lex.runmain()
