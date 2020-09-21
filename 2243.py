colunas = int(input())

muro = list(map(int, input().split()))

alturas = []

base = 0

for i in range (colunas):
    base += 1
    if muro [i] < base:
        base = muro[i]
    alturas.append(min(base, muro[i]))

base = 0

for i in range (1, colunas + 1):
    base += 1
    if alturas [-i] < base:
        base = alturas [-i]
    alturas [-i] = base

print (max(alturas))