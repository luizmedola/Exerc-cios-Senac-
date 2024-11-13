def calcular_soma(a, b):
     
    result = a + b
    return result

X = float(input("Informe o primeiro número: "))
Y = float(input("Informe o segundo número: "))
res = calcular_soma(X, Y)
print("Soma: " , res)