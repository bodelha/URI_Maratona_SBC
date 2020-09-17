out = []
while True:
    try:
        numeros = []
        count = 0

        for _ in range(int(input())):
            numeros.append(input())
        numeros.sort()

        while len(numeros) >= 2:
            for i in range(len(numeros[1])):
                if numeros[1][i] == numeros[0][i]:
                    count += 1
                else:
                    break
            del numeros[0]
        out.append(count)
    except EOFError:
        break
print(*out, sep='\n')