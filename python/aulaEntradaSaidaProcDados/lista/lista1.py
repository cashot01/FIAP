import os
os.system("cls")
"""
1. Fazer uma rotina que preencha uma lista até que seja digitado ponto(.).
45 4.6 Edson a False .
"""
lista = list()
print(lista)

while True:
    elemento = input("digite qualquer coisa: ")
    lista.append(elemento)
    print(lista)

    if elemento == ".":
        # print(lista)
        break

print(f"Lista encerrada = {lista}")

