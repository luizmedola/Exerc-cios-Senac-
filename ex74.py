def ordena_por_valores(dic):
   
    resultado = {}

    for chave, valor in sorted(dic.items(), key=lambda x: x[1]):

        resultado[chave] = valor

    return resultado

dic = {'a': 1, 'b': 2, 'c': 3}

resultado = ordena_por_valores(dic)

print(resultado) 