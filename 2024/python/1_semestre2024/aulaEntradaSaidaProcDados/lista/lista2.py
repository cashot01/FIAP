import os
os.system("cls")
"""
2. Fazer uma rotina que exiba os índices acompanhados dos elementos da lista no seguinte formato.
0-45 | 1-4.6 | 2-Edson | 3-a | 4-False 
"""

#============================= SUBALGORITIMO

def exibe_lista(l: list) -> None:
    for i in range(0, len(l), 1):
        print(f"{i}-{l[i]} | ", end=" ")



# ====================== PROGRAMA PRINCIPAL

lista = [45, 4.6, "Edson", "a", False]
print(lista)

exibe_lista(lista)


