#coding:utf-8

#按行和列的思维分析小票
#统一给出结论

file = open("xiaopiao1.txt")
content = file.read()
print(content)
result = content.split('\n')
print(result[0])
