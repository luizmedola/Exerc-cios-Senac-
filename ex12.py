def eh_palindromo(s):
   
    if (s == s[:: -1]):
        return "É um políndromo"
    else:
        return "Não é um políndromo"
    
s = str(input("Informe a palavra desejada: "))   
print(eh_palindromo(s))