def conta_vogasi(texto):
    texto = texto.lower()
    vogais = "aeiou"
    return{i: texto.count(i) for i in vogais if i in texto}
print(conta_vogasi("Luiz Otávio"))