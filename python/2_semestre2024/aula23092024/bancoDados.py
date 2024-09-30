import os
os.system("cls")
import oracledb
import pandas as pd

# conectando o banco de dados
try:
    # efetua a conexao com o usuário
    conn = oracledb.connect(user="RM555466", password = "071105", dsn='oracle.fiap.com.br:1521/ORCL')


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

# Enquanto o flag estiver apontando para conexao
margem = ' ' * 4
while conexao:
    # os.system("cls")
 
    # Apresenta o menu
    print("""
    CRUD - PETSHOP
    1 - Cadastrar Pet
    2 - Listar Pets
    3 - Alterar Pet
    4 - Excluir Pet
    5 - Excluir todos os Pets
    6 - SAIR
    """)
    escolha = int(input(margem + "Escolha -> "))
    os.system("cls")
    match escolha:
        case 1:
            try:
                print("------ CADASTRAR PET ------")
                # Recebe os valores para o cadastro
                tipo = input(margem + "Tipo.....: ")
                nome = input(margem + "Nome.....: ")
                idade = int(input(margem + "Idade....: "))
                cadastro = f"""INSERT INTO petshop(tipo_pet, nome_pet,idade) VALUES ('{tipo}','{nome}','{idade}')"""
                # Executa a gravação do registro na tabela
                inst_cadastro.execute(cadastro)
                conn.commit()
            except ValueError:
                print(margem + "Digite um numero na idade")
            except:
                print(margem + "Erro em alguma coisa")
            else:
                print(margem + "DADOS GRAVADOS COM SUCESSO!")
        case _:
            print(margem + "Opcao invalida!")
else:
    print("Obrigado por utilizar a nossa aplicação :)")