out = []
while True:
    try:
        a, b = map (lambda x: bin(int(x)), input().split())
        if len (a) < len (b):
            a, b = b, a
        resp = ''
        for i in range (len(b) - 1, 1, -1):
            soma = int(a[len(a) -len (b) + i]) + int(b[i])
            resp =  '1' + resp if soma == 1 else '0' + resp
        out.append(int ("0b" + a[2:2 + len(a)-len(b)] + resp, 2))
    except EOFError:
        break
print(*out, sep='\n')