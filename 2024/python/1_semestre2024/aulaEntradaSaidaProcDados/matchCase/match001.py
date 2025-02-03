# digitar um valor e exibir o mes 

import os
os.system("cls")

mes = int(input("digite um nº: "))
match mes:
    case 1:
        print("jan")
    case 2:
        print("fev")
    case 3: 
        print("mar")
    case 4: 
        print("abr")
    case 5:
        print("mai")
    case 6: 
        print("jun")
    case 7:
        print("jul")
    case 8: 
        print("aug")
    case 9: 
        print("set")
    case 10:
        print("out")
    case 11:
        print("nov")
    case 12:
        print("dez")
    case _:
        print("nº invalido")