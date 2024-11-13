def encontra_palavra(texto, palavra):
    n = len(texto)  
    m = len(palavra)  
    
    for i in range(n - m + 1):
        
        for j in range(m):
            if texto[i + j] != palavra[j]:  
                break  
        else:
            return i  

    return -1 

texto = "Luiz Otávio Medola"
palavra = "Lindo"
print(encontra_palavra(texto, palavra))  

palavra = "Luiz"
print(encontra_palavra(texto, palavra)) 
