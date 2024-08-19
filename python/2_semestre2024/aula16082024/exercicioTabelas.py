import os
os.system("cls")
"""
criar dicionario com 5 chaves, 1ª chave unica(cpf)
menu:
0 - sair
1 consultar
2 listar registros
3 cadastrar
4 editar
5 excluir

"""

def exibe_menu() -> None:
    print(""" 
    0 - sair
    1 - consultar
    2 - listar registros
    3 - cadastrar
    4 - editar
    5 - excluir
 """)
    
def voltar_menu(msg: str) -> None:
    msg = input(msg)
    os.system("cls")

"""
retorna o numero do indice se encontrado, caso contrario retorna -1
t: Tabela -> list

"""
def busca_cpf(t: list, cpf: int) -> int:
    for i in range(0, len(t), 1):
        if t[i]['cpf'] == cpf:
            return i
    return -1


def consultar():
    os.system("cls")
    print("consulta\n")
    cpf = input("cpf: ")

    if resgistro.get(cpf):
        nome = resgistro[nome]
        print(f"CPF existe ")
    else:
        print(f"O CPF {cpf} não existe")

    voltar_menu(msg_continuar)



def listar_registros(t: list) -> None:
    os.system("cls")
    for i in range(0, len(tabela), 1):
        print(f"Registro: {i+1}")
        print(f"CPF..................: {t[i]['cpf']}")
        print(f"Nome.................: {t[i]['nome']}")
        print(f"Idade................: {t[i]['idade']}")
        print(f"Cidade...............: {t[i]['cidade']}")
        print(f"Faculdade............: {t[i]['faculdade']} \n")
    voltar_menu(msg_continuar)

def editar(t: list, i: int, id: int) -> None:
    exibe_funcionario(t, i)
    t[retorno]['cpf'] = id

def cadastrar() -> None:
    os.system("cls")
    resgistro['cpf'] = input("CPF: ")
    resgistro['nome'] = input("nome: ")
    resgistro['idade'] = input("idade: ")
    resgistro['cidade'] = input("cidade: ")
    resgistro['faculdade'] = input("faculdade: ")
    tabela.append(resgistro.copy())
    voltar_menu(msg_continuar)




#============================= Principal
msg_continuar = "\nPressione alguma tecla para continuar . . ."

tabela = list()
resgistro = {
    'cpf': 1,
    'nome': 'cauan',
    'idade' : 18 ,
    'cidade': 'osasco',
    'faculdade' : 'fiap'
}

tabela.append(resgistro.copy())

while True:
    

    exibe_menu()
    escolha = input("Escolha: ")
    match escolha:
        case "0":
            break
        case "1":
            consultar()
        case "2":
            listar_registros(tabela)
        case "3":
            cadastrar()
        case "4":
            editar()
        case "5":
            excluir()
        case _:
            input(msg_continuar)
            os.system("cls")
            exibe_menu()


