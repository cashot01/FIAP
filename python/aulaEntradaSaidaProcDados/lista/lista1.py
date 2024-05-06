import os
os.system("cls")
"""
1. Fazer uma rotina que preencha uma lista até que seja digitado ponto(.).
45 4.6 Edson a False .
"""

# --------------------- SUBALGORITIMO
def preenche_lista(l: list) -> None:
    while True:
        elemento = input("digite qualquer coisa: ")
        # lista.append(elemento)
        # print(lista)

        # if elemento == ".":
        #     # print(lista)
        #     lista.remove(".")
        #     break
        if elemento != ".":
            l.append(elemento)
        else:
            break

# ------------------------------ PROGRAMA PRINCIPAL


lista = list()
preenche_lista(lista)


print(f"Lista encerrada = {lista}")

