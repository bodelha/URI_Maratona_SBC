out = []
while True:
    try:
        a, b = map(int, input().split())
        a, b = int(bin(a).replace("0b", "")), int(bin(b).replace("0b", ""))
        out.append (int ("0b"+(str(a+b)).replace("2", "0"), 2))
        
    except EOFError:
        break
print(*out, sep='\n')