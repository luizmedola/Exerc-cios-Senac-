def eh_perfeito(n):
    if n <= 1:
        return False  
    
    soma_divisores = 0
    
    for i in range(1, n):
        if n % i == 0: 
            soma_divisores += i
    
    return soma_divisores == n

print(eh_perfeito(6))    
  

