def dec2bin(n):
    
    if n == 0:
        return "0"
    
    binario = []
    
    
    while n > 0:
        resto = n % 2  
        binario.append(str(resto))  
        n = n // 2  
    
    
    binario.reverse()  
    
   
    return ''.join(binario)


print(dec2bin(99))  
print(dec2bin(89)) 
print(dec2bin(67))   
print(dec2bin(54))   
