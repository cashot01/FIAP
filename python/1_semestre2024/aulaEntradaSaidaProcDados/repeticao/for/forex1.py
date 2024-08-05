# peça 2 nº e exiba em ordem crescente
import os
os.system("cls")
num1 = int(input('Inicio: '))
num2 = int(input('Fim: '))

if num2 < num1:
    aux = num1
    num1 = num2
    num2 = aux

for i in range(num1, num2 + 1, 1):
    print(i, end = ' ')