def fatorial (n):
    fator = 1
    while n != 1:
        fator *= n
        n -= 1
    return fator

print (fatorial (int(input())))