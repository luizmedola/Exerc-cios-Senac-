def troca_vogais(s, nova_letra):
    
    vogais = "aeiouAEIOU"
    
    resultado = []
    
    for letra in s:
        
        if letra in vogais:
            resultado.append(nova_letra)
        else:
            resultado.append(letra) 
    
    return ''.join(resultado)

texto = "Olá, Como você está?"
nova_letra = " "
print(troca_vogais(texto, nova_letra))  
