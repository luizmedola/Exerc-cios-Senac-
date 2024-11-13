def aproxima_pi(n):

    soma = 0.0
    
    for k in range(n):
       
        soma += (-1) ** k / (2 * k + 1)
    
    pi_aproximado = 4 * soma
    return pi_aproximado

print(aproxima_pi(1))   
