l = []

while True:
    try:
        n = int(input())
        l.append(n)
    except EOFError:
        break
        

print(
    f"{len([x for x in l if x%2 ==0])} valor(es) par(es)",
    f"{len([x for x in l if x%2 !=0])} valor(es) impar(es)",
    f"{len([x for x in l if x > 0])} valor(es) positivo(s)",
    f"{len([x for x in l if x < 0])} valor(es) negativo(s)",
    sep="\n"
)