numero = input()

n = numero.count('5')
i = 0
cincos = []
for _ in range (n):
    j = numero[i:].index('5')
    cincos.append(j+ i)
    i += j + 1

for pos in cincos:
    if numero[pos -1] in '37'
