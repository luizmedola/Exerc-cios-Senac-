def somatorio_lista_recursivo(lista, indice=0):
    
    if indice >= len(lista):
        return 0
    
    else:
        return lista[indice] + somatorio_lista_recursivo(lista, indice + 1)

print(somatorio_lista_recursivo([1, 2, 3, 4]))  

