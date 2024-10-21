import os
os.system("cls")
import pandas as pd
import oracledb
import datetime

def cadastro():


def main():
    try:
        conn = oracledb.connect(user="RM555466", password="071105", dsn='oracle.fiap.com.br:1521/ORCL')
    
        inst_cadastro = conn.cursor()
        inst_consulta = conn.cursor()
    except Exception as e:
        print("Erro: ", e)

    while True:
        os.system("cls")
        print("Menu")
        print("0 - Sair")
        print("1 - Cadastrar")
        print("2 - Listar / Exportar")
        print("3 - Filtrar Registros")
        opcao = input("Escolha: ")
        match opcao:
            case "0":
                break
            case "1":
                cadastrar()
            case "2":
                listar_exportar()
            case "3":
                filtrar_registros()
            case _:
                print("opção invalida")
                input("presione enter para continuar...")
                


main()
            
