out = []
inst = 1
matrix = ''

def confere (string):
    for i in range(9):
        linha = string [i*9 : i*9 + 9]
        coluna = string [i::9]
        index = 27*(i//3) + 3*(i%3)
        quadrante = string[index: index + 3] + string[index + 9:index + 12] + string[index + 18:index + 21]
        for n in range (1, 9):
            if linha.count(str(n)) !=1 or coluna.count(str(n)) !=1 or quadrante.count(str(n)) !=1:
                return False
    return True

for _ in range (int(input())*9):
    matrix += input().replace(" ", "")
    if len(matrix) == 81:
        out.append("Instancia " + str(inst))
        out.append("SIM\n" if confere(matrix) else "NAO\n")
        matrix = ''
        inst += 1

print(*out, sep='\n')