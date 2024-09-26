# definição subalgoritimos
def cadastrar_registro(id: str, registros: dict) -> None:
    nome = input("Nome: ")
    idade = input("Idade: ")
    registros[id] = {
        'cpf': id, 
        'nome': nome, 
        'idade': idade
    }

    print("Cadastrado com sucesso")

def exibe_registro(registro: str) -> None:
    print(f"\nCPF: {registro['cpf']}")
    print(f"Nome: {registro['nome']}")
    print(f"Idade: {registro['idade']}\n")


def editar_registro(id: str, registros: dict) -> None:
    # apresentando registro existente
    exibe_registro(registros[id])

    nome = input("Nome: ")
    idade = input("Idade: ")
    # editando registro encontrado
    if nome != "":
        registros[id]['nome'] = nome
    if idade != "":
        registros[id]['idade'] = idade
    print("Editado com sucesso")




# programa principal
import os
os.system("cls")

pessoas = {}

continua = True
while continua:
    cpf = input("CPF: ")
    if cpf == "":
        continua = False
    elif cpf in pessoas:
        editar_registro(cpf, pessoas)
    else:
        cadastrar_registro(cpf, pessoas)
else:
    print("Programa finalizado")
        