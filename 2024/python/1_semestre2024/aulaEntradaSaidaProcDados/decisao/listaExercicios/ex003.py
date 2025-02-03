#3. Dado um número pelo usuário, verificar se ele é “O número é par” ou “O número é impar”, exibindo sua respectiva mensagem.
import os
os.system("cls")
num = int(input("nº: "))
if num % 2 == 0:
    print("PAR")
else:
    print("IMPAR")