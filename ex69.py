def minimax(lista):
    if not lista:  
        return None, None 

    return min(lista), max(lista)

lista = [5, 2, 9, 1, 7]
menor, maior = minimax(lista)
print(f"Menor: {menor}, Maior: {maior}") 