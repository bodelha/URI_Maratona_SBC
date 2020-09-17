out = []
while True:
    try:
        if input() == "0":
            out.append("vai ter copa!")
        else:
            out.append("vai ter duas!")
    except EOFError:
        break
print (*out, sep="\n")