def remove_duplicados(lista):
    resultado = []

    for item in lista:

        if item not in resultado:
            resultado.append(item)
    return resultado

lista = [1, 2, 3, 4, 1, 1, 5, 2]
print(remove_duplicados(lista))  
