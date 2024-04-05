"""
Dado um numero pelo usurio, exibir os seus 10 primeiros multiplos:
Digite um numero: 5
5 10 15 20 25 30 35 40 45 50

"""
import os
os.system("cls")

num = int(input("nº: "))
i = 1
while i <= 10:
    resultado = num * i
    print(resultado)
    i += 1