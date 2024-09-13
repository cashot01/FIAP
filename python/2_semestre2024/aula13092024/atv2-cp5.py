# CAUAN ARANEGA S PASSOS RM555466
import os
os.system("cls")

contatos = []
contato = {
    'cpf': '',
    'nome': '',
    'idade': int
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
                novo_contato = {}
                novo_contato['cpf'] = cpf
                novo_contato['nome'] = input("Nome: ")
                novo_contato['idade'] = input("Idade: ")
                print("Cadastrado com sucesso!")
                
                

    else:
        print(f"""\n
        CPF: {novo_contato['cpf']}
        NOME: {novo_contato['nome']}
        IDADE: {novo_contato['idade']}
        """)
