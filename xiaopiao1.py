#coding:utf-8

# TODO:正则表达式抽取处理,主内容区有多个分组
import sys
#获取当前模块对像，用于反射
thismodule = sys.modules[__name__]

templateContent = open("xiaopiao1.pattern").read()
exampleContent = open("xiaopiao1.txt").read()

templateLines = templateContent.split('\n')
exampleLines = exampleContent.split('\n')

def hello_merchantName(name,lineNo,parttern):
    print("hello: %s %s %s"%(name,lineNo,parttern))

def hello_orderTime(name,lineNo,parttern):
    print("hello: %s %s %s"%(name,lineNo,parttern))
    

def parseTemplateLine(templateLine):
    name,lineNo,parttern = templateLine.split(',')
    #用反射获取方法并执行
    if(name == "merchantName" or name == "orderTime"):
        func=getattr(thismodule,"hello_"+name)
        func(name,lineNo,parttern)

for templateLine in templateLines:
    if(len(templateLine.strip()) == 0 or templateLine.find('#') == 0):
        continue
    else:
        parseTemplateLine(templateLine)