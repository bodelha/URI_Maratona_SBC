#unfunctional

out = []
while True:
    l, c, r1, r2 = map (int, input().split())
    if (l, c, r1, r2) == (0, 0, 0, 0):
        break
    else:
        if l < c:
            l, c = c, l
        if r1 < r2:
            r1, r2 = r2, r1
        tg = (r1 - r2)/(r1 + r2)
        cos = (tg**2 + 1)**-0.5
        if c < 2*r1 or l < (2*r2 + r1)*cos + r1 or (l + c)/2 < (2*(r1**2 + r2**2) + r1*r2)/(r1 + r2):
            out.append("N") 
        else:
            out.append("S")
print (*out, sep='\n')