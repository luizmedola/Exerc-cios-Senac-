def gera_fibonacci_lista(n):
   
    fibonacci = []
    
   
    if n > 0:
        fibonacci.append(0)
    if n > 1:
        fibonacci.append(1)
    
  
    for i in range(2, n):
        
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    return fibonacci

print(gera_fibonacci_lista(0))  
print(gera_fibonacci_lista(1)) 

