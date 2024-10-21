# Cauan Passos RM555466 | Lucas Fialho RM
import os
import pandas as pd
import oracledb
import datetime as dt

def conectar_bd() -> oracledb.Connection:
    try:
        conn = oracledb.connect(user="RM555466", password="071105", dsn='oracle.fiap.com.br:1521/ORCL')
        return conn
    except Exception as e:
        print(f"Erro na conexão ao BD: {e}")
        return None

def gerarNomeArquivo() -> str:
    ano = str(dt.datetime.now().year)
    mes = str(dt.datetime.now().month)
    dia = str(dt.datetime.now().day)
    hora = str(dt.datetime.now().hour)
    min = str(dt.datetime.now().minute)
    seg = str(dt.datetime.now().second)
    nomeArquivo = f"planilha{ano}{mes}{dia}{hora}{min}{seg}.xlsx"
    return nomeArquivo


def criar_tabela(cu: oracledb.Cursor) -> None:
    cu.execute('''CREATE TABLE CARRO_PYTHON (
                    PLACA VARCHAR2(10),
                    MARCA VARCHAR2(50),
                    MODELO VARCHAR2(50),
                    PROPRIETARIO VARCHAR2(100),
                    ANO INT,
                    SALARIO FLOAT,
                    DATA_NASCIMENTO DATE,
                    ATIVO CHAR(1)
                )''')
    print("Tabela criada com sucesso!")

def cadastrar(cu: oracledb.Cursor, co: oracledb.Connection) -> None:
    try:
        print("----- CADASTRAR CARRO -----")
        placa = input("Digite a placa....: ")
        marca = input("Digite a marca....: ").strip()
        modelo = input("Digite o modelo....: ").strip()
        dono = input("Digite o nome do dono....: ").strip()
        anoCarro = int(input("Digite o ano.......: "))
        salario = float(input("Digite o salário.......: "))
        data_nasc = input("Digite a data de nascimento (YYYY-MM-DD).......: ")
        cu.execute(f"INSERT INTO CARRO_PYTHON (PLACA, MARCA, MODELO, PROPRIETARIO, ANO, SALARIO, DATA_NASCIMENTO, ATIVO) VALUES ('{placa}', '{marca}', '{modelo}', '{dono}', {anoCarro}, {salario}, TO_DATE('{data_nasc}', 'YYYY-MM-DD'), '1')")
        co.commit()
        print("\n##### Dados GRAVADOS #####\n")
    except ValueError:
        print("Digite os valores corretos!")
    except Exception as e:
        print("Erro: ", e)
    finally:
        input("Digite para continuar: ")


def filtrar_registros(cu: oracledb.Cursor) -> None:
    print("----- FILTRAR REGISTROS -----")
    print("1 – Nome (like)")
    print("2 – Salário")
    print("3 – Data de Nascimento")
    opcao = input("Escolha uma opção de filtro: ")

    if opcao == "1":
        nome = input("Digite parte do nome: ")
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE PROPRIETARIO LIKE '%{nome}%'")
    elif opcao == "2":
        filtro_salario(cu)
    elif opcao == "3":
        filtro_data_nasc(cu)
    else:
        print("Opção inválida!")

def filtro_salario(cu: oracledb.Cursor) -> None:
    print("1 – Igual")
    print("2 – Maior")
    print("3 – Menor")
    print("4 – Entre")
    opcao = input("Escolha uma opção de filtro: ")

    if opcao == "1":
        salario = float(input("Digite o salário: "))
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE SALARIO = {salario}")
    elif opcao == "2":
        salario = float(input("Digite o salário: "))
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE SALARIO > {salario}")
    elif opcao == "3":
        salario = float(input("Digite o salário: "))
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE SALARIO < {salario}")
    elif opcao == "4":
        salario_inicial = float(input("Salário inicial: "))
        salario_final = float(input("Salário final: "))
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE SALARIO BETWEEN {salario_inicial} AND {salario_final}")
    else:
        print("Opção inválida!")

def filtro_data_nasc(cu: oracledb.Cursor) -> None:
    print("1 – Igual")
    print("2 – Maior que")
    print("3 – Menor que")
    print("4 – Entre")
    opcao = input("Escolha uma opção de filtro: ")

    if opcao == "1":
        data = input("Digite a data de nascimento (YYYY-MM-DD): ")
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE DATA_NASCIMENTO = TO_DATE('{data}', 'YYYY-MM-DD')")
    elif opcao == "2":
        data = input("Digite a data de nascimento (YYYY-MM-DD): ")
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE DATA_NASCIMENTO > TO_DATE('{data}', 'YYYY-MM-DD')")
    elif opcao == "3":
        data = input("Digite a data de nascimento (YYYY-MM-DD): ")
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE DATA_NASCIMENTO < TO_DATE('{data}', 'YYYY-MM-DD')")
    elif opcao == "4":
        data_inicial = input("Data inicial (YYYY-MM-DD): ")
        data_final = input("Data final (YYYY-MM-DD): ")
        cu.execute(f"SELECT * FROM CARRO_PYTHON WHERE DATA_NASCIMENTO BETWEEN TO_DATE('{data_inicial}', 'YYYY-MM-DD') AND TO_DATE('{data_final}', 'YYYY-MM-DD')")
    else:
        print("Opção inválida!")

# Função para exportar dados filtrados ou todos os registros
def exportar_dados(cu: oracledb.Cursor) -> None:
    print("----- EXPORTAR DADOS -----")
    escolha = input("O que deseja exportar? (1) Todos os registros (2) Registros filtrados: ")
    
    if escolha == "1":
        cu.execute("SELECT * FROM CARRO_PYTHON")
    elif escolha == "2":
        filtrar_registros(cu)
    
    registros = cu.fetchall()
    df = pd.DataFrame(registros, columns=[desc[0] for desc in cu.description])
    nome_arquivo = gerarNomeArquivo()
    df.to_excel(nome_arquivo, index=False)
    print(f"Dados exportados com sucesso para o arquivo {nome_arquivo}")


def menu():
    conn = conectar_bd()
    if not conn:
        return
    cursor = conn.cursor()

    while True:
        os.system("cls")
        print("0 - SAIR")
        print("1 - Cadastrar")
        print("2 - Listar/Exportar")
        print("3 - Filtrar registros")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break
        elif opcao == "1":
            cadastrar(cursor, conn)
        elif opcao == "2":
            exportar_dados(cursor)
        elif opcao == "3":
            filtrar_registros(cursor)
        else:
            print("Opção inválida!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    menu()
