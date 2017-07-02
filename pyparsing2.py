import pyparsing as pp

key = pp.Word(pp.alphanums)('key')
equals = pp.Suppress('=')
value = pp.Word(pp.alphanums)('value')

kvexpression = key + equals + value

with open("pyparsing2.cfg") as config_in:
    config_data = config_in.read()

for match in kvexpression.scanString(config_data):
    result = match[0]
    print("{0} is {1}".format(result.key,result.value))
