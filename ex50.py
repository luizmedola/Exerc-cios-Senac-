def torre_hanoi(n, origem, destino, auxiliar):
   
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
    else:
        
        torre_hanoi(n-1, origem, auxiliar, destino)
        
        print(f"Mover disco {n} de {origem} para {destino}")
        
        torre_hanoi(n-1, auxiliar, destino, origem)

n = 3  
torre_hanoi(n, 'A', 'C', 'B')
