ah, am, bh, bm = map(int, input().split())

tempo = (bm - am) + (bh - ah)*60
if tempo <= 0:
    tempo += 24*60
print (f"O JOGO DUROU {tempo//60} HORA(S) E {tempo%60} MINUTO(S)")