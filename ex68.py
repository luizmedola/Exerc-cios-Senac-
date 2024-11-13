def tamanho_arquivo(nome_arquivo):
    try:
       
        with open(nome_arquivo, 'rb') as arquivo:
           
            arquivo.seek(0, 2)
            
            return arquivo.tell()
    except FileNotFoundError:

        return f"Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    
    except Exception as e:
        
        return f"Erro: {str(e)}"

