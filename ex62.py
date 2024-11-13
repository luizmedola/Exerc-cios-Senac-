def valida_senha(senha):
   
    if len(senha) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    
    for c in senha:
        if c.isupper(): 
            tem_maiuscula = True
        elif c.islower():  
            tem_minuscula = True
        elif c.isdigit(): 
            tem_numero = True
        elif c in "!@#$%^&*(),.?\":{}|<>": 
            tem_especial = True
    
   
    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return True
    else:
        return False


print(valida_senha("Abc12345!"))  
print(valida_senha("abc12345"))   
print(valida_senha("ABCD1234"))   
print(valida_senha("abC123!"))   
