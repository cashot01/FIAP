import os
os.system("cls")

#  1. Dado um número pelo usuário, exibir o seu positivo.
original = int(input("nº: "))
modulo = original
if original < 0:
    modulo = original * -1
print(f"|{original}| -> {modulo}")
