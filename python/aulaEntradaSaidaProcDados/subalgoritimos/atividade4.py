# Cauan Passos RM555466
import os
os.system("cls")
def menu():
    print("""
    MENU
    
    1 -Intervalo
    2 -Intervalo Aberto e Fechado
    3 -Intervalo em ordem crescente ou decrescente
    0 -SAIR""")

    escolha = int(input("Escolha: "))
    while escolha < 0 or escolha > 3:
        os.system("cls")
        print(f"Opção invalida {escolha}")
        print("""
        MENU
        
        1 -Intervalo
        2 -Intervalo Aberto e Fechado
        3 -Intervalo em ordem crescente ou decrescente
        0 -SAIR""")

        escolha = int(input("Escolha: "))
        match escolha:
            case 1:
                print("INTERVALO")
                n1 = int(input("1º numero: "))
                n2 = int(input("1º numero: "))
                
                
        










#---------------------------------------------------------- Programa
menu()