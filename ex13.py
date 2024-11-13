def conta_palavras(texto, s):
    texto = texto.lower()
    s = s.lower()
    return texto.count(s)
print(conta_palavras("Luiz Otávio" , "L"))