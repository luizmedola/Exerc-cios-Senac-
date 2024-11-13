def media_harmonica(lista):
    
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")
    
    soma_inversos = 0
    
    for num in lista:
        if num <= 0:
            raise ValueError("Todos os números na lista devem ser positivos.")
        soma_inversos += 1 / num
    
    n = len(lista)
    return n / soma_inversos

print(media_harmonica([1, 2, 4])) 


