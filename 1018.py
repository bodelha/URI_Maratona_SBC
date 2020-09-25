#Python 3.4
notas = [100, 50, 20, 10, 5, 2]
n = int(input())
out = [n]

for nota in notas:
    out.append(str(n//nota) + ' nota(s) de R$ ' + str(nota) + ',00')
    n = n % nota
out.append(str(n) + ' nota(s) de R$ 1,00')

print (*out, sep='\n')