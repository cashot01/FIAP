import json
import os
os.system("cls")

'''
EXERCÍCIO:
Criar um dicionário aninhado com 3 chaves no dicionário original.
 
Crie o menu:
0. SAIR
1. Cadastrar novo Registro
2. Listar os registros
3. Editar um registro
 
'''

# dicionario aninhado
contatos = {
    'contato1':{
        'nome':'João',
        'telefone':'(11) 1234-5678',
        'email':'joao@gmail.com'
    },
    'contato2':{
        'nome':'Maria',
        'telefone':'(11) 9012-3456',
        'email':'maria@gmail.com'
    },
    'contato3':{
        'nome': 'Cauan',
        'telefone': '(11) 1111-1111',
        'email': 'cauan@gmail.com'
    },
}

# menu
def exibe_menu():
    print("Menu")
    print("0 - Sair")
    print("1 - Cadastrar novo registro")
    print("2 - Listar registros")
    print("3 - Editar registros")

def cadastrar_novo_registro():



# programa principal
while True:
    os.system("cls")
    exibe_menu()
    escolha = input("Escolha: ")
    match escolha:
        case "0":
            break
        case "1":
            cadastrar_novo_registro()
        case "2":
            listar_registros()
        case "3":
            editar_registro()