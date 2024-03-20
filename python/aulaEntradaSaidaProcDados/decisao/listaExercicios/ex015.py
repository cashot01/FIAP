# 15. Dados três números pelo usuário, analisá-los e exibir a mensagem “3 números diferentes”, “2 dos 3 são iguais” ou “3 números iguais”.
import os
os.system("cls")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
if n1 == n2 == n3:
    print("3 nº iguais")

elif (n1 == n2) and n1 != n3:
    print("2 nº iguais") 

elif (n1 == n3) and n1 != n2:
    print("2 nº iguais")
else:
    print("3 nº diferentes")