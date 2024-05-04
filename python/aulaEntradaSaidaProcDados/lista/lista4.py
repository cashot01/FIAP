import os
os.system("cls")
"""
4. Faça uma rotina que copie os elementos de um vetor em outro, mas na ordem inversa
False a Edson 4.6 45
"""

lista = [45, 4.6, "edson", "a", "False"]
print(f"\n {lista}")

listaInvertida = lista.copy()
listaInvertida.reverse()
print(f"\n {listaInvertida}")
