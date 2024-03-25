import os
os.system("cls")


print(f"""
    1 - Cadastrar
    2 - Consultar
    3 - Alterar
    4 - Excluir
    """)
opcao = int(input("Escolha: "))
""""
if opcao == 1:
    print("Cadastrando....") 
elif opcao == 2:
    print("Consultando")
elif opcao == 3:
    print("Alterando")
"""
match opcao:
    # case 1 | 2 | 3:  | representa o or
    case 1:
        print("Cadastrando...")
    case 2: 
        print("Consultando")
    case 3:
        print("Alterando")
    case 4:
        print("Excluindo")
    # case _: (se for diferente dos outros cases, seria um else)
    case _:
        print("Opção invalida")


