# Cauan Passos RM 555466
import os
os.system("cls")
intervalo = list()
contador1 = 0
contador2 = 0
contador3 = 0


def intervalo():
    print("INTERVALO")
    n1 = int(input("1º numero: "))
    n2 = int(input("2º numero: "))
    
    if n1 < n2:
        menor = n1
        maior = n2
    else:
        menor = n2
        maior = n1
    
    for i in range(menor, maior + 1, 1 ):
        intervalo = list()
        intervalo.append(i)
        print(f"{intervalo}", end = "")

def intervalo_aberto_fechado():
    print("INTERVALO -Aberto e Fechado")
    n1 = int(input("1º numero: "))
    n2 = int(input("2º numero: "))
    
    if n1 < n2:
        menor = n1
        maior = n2
    else:
        menor = n2
        maior = n1
    
    for i in range(menor, maior + 1, 1 ):
        intervalo = list()
        intervalo.append(i)
        print(f"{intervalo}", end = "")


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
            intervalo()
            
        case 2:
            intervalo_aberto_fechado()

                
        










#---------------------------------------------------------- Programa Principal
menu()