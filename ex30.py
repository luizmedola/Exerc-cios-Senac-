def uniao_listas(lista1, lista2):
    uniao = []  
    for item in lista1: 
        
        if item not in uniao:  

            uniao.append(item)

    for item in lista2:  
        if item not in uniao: 

            uniao.append(item)

    return uniao


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
print(uniao_listas(lista1, lista2))  
