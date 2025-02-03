# peça 2 nº exiba em crescente se n1 > n2 ou decrescente se n2> n1

import os
os.system("cls")
num1 = int(input('Inicio: '))
num2 = int(input('Fim: '))

if num1 <= num2:
    for i in range(num1, num2 + 1, 1):
        print(i, end = ' ')
else:
    for i in range(num1, num2 -1, -1):
        print(i, end = ' ')