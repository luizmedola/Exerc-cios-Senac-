def conta_ocorrencias_caracteres(s):
  
    ocorrencias = {}
    
    for i in range(len(s)):
       
        letra = s[i]
        
        if letra in ocorrencias:
            ocorrencias[letra] += 1
        
        else:
            ocorrencias[letra] = 1
    
    return ocorrencias


string = "banana"
print(conta_ocorrencias_caracteres(string))  

string = "hello world"
print(conta_ocorrencias_caracteres(string))  

