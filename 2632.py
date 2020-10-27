out = []
radius = {
    "fire": (200, 20, 30, 50),
    "water": (300, 10, 25, 40),
    "earth": (400, 25, 55, 70),
    "air": (100, 18, 38, 60)
}
n = int(input())

for _ in range(n):
    w, h, x0, y0 = map(int, input().split())
    [magic, level, cx, cy] = input().split()
    level, cx, cy = int(level), int (cx), int (cy)
    points =[
        (x0, y0), (x0, y0 + h), (x0 + w, y0 + h), (x0 + w, y0)
    ]
    if cx >= points[0][0] and cx <= points [2][0]:
        points.append((cx, y0))
        points.append((cx, y0 + h))
    if cy >= points[0][1] and cy <= points[1][1]:
        points.append((x0, cy))
        points.append((x0 + w, cy))
    distances = []
    for point in points:
        distances.append(((point[0] - cx)**2+(point[1] - cy)**2)**0.5)
    if min(distances) <= radius[magic][level] or (
        points [0][0] <= cx and cx <= points [-1][0] and
        points [0][1]<= cy and cy <= points [1][1] 
    ):
        out.append(radius[magic][0])
    else:
        out.append (0)

print (*out, sep="\n")