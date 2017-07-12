#coding:utf-8

#按行和列的思维分析小票
#统一给出结论
# import re

# parttern="(\w+)\s+(\d+)\s+(\d)+\s+(\d+\.\d{2})"

# file = open("xiaopiao1.txt")
# content = file.read()
# # print(content)
# result = content.split('\n')
# for line in result:
#     m = re.match(parttern,line)
#     if m is not None:
#         print(m.groups()) #m.group(1) m.group(2) m.group(3) m.group(4)

import sys
#获取当前模块对像，用于反射
thismodule = sys.modules[__name__]

templateContent = open("xiaopiao1.pattern").read()
exampleContent = open("xiaopiao1.txt").read()

templateLines = templateContent.split('\n')
exampleLines = exampleContent.split('\n')

def hello_merchantName(name):
    print("hello: %s"%name)

def hello_orderTime(name):
    print("hello: %s"%name)
    

def parseTemplateLine(templateLine):
    name,line,parttern = templateLine.split(',')
    #用反射获取方法并执行
    if(name == "merchantName" or name == "orderTime"):
        func=getattr(thismodule,"hello_"+name)
        func(name)

for templateLine in templateLines:
    if(len(templateLine.strip()) == 0 or templateLine.find('#') == 0):
        continue
    else:
        parseTemplateLine(templateLine)


