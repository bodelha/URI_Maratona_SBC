out = []

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
        if  ((x2 - x1)**2 + (y2 - y1)**2)**0.5 > r1 - r2:
            out.append("MORTO")
        else:
            out.append("RICO")

    except EOFError:
        break

print (*out, sep='\n')