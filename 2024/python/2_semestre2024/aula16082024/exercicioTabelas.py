func = {
    'cpf' : 123,
    'nome' : 'Edson de Oliveira',
    'salario': 23456.78,
}
tabela = []

tabela.append(func.copy())

def exibe_menu():
    print("""
    0 - SAIR
    1 - Cadastrar Funcionário
    2 - Consultar Funcionário
    3 - Editar Funcionário
    4 - Excluir Funcionário
    5 - Listar Funcionários
    """)

# Retorna o numero do índice se encontrado, caso contrário retorna -1
# t: Tabela -> list
# cpf: id de busca -> int
# Retorno: int [índice encontrado]
def busca_cpf(t: list, cpf: int) -> int:
    for i in range(0,len(t),1):
        if t[i]['cpf'] == cpf:
            return i
    return -1

def exibe_funcionario(t, indice) -> None:
    print(f"\nCPF......: {t[indice]['cpf']}")
    print(f"Nome.....: {t[indice]['nome']}")
    print(f"Salário..: {t[indice]['salario']}")

def listar_funcionarios(t: list) -> None:
    mensagem_titulo("CPF        NOME                SALARIO")
    for i in range(len(t)):
        print(f"{t[i]['cpf']} | {t[i]['nome']} | {t[i]['salario']}")

def edita_funcionario(t: list, i: int, id: int) -> None:
    exibe_funcionario(t, i)
    t[retorno]['cpf'] = id
    t[retorno]['nome'] = input("Nome....:")
    t[retorno]['salario'] = float(input('Salário.:'))
    mensagem("!" ,"Editado com sucesso!")

def cadastra_funcionario(t: list, d: dict, id: int) -> None:
    d['cpf'] = id
    d['nome'] = input("Nome....: ")
    d['salario'] = float(input('Salário.: '))
    t.append(d.copy())
    mensagem("!" ,"Cadastrado com sucesso!")


def exclui_funcionario(l: list, id: int) -> None:
    resp = input("Confirma a exclusão do funcionário?")
    if resp.upper() == 'S':
        l.pop(id)
        mensagem("-" ,"Funcionário excluído!")
    else:
        print("Exclusão cancelada . . .")

# Exibe uma mensagem formatada.
# Parâmetro 1: carac -> str: O caractere que formará a mensagem
# Parâmetro 2: msg -> str: A mensagem que será exibida
# Retorno: None
def mensagem(carac:str, msg: str) -> None:
    tamanho = len(msg)
    print(f"\n{carac * tamanho}")
    print(msg)
    print(f"{carac * tamanho}")

# Formata a mensagem de título.
# Parâmetro: msg -> str: A mensagem que será exibida no título
# Retorno: None
def mensagem_titulo(msg: str) -> None:
    tamanho = len(msg)
    print(f"\n{msg}\n{tamanho * '='}")


import os
while True:
    os.system("clear")
    mensagem_titulo("M E N U")
    exibe_menu()
    escolha = input("Escolha: ")
    os.system("clear")
    match escolha:
        case '0':
            break
        case '1':
            mensagem_titulo("CADASTRANDO FUNCIONÁRIO:")
            cpf = int(input("\nCPF.....: "))
            retorno = busca_cpf(tabela, cpf)
            if retorno == -1:
                cadastra_funcionario(tabela, func, cpf)
            else:
                mensagem("-" ,"Funcionário já existe!")
                
        case '2':
            mensagem_titulo("CONSULTANDO FUNCIONARIO")
            cpf = int(input("\nCPF.....: "))
            retorno = busca_cpf(tabela, cpf)
            if  retorno != -1:
                exibe_funcionario(tabela, retorno)
            else:
                mensagem("-" ,"Funcionário inexistente!")
        case '3':
            mensagem_titulo("EDITANDO FUNCIONARIO")
            cpf = int(input("\nCPF.....: "))
            retorno = busca_cpf(tabela, cpf)
            if  retorno != -1:
                edita_funcionario(tabela, retorno, cpf)
            else:
                mensagem("-" ,"Funcionário inexistente!")
        case '4':
            mensagem_titulo("EXCLUINDO FUNCIONARIO")
            cpf = int(input("CPF.....: "))
            retorno = busca_cpf(tabela, cpf)
            if  retorno != -1:
                exibe_funcionario(tabela, retorno)
                exclui_funcionario(tabela, retorno)
                
            else:
                mensagem("-" ,"Funcionário inexistente!")
        case '5':
            listar_funcionarios(tabela)
        case _:
            mensagem("-" ,"Opção inexistente!")
            
    input("\nPressione alguma tecla para continuar...")

