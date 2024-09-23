import os
import oracledb
import pandas as pd

# conectando banco dados
try:
    # efetua a conexão com usuario
    conn = oracledb.connect(user="RM555466", password="071105", dsn="oracle.fiap.com.br:1521/ORCL")

    # criar objetos para cada operação no banco dados
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()

except Exception as e:
    print("Erro:", e)
    conexao = False
else:
    conexao = True

# enquanto o flag estiver apontando para conexão
margem = ' ' * 4
while conexao:
    os.system("cls")
    # apresenta menu
    print("""
    CRUD - PETSHOP
    1 - Cadastrar Pet
    2 - Listar Pet
    3 - Alterar Pet
    4 - Excluir Pet
    5 - Excluir todos pets
    6 - SAIR
""")
    escolha = int(input(margem + "Escolha -> "))
    os.system("cls")
    match escolha:
        case 1:
            try:
                print("------ Cadastrar Pet ------ ")
                
                # recebe os valores para o cadastro
                tipo = input(margem + "Tipo......: ")
                nome = input(margem + "Nome......: ")
                idade = int(input(margem + "Idade......: "))
                cadastro = f"""INSERT INTO petshop(tipo_pet, nome_pet, idade) values ({tipo}, {nome}, {idade}) """

                # executa a gravação do registro na tabela
                inst_cadastro.execute(cadastro)
                conn.commit()
            
            except ValueError:
                print(margem + "Digite um numero na idade")
            except:
                print(margem + "Erro alguma coisa")
            else:
                print(margem + "Dados gravados com sucesso")
                
        case _:
            print(margem + "Opção invalida")


else:
    print("Obrigado por utilizar nossa aplicação :)")