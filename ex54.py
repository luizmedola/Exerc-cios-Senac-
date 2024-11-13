def media_notas(dicionario):
    
    soma_notas = sum(dicionario.values())
    
    numero_alunos = len(dicionario)
    
    
    if numero_alunos > 0:
        return soma_notas / numero_alunos
    else:
        return 0


alunos_notas = {
    'Luiz': 6.3,
    'Otávio': 7.5,
    'Mendonça': 4.2,
    'Medola': 2.9
}

alunos_notas_vazio = {}

print(media_notas(alunos_notas))  
print(media_notas(alunos_notas_vazio)) 
