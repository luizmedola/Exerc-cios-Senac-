def classifica_triangulo(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return "Valores inválidos para os lados de um triângulo."

    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo."

    
    if a == b == c:
        return "Triângulo Equilátero"
    elif a == b or b == c or a == c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"
