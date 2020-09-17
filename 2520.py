out = []
while True:
    try:
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid += list(map(int,input().split()))
        me = grid.index(1)
        it = grid.index(2)
        out.append(abs(me//m - it//m) + abs(me%m - it%m))
    except EOFError:
        break
print (*out, sep='\n')