out = []

for _ in range(int(input())):

    mapa = []
    limite, linhas = map(int, input().split())

    for n in range(linhas):

       mapa.append(input())
       if "F" in mapa[-1]:
           fred = (n, mapa[-1].index("F"))
       if "J" in mapa[-1]:
           jos = (n, mapa[-1].index("J"))

    distancia = 10 * ((fred[0] - jos[0])**2 + (fred[1] - jos[1])**2)**0.5
    maximo = limite/(0.99**int(distancia))
    out.append(int(maximo))

    
print (*out, sep=' dBs\n', end=" dBs\n")