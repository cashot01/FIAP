import os
os.system("cls")
import pandas as pd
import datetime


def main():
    while True:
        os.system("cls")
        print("Menu")
        print("0 - Sair")
        print("1 - Cadastrar")
        print("2 - Listar / Cadastrar")
        opcao = input("Escolha: ")
        match opcao:
            case "0":
                break
            case "1":
                cadastrar()
            case "2":
                listar_exportar()
            case _:
                print("opção invalida")
                input("presione enter para continuar...")
                


main()
            
