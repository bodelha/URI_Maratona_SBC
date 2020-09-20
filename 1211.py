out = []
while True:
    try:
        numeros = []
        count = 0

        for _ in range(int(input())):
            numeros.append(input())
        numeros.sort()

        for i in range (len(numeros[0])):
            coluna = [numeros[j][i] for j in range(len(numeros))]
            test = [coluna[m] == coluna [m+1] for m in range(len(coluna)-1)]
            count += sum(test)

        out.append(count)
    except EOFError:
        break
print(*out, sep='\n')