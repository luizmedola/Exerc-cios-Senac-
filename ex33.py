def area_circulo(raio):
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    
    pi = 3.14
    area = pi * raio ** 2  
    return area

print(area_circulo(8))    
print(area_circulo(12))   
print(area_circulo(9))    
