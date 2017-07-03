# coding:utf-8

# 还有点小错误，必须加以改正
tokens = (
    "NOUN", "PRONOUN", "VERB"
)

t_NOUN = r"dog|man|woman"
t_PRONOUN = r"i|he|she|item"
t_VERB = r"like|help|fuck"

# 问题出现在下面这些函数上!!!!!!!
# def t_VERB(t):
#     r"like|help|fuck"
#     print(t.value + " is a verb")


# def t_NOUN(t):
#     r"dog|man|woman"
#     print(t.value + " is a noun")


# def t_PRONOUN(t):
#     r"i|he|she|item"
#     print(t.value + " is a pron")


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

import ply.lex as lex
lexer = lex.lex()


# 句法部分#####################3
def p_statement_expr(p):
    'statement : expression'
    print(p[1]+" is a valid sentence")


def p_expression_binop(p):
    'expression : expression VERB expression'
    p[0] = p[1] + p[2] + p[3]

# 基本表达式 名词


def p_expression_noun(p):
    'expression : NOUN'
    p[0] = p[1]

# 基本表达式 名词


def p_expression_pronoun(p):
    'expression : PRONOUN'
    p[0] = p[1]


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
