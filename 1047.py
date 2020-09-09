ah, am, bh, bm = map(int, input().split())

dm = bm - am
dh = bh - ah
if dm <  0:
    dh -= 1
    dm += 60
if (dm == 0 and dh == 0) or dh < 0:
    dh += 24
print (f"O JOGO DUROU {dh} HORA(S) E {dm} MINUTO(S)")
