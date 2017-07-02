# coding:utf-8

#符号表
tokens = (
    'NAME', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
)

#符号 匹配规则
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_NUMBER(t):#只有数字规则，不认识字母单词
    r'\d+'
    t.value = int(t.value)
    return t

#空白1 忽略
t_ignore = " \t"

#空白2 换行记录行号
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#其它输入不认识，进行错误处理
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# 生成词法分析器
import ply.lex as lex
lex.lex()


##############################################################
#               语法部分
##############################################################
# 优先规则
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# 变量词典
names = {}

# 赋值 语句
def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]

# 表达式 语句 
def p_statement_expr(p):
    'statement : expression'
    print(p[1])

# 复合表达式(p[0]: p[1] p[2] p[3])
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


# 基本表达式 数字
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# 基本表达式 变量名
def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

# 语法错误处理
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# 生成语法分析器
import ply.yacc as yacc
yacc.yacc()

# 从标准输入进行语法分析
while True:
    try:
        s = input('calc1 > ')   # use raw_input() on Python 2
    except EOFError:
        break
    yacc.parse(s)
