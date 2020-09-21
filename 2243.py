##melhor no Python 3.4 que no 3.8

colunas = int(input())

muro = list(map(int, input().split()))

alturas = []

base = 0

for i in range (colunas):
    base += 1
    if muro [i] < base:
        base = muro[i]
    alturas.append(base)

base = 0

for i in range (1, colunas):
    base += 1
    if alturas [-i] < base:
        base = alturas [-i]
    alturas [-i] = base

print (max(alturas))