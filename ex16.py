def retira_espaço(texto):
    texto = texto.lower()
    return texto.replace(" ","")
texto1 = str(input("Informe a palavra deseijada: "))
print(retira_espaço(texto1))
