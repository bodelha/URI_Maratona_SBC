out = []

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
        d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if  d > r1 - r2:
            out.append("MORTO")
        else:
            out.append("RICO")

    except:
        break

print (*out, sep='\n')