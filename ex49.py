def mcd(a, b):
    
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

def mdc_lista(lista):
    
    if len(lista) == 1:
        return lista[0]
   
    else:
        return mcd(lista[0], mdc_lista(lista[1:]))

print(mdc_lista([48, 18, 96]))   

