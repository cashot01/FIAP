import os
os.system("cls")
from collections import Counter


def menu():
    """Exibe o menu principal e lida com as opções escolhidas pelo usuário."""
    while True:
        print("Menu de Opções:")
        print("1. Adicionar um novo texto")
        print("2. Mostrar a palavra mais utilizada")
        print("3. Sair")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número de 1 a 3.")
            continue  # Retorna ao início do loop para tentar novamente

        if escolha == 1:
            adicionar_texto()
        elif escolha == 2:
            mostrar_palavra()
        elif escolha == 3:
            print("Saindo...")
            break  # Sai do loop e finaliza o programa
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1, 2 ou 3.")

def adicionar_texto():
    """Adiciona um novo texto à lista de textos armazenados."""
    while True:
        try:
            texto = input("Digite seu texto: ").strip()
            if not texto:
                raise ValueError("O texto não pode ser vazio. Por favor, insira um texto válido.")
            textos.append(texto)
        except ValueError as e:
            print(e)
            continue

        while True:
            cont = input("Deseja adicionar outro texto? (S/N): ").strip().lower()
            if cont == 'n':
                return  # Retorna ao menu principal
            elif cont == 's':
                break  # Sai do loop interno e permite adicionar outro texto
            else:
                print("Entrada inválida. Por favor, digite S ou N.")

def mostrar_palavra():
    """Mostra a palavra mais utilizada entre os textos armazenados."""
    if not textos:
        print("Nenhum texto disponível. Por favor, adicione um novo texto.")
        input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter
        return

    # Concatena todos os textos e processa as palavras
    todo_texto = ' '.join(textos)
    palavras = todo_texto.lower().replace(",", "").replace(".", "").split()
    
    contagem = Counter(palavras)
    if contagem:
        palavra_mais_usada, quantidade = contagem.most_common(1)[0]
        print(f"A palavra mais utilizada é '{palavra_mais_usada}' utilizada {quantidade} vezes.")
    else:
        print("Nenhuma palavra encontrada nos textos.")

    input("Pressione Enter para continuar...")  # Espera o usuário pressionar Enter

textos = []

# Programa Principal
menu()