# 3 - 2 nº e digite C ou D para mostar a ordem

import os
os.system("cls")
num1 = int(input('Inicio.......................: '))
num2 = int(input('Fim..........................: '))
ordem = input("[C]rescente ou [D]ecrescente? ")

if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

if ordem == 'c' or ordem == 'C':
    for i in range(menor, maior + 1, 1):
        print(i, end = ' ')
elif ordem.upper() == "D":
    for i in range(maior, menor - 1, -1):
        print(i, end = ' ')
else:
    print("Digite C ou D")

