import re
from tabulate import tabulate  # pip3 install tabulate

file = open("C:\Python\Compiler Disign Lab\input.txt", encoding="utf-8")
s = file.read().split()
# print(s)

c_keywords = ['printf','abort', 'abs', 'ceil', 'exit', 'exp', 'floor', 'scanf', 'sqrt', 'strcasecmp',
              'strcmp', 'strcpy', 'auto', 'double', 'int',	'struct', 'break', 'else', 'long',	'switch',
              'case', 'enum',	'register', 'typedef', 'char', 'extern', 'return', 'union', 'continue',
              'for', 'signed',	'void', 'do', 'static', 'while', 'default', 'goto', 'sizeof',
              'volatile', 'const', 'float', 'short', 'unsigned',]


c_operators = ['+', '-', '*', '/', '%', '++', '--', '+=', '-=', '*=', '/=', '%=', '=', '==', '>',
               '<', '>=', '<=', '!=', '&&', '!', '<<', '<<', '^', '~', '&', '|']

bracket = ['(', ')', '{', '}', '[', ']']

idd = 0
iff = 0
op = 0
num = 0
semicolon = 0
other = 0
literal = 0
table = []

for i in range(0,len(s)):
    xx = ""
    for j in range(0, len(s[i])):
        if s[i][j] == '“':
            for k in range(j+1, len(s[i])):
                if s[i][k] == '”':
                    literal = literal + 1
                    x = "literal_"
                    y = x + str(literal)
                    table.append([xx, y, "literal", "-", i + 1])
                    break
                else:
                    xx = xx + s[i][k]

    xx = ''
    for j in range(0, len(s[i])):
        if s[i][j].isdigit():
            xx = xx + s[i][j]
    if xx != '':
        num = num + 1
        x = "num_"
        y = x + str(num)
        table.append([str(xx), y, "number", str(xx), i + 1])

    s[i] = s[i].replace(xx, "")

    for j in range(0, len(c_keywords)):
        search_string = s[i]
        pattern = c_keywords[j]
        match_kw = re.match(pattern, search_string)
        if match_kw:
            idd = idd + 1
            x = "id"
            y = x + str(idd)
            table.append([pattern, y, "id", "-", i + 1])
            s[i] = s[i].replace(pattern, "")

    for k in range(0, len(c_operators)):
        search_string = s[i]
        p = c_operators[k]
        pattern = f'\{c_operators[k]}'
        match_bf = re.search(pattern, search_string)
        if match_bf:
            op = op + 1
            x = "Op_"
            y = x + str(op)
            table.append([c_operators[k], y, c_operators[k], "-", i + 1])
            s[i] = s[i].replace(p, "")

    for k in range(0, len(bracket)):
        search_string = s[i]
        p = bracket[k]
        pattern = f'\{bracket[k]}'
        match_bf = re.search(pattern, search_string)
        if match_bf:
            other = other + 1
            x = "other_"
            y = x + str(other)
            table.append([bracket[k], y, "other", "-", i + 1])
            s[i] = s[i].replace(p, "")

    if re.search(';', s[i]):
        semicolon = semicolon + 1
        x = "Semicolon_"
        y = x + str(semicolon)
        table.append([";", y, "Semicolon", "-", i + 1])
        s[i] = s[i].replace(";", "")

    if re.match('if', s[i]):
        iff = iff + 1
        x = "if_"
        y = x+str(iff)
        table.append(["if",y,"if","-",i+1])
        s[i] = s[i].replace("if", "")

    if s[i].isidentifier():
        idd = idd + 1
        x = "id"
        y = x + str(idd)
        table.append([s[i], y, "id", "-", i + 1])

print(tabulate(table, headers=["Symble", "Symble_Id", "Token_Type","Value","Line Number"]))