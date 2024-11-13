def ocorrencias_palavras(texto):
    
    texto = texto.lower()
    
    pontuacao = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '"', "'"]
    for p in pontuacao:
        texto = texto.replace(p, '')
    
    palavras = texto.split()
    
    contagem = {}
    
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem

texto = "brasil, brasil, brasil!!!"
print(ocorrencias_palavras(texto))
