def produto(a, b):
    
    if b == 0:
        return 0
    
    else:
        return a + produto(a, b - 1)

print(produto(3, 4))  

