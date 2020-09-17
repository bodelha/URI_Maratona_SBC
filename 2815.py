texto = input().split()

texto_limpo = [x[2:] if x[:2]== x[2:4] else x for x in texto]
str_out = " ".join(texto_limpo)
print (str_out)