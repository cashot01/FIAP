# Tupla é uma "lista" que não pode ser interada (manipulada / modificada), seria como uma lista

import os
os.system("cls")

lista = [4, 5, 6]
print(lista)
lista[0] = 99
print(lista)

tupla = (65, 34, 78, 29, "aniversario", "edson")
# tupla é entre parenteses
print(tupla[0]) # para mostrar algum elemento colchetes []
print(tupla)