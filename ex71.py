def conta_elementos(lista):
    
    contagem = {}

   
    for elemento in lista:
        
        if elemento in contagem:
            
            contagem[elemento] += 1
        else:
            
            contagem[elemento] = 1

    return contagem
