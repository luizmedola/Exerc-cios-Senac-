def ordena_lista(lista):
    n = len(lista)
    
    
    for i in range(n):
       
        menor_jr = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_jr]:
                menor_jr = j
        
        
        lista[i], lista[menor_jr] = lista[menor_jr], lista[i]
    
    return lista


print(ordena_lista([5, 15, 10, 6, 9]))        
