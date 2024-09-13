import os
os.system("cls")

contatos = []
contato = {
    'cpf': '',
    'nome': '',
    'idade': int
}

contatos.append(contato.copy())

cpf = input("CPF: ")
for i in contatos:
    if contato.get(cpf):
        for k, v in contato:
            print(f"{k} : {v}")

    else:
        novo_contato = {}
        novo_contato['cpf'] = cpf
        novo_contato['nome'] = input("Nome: ")
        novo_contato['idade'] = input("Idade: ")
        print("Cadastrado com sucesso!")
