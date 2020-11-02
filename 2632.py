out = []
radius = {
    "fire": (200, 20, 30, 50),
    "water": (300, 10, 25, 40),
    "earth": (400, 25, 55, 70),
    "air": (100, 18, 38, 60)
}

for n in range(int(input())):
    w, h, x0, y0 = map(int, input().split())
    xw, yh = x0 + w, y0 +h
    [magic, level, cx, cy] = input().split()
    level, cx, cy = int(level), int (cx), int (cy)
    points =[
        (x0, y0), (x0, yh), (xw, yh), (xw, y0)
    ]
    if x0 <= cx and cx <= xw:
        if y0 <= cy and cy <= yh:
            points = [(cx, cy)]
        else:
            points.append((cx, y0))
            points.append((cx, yh))
    elif y0 <= cy and cy <= yh:
        points.append((x0, cy))
        points.append((xw, cy))    
    for point in points:
        distance = ((point[0] - cx)**2+(point[1] - cy)**2)**0.5 
        if distance <= radius[magic][level]:
            out.append(radius[magic][0])
            break
    if len(out) != n + 1:
            out.append (0)

print (*out, sep="\n")