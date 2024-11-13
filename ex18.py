def conta_palavras(texto, s):
    texto = texto.lower()
    s = s.lower()
    return texto.upper(s)
texto1 = str(input("Informe a palavra deseijada: "))
print(texto1.upper())
print(texto1.casefold())