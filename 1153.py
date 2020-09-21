def fatorial (n):
    if n - 2 == 1:
        return n * (n-1)
    else:
        return n * fatorial (n-1)
        

print (fatorial (int(input())))