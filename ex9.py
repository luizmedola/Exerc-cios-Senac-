def fatorial(n):
    if n<0:
        raise ValueError
    elif n == 0 or n ==1:
        return 1
    else: 
        return n * fatorial(n-1)     
num = int(input("Informe o número: "))
print(fatorial(num))    
    
