def mediana(lista):
    
    lista.sort()
    
    n = len(lista)
    
    if n % 2 != 0:
        
        return lista[n // 2]
    else:
        
        meio1 = lista[n // 2 - 1]
        meio2 = lista[n // 2]
        return (meio1 + meio2) / 2


print(mediana([3, 1, 2]))        


