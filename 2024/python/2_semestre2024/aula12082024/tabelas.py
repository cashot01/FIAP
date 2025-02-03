import os
os.system("cls")

# preenchendo um registro
def preenche_registro(t: list, reg: dict) -> None:
    print("preenchendo o registro")
    reg['nome'] = input("Nome: ")
    reg['idade'] = int(input("Idade: "))
    t.append(reg.copy())
    # necessário ter o copy, se não sempre vai aparecer o ultimo dado  

# tabela de memoria é uma lista de dicionarios

tabela = list()
contato = {
    'nome': '',
    'idade': 0,
}

preenche_registro(tabela, contato)
preenche_registro(tabela, contato)
print(tabela)
