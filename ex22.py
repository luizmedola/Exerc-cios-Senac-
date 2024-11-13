def maior_elemento(lista):
   
    if not lista:
        return None 
    
    maior = lista[0]
    
    for numero in lista[1:]:  
        if numero > maior:
            maior = numero  
    
    return maior

lista = [10, 20, 30, 40, 50]
print(maior_elemento(lista))  
