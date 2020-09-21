matrix = []
out = []
inst = 1

def confere (lista):
    for i in range (9):
        quadrante = lista[3*(i//3)][3*(i%3):3*(i%3) + 3] + lista[3*(i//3)+1][3*(i%3):3*(i%3) + 3] + lista[3*(i//3)+2][3*(i%3):3*(i%3) + 3]
        for n in range (1, 9):
            if lista [i].count(n) != 1 or [lista[k][i] for k in range(9)].count(n) !=1 or quadrante.count(n) != 1:
                return False
    return True

for _ in range (int(input())*9):
    matrix.append (list(map(int, input().split())))
    if len(matrix) == 9:
        out.append("Instancia " + str(inst))
        out.append("SIM\n" if confere(matrix) else "NAO\n")
        matrix = []
        inst += 1

print(*out, sep='\n')