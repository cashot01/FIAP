import os
os.system("cls")
"""
2. Fazer uma rotina que exiba os índices acompanhados dos elementos da lista no seguinte formato.
0-45 | 1-4.6 | 2-Edson | 3-a | 4-False 
"""

lista = list()
print(lista)

for i in range(0, 5, 1):
    elemento = input("digite algo: ")
    lista.append(elemento)

indice0 = lista.index(lista[0])


indice1 = lista.index(lista[1])


indice2 = lista.index(lista[2])


indice3 = lista.index(lista[3])


indice4 = lista.index(lista[4])

print(lista)

print(f"\n {indice0} - {lista[0]} | {indice1} - {lista[1]} | {indice2} - {lista[2]} | {indice3} - {lista[3]} | {indice4} - {lista[4]}")
