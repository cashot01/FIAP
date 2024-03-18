# 4. Dados dois números pelo usuário, exibir o de maior valor.
import os 
os.system("cls")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
if n1 > n2:
    print(f"maior nº: {n1}")
elif n1 == n2:
    print("os 2 nºs são iguais")
else:
    print(f"maior nº {n2} ")