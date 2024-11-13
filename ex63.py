def calcula_juros_compostos(capital, taxa, tempo):
    
    montante = capital * (1 + taxa) ** tempo
    return montante

print(calcula_juros_compostos(1000, 0.05, 2))  
print(calcula_juros_compostos(1500, 0.03, 3)) 
