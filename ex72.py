def merge_dicionarios(d1, d2):
    
    resultado = d1.copy()  

    
    for chave, valor in d2.items():
        if chave in resultado:
           
            resultado[chave] += valor
        else:
           
            resultado[chave] = valor

    return resultado

d1 = {'a': 5, 'b': 10}
d2 = {'a': 3, 'c': 7}
resultado = merge_dicionarios(d1, d2)
print(resultado)  