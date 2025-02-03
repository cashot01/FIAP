# CAUAN ARANEGA S PASSOS RM555466
# Lucas Fialho - RM557884

import os
os.system("cls")

contatos = []
contato = {
    'cpf': '',
    'nome': '',
    'idade': ''
}

contatos.append(contato.copy())

while True:
    cpf = input("CPF: ")
    if cpf != "":
        for i in contatos:
            if contato.get(cpf):
                for k, v in contato:
                    print(f"{k} : {v}")

            else:
                contato = {}
                contato['cpf'] = cpf
                contato['nome'] = input("Nome: ")
                contato['idade'] = input("Idade: ")
                print("Cadastrado com sucesso!")        
                

    else:
        print("Programa finalizado")
        break