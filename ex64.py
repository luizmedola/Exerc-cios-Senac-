def gera_senha(tamanho):
    
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    digitos = "0123456789"
    simbolos = "!@#$%^&*()-_=+[{]}|;:,.<>?/`~"
    
    
    todos_caracteres = letras_maiusculas + letras_minusculas + digitos + simbolos
    
    
    def pseudo_random(seed):
     
        a = 1664525
        c = 1013904223
        m = 2**32
        return (a * seed + c) % m
    
   
    senha = []
    seed = 123456789  
    
    for _ in range(tamanho):
        seed = pseudo_random(seed)
        indice = seed % len(todos_caracteres)  
        senha.append(todos_caracteres[indice])
    
    
    return ''.join(senha)


print(gera_senha(8))  
print(gera_senha(12))  
