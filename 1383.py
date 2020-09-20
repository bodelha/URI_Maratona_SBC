matrix = []
out = []
inst = 1

def confere (lista):
    for n in range (1, 9):
        for i in range (9):
            linha = lista [i]
            coluna = [lista[k][i] for k in range(9)]
            quadrante = lista[3*(i//3)][3*(i%3):3*(i%3) + 3] + lista[3*(i//3)+1][3*(i%3):3*(i%3) + 3] + lista[3*(i//3)+2][3*(i%3):3*(i%3) + 3]
            if linha.count(n) != 1 or coluna.count(n) !=1 or quadrante.count(n) != 1:
                return False
    return True

for _ in range (int(input())*9):
    matrix.append (list(map(int, input().split())))
    if len(matrix) == 9:
        out.append("Instancia " + str(inst))
        out.append("SIM" if confere(matrix) else "NAO")
        out.append("")
        matrix = []
        inst += 1

print(*out, sep='\n')

