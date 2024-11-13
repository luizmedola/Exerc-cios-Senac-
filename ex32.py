def raiz_quadrada(n, max_iter=1000):
    if n < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    
    x = n / 2.0  
    
    for _ in range(max_iter):
        raiz = 0.5 * (x + n / x) 
        
        if x == raiz:
            break
        
        x = raiz
    
    return raiz

print(raiz_quadrada(9))    
print(raiz_quadrada(16))   
print(raiz_quadrada(2))    
