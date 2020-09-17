out = []
saida = {0:"vai ter duas!", 1:"vai ter copa!"}
while True:
    try:
        out.append(saida [input() == "0"])
    except EOFError:
        break

print (*out, sep='\n')