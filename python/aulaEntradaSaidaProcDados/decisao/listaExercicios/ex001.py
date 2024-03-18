# 1. Dado um número pelo usuário, verificar se ele é positivo, exibindo a mensagem “O numero é positivo” ou “O numero não é positivo”.
import os
os.system("cls")
num = float(input("nº: "))
if num >= 0:
    print("POSITIVO")
else:
    print("NEGATIVO")