def inverte_dicionario(dic):
    
    return {valor: chave for chave, valor in dic.items()}

dic = {'a': 1, 'b': 2, 'c': 3}

resultado = inverte_dicionario(dic)

print(resultado)  