def filtro_dicionario(dic, valor):
    
    return {chave: val for chave, val in dic.items() if val > valor}
dic = {'a': 5, 'b': 10, 'c': 3, 'd': 15}

valor = 5

resultado = filtro_dicionario(dic, valor)

print(resultado)  


