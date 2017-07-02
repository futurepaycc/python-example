#coding:utf-8
import pyparsing as pp

def upper_case_it(tokens):
    return [t.upper() for t in tokens]

#前缀
prefix = 'A Fistful of' + pp.White()

#关键值
fist_contents = pp.Word(pp.alphas)
fist_contents.setParseAction(upper_case_it)

#合并
title_parser = pp.Combine(prefix + fist_contents)

for title in (
    "A Fistful of Dollars",
    "A Fistful of Spaghetti",
    "A Fistful of Doughnuts"
):
    print(title_parser.parseString(title)) # 不匹配为何要抛异常
