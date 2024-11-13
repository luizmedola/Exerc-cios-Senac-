def conta_ocorrencias(lista):
    
    contador = {}
    
    for item in lista:
        
        if item in contador:
            contador[item] += 1
            
        else:
            contador[item] = 1
    
    return contador

lista = [1, 2, 3, 4, 1, 1, 5, 2]
print(conta_ocorrencias(lista)) 
