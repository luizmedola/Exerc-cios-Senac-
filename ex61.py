def bubblesort(lista):
    n = len(lista)
    
    
    for i in range(n):
        
        trocou = False
        
       
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        
        if not trocou:
            break

    return lista

print(bubblesort([5, 3, 8, 1, 2]))        
print(bubblesort([10, 2, 8, 3, 7, 1]))   

