# digitar 4 nº placa antiga de carro  , e dizer qual o dia do r0dizio
import os
os.system("cls")

placa = int(input("digite 4 nº: "))
finalPlaca = placa % 10

match finalPlaca:
    case 1 | 2:
        print("Segunda")
    case 3 | 4:
        print("Terça")
    case 5 | 6:
        print("Quarta")
    case 7 | 8:
        print("Quinta")
    case _:
        print("Sexta")
