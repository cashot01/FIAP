# Cauan Passos RM555466 | Lucas Fialho RM557884

import os
os.system("cls")

perguntas = {
    'Pergunta 1': 
    {   'pergunta': 'Quanto é 10 elevado ao cubo ?', 
        'respostas':
        {   'a': '300',
            'b': '1000', 
            'c': '30'} ,
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual a raiz quadrada 81?', 
        'respostas':
        {   'a': '9',
            'b': '6', 
            'c': '10'},
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Qual o resultado da equação 4x - 8 = 6 + 2x?', 
        'respostas':
        {   'a': '8',
            'b': '6', 
            'c': '7'},
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Qual o modulo de |-6| ? ', 
        'respostas':
        {   'a': '6',
            'b': '0', 
            'c': '1'},
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Qual o resultado de 87 elevado á 0 ?', 
        'respostas':
        {   'a': '87',
            'b': '1', 
            'c': '-87'},
        'resposta_certa': 'b',
    },
    }
    
def quiz():
    acertos = 0
    total_perguntas = len(perguntas)
    for pergunta in perguntas.values():
        os.system("cls")
        print(f"\n{pergunta['pergunta']}\n")
        for resposta, valor in pergunta['respostas'].items():
            print(f"{resposta}: {valor}")
        resposta_usuario = input("Alternativa:  ")
        if resposta_usuario == pergunta['resposta_certa']:
            print("Resposta correta!")
            acertos += 1
        else:
            print(f"Resposta incorreta.")
    porcentagem_acertos = (acertos / total_perguntas) * 100
    print(f"\nVocê acertou {acertos} de {total_perguntas} perguntas.")
    print(f"Sua porcentagem de acertos é de {porcentagem_acertos:.2f}%.")


quiz()