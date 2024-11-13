def elementos_unicos(lista):
    unicos = []  
    for item in lista: 
        if lista.count(item) == 1:  
            unicos.append(item)  
            
    return unicos

lista = [1, 2, 2, 3, 4, 4, 5]
print(elementos_unicos(lista))  
