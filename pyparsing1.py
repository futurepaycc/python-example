import pyparsing as pyp

'''
grammar:
ssn ::= nums+ '-' nums+ '-' nums+
nums ::= '0'|'1'|'2' etc etc
'''
dash = '-'

ssn_parser = pyp.Combine(
    pyp.Word(pyp.nums, exact=3)
    + dash
    + pyp.Word(pyp.nums, exact=2)
    + dash
    + pyp.Word(pyp.nums, exact=4)
)

input_string = '''
    xxx 225-92-8416 yyy
    103-33-3929 zzz 028-91-0122
'''

for match, start, stop in ssn_parser.scanString(input_string):
    print(match, start, stop)
