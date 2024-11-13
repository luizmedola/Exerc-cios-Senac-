def potencia(base, expoente):
    if expoente == 0:
        return 1  
    
    resultado = 1
    
    if expoente > 0:

        for _ in range(expoente):  

            resultado *= base
    else:
        for _ in range(-expoente):  

            resultado *= base

        resultado = 1 / resultado  

    return resultado

print(potencia(2, 3))    
print(potencia(5, -2)) 
print(potencia(3, 0))  
print(potencia(2, -3))   
