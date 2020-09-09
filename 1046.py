a, b = map(int, input().split())
tempo = b-a
if tempo <= 0:
    tempo += 24
print (f"O JOGO DUROU {tempo} HORA(S)")