out = []
while True:
    try:
        a, b = map(int, input().split())
        soma = int(bin(a)[2:]) + int(bin(b)[2:])
        out.append (int ((str(soma)).replace("2", "0"), 2))
        
    except EOFError:
        break
print(*out, sep='\n')