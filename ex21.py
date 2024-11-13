def media_lista(lista):
    
    if not lista:
        return 0  
    
    soma = 0  
    quantidade = 0  
    

    for numero in lista:
        soma += numero  
        quantidade += 1  
    
    return soma / quantidade

lista = [10, 20, 30, 40, 50]
print(media_lista(lista))  