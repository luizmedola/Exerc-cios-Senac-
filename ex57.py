def substitui_espaco(texto, simbolo):
   
    return texto.replace(' ', simbolo)

print(substitui_espaco("Olá Mundo", "/"))    
print(substitui_espaco("Teste de espaços", "-"))  
print(substitui_espaco("Python é incrível", "_"))
