def apaga_vogais(s):
   
    resultado = ""
    
    for letra in s:
    
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' and letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
            resultado += letra  
    
    return resultado

texto = "Oi, Você está bem?"
print(apaga_vogais(texto)) 