def conta_maiusculas(texto):
    
    contador = 0
    
    
    for i in range(len(texto)):
        if texto[i].isupper():  
            contador += 1
    
    return contador

print(conta_maiusculas("Olá!"))  
print(conta_maiusculas("JavaScript!"))  
print(conta_maiusculas("abcde"))         
print(conta_maiusculas("A B C D E"))    
