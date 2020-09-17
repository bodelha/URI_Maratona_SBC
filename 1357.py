digitos = {
    1:"*. .. ..",
    2:"*. *. ..",
    3:"** .. ..",
    4:"** .* ..",
    5:"*. .* ..",
    6:"** *. ..",
    7:"** ** ..",
    8:"*. ** ..",
    9:".* *. ..",
    0:".* ** .."
    }

out = []

while True:

    if int(input()) == 0:
        break

    if input() == "S": #traduzir para braile
        texto = input()
        linha1, linha2, linha3 = "", "", ""
        for digito in texto:
            braile = digitos[int(digito)].split()
            linha1 += braile[0] + " "
            linha2 += braile[1] + " "
            linha3 += braile[2] + " "
        out.append (linha1[:-1])
        out.append (linha2[:-1])
        out.append (linha3[:-1])

    else: #traduzir do braile
        linha1 = input()
        linha2 = input()
        linha3 = input()
        texto = ""
        for i in range (0, len(linha1), 3):
            numero = linha1[i: i+2] + " " + linha2[i: i+2] + " " + linha3[i: i+2]
            texto += str(list(digitos.keys()) [list(digitos.values()).index(numero)])
        out.append(texto)


print(*out, sep="\n")