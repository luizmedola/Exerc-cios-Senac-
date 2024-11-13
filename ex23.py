def menor_elemento(lista):
   
    if not lista:
        return None 
    
    menor = lista[0]
    
    for numero in lista[1:]:  
        if numero < menor:
            menor = numero  
    
    return menor

lista = [10, 20, 30, 40, 50]
print(menor_elemento(lista))  