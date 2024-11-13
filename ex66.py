def bin2dec(binario):
   
    if not isinstance(binario, str):
        raise ValueError("A entrada deve ser uma string.")
    
    
    decimal = 0
    comprimento = len(binario)
    
    
    for i in range(comprimento):
        
        if binario[i] not in '01':
            raise ValueError("Entrada inválida! A string deve conter apenas os caracteres '0' e '1'.")
        
       
        decimal += int(binario[i]) * (2 ** (comprimento - 1 - i))
    
    return decimal
