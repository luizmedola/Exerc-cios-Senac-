def soma_diagonais(matriz):
    soma = 0
    n = len(matriz)  

    for i in range(n):
       
        soma += matriz[i][i]
        
        soma += matriz[i][n - 1 - i]
    
    if n % 2 == 1:
        soma -= matriz[n // 2][n // 2]
    
    return soma


matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [10, 11, 12, 13],
    [14, 15, 16, 17],
    [18, 19, 20, 21],
    [22, 23, 24, 25]
]

print(soma_diagonais(matriz1))  
print(soma_diagonais(matriz2))  
