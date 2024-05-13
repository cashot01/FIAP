# 6 - conta_string() conta quantas strings tem em uma lista
import os
os.system("cls")

lista = ["eds", "56", "fiap", "ester", "True", "45.78", "12", "78" ]
print(lista)
print(type(lista))
# type(lista[0])
print(f"{type(lista[0])}, {type(lista[1])} , {type(lista[2])}, {type(lista[3])}, {type(lista[4])}, {type(lista[5])}, {type(lista[6])} ")

if type(lista) == "list":
    qtd_string = lista.count()
    print(qtd_string)

# for i in range(len(lista)):
#     if type((lista)) == str:
#         qtd_strings = lista.count(lista(str))
#         qtd = len(lista)
#         print(len(lista))
#         print(qtd_strings)

