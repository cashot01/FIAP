"""
exibir  os numeros do intervalo sem considerar os digitados

inicial: 3
final: 8
4 5 6 7
"""
import os
os.system("cls")

inicial = int(input("inicial: "))
fim = int(input("final: "))

inicial += 1

while inicial < fim:
    print(inicial)
    
    inicial += 1

"""
outro jeito:

inicial += 1
fim -= 1

while inicial <= fim:
    print(inicial)
    inicial += 1
"""