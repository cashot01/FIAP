import os
os.system("cls")

def lista_tabela(t: list) -> None:
    for i in range(0, len(tabela), 1):
        print(f"Registro: {i+1}")
        print(f"Nome........: {t[i]['nome']}")
        print(f"Idade........: {t[i]['idade']}\n")


tabela = list()
agenda = {
    'nome': 'Edson',
    'idade': 50,
}

tabela.append(agenda.copy())

agenda['nome'] = input("Nome: ")
agenda['idade'] = input("Idade: ")
tabela.append(agenda.copy())

agenda['nome'] = input("Nome: ")
agenda['idade'] = input("Idade: ")
tabela.append(agenda.copy())

# for i in range(0, len(tabela), 1):
#     print(f"Registro: {i+1}")
#     print(f"Nome........: {tabela[i]['nome']}")
#     print(f"Idade........: {tabela[i]['idade']}")
#     print()
# esse for foi jogado na função listar_tabela

lista_tabela(tabela)

