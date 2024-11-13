def eh_armstrong(n):
    
    str_n = str(n)
    
    num_digitos = len(str_n)
    
    soma = sum(int(digit) ** num_digitos for digit in str_n)
    
    return soma == n

print(eh_armstrong(153)) 

