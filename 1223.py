# unfunctional
out = []
while True:
    try:
        diametro = []
        n = int(input())
        l, h = map(int, input().split())
        xia, yia, xfa, yfa = 0, 0, 0, 0
        for k in range(n):
            yib, xfb, yfb = map(int, input().split())
            if k%2 == 0:
                xib = 0
                d = (yfa - yfb)*xfb/((yib - yfb)**2 + xfa**2)**0.5
                b = xfb
            else:
                xib = l
                d = (yfa - yfb)*(l - xfa)/((yib - yfb)**2 + (l - xfb)**2)**0.5
                b = l - xfa
            diametro.append(min(b,d))
            xia, yia, xfa, yfa = xib, yib, xfb, yfb
        out.append(min(diametro[1:]))
    except:
        break
print (*out, sep='\n')